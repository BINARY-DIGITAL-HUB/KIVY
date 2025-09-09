from dataclasses import dataclass
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from kivymd.uix.list import OneLineIconListItem, ThreeLineAvatarListItem
from numpy import float32
import datapoint as dpt
import numpy as np
import joblib


class LoanPredictionSystem(MDApp):

    
    
    def build(self):
        self.datapoint = dpt.DataPoint(0,0,0,0,0,0,0,0,0,0,0)
        # loading themes.......
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.accent_palette = 'LightBlue'
        return Builder.load_file('layout.kv')

    def on_start(self):
        sex_menu_items = [
            {
                "viewclass": "OneLineIconListItem",
                "icon": "account-user",
                "height": dp(50),
                'width':dp(110),
                "text": f"{i}",
                "on_release": lambda x=f"{i}": self.set_sex_item(x),
            } for i in ['male', 'female']]
            
        self.sex_menu = MDDropdownMenu(
            caller= self.root.ids.id_sex,
            items=sex_menu_items,  
            position="top",
            width_mult=40,
            width=40
        )



        married_menu_items = [
            {
                "viewclass": "OneLineIconListItem",
                "icon": "account-user",
                "height": dp(50),
                'width':dp(110),
                "text": f"{i}",
                "on_release": lambda x=f"{i}": self.set_married_item(x),
            } for i in ['yes', 'no']]
            
        self.married_menu = MDDropdownMenu(
            caller= self.root.ids.id_married,
            items=married_menu_items,  
            position="top",
            width_mult=40,
            width=40
        )




        dependent_menu_items = [
            {
                "viewclass": "OneLineIconListItem",
                "icon": "account-user",
                "height": dp(50),
                'width':dp(110),
                "text": f"{i}",
                "on_release": lambda x=f"{i}": self.set_dependent_item(x),
            } for i in ['0', '1', '2', '3']]
            
        self.dependent_menu = MDDropdownMenu(
            caller= self.root.ids.id_dependent,
            items=dependent_menu_items,  
            position="top",
            width_mult=40,
            width=40
        )



        education_menu_items = [
            {
                "viewclass": "OneLineIconListItem",
                "icon": "account-user",
                "height": dp(50),
                'width':dp(110),
                "text": f"{i}",
                "on_release": lambda x=f"{i}": self.set_education_item(x),
            } for i in ['yes', 'no']]
            
        self.education_menu = MDDropdownMenu(
            caller= self.root.ids.id_education,
            items=education_menu_items,  
            position="top",
            width_mult=40,
            width=40
        )


        selfemploye_menu_items = [
            {
                "viewclass": "OneLineIconListItem",
                "icon": "account-user",
                "height": dp(50),
                'width':dp(110),
                "text": f"{i}",
                "on_release": lambda x=f"{i}": self.set_selfemploye_item(x),
            } for i in ['yes', 'no']]
            
        self.selfemploye_menu = MDDropdownMenu(
            caller= self.root.ids.id_self_employe,
            items=selfemploye_menu_items,  
            position="top",
            width_mult=40,
            width=40
        )




        history_menu_items = [
            {
                "viewclass": "OneLineIconListItem",
                "icon": "account-user",
                "height": dp(50),
                'width':dp(110),
                "text": f"{i}",
                "on_release": lambda x=f"{i}": self.set_history_item(x),
            } for i in ['yes', 'no']]
            
        self.history_menu = MDDropdownMenu(
            caller= self.root.ids.id_history,
            items=history_menu_items,  
            position="top",
            width_mult=40,
            width=40
        )


        proparea_menu_items = [
            {
                "viewclass": "OneLineIconListItem",
                "icon": "account-user",
                "height": dp(50),
                'width':dp(80),
                "text": f"{i}",
                "on_release": lambda x=f"{i}": self.set_proparea_item(x),
            } for i in ['urban', 'semi_urban', 'rural']]
            
        self.proparea_menu = MDDropdownMenu(
            caller= self.root.ids.id_proparea,
            items=proparea_menu_items,  
            position="top",
            width_mult=40,
            width=40
        )
        





         # menu list for sex activation menu
    # ===========================================================
    def activate_sex(self):
            self.sex_menu.caller = self.root.ids.id_sex
            self.sex_menu.open()
            # print('method called', text_field)

    def set_sex_item(self, text__item):
         self.root.ids.id_sex.text = text__item
         self.datapoint.sex = self.root.ids.id_sex.text
         self.sex_menu.dismiss()

    # ===========================================================
    def activate_married(self):
            self.married_menu.caller = self.root.ids.id_married
            self.married_menu.open()
            # print('method called', text_field)

    def set_married_item(self, text__item):
         self.root.ids.id_married.text = text__item
         self.datapoint.married = self.root.ids.id_married.text
         self.married_menu.dismiss()
        

    # ===========================================================
    def activate_dependent(self):
            self.dependent_menu.caller = self.root.ids.id_dependent
            self.dependent_menu.open()
            # print('method called', text_field)

    def set_dependent_item(self, text__item):
         self.root.ids.id_dependent.text = text__item
         self.datapoint.dependent = self.root.ids.id_dependent.text
         self.dependent_menu.dismiss()
    
    # ===========================================================
    def activate_education(self):
            self.education_menu.caller = self.root.ids.id_education
            self.education_menu.open()
            # print('method called', text_field)

    def set_education_item(self, text__item):
         self.root.ids.id_education.text = text__item
         self.datapoint.educated = self.root.ids.id_education.text
         self.education_menu.dismiss()

    
    # ===========================================================
    def activate_self_employe(self):
            self.selfemploye_menu.caller = self.root.ids.id_self_employe
            self.selfemploye_menu.open()
            # print('method called', text_field)

    def set_selfemploye_item(self, text__item):
         self.root.ids.id_self_employe.text = text__item
         self.datapoint.employed = self.root.ids.id_self_employe.text
         self.selfemploye_menu.dismiss()

    
    # ===========================================================
    def activate_history(self):
            self.history_menu.caller = self.root.ids.id_history
            self.history_menu.open()
            # print('method called', text_field)

    def set_history_item(self, text__item):
         self.root.ids.id_history.text = text__item
         self.datapoint.credit_history = self.root.ids.id_history.text
         self.history_menu.dismiss()
    
    # ===========================================================
    def activate_proparea(self):
            self.proparea_menu.caller = self.root.ids.id_proparea
            self.proparea_menu.open()
            # print('method called', text_field)

    def set_proparea_item(self, text__item):
         self.root.ids.id_proparea.text = text__item
         self.datapoint.prop_area = self.root.ids.id_proparea.text
         self.proparea_menu.dismiss()

    def prediction_box(self):
        self.datapoint.income = self.root.ids.id_income_amount.text
        self.datapoint.co_income = self.root.ids.id_other_income.text
        self.datapoint.loan_amount = self.root.ids.id_loan_amount.text

        sex = 1 if self.datapoint.sex.lower() == "male" else 0
        print('============ SEX VALUE==== ', sex)
        
        married = 1 if self.datapoint.married == "yes" else 0
        print('============ MARRIED VALUE==== ', married)

        educated = 0 if self.datapoint.educated == "yes" else 1
        print('============ EDUCATED VALUE==== ', educated)

        employed = 1 if self.datapoint.employed == 'yes' else 0

        credict_history = 1 if self.datapoint.credit_history == 'yes' else 0
        dependent = self.datapoint.dependent
        income = self.datapoint.income
        co_income = self.datapoint.co_income
        loan_amount = self.datapoint.loan_amount
        loan_term = self.datapoint.loan_term

        location  = 0.0
        if self.datapoint.prop_area == 'rural':
            location = 0.0
        elif self.datapoint.prop_area == 'urban':
            location = 2.0
        else:
            location = 1.0
        
        sample = np.array([[float(sex), float(married) , float(dependent), float(educated), float(employed) , float(income)/8100, float(co_income)/41667, float(loan_amount)/700,float(loan_term)/480, float(credict_history), float(location) ]], float32)

        print(sample)

         # loading models....
        models = ['rf_model' , 'knn_model' , 'svm_model' , 'nb_model' , 'lg_model']
        label, final_score = self.aggregated_sample_prediction(models=models, data_point=sample)
        print(label, final_score)

        # SETTING UI BUTTON TO MODEL PREDICTION
        rf, knn, svm, nb, lg = label
        x,svm_val = svm
        x,lg_val = lg
        x,rf_val = rf
        x,knn_val = knn
        x,nb_val = nb

        self.root.ids.id_support_vector.text = 'YES' if svm_val == 1 else 'FALSE'
        self.root.ids.id_logistic_regression.text = 'YES' if lg_val == 1 else 'FALSE'
        self.root.ids.id_decision_tree.text = 'YES' if rf_val == 1 else 'FALSE'
        self.root.ids.id_knn.text = 'YES' if knn_val == 1 else 'FALSE'
        self.root.ids.id_naive_bayes.text = 'YES' if nb_val == 1 else 'FALSE'
        self.root.ids.id_final_decission.text = 'YES' if final_score == 1 else 'FALSE'

    def reselt_all_ui():
        pass    

    def aggregated_sample_prediction(self, models, data_point):
        model_list = []
        predictions = []
        for model in models:
            m  = joblib.load(model)
            model_list.append(m)
            
        
        predictions.append([m.predict(data_point) for m in model_list])
        merge_prediction = np.concatenate(predictions)
        merge_prediction = merge_prediction.flatten()
        value, count = np.unique(merge_prediction, return_counts=True)
    #     print(merge_prediction)
    #     print(value, count)
        final_prediction = value[np.argmax(count)]
        
        #model name and score
        model_label_score = []
        for index in range(len(models)):
            model_label_score.append((models[index], merge_prediction[index]))
        
        return model_label_score, final_prediction
    
       



LoanPredictionSystem().run()