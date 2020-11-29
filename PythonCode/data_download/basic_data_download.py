from token_list import pro,ts_engine,stock_names
import random
import time

def basic_data_download():
    #数据接口列表
    ts_basic_data=['stock_basic','trade_cal','namechange','hs_const','stock_company','stk_managers','stk_rewards','new_share']
    #临时列表
    #ts_basic_data=['stk_rewards']

    #下载数据
    for basic_data_name in ts_basic_data:
        if basic_data_name=="hs_const":       
            data=pro.query("hs_const",hs_type='SH')
            data.to_sql("hs_const_sh",con=ts_engine,if_exists="append",index=False)
            data=pro.query("hs_const",hs_type='SZ')
            data.to_sql("hs_const_sz",con=ts_engine,if_exists="append",index=False)
        elif basic_data_name=="stk_rewards": 
            #需要增加一个终端以后，从中断的地方开始的功能，避免每次都重新从0开始。目前中断股票代码000950.SZ
            stock_name=input("请输入上次中断的股票代码,如000001.SZ:")
            #找到上次中断股票的索引
            index=stock_names.index(stock_name)
            for index in range(index,len(stock_names)+1): 
                t=random.randint(5,13)           
                data = pro.query('stk_rewards',ts_code="%s"%stock_names[index])
                data.to_sql("stk_rewards",con=ts_engine,if_exists="append",index=False)
                print(stock_names[index])
                index +=1
                #2000积分需要休息5秒，5000积分无限制不需要下面一条语句
                time.sleep(t)
                
            # for stock_name in stock_names:
            #     data = pro.query('stk_rewards',ts_code="%s"%st868.SHk_name)
            #     data.to_sql("stk_rewards",con=ts_engine,if_exists="append",index=False)
            #     print(stock_name)
            #     print(len(stock_names(stock_name)))
            #     #2000积分需要休息5秒，5000积分无限制不需要下面一条语句
            #     time.sleep(5)
        else:
            data = pro.query('%s'%basic_data_name)
            data.to_sql("%s"%basic_data_name,con=ts_engine,if_exists="append",index=False)
            #2000积分需要休息5秒，5000积分无限制不需要下面一条语句
            #time.sleep(5)
            print("======================="+"%s"%basic_data_name+"已完成======================")