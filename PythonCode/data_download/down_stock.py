from token_list import pro,ts_engine,stock_names,id,markets,index_cn,level_sw,index_codes
from token_list import sect_names,ts_index_codes
import random
import time

#下载沪深股票数据并存储到数据库
def down_stock_basic():
    df=pro.query("stock_basic")
    df.to_sql("stock_basic",con=ts_engine,if_exists="append",index=False)
    print(df)
  

def down_trade_cal():
    df=pro.query("trade_cal")
    df.to_sql("trade_cal",con=ts_engine,if_exists="append",index=False)
    print(df)

def down_namechange():
    df=pro.query("namechange")
    df.to_sql("namechange",con=ts_engine,if_exists="append",index=False)
    print(df)

def down_hs_const():
    #code=input("请输入沪深股通成份股，SZ或者SH:")
    df=pro.query("hs_const",hs_type="SZ")
    df.to_sql("hs_const",con=ts_engine,if_exists="append",index=False)
    df=pro.query("hs_const",hs_type="SH")
    df.to_sql("hs_const",con=ts_engine,if_exists="append",index=False)
    print(df)
def down_stock_company():
    df=pro.query("stock_company")
    df.to_sql("stock_company",con=ts_engine,if_exists="append",index=False)
    print(df)

def down_stk_managers():
    stock_name=input("请输入股票的起始代码，如果是第一次运行请输入000001.SZ，如果是中断继续请输入上次中断时的股票代码：")
    index = stock_names.index(stock_name)
    for i in range(index,len(stock_names)+1):
        #t=random.randint(5,13)
        df=pro.stk_managers(ts_code=stock_names[i])
        df.to_sql("stock_managers",con=ts_engine,if_exists="append",index=False)
        print("用时较长，如果中断请从输入这个代码：%s，重新运行。"%stock_names[i])
        #time.sleep(t)
        

def down_stk_rewards():
    stock_name=input("请输入股票的起始代码，如果是第一次运行请输入000001.SZ，如果是中断继续请输入上次中断时的股票代码：")
    index = stock_names.index(stock_name)
    for i in range(index,len(stock_names)+1):
        #t=random.randint(5,13)
        df=pro.stk_rewards(ts_code=stock_names[i])
        df.to_sql("stock_rewards",con=ts_engine,if_exists="append",index=True)
        print("用时较长，如果中断请从输入这个代码：%s，重新运行。"%stock_names[i])
        #time.sleep(t)

def down_new_share():
    start_date=input("请输入开始日期,如20201130:")
    df=pro.query("new_share",start_date=start_date)
    df.to_sql("new_share",con=ts_engine,if_exists="append",index=False)
    print(df)


#下载股票行情数据
def down_basic():
    stock_name=input("请输入股票的起始代码，如果是第一次运行请输入000001.SZ，如果是中断继续请输入上次中断时的股票代码：")
    index = stock_names.index(stock_name)
    for i in range(index,len(stock_names)+1):
        #t=random.randint(5,13)
        df=pro.basic(ts_code=stock_names[i])
        df.to_sql("basic",con=ts_engine,if_exists="append",index=False)
        print("用时较长，如果中断请从输入这个代码：%s，重新运行。"%stock_names[i])
        #time.sleep(t)
        # print(df)

def down_weekly():
    stock_name=input("请输入股票的起始代码，如果是第一次运行请输入000001.SZ，如果是中断继续请输入上次中断时的股票代码：")
    index = stock_names.index(stock_name)
    for i in range(index,len(stock_names)+1):
        #t=random.randint(5,13)
        df=pro.weekly(ts_code=stock_names[i])
        df.to_sql("weekly",con=ts_engine,if_exists="append",index=False)
        print("用时较长，如果中断请从输入这个代码：%s，重新运行。"%stock_names[i])
        #time.sleep(t)
        # print(df)


def down_monthly():
    stock_name=input("请输入股票的起始代码，如果是第一次运行请输入000001.SZ，如果是中断继续请输入上次中断时的股票代码：")
    index = stock_names.index(stock_name)
    for i in range(index,len(stock_names)+1):
        #t=random.randint(5,13)
        df=pro.monthly(ts_code=stock_names[i])
        df.to_sql("monthly",con=ts_engine,if_exists="append",index=False)
        print("用时较长，如果中断请从输入这个代码：%s，重新运行。"%stock_names[i])
        #time.sleep(t)
        # print(df)

