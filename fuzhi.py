import datetime as dt
import akshare as ak
import matplotlib.pyplot as plt
import numpy as np
import sql_py as sp
import ak_sql as asq

colors=['red','black','green','yellow','blue','purple','grey','brown','pink','orange','sandy','salmon','maroon','chocolate','gold']
#取当日日期为默认日期
default_date=dt.date.today()
default_format_date=default_date.strftime("%Y%m%d")
df=sp.cx_db_fund()
fund_code=list(df['基金代码'].head(6))
print(fund_code)

m=0
x = dict()
y = dict()
z = dict()
lns=dict()
#依次画出每前5只基金最近30个交易日的万分收益及7日年化收益图。
while m<=5:
    for i in fund_code:
        try:
            df=sp.cx_fund_his(fund_code=i)        
        except Exception as e:
            print(e)
            print("正在下载。。。")
            asq.down_ak_m_fund_his(i)
            df=sp.cx_fund_his(fund_code=i)
        finally:
            #如果刚刚建立数据库第一次运行会有个错误提示，没关系，在运行一次就好了。
            #x=df.head(30)['净值日期']
            x[m]=list(df.head(30)['净值日期'])
            x[m].reverse()
            y[m]=list(df.head(30)['每万份收益'])
            y[m].reverse()
            y[m]= list(map(float,y[m]))
            z[m]=list(df.head(30)['7日年化收益率']) 
            z[m].reverse()
            z[m] = list(map(float,z[m]))
        m+=1
            #print(z[m])        

#随机变颜色
fig=plt.figure(figsize = (30,10))
ax=fig.add_subplot(211)
for s in range(0,len(fund_code)):
    lns[s]=ax.plot(x[s],y[s],color=colors[s%len(fund_code)],linewidth=1,marker="o",label=fund_code)
    lns[s]+=lns[s]
# for m in range(0,len(fund_code)):
#     lns[m]=ax.plot(x[m],y[m],color=colors[m%len(fund_code)],linewidth=1,marker="o",label=fund_code)
#     lns[m]+=lns[m]
labs = [l for l in fund_code]
ax.legend(labs,loc=0)
plt.title("%s日467支货基中，选前5货币基金万份收益及7日年化收益率对比图.jpg"%default_format_date,fontsize=12,color='r')
ax2=fig.add_subplot(212)
for n in range(0,len(fund_code)):
    lns[n]=ax2.plot(x[n],z[n],color=colors[n%len(fund_code)],linewidth=1,marker="s",label=fund_code)
    lns[n]+=lns[n]
labs = [l for l in fund_code]
ax2.legend(labs,loc=0)
ax.grid()
ax2.grid()
ax.set_xlabel("日期", fontsize=13)
ax2.set_xlabel("日期", fontsize=13)
fig.autofmt_xdate()
ax.set_ylabel("每万份收益", fontsize=13)

ax2.set_ylabel("7日年化收益率", fontsize=13)
ax.set_ylim(0.5, 3, 0.0001)
ax2.set_ylim(1.5, 5, 0.1)
plt.savefig('%s日前5货币基金.jpg'%default_format_date,dpi=400,bbox_inches = 'tight')
plt.show()
 