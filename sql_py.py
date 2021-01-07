import MySQLdb,sys
import pandas as pd
import datetime as dt
import ak_sql as asq

#取当日日期为默认日期
default_date=dt.date.today()
default_format_date=default_date.strftime("%Y%m%d")

#从本地数据库读取货币基金排名，取前十
def cx_db_fund(date=default_format_date):
    try:
        conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',db='akshare_db',charset='utf8')
    except Exception as e:
        print(e)
        sys.exit()
    cursor=conn.cursor()
    #所有货基
    #sql = "select * from akshare_db.fund_rank_%s"%default_format_date
    #去掉了带B的货基
    sql = "select * from akshare_db.fund_rank_%s where 基金简称 NOT like '%%B'"%default_format_date
    df=pd.read_sql(sql,conn)    
    cursor.close()
    conn.close()
    return df

#从本地数据库读取货币基金数据
def cx_fund_his(fund_code):
    fund_code=fund_code
    #asq.down_ak_m_fund_his(fund_code)
    try:
        conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',db='akshare_db',charset='utf8')
    except Exception as e:
        print(e)
        sys.exit()
    cursor=conn.cursor()
    sql = "select * from akshare_db.%s"%fund_code
    df=pd.read_sql(sql,conn)    
    cursor.close()
    conn.close()
    return df

# cx_db_fund()
# cx_fund_his('000533')
#print(cx_db_fund(date=default_format_date))
#有些货币基金是暂停销售的，在交易模块需要剔除。
