import turtle #turtleモジュールを呼び出す
import datetime
import math
from module import* #module.pyを呼び出す

#マジックナンバーは定数で保持
SCREEN_WIDTH = 900 #スクリーンの横幅
SCREEN_HEIGHT = 900 #スクリーンの縦幅

X_LIMIT = 400 #スクリーンのx軸限界
Y_LIMIT = 400 #スクリーンのy軸限界

#TurtleGameクラス
class TurtleGame:
    #分かりにくいのでメンバ変数は一番上で定義しておく
    screen = None #スクリーン用のメンバ変数

    targets = [] #今いるターゲットのオブジェクトを格納しておくリスト
    black_count = 0 #今いる黒い亀の数

    player = None #プレイヤー用のメンバ変数

    rtext = None #残りのターゲット描画用のメンバ変数
    ttext = None #時間の描画用のメンバ変数

    stime = 0 #ゲーム開始時間を保持するメンバ変数

    #コンストラクタ
    def __init__(self):
        #drawメソッドを呼び出す
        self.draw()
        #ゲームの開始時刻を記録
        self.stime = datetime.datetime.now()
        #スクリーンの更新をスタート
        self.on_paint()
        #スクリーンが勝手に消えてしまうのを防止
        self.screen.mainloop()

    #画面の初期描画用メソッド
    def draw(self):
        #スクリーンのインスタンスを生成して代入
        self.screen = turtle.Screen()
        #スクリーンの大きさと、座標の設定
        self.screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT, 500, 0)
        #スクリーンのタイトル
        self.screen.title("カメ当てゲーム")

        #playerの初期設定
        self.player = Player()

        #Targetクラスより色リストを取得して初期のターゲット用色リストに変更する
        #初期のリストはcolorsを二倍してそこにblackを加えた物となる
        s_colors = Target.colors
        s_colors.extend(s_colors)
        s_colors.append("black")
        #ターゲットを1匹ずつ合計20匹表示していく
        for i in range(20):
            #ターゲットのインスタンスを生成
            target = Target(color = random.choice(s_colors),
            setup = True, eley = i)
            #もし黒い亀だったらblack_countの値を1増やす
            if target.bad:
                self.black_count += 1
            #ターゲット用のリストに格納する
            self.targets.append(target)

        #キーの割り当て
        self.on_key_down()

        #チラツキを防止する
        self.screen.tracer(0)

        #残りのtargetの数描画の初期設定
        self.rtext = turtle.Turtle()
        self.rtext.penup()
        #描画用のタートルオブジェクトを見えなくする
        self.rtext.ht()
        #描画位置に移動
        self.rtext.goto(-420, -400)
        #描画する
        self.rtext.write(f"残りのターゲット:{len(self.targets)}",
                        font = ("helvetica", 24))

        #時間の描画の初期設定
        self.ttext = turtle.Turtle()
        self.ttext.penup()
        self.ttext.ht()
        self.ttext.goto(0, -420)

        #初期のtargetの方向を変更
        for t in self.targets:
            t.left(random.randrange(36) * 10)

        #もし黒い亀が0匹だったら3匹追加する
        if self.black_count == 0:
            self.add_black()

        #初期のplayerの向きを変更
        self.player.left(37)

    #キーの割り当て
    def on_key_down(self):
        #スクリーンがキー・イベントを収集するようにする
        self.screen.listen()
        #左矢印ボタンに左回転を割り当てる
        self.screen.onkey(self.tleft, "Left")
        #右矢印ボタンに右回転を割り当てる
        self.screen.onkey(self.tright, "Right")

    #playerを左に回転
    def tleft(self):
        self.player.left(10)

    #playerを右に回転
    def tright(self):
        self.player.right(10)

    #黒い亀を3匹追加する
    def add_black(self):
        for i in range(3):
            target = Target(b = True)
            self.black_count += 1
            self.targets.append(target)

    #画面更新時のイベント
    def on_paint(self):
        #プレイヤーのイベントを実行
        self.player_event()

        #ターゲットのイベントの実行
        for t in self.targets:
            self.target_event(t)

    #playerのイベント
    def player_event(self):
        #壁との当たり判定
        #もしx軸側で当たったら回転する
        if self.is_hit_wall(self.player, "x"):
            angle = 180 - self.player.heading()
            self.player.setheading(angle)
            print(f"p : x : {angle}")

        #もしy軸側で当たったら回転する
        if self.is_hit_wall(self.player, "y"):
            angle = 360 - self.player.heading()
            self.player.setheading(angle)
            print(f"p : y : {angle}")

        #playerをstepに保持されている距離だけ進める
        self.player.forward(self.player.step)

    #targetのイベント
    def target_event(self, t):
        #ターゲットを進める
        t.forward(random.randrange(5))

        #壁とtargetとの当たり判定と衝突時のイベント
        if self.is_hit_wall(t, "x"):
            angle = 180 - t.heading()
            t.setheading(angle)
            t.forward(10)
            print(f"t : x : {angle}")

        if self.is_hit_wall(t, "y"):
            angle = 360 - t.heading()
            t.setheading(angle)
            t.forward(10)
            print(f"t : y : {angle}")

        #targetとplayerとの当たり判定
        if self.is_hit_target(t):
            #当たったtargetの色が黒色だった時の対応
            if t.bad:
                #プレイヤーの色や大きさなどを変更
                self.player.his_size = 0
                self.player.bef_size = 0
                self.player.app_size = 1
                self.player.size = 40
                self.player.step += 9
                self.player.color("red")
                self.black_count -= 1

                if self.black_count == 0:
                    self.add_black()
            #当たったtargetの色が黒色意外だった時の対応
            else:
                #プレイヤーの色や大きさを変更
                s = t.shapesize()
                self.player.his_size += s[0]
                self.player.color(t.pencolor())

                if self.player.his_size - self.player.bef_size >= 5:
                    self.player.app_size += 1
                    self.player.bef_size = self.player.his_size
                    self.player.size += 10
                    if self.player.step > 1:
                        self.player.step -= 1

                if self.player.step > 30:
                    self.player.step -= 10
                elif self.player.step > 20:
                    self.player.step -= 5
            #見かけの大きさを変更
            self.player.shapesize(self.player.app_size)
            #当たったターゲットを消す
            t.ht()
            self.target.remove(t)
            #残りのターゲットの表記を変更する
            self.rtext.clear()
            self.rtext.write(f"残りのターゲット:{len(self.targets)}",
                            font = ("helvetica", 24))

            print(f"s : {self.player.step}")

    #壁とオブジェクトとの当たり判定
    def is_hit_wall(self, t, dir):
        #呼び出されたのがx軸だった場合の判定
        if dir == "x":
            n = math.fabs(t.xcor())
            m = X_LIMIT
        #呼び出されたのがy軸だった場合の判定
        elif dir == "y":
            n = math.fabs(t.ycor())
            m = Y_LIMIT
        else:
            return False

        return n > m

    #targetとplayerとの当たり判定
    def is_hit_target(self, t):
        diff = math.sqrt(math.pow(t.xcor() - self.player.xcor(), 2)
                        + math.pow(t.ycor() - self.player.ycor(), 2))

        return diff < self.player.size

#importされた際に勝手にプログラムが実行されないようにする
if __name__ == "__main__":
    #TurtleGameクラスのインスタンスを生成
    turtle_game = TurtleGame()
