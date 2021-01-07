'''
这个模块是从akshare取货币基金排名及历史净值、实时数据存储到数据库
'''
import akshare as ak 
from sqlalchemy import create_engine
import datetime as dt
ak_engine = create_engine('mysql+pymysql://root:123456@localhost:3306/akshare_db?charset=utf8')

default_date=dt.date.today()
default_format_date=default_date.strftime("%Y%m%d")

#从ak数据网站读取货币基金排行,把数据存入mysql（数据来源东方财富网站-天天基金网）
def down_ak_m_fund_rank(date=default_format_date):
    df=ak.fund_em_money_rank()
    df.to_sql('fund_rank_%s'%date,con=ak_engine,if_exists="append",index=False)
    return df


#采集货币型基金-历史数据把数据存入mysql（数据来源东方财富网站-天天基金网）
def down_ak_m_fund_his(fund_code):
    df=ak.fund_em_money_fund_info(fund=fund_code)
    df.to_sql(fund_code,con=ak_engine,if_exists="append",index=False)
    return df

#采集货币型基金-实时数据（数据来源东方财富网站-天天基金网）
def down_ak_m_fund_daily():
    df=ak.fund_em_money_fund_daily()
    print(df)

#定义主函数
def main():
    #down_ak_m_fund_his('000533')
    #down_ak_m_fund_rank(date=default_format_date)
    pass


if __name__=="__main__":
    pass
else:
    print("当日货币基金排行函数或货基下载历史数据函数被调用！")   
