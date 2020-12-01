from token_list import pro,ts_engine,fund_ts_codes,fund_types,szsh_fund_codes
import random
import time
#公募基金列表
def down_fund_basic():
    #注意分页参数offset='10000'
    df = pro.fund_basic()
    df.to_sql("fund_basic_all",con=ts_engine,if_exists="append",index=False)
    print(df)


#公募基金公司
def down_fund_company():
    df=pro.fund_company()
    df.to_sql("fund_company",con=ts_engine,if_exists="append",index=False)
    print(df)

#基金经理
def down_fund_manager():
    fund_ts_code=input("请输入股票的起始代码，如果是第一次运行请输入010650.OF，如果是中断继续请输入上次中断时的基金代码：")
    index = fund_ts_codes.index(fund_ts_code)
    for i in range(index,len(fund_ts_codes)):
        #t=random.randint(5,13)
        df=pro.fund_manager(ts_code=fund_ts_codes[i])
        df.to_sql("fund_manager",con=ts_engine,if_exists="append",index=False)
        print("用时较长，如果中断请从输入这个代码：%s，重新运行。"%fund_ts_codes[i])
        #time.sleep(t)
        print(df)

#基金规模数据
def down_fund_share():
    fund_ts_code=input("请输入股票的起始代码，如果是第一次运行请输入010650.OF，如果是中断继续请输入上次中断时的基金代码：")
    index = fund_ts_codes.index(fund_ts_code)
    for i in range(index,len(fund_ts_codes)):
        df=pro.fund_share(ts_code=fund_ts_codes[i])
        df.to_sql("fund_share",con=ts_engine,if_exists="append",index=False)
        print("用时较长，如果中断请从输入这个代码：%s，重新运行。"%fund_ts_codes[i])
        #print(df)



#公募基金净值
def down_fund_nav():
    fund_ts_code=input("请输入股票的起始代码，如果是第一次运行请输入010650.OF，如果是中断继续请输入上次中断时的基金代码：")
    index = fund_ts_codes.index(fund_ts_code)
    for i in range(index,len(fund_ts_codes)):
        df=pro.fund_nav(ts_code=fund_ts_codes[i])
        df.to_sql("fund_nav",con=ts_engine,if_exists="append",index=False)
        print("用时较长，如果中断请从输入这个代码：%s，重新运行。"%fund_ts_codes[i])
        print(df)
 

#公募基金分红,每分钟最多访问60次
def down_fund_div():
    fund_ts_code=input("请输入股票的起始代码，如果是第一次运行请输入010650.OF，如果是中断继续请输入上次中断时的基金代码：")
    index = fund_ts_codes.index(fund_ts_code)
    for i in range(index,len(fund_ts_codes)):
        df=pro.fund_div(ts_code=fund_ts_codes[i])
        df.to_sql("fund_div",con=ts_engine,if_exists="append",index=False)
        print("用时较长，如果中断请从输入这个代码：%s，重新运行。"%fund_ts_codes[i])
        print(df)

#公募基金持仓数据
def down_fund_portfolio():
    fund_ts_code=input("请输入股票的起始代码，如果是第一次运行请输入010650.OF，如果是中断继续请输入上次中断时的基金代码：")
    index = fund_ts_codes.index(fund_ts_code)
    for i in range(index,len(fund_ts_codes)):
        t=random.randint(1,5)
        df=pro.fund_portfolio(ts_code=fund_ts_codes[i])
        df.to_sql("fund_portfolio",con=ts_engine,if_exists="append",index=False)
        print("用时较长，如果中断请从输入这个代码：%s，重新运行。"%fund_ts_codes[i])
        print(df)
        time.sleep(t)


#场内基金日线行情
def down_fund_daily():
    szsh_fund_code=input("请输入股票的起始代码，如果是第一次运行请输入010650.OF，如果是中断继续请输入上次中断时的基金代码：")
    index = szsh_fund_codes.index(szsh_fund_code)
    for i in range(index,len(szsh_fund_codes)):
        df=pro.fund_daily(ts_code=szsh_fund_codes[i])
        df.to_sql("fund_daily",con=ts_engine,if_exists="append",index=False)
        print("用时较长，如果中断请从输入这个代码：%s，重新运行。"%szsh_fund_codes[i])
        print(df)
        time.sleep(0.5)


#基金复权因子,可设置分页显示
def down_fund_adj():
    offset_index=int(input("请输入起始页码，如果是第一次运行请输入0，如果是中断继续请输入上次中断时的页码："))
    for i in range(offset_index,1000000,2000):
        df=pro.fund_adj(offset=i)
        df.to_sql("fund_adj",con=ts_engine,if_exists="append",index=False)
        print("用时较长，如果中断请从输入这个代码%s，重新运行。"%i)
        print(df)

