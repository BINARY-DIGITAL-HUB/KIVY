from kivy.lang import Builder
from kivymd.app import MDApp  
from kivymd.uix.datatables import MDDataTable
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.metrics import dp



import database as db
import patient as pt
import aes_ctrmode as en_de
import re



class LoginScreen(Screen):
    pass

class MainScreen(Screen):
    pass

class MedicalDetailScreen(Screen):
    pass

class ScreenController(ScreenManager):
    pass 

class CryptoSystem(MDApp):
    database = db.Database()
    init_table_data = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
       
        self.current_record = '' 
        # initializing the encryption instance
        self.encryption_engine = en_de.AESCTRXEncryption()

    # loading database content into the database..
    def load_medical_record(self):
        patient_records = CryptoSystem.database.fetch_all_record()  
        
        # looping all the patient record .......
        for patient_ in patient_records:
           patient_turple =  (id , name , age, sex, antivirals, liverbig, bilirubin, albumin) = patient_.id, patient_.name, patient_.age, patient_.sex, patient_.antiviral, patient_.liverbig, patient_.bilirubin, patient_.albumin
           CryptoSystem.init_table_data.append(patient_turple)

        #  checking the turple list 
        # print([p for p in CryptoSystem.init_table_data])

    def on_start(self):
        # loading main screen.....
        self.main_screen = self.root.get_screen('main_screen')
        self.detail_screen = self.root.get_screen('detail_screen')
        

        # calling method to load database record
        self.load_medical_record()

        record_table = MDDataTable(
                            size_hint=(1, 7),
                            pos_hint =  {'center_x': 0.5,'center_y': 0.6}, 
                            check = True,
                            use_pagination=True,
                            # rows_num= 3, 
                            column_data = [
                                ("ID",dp(20)), 
                                ("NAME", dp(30)),
                                ("AGE", dp(15)),
                                ("SEX", dp(15)),
                                ("ANTIVIRALS", dp(20)),
                                ("LIVERBIG", dp(20)),
                                ("BILIRUBIN", dp(20)),
                                ("ALBUMIN", dp(20))
                            ],
                            row_data = CryptoSystem.init_table_data
                            )

            # table listiners 
        record_table.bind(on_check_press=self.table_checked)
        record_table.bind(on_row_press=self.tablerow_checked)
        self.main_screen.ids.layout.add_widget( record_table, index=0)   

    def table_checked(self, instance_table, current_row):
        self.current_record = current_row
        

    def tablerow_checked(self, instance_table, instance_row):
        print(instance_row)

    # this module help to link main.py to encryption modules (ctr and rsa encryption module)
    def encryption_box(self):
        print(f'current record --->> ', '-'.join(self.current_record))
        join_record = '-'.join(self.current_record)
        print('joint record ' , join_record)

        # crypo = AESCTRXEncryption()
        # crypo.encrypt('ade-12-yes-1995' , 5 , '1234567891234567')
        # CALLING THE ENCRYPTION MODULE .....
        encrypt_key = self.main_screen.ids.text_encryption_key.text
        print('ENCRYPTION KEY ' , encrypt_key)
        if len(encrypt_key) ==  16 and re.match("[0-9]+", encrypt_key ) and join_record != "" :
            print('condition matched..............')
            self.encryption_engine.encrypt(join_record, self.current_record[0] , encrypt_key )
            print('encryption completed... ')
        else:
            print('invalid encryption code')

    def decryption_box(self):
        # dic_id = self.detail_screen.ids.text_patient_id.text 
        file_id = self.detail_screen.ids.id_txt_id_file.text
        print('ID KEY ', file_id )
        print('decryption box called')
        record = message = self.encryption_engine.decrypt(file_id, '1234567891234567')
        record = record.decode('utf-8')
        id, name, age, sex, antivirals, liverbig, bilirubin, albumin  = record.split("-")
        patient = pt.Patient(id, name, age, sex, antivirals, liverbig, bilirubin, albumin)
        print('FINAL decryption' , record)
        print("FINAL patient DATA " , patient)
        self.load_ui_decrypted_data(patient)

    def load_ui_decrypted_data(self, patient):
        self.detail_screen.ids.label_id.text = patient.id
        self.detail_screen.ids.label_name.text = patient.name
        self.detail_screen.ids.label_age.text = patient.age
        self.detail_screen.ids.label_sex.text = patient.sex
        self.detail_screen.ids.label_antiviral.text = patient.antiviral
        self.detail_screen.ids.label_liverbig.text = patient.liverbig
        self.detail_screen.ids.label_bilirubin.text =  patient.bilirubin
        self.detail_screen.ids.label_albumin.text = patient.albumin

    def build(self):
        # loading themes.......
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = 'Amber'
        self.theme_cls.accent_palette = 'Yellow'

       
        return Builder.load_file('layout.kv')
  

CryptoSystem().run()
