import turtle #turtleモジュールを呼び出す
from module import* #module.pyを呼び出す

#マジックナンバーは定数で保持
SCREEN_WIDTH = 900 #スクリーンの横幅
SCREEN_HEIGHT = 900 #スクリーンの縦幅

#TurtleGameクラス
class TurtleGame:
    #分かりにくいのでメンバ変数は一番上で定義しておく
    screen = None #スクリーン用のメンバ変数

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
        

#importされた際に勝手にプログラムが実行されないようにする
if __name__ == "__main__":
    #TurtleGameクラスのインスタンスを生成
    turtle_game = TurtleGame()
