import tkinter
import time
from AlgorithmSimulator.config import general_setting
from AlgorithmSimulator.model import sort

class View():

    def __init__(self, master):
        'UI関連のオブジェクト生成'

        # 各種設定
        self.drawn_obj = []

        # キャンバスのサイズを決定
        self.canvas_width = general_setting.CANVAS_WIDTH
        self.canvas_height = general_setting.CANVAS_HEIGHT

        # 情報表示用のフレームを作成
        self.canvas_frame = tkinter.Frame(
            master,
        )
        self.canvas_frame.grid(column=1, row=1)

        # 操作用ウィジェットのフレームを作成
        self.operation_frame = tkinter.Frame(
            master,
        )
        self.operation_frame.grid(column=2, row=1, padx=10)

        # キャンバスの生成と配置
        self.canvas = tkinter.Canvas(
            self.canvas_frame,
            width=self.canvas_width,
            height=self.canvas_height,
        )
        self.canvas.pack()

        # ラベルの生成と配置
        self.text = tkinter.StringVar()
        self.text.set("開始ボタンを押してね")

        self.label = tkinter.Label(
            self.canvas_frame,
            textvariable=self.text,
        )
        self.label.pack()

        # テキストボックス配置用のフレームの生成と配置
        max_w = self.canvas_width // 2
        max_h = self.canvas_height // 2
        if max_w < max_h:
            max = max_w
        else:
            max = max_h

        self.text_frame = tkinter.LabelFrame(
            self.operation_frame,
            text="データ数（最大" + str(max) + "）"
        )
        self.text_frame.pack(ipadx=10, pady=10)

        self.entry = tkinter.Entry(
            self.text_frame,
            width=4
        )
        self.entry.pack()

        # ラジオボタン配置用のフレームの生成と配置
        self.radio_frame = tkinter.LabelFrame(
            self.operation_frame,
            text="アルゴリズム"
        )
        self.radio_frame.pack(ipadx=10, pady=10)

        # チェックされているボタン取得用のオブジェクト生成
        self.sort = tkinter.IntVar()
        self.sort.set(sort.Sort.QUICK_SORT)

        # アルゴリズム選択用のラジオボタンを３つ作成し配置
        self.selection_button = tkinter.Radiobutton(
            self.radio_frame,
            variable=self.sort,
            text="選択ソート",
            value=sort.Sort.SELECTION_SORT
        )
        self.selection_button.pack()

        self.quick_button = tkinter.Radiobutton(
            self.radio_frame,
            variable=self.sort,
            text="クイックソート",
            value=sort.Sort.QUICK_SORT
        )
        self.quick_button.pack()

        self.merge_button = tkinter.Radiobutton(
            self.radio_frame,
            variable=self.sort,
            text="マージソート",
            value=sort.Sort.MERGE_SORT
        )
        self.merge_button.pack()

        # 開始ボタンの生成と配置
        self.button = tkinter.Button(
            self.operation_frame,
            text="開始",
        )
        self.button.pack()

    def start(self, n):
        '背景を描画'

        # データ数をセット
        self.num = n

        # １つのデータを表す線の幅を決定
        self.line_width =  self.canvas_width / self.num

        # データの値１の線の高さを決定
        # データの値が N の時、線の高さは self.line_height * N となる
        self.line_height =  self.canvas_height / self.num

        # データ数が多すぎて描画できない場合
        if self.line_width < 2 or self.line_height < 2:
            return False

        # 背景位置調整用（中央寄せ）
        self.offset_x = int(
            (self.canvas.winfo_width() - self.line_width * self.num) / 2
        )
        self.offset_y = int(
            (self.canvas.winfo_height() - self.line_height * self.num + 1) / 2
        )

        # 一旦描画しているデータを削除
        for obj in self.drawn_obj:
            self.canvas.delete(obj)

        # 削除したので描画済みデータリストは空にする
        self.drawn_obj = []

        # 事前に背景オブジェクトを削除
        self.canvas.delete("background")

        # 背景を描画
        self.canvas.create_rectangle(
            self.offset_x,
            self.offset_y,
            int(self.offset_x + self.line_width * self.num),
            int(self.offset_y + self.line_height * self.num),
            width=0,
            fill="#EEEEFF",
            tag="background"
        )

        # 即座に描画を反映
        self.canvas.update()

        return True

    def get_algorithm(self):
        'ソートアルゴリズム取得'

        return self.sort.get()

    def get_data_num(self):
        'データ数取得'

        return int(self.entry.get())

    def draw_data(self, data):
        'データの並びを線としてを描画'

        # 一旦描画しているデータを削除
        for obj in self.drawn_obj:
            self.canvas.delete(obj)

        # 削除したので描画済みデータリストは空にする
        self.drawn_obj = []

        # リストの数字を矩形で描画
        i = 0
        for value in data:
            # 矩形の始点と終点を決定

            # データ位置から矩形の横方向座標を決定
            x1 = int(self.offset_x + i * self.line_width)
            x2 = int(self.offset_x + (i + 1) * self.line_width)

            # データの値から矩形の縦方向座標を決定
            y1 = int(self.offset_y + self.line_height * (self.num - value))
            y2 = int(self.offset_y + self.line_height * self.num)

            # 後から消せるようにtagをつけておく
            tag = "line" + str(i)
            self.drawn_obj.append(tag)

            # 長方形を描画
            self.canvas.create_rectangle(
                x1, y1,
                x2, y2,
                tag=tag,
                fill="#FFA588",
                width=1
            )

            i += 1

        # 描画を即座に反映
        self.canvas.update()

        # WAIT秒分だけスリープ
        time.sleep(general_setting.WAIT)

    def update_message(self, text):
        'メッセージを更新してラベルに表示'

        # ラベルに描画する文字列をセット
        self.text.set(text)

        # 描画を即座に反映
        self.label.update()
