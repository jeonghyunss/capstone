import scipy.io
import csv
import pymysql
import pandas as pd
from sqlalchemy import create_engine

# db 연결을 얻어오는 클래스
class DBConnector:
    
#   private member variable

    __host = '127.0.0.1'
    __user = 'root'
    __password ='1234'
    __db = 'capstone'
    __charset = 'utf8'

    def __init__(self) :
        
        print('init DBConnector')
        
    def getDBConnection(self) :
        
        cursorclass = pymysql.cursors.DictCursor
        
        conn = pymysql.connect(host=self.__host, user=self.__user, password=self.__password,

                       db=self.__db, charset=self.__charset,cursorclass=cursorclass)
        
        return conn

    def getDBEngine(self) :
        
        engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user=self.__user,
                               pw=self.__password,
                               db=self.__db))
        
        return engine
    

# table로 부터 데이터를 얻어오는 클래스
class DataGetter:
    
#   DBConnector를 인수로 전달

    def __init__(self,connector) :
        
        self.connector = connector

    def selectData(self,start,end) :
        
        conn = self.connector.getDBConnection()
          
        curs = conn.cursor()
        
        query = "SELECT * FROM test_data WHERE date >= '" +  start +  "' AND date < '" + end + "'"
        
        curs.execute(query)
        
        result = curs.fetchall()
        
        data = pd.DataFrame(result).set_index(['date'])

        return data

# mysql 스키마를 생성한 후 db에 스키마 이름이 들어가야 됨
# conn = pymysql.connect(host='127.0.0.1', user='root', password='1234',

#                        db='capstone', charset='utf8',cursorclass=pymysql.cursors.DictCursor)

# conn.commit()

# # table을 dataframe으로 저장
# curs = conn.cursor()
# curs.execute("SELECT * FROM test_data WHERE date >= '2015-01-01' AND date < '2016-12-31'")

# result = curs.fetchall()

# df = pd.DataFrame(result)
# df
    
# # create table
# # mycursor.execute("CREATE TABLE customers(name VARCHAR(255), address VARCHAR(255))")

# # read csv Data to dataframe
# data= pd.read_excel('sejong_power_consumption_per_hour_train_data.xlsx', index=True,index_col='date',sheet_name ="Sheet1" )
# data

# # create sqlalchemy engine
# engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
#                        .format(user="root",
#                                pw="1234",
#                                db="capstone"))

# # read csv Data to dataframe
# data= pd.read_excel('sejong_power_consumption_per_hour_train_data.xlsx', index=True,index_col='date',sheet_name ="Sheet1" )

# # save dataframe to table
# data.to_sql('test_data', con = engine, if_exists = 'append', chunksize = 1000)

# # read table to datafram
# conn = engine.connect()
# data = pd.read_sql_table('test_data',conn,index_col='date')
# data


# connector = DBConnector()
# connector


# # In[3]:


# conn = connector.getDBConnection()
# conn


# # In[8]:


# getter = DataGetter(conn)
# df = getter.selectData('2015-01-01','2020-01-01')


# # In[9]:


# df


# # In[93]:


# conn = test2.connect()
# data = pd.read_sql_table('test_data',conn,index_col='date')
# data


# # In[ ]:


# connector = DB