#复权行情
def down_pro_bar():
    pass

def down_adj_factor():
    pass

def down_suspend():
    stock_name=input("请输入股票的起始代码，如果是第一次运行请输入000001.SZ，如果是中断继续请输入上次中断时的股票代码：")
    index = stock_names.index(stock_name)
    for i in range(index,len(stock_names)+1):
        #t=random.randint(5,13)
        df=pro.suspend(ts_code=stock_names[i])
        df.to_sql("suspend",con=ts_engine,if_exists="append",index=False)
        print("用时较长，如果中断请从输入这个代码：%s，重新运行。"%stock_names[i])
        #time.sleep(t)
        # print(df)

def down_basic_basic():
    stock_name=input("请输入股票的起始代码，如果是第一次运行请输入000001.SZ，如果是中断继续请输入上次中断时的股票代码：")
    index = stock_names.index(stock_name)
    for i in range(index,len(stock_names)+1):
        #t=random.randint(5,13)
        df=pro.basic_basic(ts_code=stock_names[i])
        df.to_sql("basic_basic",con=ts_engine,if_exists="append",index=False)
        print("用时较长，如果中断请从输入这个代码：%s，重新运行。"%stock_names[i])
        #time.sleep(t)
        #print(df)

def down_moneyflow():
    stock_name=input("请输入股票的起始代码，如果是第一次运行请输入000001.SZ，如果是中断继续请输入上次中断时的股票代码：")
    index = stock_names.index(stock_name)
    for i in range(index,len(stock_names)+1):
        #t=random.randint(5,13)
        df=pro.moneyflow(ts_code=stock_names[i])
        df.to_sql("moneyflow",con=ts_engine,if_exists="append",index=False)
        print("用时较长，如果中断请从输入这个代码：%s，重新运行。"%stock_names[i])
        #time.sleep(t)
        #print(df)

def down_stk_limit():
    date=input("请输入查询日期，如20201130:")
    df = pro.stk_limit(trade_date=date)
    df.to_sql("stk_limit",con=ts_engine,if_exists="append",index=False)
    print(df)


def down_limit_list():
    date=input("请输入查询日期，如20201130:")
    df = pro.limit_list(trade_date=date)
    df.to_sql("limit_list",con=ts_engine,if_exists="append",index=False)
    print(df)


def down_moneyflow_hsgt():
    date=input("请输入查询日期，如20201130:")
    df=pro.query('moneyflow_hsgt', trade_date=date)
    df.to_sql("moneyflow_hsgt",con=ts_engine,if_exists="append",index=False)
    print(df)

def down_hsgt_top10():
    date=input("请输入查询日期，如20201130:")
    df=pro.hsgt_top10(trade_date=date)
    df.to_sql("hsgt_top10",con=ts_engine,if_exists="append",index=False)

#沪深港股通持股明细
def down_hk_hold():
    date=input("请输入查询交易日期，如20201130:")
    df = pro.hk_hold(trade_date=date)
    df.to_sql("hk_hold",con=ts_engine,if_exists="append",index=False)

#港股通每日成交统计，有访问次数限制
def down_ggt_basic():
    date=input("请输入查询交易日期，如20201130:")
    df = pro.ggt_basic(trade_date=date)
    df.to_sql("ggt_basic",con=ts_engine,if_exists="append",index=False)
    print(df)

def down_ggt_monthly():
    date=input("请输入查询交易日期，如202011:")
    df = pro.ggt_monthly(trade_date=date)
    df.to_sql("ggt_monthly",con=ts_engine,if_exists="append",index=False)
    print(df)

def down_bak_basic():
    df=pro.bak_basic(offset='2')
    df.to_sql("bak_basic",con=ts_engine,if_exists="append",index=False)
    print(df)

#下载财务指标
#公司利润表
def down_income():
    stock_name=input("请输入股票的起始代码，如果是第一次运行请输入000001.SZ，如果是中断继续请输入上次中断时的股票代码：")
    index = stock_names.index(stock_name)
    for i in range(index,len(stock_names)+1):
        #t=random.randint(5,13)
        df=pro.income(ts_code=stock_names[i])
        df.to_sql("income",con=ts_engine,if_exists="append",index=False)
        print("用时较长，如果中断请从输入这个代码：%s，重新运行。"%stock_names[i])
        #time.sleep(t)
        # print(df)
