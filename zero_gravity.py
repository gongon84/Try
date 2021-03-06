
#インポート
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import animation
import random
import time


# プログラムの実行時間を測る
def get_h_m_s(td):
    m, s = divmod(td, 60)
    h, m = divmod(m, 60)
    return h, m, s


# 関数
def SIR():

    # 定義
    times = 40  # 観測時間
    max = 40  # グラフの幅
    speed = 100  #アニメーションの速さ（小さい方が早い）
    ims = []  # アニメーションの画像を追加する

    #ゴール画像
    mike = [[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],
            [2,1],[3,1],[4,1],[5,1],[6,1],
            [3,2],[4,2],[5,2],[6,2],[7,2],
            [4,3],[5,3],[6,3],[7,3],[8,3],
            [5,4],[6,4],[7,4],[8,4],[9,4],
            [6,5],[7,5],[8,5],[9,5],[10,5],
            [7,6],[8,6],[9,6],[10,6],[11,6],
            [8,7],[9,7],[10,7],[11,7],[12,7],
            [9,8],[10,8],[11,8],[12,8],[13,8],
            [10,9],[11,9],[12,9],[13,9],[14,9],
            [11,10],[12,10],[13,10],[14,10],[15,10],
            [11,11],[12,11],[13,11],[14,11],[15,11],[16,11],
            [11,12],[12,12],[13,12],[14,12],[15,12],[16,12],[17,12],
            [11,13],[12,13],[13,13],[14,13],[15,13],[16,13],[17,13],[18,13],
            [12,14],[13,14],[14,14],[15,14],[16,14],[17,14],[18,14],[19,14],
            [12,15],[13,15],[14,15],[15,15],[16,15],[17,15],[18,15],[19,15],[20,15],[21,15],
            [13,16],[14,16],[15,16],[16,16],[17,16],[18,16],[19,16],[20,16],[21,16],[22,16],
            [13,17],[14,17],[15,17],[16,17],[17,17],[18,17],[19,17],[20,17],[21,17],[22,17],[23,17],
            [14,18],[15,18],[16,18],[17,18],[18,18],[19,18],[20,18],[21,18],[22,18],[23,18],[24,18],
            [14,19],[15,19],[16,19],[17,19],[18,19],[19,19],[20,19],[21,19],[22,19],[23,19],[24,19],[25,19],
            [15,20],[16,20],[17,20],[18,20],[19,20],[20,20],[21,20],[22,20],[23,20],[24,20],[25,20],[26,20],
            [15,21],[16,21],[17,21],[18,21],[19,21],[20,21],[21,21],[22,21],[23,21],[24,21],[25,21],[26,21],
            [16,22],[17,22],[18,22],[19,22],[20,22],[21,22],[22,22],[23,22],[24,22],[25,22],[26,22],
            [16,23],[17,23],[18,23],[19,23],[20,23],[21,23],[22,23],[23,23],[24,23],[25,23],[26,23],
            [17,24],[18,24],[19,24],[20,24],[21,24],[22,24],[23,24],[24,24],[25,24],[26,24],[27,24],
            [17,25],[18,25],[19,25],[20,25],[21,25],[22,25],[23,25],[24,25],[25,25],[26,25],[27,25],
            [18,26],[19,26],[20,26],[21,26],[22,26],[23,26],[24,26],[25,26],[26,26],[27,26],
            [18,27],[19,27],[20,27],[21,27],[22,27],[23,27],[24,27],[25,27],[26,27],[27,27],[28,27],
            [19,28],[20,28],[21,28],[22,28],[23,28],[24,28],[25,28],[26,28],[27,28],[28,28],
            [19,29],[20,29],[21,29],[22,29],[23,29],[24,29],[25,29],[26,29],[27,29],[28,29],[29,29],[30,29],[31,29],[32,29],
            [20,30],[21,30],[22,30],[23,30],[24,30],[25,30],[26,30],[27,30],[28,30],[29,30],[30,30],[31,30],[32,30],
            [20,31],[21,31],[22,31],[23,31],[24,31],[25,31],[26,31],[27,31],[28,31],[29,31],[30,31],[31,31],[32,31],[33,31],[34,31],
            [21,32],[22,32],[23,32],[24,32],[25,32],[26,32],[27,32],[28,32],[29,32],[30,32],[31,32],[32,32],[33,32],[34,32],[35,32],
            [23,33],[24,33],[25,33],[26,33],[27,33],[28,33],[29,33],[30,33],[31,33],[32,33],[33,33],[34,33],[35,33],[36,33],
            [27,34],[28,34],[29,34],[30,34],[31,34],[32,34],[33,34],[34,34],[35,34],
            [27,35],[28,35],[29,35],[30,35],[31,35],[32,35],[33,35],[34,35],
            [28,36],[29,36],[30,36],[31,36],[32,36],[33,36],
            [29,37],[30,37],[31,37],
            ]

    # 人の初期位置（ランダム）
    start = []
    person_x = [random.randint(0, max) for i in range(len(mike))]
    person_y = [random.randint(0, max) for i in range(len(mike))]
    for i, j in zip(person_x, person_y):
        start.append([i,j])

    # 初期位置　グラフ表示
    fig = plt.figure(figsize=(8,8))  # グラフを表示する場所を設定
    ax1 = fig.add_subplot(111)  # figの上にax1を設定
    img = ax1.plot(start[0][0], start[0][1], marker='.', markersize=20, linestyle='None', color='black')
    # for mike2 in mike:
    #     img += ax1.plot(mike2[0], mike2[1], marker='.', markersize=20, linestyle='None', color='blue')
    ims.append(img)  #プロット画像を追加

    # 観測スタート
    for t in range(times):
        print(t)
        for i in range(len(mike)):
            if start[i][0] < mike[i][0]:
                start[i][0] += 1
            elif start[i][0] > mike[i][0]:
                start[i][0] -= 1
            if start[i][1] < mike[i][1]:
                start[i][1] += 1
            elif start[i][1] > mike[i][1]:
                start[i][1] -= 1

        # グラフのプロット
        img = ax1.plot(start[0][0], start[0][1], marker='.', markersize=18, linestyle='None', color='blue',
                        label='Susceptible')
        for i in range(len(mike)):
            img += ax1.plot(start[i][0], start[i][1], marker='.', markersize=18, linestyle='None', color='blue', label='Susceptible')
        # for mike2 in mike:
        #     img += ax1.plot(mike2[0], mike2[1], marker='.', markersize=20, linestyle='None', color='blue')

        # タイトル、軸
        ax1.set_title("SIR Model  --Random Walk--", size=14)
        ax1.set_xticks(np.arange(0, max+1))
        ax1.set_yticks(np.arange(0, max+1))
        ax1.set_xlim(0, max+1)
        ax1.set_ylim(0, max+1)
        # 目盛りなし
        # ax1.xaxis.set_major_locator(mpl.ticker.NullLocator())
        # ax1.yaxis.set_major_locator(mpl.ticker.NullLocator())

        # アニメーション使用する画像を追加
        ims.append(img)

    # アニメーション開始
    ani = animation.ArtistAnimation(fig, ims, interval=speed, repeat=False)
    plt.show()

if __name__ == '__main__':

    SIR()