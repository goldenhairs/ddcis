'''
这个模块是取前10或者前5的的货币基金，在同一个图上显示其万分收益及7日年华收益率。
'''
import datetime as dt
import akshare as ak
import matplotlib.pyplot as plt
import numpy as np
import sql_py as sp
import ak_sql as asq
import MySQLdb
import pandas as pd

colors=['red','black','green','maroon','blue','purple','grey','brown','pink','orange','sandy','salmon','yellow','chocolate','gold']
#取当日日期为默认日期
default_date=dt.date.today()
default_format_date=default_date.strftime("%Y%m%d")
df=sp.cx_db_fund()
#这个数值4，就是可以取前几名的货基进行比较。
fund_code=list(df['基金代码'].head(4))
print(fund_code)

m=0
x = dict()
y = dict()
z = dict()
lns=dict()
lnn=dict()
#依次画出每前5只基金最近30个交易日的万分收益及7日年化收益图。

conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',db='akshare_db',charset='utf8')
cursor=conn.cursor()
for i in fund_code:
    sql = "select * from akshare_db.%s"%i
    df=pd.read_sql(sql,conn)
    x[m]=list(df.head(30)['净值日期'])
    x[m].reverse()
    y[m]=list(df.head(30)['每万份收益'])
    y[m].reverse()
    y[m]= list(map(float,y[m]))
    z[m]=list(df.head(30)['7日年化收益率']) 
    z[m].reverse()
    z[m] = list(map(float,z[m]))
    labs = [i for i in fund_code]
    m+=1
    if m>(len(fund_code)-1):
        break
fig=plt.figure(figsize = (30,10))
ax=fig.add_subplot(211)
ax.grid()
for l in range(0,len(fund_code)):   
    lns[l]=ax.plot(x[l],y[l],color=colors[l%len(fund_code)],linewidth=1,marker="o",label=fund_code)
    lns[l]+=lns[l]
    ax.legend(labs,loc=0)
plt.title("货基前%s名,近30日万份收益及7日年化收益率对比走势图"%len(fund_code))
ax2=fig.add_subplot(212)
ax2.grid()
for s in range(0,len(fund_code)): 
    lnn[s]=ax2.plot(x[s],z[s],color=colors[s%len(fund_code)],linewidth=1,marker="s",label=fund_code)
    lnn[s]+=lnn[s]
    ax2.legend(labs,loc=0)
ax.set_xlabel("日期", fontsize=13)
ax2.set_xlabel("日期", fontsize=13)
fig.autofmt_xdate()
ax.set_ylabel("每万份收益", fontsize=13)
ax2.set_ylabel("7日年化收益率", fontsize=13)
ax.set_ylim(0.5, 6, 0.0001)
ax2.set_ylim(1.5, 6, 0.1)
#这个地方是本地保存的名称。
plt.savefig('%s日前%s货币基金对比图.jpg'%(default_format_date,len(fund_code)),dpi=400,bbox_inches = 'tight')
plt.show()



 