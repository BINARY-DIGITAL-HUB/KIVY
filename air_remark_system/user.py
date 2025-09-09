

import email
from time import sleep


class User:
    
    def __init__(self, id, name, age, email, password, sex):
        self.__id = id 
        self.__name = name 
        self.__age = age
        self.__email = email
        self.__password = password
        self.__sex = sex
 
    
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self):
        pass


    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password =password

    @property
    def sex(self):
        return self.__sex
    
    @sex.setter
    def sex(self, sex):
        self.__sex = sex


    def __str__(self) -> str:
        sex = 'Male' if bool(self.sex) else 'Female'
        return f'USER - > id:{self.id}, name:{self.name}, email:{self.email}, age:{self.age}, password:{self.password}, Sex : {sex}'




#user = User('1234', 'akin' , 23, 'kin', '123456')
#print(user)
