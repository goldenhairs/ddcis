import pandas as pd
import tushare as ts
import numpy as np
import time
import random
from token_list import ts_engine,pro,stock_names
from sqlalchemy import create_engine

def ts_marketdata_download():
    #data_api
    #ts_market_datas=['daily','weekly','monthly','pro_bar','adj_factor','suspend','suspend_d','daily_basic','moneyflow','stk_limit','limit_list','moneyflow_hsgt','hsgt_top10','hk_hold','ggt_daily','ggt_monthly','bak_daily']
    ts_market_datas=['moneyflow','stk_limit','limit_list','moneyflow_hsgt','hsgt_top10','hk_hold','ggt_daily','ggt_monthly','bak_daily']
    start_date=input("请输入开始下载起始日期，如20201101：")
    end_date=input("请输入开始下载终止日期日期，如20201118：")
    trade_date=input("请输入查询的交易日期,如20201118：")
    for ts_market_data in ts_market_datas:
        if ts_market_data=="daily"or"weekly"or"monthly":
            for stock_name in stock_names:
                print(stock_name)
                data = pro.query("%s"%ts_market_data,ts_code="%s"%stock_name,start_date='%s'%start_date,end_date='%s'%end_date)
                data.to_sql("%s"%ts_market_data,con=ts_engine,if_exists="append",index=False)
            print("完成：",ts_market_data)
        elif ts_market_data=="pro_bar":
            for stock_name in stock_names:
                data=ts.pro_bar(ts_code='%s'%stock_name,adj='qfq',start_date='%s'%start_date,end_date='%s'%end_date)
                data.to_sql("%s"%ts_market_data+'qfq',con=ts_engine,if_exists="append",index=False)
                data=ts.pro_bar(ts_code='%s'%stock_name,adj='hfq',start_date='%s'%start_date,end_date='%s'%end_date)
                data.to_sql("%s"%ts_market_data+'hfq',con=ts_engine,if_exists="append",index=False)
                #上证指数
                data=ts.pro_bar(ts_code='000001.SH', asset='I',start_date='%s'%start_date,end_date='%s'%end_date)
                data.to_sql("%s"%ts_market_data+"上证综指",con=ts_engine,if_exists="append",index=False)

        elif ts_market_data=="suspend_d":
            data = pro.suspend_d(suspend_type='S', trade_date='%s'%trade_date)
            data.to_sql("%s"%ts_market_data,con=ts_engine,if_exists="append",index=False)
        elif ts_market_data=="moneyflow":
            data = pro.moneyflow(trade_date='%s'%trade_date)
            data.to_sql("%s"%ts_market_data,con=ts_engine,if_exists="append",index=False)
        elif ts_market_data=="stk_limit":
            data = pro.stk_limit(trade_date='%s'%trade_date)
            data.to_sql("%s"%ts_market_data,con=ts_engine,if_exists="append",index=False)
        elif ts_market_data=="limit_list":
            data = pro.limit_list(trade_date='%s'%trade_date)
            data.to_sql("%s"%ts_market_data,con=ts_engine,if_exists="append",index=False)
        elif ts_market_data=="moneyflow_hsgt": 
            data=pro.query('moneyflow_hsgt',trade_date='%s'%trade_date)
            data.to_sql("%s"%ts_market_data,con=ts_engine,if_exists="append",index=False)
        elif ts_market_data=="hk_hold": 
            data = pro.hk_hold(trade_date='%s'%trade_date)
            data.to_sql("%s"%ts_market_data,con=ts_engine,if_exists="append",index=False)
        elif ts_market_data=="ggt_daily": 
            data = pro.ggt_daily(start_date='%s'%start_date,end_date='%s'%end_date)
            data.to_sql("%s"%ts_market_data,con=ts_engine,if_exists="append",index=False)
        elif ts_market_data=="ggt_monthly":
            data = pro.ggt_monthly(start_date='%s'%start_date[:6],end_date='%s'%end_date[:6])
            data.to_sql("%s"%ts_market_data,con=ts_engine,if_exists="append",index=False)
        #其他接口有 adj_factor、suspend、hsgt_top10
        else:
            for stock_name in stock_names:
                data = pro.query('%s'%ts_market_data, ts_code="%s"%stock_name)
                data.to_sql("%s"%ts_market_data,con=ts_engine,if_exists="append",index=False)


