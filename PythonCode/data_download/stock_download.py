from token_list import public_funds,pro,ts_engine
fund_names=public_funds

#下载数据
def download(names):
    for i in names:
        df=pro.query("%s"%i)
        df.to_sql("%s"%i,con=ts_engine,if_exists="append",index=False)
        print("%s已完成"%i)


#提取代码名称：
def extract_names():


download(fund_names)