#公司资产负债表
def down_balancesheet():
    stock_name=input("请输入股票的起始代码，如果是第一次运行请输入000001.SZ，如果是中断继续请输入上次中断时的股票代码：")
    index = stock_names.index(stock_name)
    for i in range(index,len(stock_names)+1):
        #t=random.randint(5,13)
        df=pro.balancesheet(ts_code=stock_names[i])
        df.to_sql("balancesheet",con=ts_engine,if_exists="append",index=False)
        print("用时较长，如果中断请从输入这个代码：%s，重新运行。"%stock_names[i])
        #time.sleep(t)
        # print(df)
#
def down_cashflow():
    stock_name=input("请输入股票的起始代码，如果是第一次运行请输入000001.SZ，如果是中断继续请输入上次中断时的股票代码：")
    index = stock_names.index(stock_name)
    for i in range(index,len(stock_names)+1):
        #t=random.randint(5,13)
        df=pro.cashflow(ts_code=stock_names[i])
        df.to_sql("cashflow",con=ts_engine,if_exists="append",index=False)
        print("用时较长，如果中断请从输入这个代码：%s，重新运行。"%stock_names[i])
        #time.sleep(t)
        print(df)

def down_forecast():
    # date=input("请输入查询交易日期，如20201130:")
    # df=pro.forecast(ann_date=date)
    # df.to_sql("forecast",con=ts_engine,if_exists="append",index=False)
    # print(df)
    stock_name=input("请输入股票的起始代码，如果是第一次运行请输入000001.SZ，如果是中断继续请输入上次中断时的股票代码：")
    index = stock_names.index(stock_name)
    for i in range(index,len(stock_names)+1):
        #t=random.randint(5,13)
        df=pro.forecast(ts_code=stock_names[i])
        df.to_sql("forecast",con=ts_engine,if_exists="append",index=False)
        print("用时较长，如果中断请从输入这个代码：%s，重新运行。"%stock_names[i])
        #time.sleep(t)
        #print(df)

#业绩快报
def down_express():
    stock_name=input("请输入股票的起始代码，如果是第一次运行请输入000001.SZ，如果是中断继续请输入上次中断时的股票代码：")
    index = stock_names.index(stock_name)
    for i in range(index,len(stock_names)+1):
        t=random.randint(10,20)
        df=pro.express(ts_code=stock_names[i])
        df.to_sql("express",con=ts_engine,if_exists="append",index=False)
        print("用时较长，如果中断请从输入这个代码：%s，重新运行。"%stock_names[i])
        time.sleep(t/10)
        #print(df)

#分红送股
def down_dividend():
    stock_name=input("请输入股票的起始代码，如果是第一次运行请输入000001.SZ，如果是中断继续请输入上次中断时的股票代码：")
    index = stock_names.index(stock_name)
    for i in range(index,len(stock_names)+1):
        t=random.randint(5,10)
        df=pro.dividend(ts_code=stock_names[i])
        df.to_sql("dividend",con=ts_engine,if_exists="append",index=False)
        print("用时较长，如果中断请从输入这个代码：%s，重新运行。"%stock_names[i])
        time.sleep(t/10)
        #print(df)
#财务指标数据
def down_fina_indicator():
    stock_name=input("请输入股票的起始代码，如果是第一次运行请输入000001.SZ，如果是中断继续请输入上次中断时的股票代码：")
    index = stock_names.index(stock_name)
    for i in range(index,len(stock_names)+1):
        t=random.randint(5,10)
        df=pro.fina_indicator(ts_code=stock_names[i])
        df.to_sql("fina_indicator",con=ts_engine,if_exists="append",index=False)
        print("用时较长，如果中断请从输入这个代码：%s，重新运行。"%stock_names[i])
        time.sleep(t/10)
        #print(df)
#财务审计意见
def down_fina_audit():
    stock_name=input("请输入股票的起始代码，如果是第一次运行请输入000001.SZ，如果是中断继续请输入上次中断时的股票代码：")
    index = stock_names.index(stock_name)
    for i in range(index,len(stock_names)+1):
        t=random.randint(5,10)
        df=pro.fina_audit(ts_code=stock_names[i])
        df.to_sql("fina_audit",con=ts_engine,if_exists="append",index=False)
        print("用时较长，如果中断请从输入这个代码：%s，重新运行。"%stock_names[i])
        time.sleep(t/10)
        print(df)

