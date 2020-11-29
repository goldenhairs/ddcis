import pandas as pd
from sqlalchemy import create_engine

#xlsx导入mssql数据库
def xlsx2_mssql():
    mypath="d:/bookstore.xlsx"
    df=pd.read_excel(mypath)
    engine=create_engine("mssql+pymssql://sa:123456@127.0.0.1:1433/bookstore?charset=utf8",echo=True)
    df.to_sql("%s"%mypath[3:-5],con=engine,if_exists="replace",index=False)


