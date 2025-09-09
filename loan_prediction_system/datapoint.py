

from msilib.schema import Property


class DataPoint:

    def __init__(self , sex, married, dependent , educated, employed, income, co_income, loan_amount, loan_term, credit_history, prop_area) -> None: 
        self.__sex = sex
        self.__married = married 
        self.__dependent = dependent
        self.__educated = educated
        self.__employed = employed
        self.__income = income
        self.__co_income = co_income
        self.__loan_amount = loan_amount
        self.__loan_term = loan_term
        self.__credit_history = credit_history
        self.__property_area = prop_area

    @property
    def sex(self):
        return self.__sex

    @sex.setter 
    def sex(self, sex):
        self.__sex = sex

    
    @property
    def married(self):
        return self.__married

    @married.setter 
    def married(self, married):
        self.__married = married

    
    @property
    def dependent(self):
        return self.__dependent

    @dependent.setter 
    def dependent(self, dependent):
        self.__dependent = dependent


    @property
    def educated(self):
        return self.__educated

    @educated.setter 
    def educated(self, educated):
        self.__educated = educated

    @property
    def employed(self):
        return self.__employed
    
    @employed.setter
    def employed(self, employed):
        self.__employed = employed
    
    @property
    def income(self):
        return self.__income

    @income.setter 
    def income(self, income):
        self.__income = income
    
    @property
    def co_income(self):
        return self.__co_income

    @co_income.setter 
    def co_income(self, co_income):
        self.__co_income = co_income
    
    @property
    def loan_amount(self):
        return self.__loan_amount

    @loan_amount.setter 
    def loan_amount(self, loan_amount):
        self.__loan_amount = loan_amount

    @property
    def loan_term(self):
        return self.__loan_term 

    @loan_amount.setter
    def loan_term(self, loan):
        self.__loan_term = loan

    
    @property
    def credit_history(self):
        return self.__credit_history

    @credit_history.setter 
    def credit_history(self, credit_history):
        self.__credit_history = credit_history

    
    @property
    def prop_area(self):
        return self.__property_area

    @prop_area.setter 
    def prop_area(self, prop_area):
        self.__property_area = prop_area

    
    def __str__(self) -> str:
        return f'sex:{self.sex} , married:{self.married} , educated {self.dependent} , income {self.income} '




# d = DataPoint()
# d.income = 0.234

# print(d.income)