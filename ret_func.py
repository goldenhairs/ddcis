import datetime as dt
import akshare as ak
import matplotlib.pyplot as plt
import numpy as np
from sql_py import cx_db_fund,cx_fund_his
import ak_sql as asq
from dt_color import colors,default_format_date

df=cx_db_fund()
fund_code=list(df['基金代码'].head(10))

def ret_func():
    m=0
    x = dict()
    y = dict()
    z = dict()
    for i in fund_code:
        m+=1
        try:
            df=cx_fund_his(fund_code=i)        
        except Exception as e:
            print(e)
            print("正在下载。。。")
            asq.down_ak_m_fund_his(i)
            pass
        finally:
            x[m]=list(df.head(30)['净值日期'])
            x[m].reverse()
            y[m]=list(df.head(30)['每万份收益'])
            y[m].reverse()
            y[m]= list(map(float,y[m]))
            z[m]=list(df.head(30)['每万份收益']) 
            z[m].reverse()
            z[m] = list(map(float,z[m]))            
            return(x[m],y[m],z[m])


print(ret_func())


