import sqlite3  as database
import csv as cv
import patient as pt


class Database:

    def load_csv_data(self, filename)-> list:
        with open(filename) as file:
            dataset = cv.reader(file)
            header = [next(dataset)]
            datalist = []
            for row in list(dataset):
                print('row==>:' , row)
                datalist.append(row)

        return datalist


    def __init__(self) -> None:
        self.connection = None
        with database.connect('medical_record.db') as db :
            self.connection = db
            print('connection established')


    def create_medical_record_table(self):
        self.connection.execute("""CREATE TABLE IF NOT EXISTS medical_table (
            id INT NOT NULL, 
            name TEXT NOT NULL,
            age INT NOT NULL,
            sex TEXT NOT NULL,
            antivirals TEXT NOT NULL,
            liverbig TEXT NOT NULL,
            bilirubin TEXT NOT NULL, 
            Albumin TEXT NOT NULL,
            PRIMARY KEY (id)

        )
        """)

        self.connection.commit()
        print('medical record table created.........')


    def add_record(self, patient):

        id = patient.id 
        name = patient.name
        age = patient.age
        sex = patient.sex
        antivirals = patient.antiviral
        liverbig = patient.liverbig
        bilirubin = patient.bilirubin
        albumin = patient.albumin

        # print('ID .....====> ', id)
        self.connection.execute(
            'INSERT INTO medical_table VALUES(?,?,?,?,?,?,?,?)', (id, name, age, sex,antivirals, liverbig,bilirubin,albumin)
            )
        self.connection.commit()
        print(patient.id  , '  .... record inserted.....')

    def fetch_all_record(self):
        record_list = []
        cr = self.connection.cursor().execute('SELECT * FROM medical_table')
        data = cr.fetchall()
        for patient in data:
            #  id , name , age, sex, antivirals, liverbig, bilirubin, albumin
            us = pt.Patient(patient[0], patient[1], patient[2], patient[3], patient[4], patient[5], patient[6], patient[7])
            record_list.append(us)
        return record_list

    def csv_to_database(self, f):
        csv_record = self.load_csv_data(f)
        patient_list = []
        for record in csv_record:
            id,  age, sex, antivirals, liverbig, bilirubin, albumin , name = record
            patient = pt.Patient(id, name, age, sex, antivirals, liverbig, bilirubin, albumin)
            print(f"{patient}")
            self.add_record(patient)
        
        else:
            print('all record inserted completely')

    def database_to_csv(self):
        patient_records = self.fetch_all_record() 
        
        # write to csv 
        with open("datas.csv", "w") as file:
            writer = cv.writer(file)
            writer.writerow(['ID', 'NAME', 'AGE', 'SEX', 'ANTIVIRALS' , 'LIVERBIG', 'BILIRUBIN', 'ALBUMIN'])
            for patient in patient_records:
                id, name, age, sex, antivirals, liverbig, bilirubin, albumin = patient.id, patient.name, patient.age, patient.sex, patient.antiviral, patient.liverbig, patient.bilirubin, patient.albumin
                writer.writerow([id, name, age, sex, antivirals, liverbig, bilirubin, albumin])
                # print(f"{id} {name} {age}") 
            print('program completed....')

# db = Database()

# # db.create_medical_record_table()
# patient = db.fetch_all_record()
# # db.load_csv_data('final_medical_record.csv')
# # db.csv_to_database('final_medical_record.csv')
# # for p in patient:
# #     print('record : ' , p)

# # print([str(p) for p in patient])
# db.database_to_csv()