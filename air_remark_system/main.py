from ast import Global
from distutils import text_file
from distutils.text_file import TextFile
from turtle import width
from unicodedata import category

from numpy import source
from soupsieve import select

from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from kivy.properties import StringProperty,ObjectProperty
from kivymd.uix.list import OneLineIconListItem, ThreeLineAvatarListItem
import database as db 
from user import User
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
import comment_sentiment as com_sent


x = ['postive' , 'neutral' , 'negative']
y = [23, 30, 40]

plt.bar(x,y)

class Statistic(MDBoxLayout):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        
        # stac = MainApp.loginscreen.ids.stac_box
        # stac.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # https://www.youtube.com/playlist?list=PLeo1K3hjS3us_ELKYSj_Fth2tIEkdKXvV

class SignUpScreen(Screen):
    pass


class LoginScreen(Screen):
    pass

class AppScreen(Screen):
    pass
 
class ScreenPack(ScreenManager):
    pass


class ContentNavigationDrawer(MDBoxLayout):
    pass

class IconListItem(OneLineIconListItem):
    icon = StringProperty()

Window.size= (350, 700)
class MainApp(MDApp):

    database = db.Database()
    loginscreen = None

    def prepear_statistical_data(self):
        remarks = MainApp.database.fetch_all_remark()
        review_categories = ['customer service', 'theft issue', 'management issue' ]
        category , positive_review, negative_review = '', 0,0
        cs , ti, mi = [] , [] , []
        for remark in remarks : 
            if remark.remark_category == review_categories[0]:
                # print('customer service' , remark)
                cs.append(remark.remark_text)
            elif remark.remark_category == review_categories[1]:
                # print('customer theft ' , remark)
                ti.append(remark.remark_text)
            elif remark.remark_category == review_categories[2]:
                # print('management ' , remark)
                mi.append(remark.remark_text)
        
        cs_sentiment = com_sent.Remark_Sentiment(cs)
        ti_sentiment = com_sent.Remark_Sentiment(ti)
        mi_sentiment = com_sent.Remark_Sentiment(mi)

        print('ITEMS', ti)

        print('comment P coutn' , cs_sentiment.get_negative_review())

    def on_start(self):
      #  print('SCREEN DATA' , self.root.get_screen('app_screen').ids.field.text)
    #   GETTING A REFERENCE TO THE WIDGET IN THE APP AND LOGIN SCREEN
        self.application_screen = self.root.get_screen('app_screen')
        self.login_screen = self.root.get_screen('login_screen')
        self.registration_screen = self.root.get_screen('signup_screen')
        

        self.prepear_statistical_data()
        # statistic representation .... 
        stac =  self.application_screen.ids.stac_box
        stac.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # LOADING COMMENT FROM DATABASE.... 
        for comment in MainApp.database.fetch_all_remark():
            # print('ID' , comment.customer_id)
            current_user = MainApp.database.fetch_user(comment.customer_id)
            print('CURRENT USER..... ', current_user.name)
            self.application_screen.ids.comment_list.add_widget(
                ThreeLineAvatarListItem(
                    text=f'{current_user.email}',
                    secondary_text = f'{comment.customer_id}',
                    tertiary_text = f'{comment.remark_text}', 
                    
                )
            )
        
