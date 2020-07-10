class Controller():
    def __init__(self, view, sort):
        'SortとViewを制御するオブジェクトを生成'

        # 制御するViewとSortのオブジェクト設定
        self.view = view
        self.sort = sort

        # ボタンクリック時のイベントを受け付け
        self.view.button["command"] = self.button_click

    def button_click(self):
        'ボタンクリック時の処理'

        num = self.view.get_data_num()
        # Viewの開始
        if not self.view.start(num):
            # メッセージ更新
            self.view.update_message(
                "Too much data"
            )

            # 失敗したら何もしない
            return

        # NUMを最大値としたデータ数NUMの乱数リストを生成
        data = []
        for _ in range(num):
            import random
            data.append(int(random.randint(0, num - 1)))

        # 初期データの並びを降順にする場合
        #data = []
        # for i in range(num):
        #	data.append(num - i)

        # メッセージ更新
        self.view.update_message("Sorting")

        # ソートを開始
        compare_num = self.sort.start(data, self.view.get_algorithm())

        # メッセージ更新
        self.view.update_message(
            "Simulation Completed！（Number of comparison：" + str(compare_num) + "）"
        )

