

class Patient:
    def __init__(self, id , name , age, sex, antivirals, liverbig, bilirubin, albumin ) -> None:
        self.__id = id
        self.__name = name
        self.__age = age 
        self.__sex = sex
        self.__antivirals = antivirals
        self.__liverbig = liverbig
        self.__bilirubin = bilirubin
        self.__albumin = albumin

    #  patient id 
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self , id):
        self._id = id

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self , age):
        self.__age = age

        #  patient name 
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self , name):
        self__name = name


#  patent sex
    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self , sex):
        self.__sex = sex


    # the antivarals property 
    @property
    def antiviral(self):
        return self.__antivirals

    @antiviral.setter
    def antiviral(self , antivarals):
        self.__antivirals = antivarals

     # the antivarals property 
    @property
    def liverbig(self):
        return self.__liverbig

    @liverbig.setter
    def liverbig(self , liverbig):
        self.__liverbig = liverbig

    
     # the antivarals property 
    @property
    def bilirubin(self):
        return self.__bilirubin

    @bilirubin.setter
    def bilirubin(self , bilirubin):
        self.__bilirubin = bilirubin   


#  the albumin property
    @property
    def albumin(self):
        return self.__albumin

    @albumin.setter
    def albumin(self , albumin):
        self.__albumin = albumin  


    def __str__(self):
        return f"patient => {self.id} , {self.name} , {self.sex} , {self.liverbig}"