#												source:'image/images.jpg'

        #............. CODE SECTION FOR REMARK TABE APP SCREEN...............
        
          # menu list for complain or compliment categories
        categories = ['Services', 'flight Attendance', 'Lost Item', 'Management']
        c_c_menu_items = [
            {
                "viewclass": "IconListItem",
                "icon": "git",
                "height": dp(50),
                "width":dp(200),
                "text": f"{i}",
                "on_release": lambda x=f"{i}": self.set_cc_item(x),
            } for i in categories]
        self.complain_compliment_menu = MDDropdownMenu(
            caller= self.application_screen.ids.cc_field,
            items=c_c_menu_items,
            position="top",
            width_mult=10,
        )


          # menu list for states Routh categories
        state_menu_items = [
            {
                "viewclass": "IconListItem",
                "icon": "git",
                "height": dp(50),
                'width':dp(110),
                "text": f"{i}",
                "on_release": lambda x=f"{i}": self.set_state_item(x),
            } for i in ['Abuja', 'Kano', 'Benin']]

        self.state_menu = MDDropdownMenu(
            caller= self.application_screen.ids.state_field,
            items=state_menu_items,  
            position="top",
            width_mult=40,
            width=60
        )     

        state_menu_items2 = [
        {
            "viewclass": "IconListItem",
            "icon": "git",
            "height": dp(50),
            'width':dp(110),
            "text": f"{i}",
            "on_release": lambda x=f"{i}": self.set_state_item2(x),
        } for i in ['Ibadan', 'Lagos', 'Jos']]

        self.state_menu2 = MDDropdownMenu(
            caller= self.application_screen.ids.state_field2,
            items=state_menu_items2,  
            position="top",
            width_mult=40,
            width=60
        )     
        
         
    def activate_add_remark(self):
        print('button clicked')


    def activate_remark_clear(self):
        print('button clear clicked')



    # ..................CODE SECTION FOR REGISTRATION ....................
      # menu list for SEX MALE/FEMALE IN REGISTRATION
        sex_menu_items = [
            {
                "viewclass": "IconListItem",
                "icon": "account-user",
                "height": dp(50),
                'width':dp(110),
                "text": f"{i}",
                "on_release": lambda x=f"{i}": self.set_sex_item(x),
            } for i in ['Male', 'Female']]
            
        self.sex_menu = MDDropdownMenu(
            caller= self.registration_screen.ids.id_register_sex,
            items=sex_menu_items,  
            position="top",
            width_mult=40,
            width=60
        )     

    # END OF ON START FUNCTION ......................
    
    
    #..... FUNCTION FOR REGISTRATION SUBMIT AND CANCEL..      
    def activate_registration_submit(self):
        name = self.registration_screen.ids.id_register_name.text
        email = self.registration_screen.ids.id_register_email.text
        age = self.registration_screen.ids.id_register_age.text
        password = self.registration_screen.ids.id_register_password.text
        con_password = self.registration_screen.ids.id_register_confirmed_password.text
        sex_string= self.registration_screen.ids.id_register_sex.text
        sex = 1 if sex_string == 'Male' else 0
       #...GETTING THE LAST USER ID AND PLUS IT WITH ONE
        id = int(MainApp.database.fetch_users()[-1].id) + 1 
        user = User(id,name, age, email, password,sex)
        print('USER {user.sex}' , str(user))


    def activate_registration_cancel(self):
        pass

    # menu list for sex activation menu
    def activate_sex_states(self):
            self.sex_menu.caller = self.registration_screen.ids.id_register_sex
            self.sex_menu.open()
            # print('method called', text_field)

    def set_sex_item(self, text__item):
         self.registration_screen.ids.id_register_sex.text = text__item
         self.state_menu.dismiss()


     # menu list for complain or compliment categories
    def activate_menu_c_c(self):
            self.complain_compliment_menu.caller = self.application_screen.ids.cc_field
            self.complain_compliment_menu.open()
            # print('method called', text_field)

    def set_cc_item(self, text__item):
         self.application_screen.ids.cc_field.text = text__item
         self.complain_compliment_menu.dismiss()
     
     


    # menu list for states route categories
    def activate_menu_states(self):
            self.state_menu.caller = self.application_screen.ids.state_field
            self.state_menu.open()
            print('method called')

    def set_state_item(self, text__item):
         self.application_screen.ids.state_field.text = text__item
         self.state_menu.dismiss()

      # menu list for states route categories 2
    def activate_menu_states2(self):
            self.state_menu2.caller = self.application_screen.ids.state_field2
            self.state_menu2.open()
            print('method called')

    def set_state_item2(self, text__item):
         self.application_screen.ids.state_field2.text = text__item
         self.state_menu2.dismiss()
    
    # THE BUILD METHOD......
    def build(self):
        self.theme_cls.theme_style="Light"
        self.theme_cls.primary_pallete = "Blue"
        self.theme_cls.accent_pallet= "White"
        self.application_screen = None
        # (Global) loginscreen  = self.login_screen 
        
        self.icon_name = ['account' , 'cellphone' , 'key']
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"{i}",
                #'icon':'git',
                "height": dp(56),
                "on_release": lambda x= self.menu_name(): self.menu_callback(x),
            } for i in list(self.menu_name())
        ]
        self.menu = MDDropdownMenu(
            items=menu_items,
            width_mult=2,
        )

       


        
        kv = Builder.load_file("layout.kv")
        return kv


    # for the menu three doted tool bar
    def menu_name(self):
        item_list = {'signup', 'logout', 'setting'}
        return item_list

    def activate_menu(self, button):
        self.menu.caller = button
        self.menu.open()

    def menu_callback(self, text_item):
        self.menu.dismiss()
        print('text item = ' , text_item)
        for item in text_item:
            if item == 'logout':
                self.root.current = 'login_screen'
            elif item == 'signup':
                self.root.current = 'signup_screen'
            else :
                pass 

    # for the compliment and complain check box 
    def on_checkbox_active(self, checkbox, value, text):

        if value:
            option = 'compliment' if text == 'compliment' else 'complains'
            print(f'it is {option}')
            

    def activate_login(self):
       # print('LOGIN ACTIVATED')
        user_name = self.login_screen.ids.user_name_input.text 
        password  = self.login_screen.ids.password_input.text 
        button = self.login_screen.ids.login_button
        print(f'username :{user_name} password:{password}')
        authenticated = MainApp.database.validate_user([user_name,password])
        if authenticated:
            print('login successfull')
            self.root.current = 'app_screen'
        else:
            print('login failed')
            self.root.current = 'app_screen'
        


MainApp().run()



