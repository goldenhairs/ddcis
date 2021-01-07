import datetime as dt
import akshare as ak
import matplotlib.pyplot as plt
import numpy as np
import sql_py as sp
import ak_sql as asq
import MySQLdb
import pandas as pd

colors=['red','black','green','yellow','blue','purple','grey','brown','pink','orange','sandy','salmon','maroon','chocolate','gold']
#取当日日期为默认日期
default_date=dt.date.today()
default_format_date=default_date.strftime("%Y%m%d")
df=sp.cx_db_fund()
fund_code=list(df['基金代码'].head(4))
print(fund_code)

m=0
x = dict()
y = dict()
z = dict()
lns=dict()
lnn=dict()
#依次画出每前5只基金最近30个交易日的万分收益及7日年化收益图。

fig=plt.figure(figsize = (30,10))
plt.title("货基近30日万份收益及7日年化收益率对比走势图")
ax=fig.add_subplot(211)    
ax.grid()
ax.set_xlabel("日期", fontsize=13)
ax.set_ylabel("每万份收益", fontsize=13)
ax.set_ylim(0.5, 3, 0.0001)
ax2=fig.add_subplot(212)
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
    lns[m]=ax.plot(x[m],y[m],color=colors[m%len(fund_code)],linewidth=1,marker="o",label=fund_code)
    lnn[m]=ax2.plot(x[m],z[m],color=colors[m%len(fund_code)],linewidth=1,marker="s",label=fund_code)
    labs = [i for i in fund_code]
    m+=1
    if m>(len(fund_code)-1):
        break
ax.legend(labs,loc=0)
ax2.grid()
ax2.set_xlabel("日期", fontsize=13)
fig.autofmt_xdate()
ax2.legend(labs,loc=0)
ax2.set_ylim(1.5, 5, 0.1)
ax2.set_ylabel("7日年化收益率", fontsize=13)
plt.savefig('%s日前%s货币基金对比图.jpg'%(default_format_date,len(fund_code)),dpi=400,bbox_inches = 'tight')
plt.show()



 