#主营业务构成
def down_fina_mainbz():
    stock_name=input("请输入股票的起始代码，如果是第一次运行请输入000001.SZ，如果是中断继续请输入上次中断时的股票代码：")
    index = stock_names.index(stock_name)
    for i in range(index,len(stock_names)+1):
        t=random.randint(5,10)
        df=pro.fina_mainbz(ts_code=stock_names[i])
        df.to_sql("fina_mainbz",con=ts_engine,if_exists="append",index=False)
        print("用时较长，如果中断请从输入这个代码：%s，重新运行。"%stock_names[i])
        time.sleep(t/10)
        print(df)

#财报披露计划,每分钟限制访问80次
def down_disclosure_date():
    stock_name=input("请输入股票的起始代码，如果是第一次运行请输入000001.SZ，如果是中断继续请输入上次中断时的股票代码：")
    index = stock_names.index(stock_name)
    for i in range(index,len(stock_names)+1):
        #t=random.randint(1,3)
        df=pro.disclosure_date(ts_code=stock_names[i])
        df.to_sql("disclosure_date",con=ts_engine,if_exists="append",index=False)
        print("用时较长，如果中断请从输入这个代码：%s，重新运行。"%stock_names[i])
        #time.sleep(t)
        #print(df)

#下载市场参考数据
#港股通十大成交
def down_ggt_top10():
    date=input("请输入查询交易日期，如20201130:")
    df=pro.ggt_top10(trade_date=date)
    df.to_sql("ggt_top10",con=ts_engine,if_exists="append",index=False)
    print(df)
#融资融券交易汇总
def down_margin():
    date=input("请输入查询交易日期，如20201130:")
    df=pro.margin(trade_date=date)
    df.to_sql("margin",con=ts_engine,if_exists="append",index=False)
    print(df)
#融资融券交易明细
def down_margin_detail():
    date=input("请输入查询交易日期，如20201130:")
    df=pro.margin_detail(trade_date=date)
    df.to_sql("margin_detail",con=ts_engine,if_exists="append",index=False)
    print(df)
#前十大股东
def down_top10_holders():
    stock_name=input("请输入股票的起始代码，如果是第一次运行请输入000001.SZ，如果是中断继续请输入上次中断时的股票代码：")
    index = stock_names.index(stock_name)
    for i in range(index,len(stock_names)+1):
        #t=random.randint(1,3)
        df=pro.top10_holders(ts_code=stock_names[i],start_date='20200101', end_date='20201231')
        df.to_sql("top10_holders",con=ts_engine,if_exists="append",index=False)
        print("用时较长，如果中断请从输入这个代码：%s，重新运行。"%stock_names[i])
        #time.sleep(t)
        #print(df)
#前十大流通股东
def down_top10_floatholders():
    stock_name=input("请输入股票的起始代码，如果是第一次运行请输入000001.SZ，如果是中断继续请输入上次中断时的股票代码：")
    index = stock_names.index(stock_name)
    for i in range(index,len(stock_names)+1):
        #t=random.randint(1,3)
        df=pro.top10_floatholders(ts_code=stock_names[i],start_date='20200101', end_date='20201231')
        df.to_sql("top10_floatholders",con=ts_engine,if_exists="append",index=False)
        print("用时较长，如果中断请从输入这个代码：%s，重新运行。"%stock_names[i])
        #time.sleep(t)
        #print(df)
#龙虎榜每日明细
def down_top_list():
    date=input("请输入查询交易日期，如20201130:")
    stock_name=input("请输入股票的起始代码，如果是第一次运行请输入000001.SZ，如果是中断继续请输入上次中断时的股票代码：")
    index = stock_names.index(stock_name)
    for i in range(index,len(stock_names)+1):
        #t=random.randint(1,3)
        df=pro.top_list(trade_date=date,ts_code=stock_names[i])
        df.to_sql("top_list",con=ts_engine,if_exists="append",index=False)
        print("用时较长，如果中断请从输入这个代码：%s，重新运行。"%stock_names[i])
        #time.sleep(t)
        #print(df)
