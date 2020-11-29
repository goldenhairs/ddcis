import akshare as ak
import matplotlib.pyplot as plt
import pandas as pd
from token_list import ak_engine

plt.rcParams['figure.figsize'] = (16.0, 9.0) 
plt.rcParams['savefig.dpi'] = 600 #图片像素
plt.rcParams['figure.dpi'] = 600 #分辨率

#ak_etf_list=["004347","002900","002974","512330","000942","159939","160626"]
ak_etf_list=["005123","005447","006587","370021","370022","398011","398012","519087","519088"]
#ts_golde_etf=['008701','008702','008142','008143','009198','159812','518660','518850','007977','007976','007978','004253','002963','002610','002611','000307','000218','000930','000929','159937','159934','000217','000216','518880','518800','160719','161116','320013']
ts_golde_etf=['518660','518850','159937','159934','518880','518800']
def fund_list(tscode):
    tscode=tscode
    df = ak.fund_em_open_fund_info(fund="%s"%tscode, indicator="单位净值走势")
    df.to_sql("%s"%tscode,con=ak_engine,if_exists="append",index=False)
    x=df.x
    y=df.y
    return x,y

def out_img(ak_etf_list):
    title=input("请输入输出的基金类标题，如'信息技术':")
    for tscode in ak_etf_list:
        x,y=fund_list(tscode)
        plt.plot(x,y,label='%s'%tscode)

    plt.rcParams['font.sans-serif']=['SimHei'] 
    plt.xlabel("日期")
    plt.ylabel("净值")
    plt.legend()
    plt.title("%sETF基金"%title)
    plt.savefig("E:/DDCIS/Image/%sETF基金.png"%title)

out_img(ts_golde_etf)