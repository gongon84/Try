import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas_datareader
import sklearn
import sklearn.linear_model
import sklearn.model_selection
import datetime


#株価予測
def stock_price_forecast(code, day):

    #日経平均 or 証券コード
    if code == 'N225':
        code = '^' + str(code)
        df_n225 = pandas_datareader.data.DataReader('^N225', 'yahoo', '2015-08-01')
    else:
        code = str(code) + '.JP'

        # 株価データ読み取り
        df_n225 = pandas_datareader.data.DataReader(code, 'stooq')
        df_n225 = df_n225.sort_index()

    #証券コードのエラー
    if len(df_n225) == 0:
        print('証券コードが読み取れません')
        exit()


    # 変化率
    df_n225['change'] = ((df_n225['Close'] - df_n225['Open']) / (df_n225['Open']) * 100)

    # 日数分データをシフト
    df_n225['new'] = df_n225['Close'].shift(-day)

    # 機械学習
    # ['new']を省いたデータ
    X = np.array(df_n225.drop(['new'], axis=1))
    X = sklearn.preprocessing.scale(X)

    # 予測に使う部分
    predict_data = X[-day:]
    X = X[:-day]
    # ['new']のデータ
    y = np.array(df_n225['new'])
    y = y[:-day]

    # 機械学習
    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
    lr = sklearn.linear_model.LinearRegression()
    lr.fit(X_train, y_train)

    # 予測の正確さの指標
    accuracy = lr.score(X_test, y_test)
    print('正確さ：', accuracy)

    # 予測に用いるデータ
    predict_data = lr.predict(predict_data)

    # グラフ
    df_n225['predict'] = np.nan
    last_date = df_n225.iloc[-1].name

    one_day = 86400
    next_unix = last_date.timestamp() + one_day

    for data in predict_data:
        next_data = datetime.datetime.fromtimestamp(next_unix)
        next_unix += one_day
        df_n225.loc[next_data] = np.append([np.nan] * (len(df_n225.columns) - 1), data)

    #日付を調整
    date = df_n225.index.to_pydatetime()
    close = df_n225['Close'].values
    predict = df_n225['predict'].values

    print('\n予測された株価（一部）')
    print(df_n225['predict'].tail(10))

    #グラフ描画
    plt.title('Securities Code : {}'.format(code))
    plt.plot(date, close, color='green')
    plt.plot(date, predict, color='yellow')
    plt.xticks(rotation=45)
    plt.show()


if __name__ == '__main__':

    #matplotlibの日本語対応
    matplotlib.rcParams['font.family'] = 'AppleGothic'

    code = input('証券コードを入力してください。\n（日経平均の場合はN225と入力）')
    day = int(input('何日先まで予測しますか？ : '))
    stock_price_forecast(code, day)