#龙虎榜机构明细
def down_top_inst():
    date=input("请输入查询交易日期，如20201130:")
    stock_name=input("请输入股票的起始代码，如果是第一次运行请输入000001.SZ，如果是中断继续请输入上次中断时的股票代码：")
    index = stock_names.index(stock_name)
    for i in range(index,len(stock_names)+1):
        #t=random.randint(1,3)
        df=pro.top_inst(trade_date=date,ts_code=stock_names[i])
        df.to_sql("top_inst",con=ts_engine,if_exists="append",index=False)
        print("用时较长，如果中断请从输入这个代码：%s，重新运行。"%stock_names[i])
        #time.sleep(t)
        print(df)
#股权质押统计数据
def down_pledge_stat():
    date=input("请输入查询截止日期，如20201130:")
    stock_name=input("请输入股票的起始代码，如果是第一次运行请输入000001.SZ，如果是中断继续请输入上次中断时的股票代码：")
    index = stock_names.index(stock_name)
    for i in range(index,len(stock_names)+1):
        #t=random.randint(1,3)
        df=pro.pledge_stat(ts_code=stock_names[i],end_date=date)
        df.to_sql("pledge_stat",con=ts_engine,if_exists="append",index=False)
        print("用时较长，如果中断请从输入这个代码：%s，重新运行。"%stock_names[i])
        #time.sleep(t)
        print(df)

#获取股票质押明细数据
def down_pledge_detail():
    stock_name=input("请输入股票的起始代码，如果是第一次运行请输入000001.SZ，如果是中断继续请输入上次中断时的股票代码：")
    index = stock_names.index(stock_name)
    for i in range(index,len(stock_names)+1):
        #t=random.randint(1,3)
        df=pro.pledge_detail(ts_code=stock_names[i])
        df.to_sql("pledge_detail",con=ts_engine,if_exists="append",index=False)
        print("用时较长，如果中断请从输入这个代码：%s，重新运行。"%stock_names[i])
        #time.sleep(t)
        print(df)
#股票回购
def down_repurchase():
    df=pro.query("repurchase",offset='1')
    df.to_sql("repurchase",con=ts_engine,if_exists="append",index=False)
    print(df)
#概念股分类
def down_concept():
    df=pro.query("concept",src='ts')
    df.to_sql("concept",con=ts_engine,if_exists="append",index=False)
    print(df)
#概念股分类明细
def down_concept_detail():
    id_name=input("请输入概念股的起始代码，如果是第一次运行请输入TS0，如果是中断继续请输入上次中断时的概念股代码：")
    index = id.index(id_name)
    for i in range(index,len(id)+1):
        #t=random.randint(1,3)
        df=pro.concept_detail(id=id[i])
        df.to_sql("concept_detail",con=ts_engine,if_exists="append",index=False)
        print("用时较长，如果中断请从输入这个代码：%s，重新运行。"%stock_names[i])
        #time.sleep(t)
        #print(df)

#限售股解禁
def down_share_float():
    stock_name=input("请输入股票的起始代码，如果是第一次运行请输入000001.SZ，如果是中断继续请输入上次中断时的股票代码：")
    index = stock_names.index(stock_name)
    for i in range(index,len(stock_names)+1):
        #t=random.randint(1,3)
        df=pro.share_float(ts_code=stock_names[i])
        df.to_sql("share_float",con=ts_engine,if_exists="append",index=False)
        print("用时较长，如果中断请从输入这个代码：%s，重新运行。"%stock_names[i])
        #time.sleep(t)
        print(df)

#大宗交易
def down_block_trade():
    date=input("请输入查询截止日期，如20201130:")
    df=pro.block_trade(trade_date=date)
    df.to_sql("block_trade",con=ts_engine,if_exists="append",index=False)
    print(df)

#股票账户开户数据
def down_stk_account():
    date=input("请输入查询截止日期，如20201130:")
    df=pro.stk_account(start_date='20180101', end_date=date)
    df.to_sql("stk_account",con=ts_engine,if_exists="append",index=False)
    print(df)

#获取上市公司股东户数数据
def down_stk_holdernumber():
    stock_name=input("请输入股票的起始代码，如果是第一次运行请输入000001.SZ，如果是中断继续请输入上次中断时的股票代码：")
    index = stock_names.index(stock_name)
    for i in range(index,len(stock_names)+1):
        #t=random.randint(1,3)
        df=pro.stk_holdernumber(ts_code=stock_names[i])
        df.to_sql("stk_holdernumber",con=ts_engine,if_exists="append",index=False)
        print("用时较长，如果中断请从输入这个代码：%s，重新运行。"%stock_names[i])
        #time.sleep(t)
        print(df)



