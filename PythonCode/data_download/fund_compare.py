import akshare as ak
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['figure.figsize'] = (16.0, 9.0) 
plt.rcParams['savefig.dpi'] = 600 #图片像素
plt.rcParams['figure.dpi'] = 600 #分辨率
import pandas as pd
from down.token_list import ak_engine
import MySQLdb
import numpy as np
import pandas as pd
from func import r_color

#此处输入基金列表
#ak_etf_list=["004347","002900","002974","512330","000942","159939","160626"]
#ak_etf_list=["005123","005447","006587","370021","370022","398011","398012","519087","519088"]
#ts_golde_etf=['008701','008702','008142','008143','009198','159812','518660','518850','007977','007976','007978','004253','002963','002610','002611','000307','000218','000930','000929','159937','159934','000217','000216','518880','518800','160719','161116','320013']
#ts_golde_etf=['518660','518850','159937','159934','518880','518800']
#ak_etf_list=['010236','159805','006080','006081','004752','004753','512980','005310','004514','001223','001319','163117','150234','150233','150248','150247','164818','001150','150203','160629','150204','000522']
#xf_list=['001133','159936','004347']
kxxf=['002977','001133','159936']

#下载基金保存到数据库
def fund_list(tscode):
    ts_name=tscode
    df = ak.fund_em_open_fund_info(fund="%s"%ts_name, indicator="单位净值走势")
    df.to_sql("%s"%ts_name,con=ak_engine,if_exists="append",index=False)
    x=df['净值日期']
    y=df['单位净值'] 
    return x,y

#查询数据库
def query_db(tscode):
    conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',db='akshare_db',charset='utf8')
    cursor=conn.cursor()
    sql = "select * from akshare_db.%s"%tscode
    df=pd.read_sql(sql,conn)
    cursor.close()
    conn.close()
    x=df['净值日期']
    y=df['单位净值'] 
    return x,y

#绘制基金净值走势
def out_img(ak_etf_list):
    title=input("请输入输出的基金类标题，如'信息技术':")
    for etf in ak_etf_list:
        try:
            x,y=query_db(etf)
        except Exception:
            print("数据库中基金代码不存在，正在下载。。。")                
            x,y=fund_list(etf)
        finally:
            r=r_color()      
            plt.plot(x,y,color=r,label='%s'%etf)  
            plt.xlabel("日期")
            plt.ylabel("净值")
            plt.legend()
            plt.title("%sETF基金"%title)
            plt.annotate('fund=%s'%etf, xy=(x.tail(1),y.tail(1)), xytext=(x.tail(1),y.tail(1)), arrowprops=dict(facecolor='black', shrink=1, width=10))
            #基金的存储位置
            plt.savefig("d:/DDCIS/Image/%sETF基金.png"%title)

out_img(kxxf)
