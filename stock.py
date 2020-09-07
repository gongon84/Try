#インポート
from pandas_datareader import data
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':

    #値の取得
    start = '2019-06-01'
    end = '2020-06-01'
    df = data.DataReader('^N225', 'yahoo', start, end)
    df_d = pd.DataFrame(df)

    #日付と終値を変数に代入
    date = df_d.index
    price = df_d['Adj Close']

    #移動平均 過去５日、２５日、５０日
    span01 = 5
    span02 = 25
    span03 = 50

    #新しいカラムに平均を追加　rollingは移動平均を抽出するもの
    df_d['sma01'] = price.rolling(window=span01).mean()
    df_d['sma02'] = price.rolling(window=span02).mean()
    df_d['sma03'] = price.rolling(window=span03).mean()

    #numpy配列に変更
    date_np = date.values
    price_np = price.values
    sma01_np = df_d['sma01'].values
    sma02_np = df_d['sma02'].values
    sma03_np = df_d['sma03'].values

    #買いと売りのタイミング
    point = 'none'
    buy = 0
    sell = 0
    profit = 0
    profit_sum = 0

    for i in range(len(date_np)):

        #５分線が下
        if point == 'none':
            if sma01_np[i] < sma02_np[i]:
                point = 'start'

        #ゴールデンクロス
        if point == 'start' or point == 'sell':
            if sma01_np[i] > sma02_np[i]:
                point = 'buy'
                buy = price_np[i]
                print('タイミング(買):', i)

        #デッドクロス
        if point == 'buy':
            if sma01_np[i] < sma02_np[i]:
                point = 'sell'
                sell = price_np[i]
                print('タイミング(売):', i)

        #利益
        if buy != 0 and sell != 0:
            profit = buy - sell
            print('買い値:{}\n売り値:{}\n利益:{}'.format(buy, sell, profit))
            profit_sum += profit
            print('利益合計:',profit_sum)
            if point == 'sell':
                buy = 0
            elif point == 'buy':
                sell = 0
            print('\n')

    #dateを変更
    date2 = df.index
    date3 = []
    for i in date2:
        x = i.to_pydatetime()
        date3.append(x)


    #グラフ作成
    fig = plt.figure(figsize=(20, 10))
    ax = fig.add_subplot(211)

    #日経225
    ax.plot(date3, price_np, label='Nikkei225', color='green')

    #移動平均
    ax.plot(date3, sma01_np, label='sma01', color='#e84a5f')
    ax.plot(date3, sma02_np, label='sma02', color='#ff847c')
    ax.plot(date3, sma03_np, label='sma03', color='#feceab')

    #タイトルとラベル
    plt.title('N225', color='white', backgroundcolor='grey', size=20, loc='center')
    plt.xlabel('date', color='grey', size=20)
    plt.ylabel('price', color='grey', size=20)

    #ラベルを表示するためのもの
    plt.legend()

    plt.show()