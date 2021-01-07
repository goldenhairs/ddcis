'''
这个模块开始作图，前十的货币基金，挨个显示万分收益及7日年化收益率。
'''
import datetime as dt
import akshare as ak
import matplotlib.pyplot as plt
import numpy as np
import sql_py as sp
import ak_sql as asq

#取当日日期为默认日期
default_date=dt.date.today()
default_format_date=default_date.strftime("%Y%m%d")
df=sp.cx_db_fund()
#这个数值15，是可以修改取货币基金的个数，也就是下载的历史
fund_code=list(df['基金代码'].head(15))
print(fund_code)

#依次画出每前15只基金最近30个交易日的万分收益及7日年化收益图。
for i in fund_code:
    try:
        df=sp.cx_fund_his(fund_code=i)        
    except Exception as e:
        print(e)
        print("正在下载。。。")
        asq.down_ak_m_fund_his(i)
        pass
    finally:
        #print(data['净值日期'])
        x=list(df.head(30)['净值日期'])
        x.reverse()
        y=list(df.head(30)['每万份收益'])
        y.reverse()
        y = list(map(float,y))
        z=list(df.head(30)['7日年化收益率'])
        z.reverse()
        z = list(map(float,z))
        fig=plt.figure(figsize = (20,10))#figsize = (5,5)数组（5，5）为英寸
        ax=fig.add_subplot(111)
        lns1=ax.plot(x,y,color='blue',linewidth=1,marker="o", label='每万份收益')
        ax2=ax.twinx()
        lns2=ax2.plot(x,z,color='red',linewidth=1,marker="s", label='7日年化收益率')
        lns = lns1+lns2
        labs = [l.get_label() for l in lns]
        ax.legend(lns, labs, loc=0)
        ax.grid()
        ax.set_xlabel("日期", fontsize=13)
        fig.autofmt_xdate()
        ax.set_ylabel("每万份收益", fontsize=13)
        ax2.set_ylabel("7日年化收益率", fontsize=13)
        ax2.set_ylim(0, 5, 0.0001)
        ax.set_ylim(0, 3, 0.0001)
        plt.title("%s货基万分收益及7日年化收益图"%i)
        #可以保存到本地
        plt.savefig('%s货基30日的走势图.jpg'%i,dpi=400,bbox_inches = 'tight')
        plt.show()




