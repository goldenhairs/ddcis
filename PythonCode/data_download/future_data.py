import akshare as ak

#国泰君安交易日历
#example:ak.futures_rule(trade_date="20201127")
def futures_rule():
    df=ak.futures_rule(trade_date="20201127")
    print(df)

#库存数据-99期货
def get_inventory_data():
    df = ak.get_inventory_data(exchange=1, symbol=6, plot=True)
    print(df)

#库存数据-东方财富
def futures_inventory_em():
    df=ak.futures_inventory_em(exchange="上海期货交易所", symbol="沪铜")
    print(df)

futures_inventory_em()