#股东增减持
def down_stk_holdertrade():
    date=input("请输入查询截止日期，如20201130:")
    stock_name=input("请输入股票的起始代码，如果是第一次运行请输入000001.SZ，如果是中断继续请输入上次中断时的股票代码：")
    index = stock_names.index(stock_name)
    #获取单日全部增减持数据
    df = pro.stk_holdertrade(ann_date=date)
    df.to_sql("stk_holdertrade",con=ts_engine,if_exists="append",index=False)
    #获取当日增持数据
    df = pro.stk_holdertrade(ann_date=date, trade_type='IN')
    df.to_sql("stk_holdertrade",con=ts_engine,if_exists="append",index=False)
    for i in range(index,len(stock_names)+1):
        #t=random.randint(1,3)
        df=pro.stk_holdertrade(ts_code=stock_names[i])
        df.to_sql("stk_holdertrade",con=ts_engine,if_exists="append",index=False)
        print("用时较长，如果中断请从输入这个代码：%s，重新运行。"%stock_names[i])
        #time.sleep(t)

#下载指数
def down_index_basic():
    for market in markets:
        df=pro.index_basic(market=market)
        df.to_sql("index_basic",con=ts_engine,if_exists="append",index=False)
        print(df)
def down_index_daily():
    for index in index_cn:
        df=pro.query("index_daily",ts_code=index)
        df.to_sql("index_daily",con=ts_engine,if_exists="append",index=False)
        print(df)

def down_index_weekly():
    for index in index_cn:
        df=pro.query("index_weekly",ts_code=index)
        df.to_sql("index_weekly",con=ts_engine,if_exists="append",index=False)
        print(df)

def down_index_monthly():
    for index in index_cn:
        df=pro.query("index_monthly",ts_code=index)
        df.to_sql("index_monthly",con=ts_engine,if_exists="append",index=False)
        print(df)


def down_index_weight():
    date=input("请输入截止日期，如20201130:")
    for index in index_cn:
        df = pro.index_weight(index_code=index, start_date='20200101',end_date=date)
        df.to_sql("index_weight",con=ts_engine,if_exists="append",index=False)
        print(df)

def down_index_dailybasic():
    date=input("请输入截止日期，如20201130:")
    df=pro.index_dailybasic(trade_date=date)
    df.to_sql("index_dailybasic",con=ts_engine,if_exists="append",index=False)
    print(df)

def down_index_classify():
    for level in level_sw:
        df = pro.index_classify(level=level, src='SW')
        df.to_sql("index_classify",con=ts_engine,if_exists="append",index=False)
        print(df)

#申万行业成分构成,访问次数限制每分钟150次
def down_index_member():
    index_code=input("请输入行业分类的起始代码，如果是第一次运行请输入801020.SI，如果是中断继续请输入上次中断时的股票代码：")
    index = index_codes.index(index_code)
    for i in range(index,len(index_codes)):
        #t=random.randint(1,3)
        df=pro.index_member(index_code=index_codes[i])
        df.to_sql("index_member",con=ts_engine,if_exists="append",index=False)
        print("用时较长，如果中断请从输入这个代码：%s，重新运行。"%index_codes[i])
        print(df)

def down_daily_info():
    sect_name=input("请输入版块名称的起始代码，如果是第一次运行请输入SZ_MARKET，如果是中断继续请输入上次中断的代码：")
    index = sect_names.index(sect_name)
    for i in range(index,len(sect_names)):
        #t=random.randint(1,3)
        df=pro.daily_info(ts_code=sect_names[i])
        df.to_sql("daily_info",con=ts_engine,if_exists="append",index=False)
        print("用时较长，如果中断请从输入这个代码：%s，重新运行。"%sect_names[i])
        #print(df)

#国际指数
def down_index_global():
    ts_index_code=input("请输入版块名称的起始代码，如果是第一次运行请输入XIN9，如果是中断继续请输入上次中断的代码：")
    index = ts_index_codes.index(ts_index_code)
    for i in range(index,len(ts_index_codes)):
        #t=random.randint(1,3)
        df=pro.index_global(ts_code=ts_index_codes[i])
        df.to_sql("index_global",con=ts_engine,if_exists="append",index=False)
        print("用时较长，如果中断请从输入这个代码：%s，重新运行。"%ts_index_codes[i])
        print(df)



