import turtle
import random #randomモジュールを呼び出す

#playerのクラス
#turtle.Turtleクラスを継承し派生クラスを作る
class Player(turtle.Turtle):
    "ーーーーーーー以下書き足しーーーーーーー"
    #メンバ変数の定義
    step = 9
    size = 40
    his_size = 0
    bef_size = 0
    app_size = 1
    "ーーーーーーーーーーーーーーーーーーーー"

    #コンストラクタ
    def __init__(self):
        #基底クラスのコンストラクタを実行する
        super().__init__()
        #プレイヤーの形をタートルにする
        self.shape("turtle")
        #プレイヤーのサイズを１にする
        self.shapesize(1)
        #プレイヤーの色を赤色にする
        self.color("red")
        #プレイヤーのペンを上げる
        self.penup()

#targetのクラス
class Target(turtle.Turtle):
    #この亀が黒い亀かどうか
    bad = None
    #targetが使用できる色のリスト
    colors = ["blue", "green", "purple", "pink", "yellow", "orange"]

    #コンストラクタ
    #colorは上の色のリストよりランダムに決定しているが任意での設定も可能
    #setupはゲームが始まる前の最初のターゲットを表示させるときに使う
    #eleyは上記の場合に出現させるy座標を指定するためのもの
    #bはその亀を黒い亀にするかどうかを決めるもの
    def __init__(self, color = random.choice(colors),
    setup = False, eley = None, b = False):
        #基底クラスのコンストラクタを実行する
        super().__init__()
        #黒い亀になるかどうかを判断
        self.bad = b
        if self.bad:
            color = "black"
        elif color == "black":
            self.bad = True

        self.shape("turtle")
        #targetの大きさをランダムで選ぶ
        self.shapesize(random.randrange(2, 6))
        self.color(color)
        self.penup()
        #出現地のｘ座標をランダムに決定
        self.setx(random.randrange(9) * 100 - 400)
        #出現地のｙ座標をランダムに決定　eleyがある場合はその値を利用する
        self.sety(eley * 35 - 350 if eley else random.randrange(15) * 50 - 350)
        #setupがFalseだったらターゲットが最初に向く角度をランダムに変える
        if not setup:
            self.left(random.randrange(36) * 10)
