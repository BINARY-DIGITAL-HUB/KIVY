
import sqlite3 as database
from user import User
from remark import Remark
import datetime as dt 

class Database:
    
    connection = None 
    def __init__(self) -> None:
        with database.connect('airmark_database.db') as db:
            Database.connection = db 
            print('database connected....')

# ===================== REMARK DATABASE ==========================
#customer_id, ticket_id, remark_category, timestamp, remark, route, remark_text
    def create_remark_table(self):
        Database.connection.execute("""CREATE TABLE IF NOT EXISTS airmark_remark(
            id TEXT NOT NULL,
            ticket_id TEXT NOT NULL, 
            remark_category TEXT NOT NULL,
            timestamp TEXT NOT NULL, 
            route TEXT NOT NULL,
            remark_text TEXT NOT NULL
        ) 

        """)

        Database.connection.commit()
        print('REMARK TABLE CREATED SUCCESSFULLY..')

    def add_remark(self, remark):
        id = remark.customer_id 
        ticket_id = remark.ticket_id
        remark_category = remark.remark_category
        timestamp = remark.timestamp
        route = remark.route
        text = remark.remark_text
        print(text)
        Database.connection.execute(
            'INSERT INTO airmark_remark VALUES(?,?,?,?,?,?)', (id, ticket_id, remark_category, timestamp,route, text)
            )
        Database.connection.commit()
        print(remark , '  ....inserted.....')



    def fetch_all_remark(self):
        remark_list = []
        cr = Database.connection.cursor().execute('SELECT * FROM airmark_remark')
        data = cr.fetchall()
        for remark in data:
            us = Remark(remark[0], remark[1], remark[2], remark[3], remark[4], remark[5])
            remark_list.append(us)
        return remark_list

    def drop_remark_table(self):
        Database.connection.execute('DROP TABLE airmark_remark')
        print('remark table deleted successfully ')

# ======================= END REMARK DATABASE ====================



# ===================== USER DATABASE ==========================
    def create_table(self):
        Database.connection.execute("""CREATE TABLE IF NOT EXISTS airmark_user(
        id TEXT PRIMARY KEY NOT NULL, 
        name TEXT NOT NULL,
        age INT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL, 
        sex INT NOT NULL
        )
        """)
        Database.connection.commit()
        print('account table created successfully...')


    def add_user(self, user):
        id = user.id 
        name = user.name
        age= user.age
        email = user.email
        password = user.password
        sex = user.sex
        print(name)
        Database.connection.execute(
            'INSERT INTO airmark_user VALUES(?,?,?,?,?,?)', (id, name, age, email, password,sex)
            )
        Database.connection.commit()
        print(user , '  ....inserted.....')


    def fetch_users(self):
        user_list = []
        cr = Database.connection.cursor().execute('SELECT * FROM airmark_user')
        data = cr.fetchall()
        for user in data:
            us = User(user[0], user[1], user[2], user[3], user[4], user[5])
            user_list.append(us)
        return user_list
    
    def fetch_user(self, user_id):
        cursor = Database.connection.cursor().execute('SELECT * FROM airmark_user') 
        for item in cursor:
            id, *other = item  
            if id.strip() == user_id:
                id, name, age, email, password, sex = item
                user = User(id, name, age, email, password, sex)
                print(item)
        return user
    def validate_user(self, credentials):
        email, passwd = credentials
        validate = False
        credential = Database.connection.execute('SELECT email, password FROM airmark_user WHERE email=? AND password=? ', (email, passwd))
        for cred in credential:
            validate = True
            break
    
        return validate 


    def drop_table(self):
        Database.connection.execute('DROP TABLE airmark_user')
        print('table deleted successfully ')


# ======================= END USER DATABASE ====================


data = Database()
# user = data.fetch_user('12345')

# print(str(user.name))
# data.create_table()

# users = [
#     User('12345' , 'abdulsalam taofeek', 25, 'kinshat1995@gmail.com', '12345', 1),
#     User('12346' , 'abdulsalam ahmed', 23, 'ahmed1995@gmail.com', '12346', 1),
#     User('12347' , 'abdulsalam qudus', 18, 'qudus1995@gmail.com', '12347', 1),
# ]
# for user in users:
#    data.add_user(user)

#

# con = data.validate_user(['ahmed1995@gmail.com',12346])
# print(con)
#print ([str(user) for user in data.fetch_users()])

#customer_id, ticket_id, remark_category, timestamp, remark, route, remark_text


# data.create_remark_table()
# x = dt.datetime.now()
# print('data :' , x.strftime('%d %b, %Y %I:%M:%S'))
# print(x.isoformat())
# timestamp = x.strftime('%d %b, %Y %I:%M:%S')

# remarks = [
#     # Remark('12345' , 'ticket_12345', 'customer service', timestamp , 'lagos-minna', 'very bad customer service'),
#     # Remark('12346' , 'ticket_12346', 'theft issue', timestamp,  'abuja-lagos', 'very bad in keeping items'),
#     # Remark('12347' , 'ticket_12347', 'management issue', timestamp,  'kano-ibadan', 'no composure in managing customer'),
#     # Remark('12345' , 'ticket_12345', 'customer service', timestamp , 'lagos-minna', 'worst in term of custormer service'),
# #     Remark('12346' , 'ticket_12346', 'theft issue', timestamp,  'abuja-lagos', 'no issue related to lost of item'),
# #     Remark('12347' , 'ticket_12347', 'management issue', timestamp,  'kano-ibadan', 'they are not compose in managing customer'),
# #     Remark('12345' , 'ticket_12345', 'customer service', timestamp , 'lagos-minna', 'they have a good customer service'),
# #     Remark('12346' , 'ticket_12346', 'theft issue', timestamp,  'abuja-lagos', 'no issue related to lost of item'),
# #     Remark('12347' , 'ticket_12347', 'management issue', timestamp,  'kano-ibadan', 'they are not compose in managing customer'),
# #     Remark('12345' , 'ticket_12345', 'customer service', timestamp , 'lagos-minna', 'they have a good customer service'),
# #     Remark('12346' , 'ticket_12346', 'theft issue', timestamp,  'abuja-lagos', 'no issue related to lost of item'),
# #     Remark('12347' , 'ticket_12347', 'management issue', timestamp,  'kano-ibadan', 'they are not compose in managing customer')
#  ]


# for remark in remarks:
#     data.add_remark(remark)

# # print('all comment placed')

# # for remark in data.fetch_all_remark():
# #     print(str(remark))

# # # data.drop_remark_table()