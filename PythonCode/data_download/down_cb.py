#下载可转债数据
from token_list import pro,ts_engine,cb_codes
import time
import random

#可转债基本信息
def down_cb_basic():
    df=pro.cb_basic()
    #存储到数据库
    df.to_sql("cb_basic",con=ts_engine,if_exists="append",index=False)
    print(df)


#可转债发行
def down_cb_issue():
    df=pro.cb_issue()
    df.to_sql("cb_issue",con=ts_engine,if_exists="append",index=False)
    print(df)

#可转债行情
def down_cb_daily():
    cb_code=input("请输入可转债起始代码，如果是第一次运行请输入125002.SZ，如果是中断继续请输入上次中断时的代码：")
    index = cb_codes.index(cb_code)
    for i in range(index,len(cb_codes)):
        df=pro.cb_daily(ts_code=cb_codes[i])
        df.to_sql("cb_daily",con=ts_engine,if_exists="append",index=False)
        print("用时较长，如果中断请从输入这个代码：%s，重新运行。"%cb_codes[i])
        print(df)    


#可转债转股价变动
def down_cb_price_chg():
    cb_code=input("请输入可转债起始代码，如果是第一次运行请输入125002.SZ，如果是中断继续请输入上次中断时的代码：")
    index = cb_codes.index(cb_code)
    for i in range(index,len(cb_codes)):
        df=pro.cb_price_chg(ts_code=cb_codes[i])
        df.to_sql("cb_price_chg",con=ts_engine,if_exists="append",index=False)
        print("用时较长，如果中断请从输入这个代码：%s，重新运行。"%cb_codes[i])
        print(df)   

#可转债转股结果
def down_cb_share():
    cb_code=input("请输入可转债起始代码，如果是第一次运行请输入125002.SZ，如果是中断继续请输入上次中断时的代码：")
    index = cb_codes.index(cb_code)
    for i in range(index,len(cb_codes)):
        df=pro.cb_share(ts_code=cb_codes[i])
        df.to_sql("cb_share",con=ts_engine,if_exists="append",index=False)
        print("用时较长，如果中断请从输入这个代码：%s，重新运行。"%cb_codes[i])
        print(df)   

#债券回购日行情
def down_repo_daily():
    date=input("请输入查询日期如20201201：")
    df=pro.repo_daily(trade_date=date)
    df.to_sql("cb_repo_daily",con=ts_engine,if_exists="append",index=False)
    print(df)


#财经日历,每分钟限制访问20次
def down_eco_cal():
    for i in range(0,10000,100):
        df=pro.eco_cal(offset=i)
        df.to_sql("cb_eco_cale",con=ts_engine,if_exists="append",index=False)
        time.sleep(3)
        print(df)

