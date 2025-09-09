
class Remark:
    def __init__(self,customer_id, ticket_id, remark_category, timestamp, route, remark_text) -> None:
        self.__customer_id = customer_id
        self.__ticket_id = ticket_id
        self.__remark_category = remark_category
        self.__timestamp = timestamp 
        self.__route = route
        self.__remark_text = remark_text


    @property
    def customer_id(self):
        return self.__customer_id
    
    @customer_id.setter
    def customer_id(self, customer_id):
        self.__customer_id = customer_id

    @property
    def ticket_id(self):
        return self.__ticket_id 

    @ticket_id.setter
    def ticket_id(self, ticket_id):
        self.__ticket_id = ticket_id 

        
    @property
    def remark_category(self):
        return self.__remark_category 

    @remark_category.setter
    def remark_category(self, remark_cat):
        self.__remark_category = remark_cat


    @property
    def timestamp(self):
        return self.__timestamp 

    @timestamp.setter
    def timestamp(self, time):
        self.__timestamp = time 


    @property
    def route(self):
        return self.__route

    @route.setter
    def route(self, route):
        self.__route = route  
    
    @property
    def remark_text(self):
        return self.__remark_text

    @remark_text.setter
    def remark_text(self, remark_text):
        self.__remark_text = remark_text  

    
    def __str__(self) -> str:
        return f'id:{self.customer_id} category:{self.remark_category} route:{self.__route} time:{self.__timestamp} comment{self.__remark_text}'

print('hello world')