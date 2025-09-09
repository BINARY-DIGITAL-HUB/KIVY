import turtle
from textblob import TextBlob


comment = "the customer service is poor"


class Remark_Sentiment:

    def __init__(self, comments) -> None:
        
        self.analysis_list = dict()
        print('COMMNET LENGHT ', len(comments))
        index = 0
        for comment in comments:
            self.blob = TextBlob(comment)
            sentiment , polarity = self.blob.sentiment
            self.analysis_list[index] = [sentiment*100 , comment]
            index +=1

        for key, item in self.analysis_list.items():
            print(f'key  : {key} == sentiment and comment : {item[0]},{item[1]}')

    def get_positive_review(self)->turtle:
        count = 0
        sentiment_data = []
        for sentiment, comments in self.analysis_list.items():
           # print(f'comment : {item} == sentiment : {key}')
            if int(comments[0]) >= 0 :
                count+= 1
                comment , sentiment = comments
                sentiment_data.append((comment , sentiment)) 

        return sentiment_data , count


    # def get_low_positive_review(self)->turtle:
    #     count = 0
    #     sentiment_data = []
    #     for sentiment, comments in self.analysis_list.items():
    #        # print(f'comment : {item} == sentiment : {key}')
    #         if int(comments[0]>=0) and int(comments[0]) <= 35 :
    #             count+= 1
    #             comment , sentiment = comments
    #             sentiment_data.append((comment , sentiment)) 

    #     return sentiment_data , count

   
    # def get_low_negative_review(self)->turtle:
    #     count = 0
    #     sentiment_data = []
    #     for sentiment, comments in self.analysis_list.items():
    #        # print(f'comment : {item} == sentiment : {key}')
    #         if int(comments[0]) > 0 and int(sentiment) < -35 :
    #             count+= 1
    #             comment , sentiment = comments
    #             sentiment_data.append((comment , sentiment)) 


        return sentiment_data , count

    def get_negative_review(self)->turtle:
        count = 0
        sentiment_data = []
        for sentiment, comments in self.analysis_list.items():
           # print(f'comment : {item} == sentiment : {key}')
            if int(comments[0]) < 0 :
                print('HIGH NEGATIVE ============= ', comments[0])
                count+= 1
                comment , sentiment = comments
                sentiment_data.append((comment , sentiment)) 


        return sentiment_data, count
   
# my_comments = ["this is a good service" , 'the management is very good well' , 'the customer manager is trying']


import database as db 

data = db.Database()
remark = data.fetch_all_remark()

# for r in remark:
#     print('remark' , str(r.remark_text))

remarks = [com.remark_text for com in remark]

print('remark _text ', remarks)


rm = Remark_Sentiment(remarks)

# print('high positive : ' , [r for r in rm.get_high_positive_review()])
# print('HGITH NEGATIVE : ',[r for r in rm.get_high_negative_review()])
# print('low positive : ' ,[r for r in rm.get_low_positive_review()])
print('low NEGATIVE : ' ,[r for r in rm.get_negative_review()])



p_riview = [r for r in rm.get_negative_review()]
print(p_riview[1]) 