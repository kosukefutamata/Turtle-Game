import turtle #turtleモジュールを呼び出す
from module import* #module.pyを呼び出す

#マジックナンバーは定数で保持
SCREEN_WIDTH = 900 #スクリーンの横幅
SCREEN_HEIGHT = 900 #スクリーンの縦幅

#TurtleGameクラス
class TurtleGame:
    #分かりにくいのでメンバ変数は一番上で定義しておく
    screen = None #スクリーン用のメンバ変数

    targets = [] #今いるターゲットのオブジェクトを格納しておくリスト
    black_count = 0 #今いる黒い亀の数

    player = None #プレイヤー用のメンバ変数

    #コンストラクタ
    def __init__(self):
        #drawメソッドを呼び出す
        self.draw()

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


#importされた際に勝手にプログラムが実行されないようにする
if __name__ == "__main__":
    #TurtleGameクラスのインスタンスを生成
    turtle_game = TurtleGame()
