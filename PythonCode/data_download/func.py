import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import psycopg2
import os,sys
import MySQLdb
import random

myfile="d:/bookstore1.xlsx"
mypath="e:/ddcis"

#r"e:\ddcis"
#xlsx导入mssql数据库
def xlsx2_mssql():
    df=pd.read_excel(myfile)
    engine=create_engine("mssql+pymssql://sa:123456@127.0.0.1:1433/bookstore?charset=utf8",echo=True)
    df.to_sql("%s"%myfile[3:-5],con=engine,if_exists="replace",index=False)


#xlsx导入postgrel数据库
def xlsx2_posgrel():
    df=pd.read_excel(myfile)
    engine = create_engine("postgresql+psycopg2://odoo:odoo@127.0.0.1/sss")
    df.to_sql("myfile",con=engine,if_exists="replace",index=False)

#列出指定目录下的所有文件
def get_file_path(root_path):
    dir_list=[]
    file_list=[]
    #获取该目录下所有的文件名称和目录名称
    dir_or_files = os.listdir(root_path)
    for dir_file in dir_or_files:
        #获取目录或者文件的路径
        dir_file_path = os.path.join(root_path,dir_file)
        #判断该路径为文件还是路径
        if os.path.isdir(dir_file_path):
            dir_list.append(dir_file_path)
            #递归获取所有文件和目录的路径
            get_file_path(dir_file_path)
        else:
            file_list.append(dir_file_path)
    print(file_list)
    print(dir_list)


#数据库查询
def cx_db():
    try:
        conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',db='akshare_db',charset='utf8')
    except Exception as e:
        print(e)
        sys.exit()
    cursor=conn.cursor()
    sql = "select * from tushare_db.stock_basic"
    df=pd.read_sql(sql,conn)    
    cursor.close()
    conn.close()
    print(df)


#随机颜色
def r_color():
    a=random.randint(0,1)
    b=random.randint(0,1)
    c=random.randint(0,1)
    return a,b,c



        
     
