import turtle

#playerのクラス
#turtle.Turtleクラスを継承し派生クラスを作る
class Player(turtle.Turtle):

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
