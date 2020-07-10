import time

class Sort():

    # ソート種類
    SELECTION_SORT = 1
    QUICK_SORT = 2
    MERGE_SORT = 3
    INSERTION_SORT = 4

    def __init__(self, view):
        'ソートを行うオブジェクト生成'

        self.view = view
        self.elapsed_time = 0

    def start(self, data, method):
        'ソートを開始'

        # ソートするデータのリストを設定
        self.data = data

        # ソートするデータの数を設定
        self.num = len(data)

        # 比較回数の初期化
        self.compare_num = 0

        # methodに応じてソートを実行
        if method == Sort.SELECTION_SORT:
            # 選択ソート実行
            self.selection_sort(self.data)

        elif method == Sort.QUICK_SORT:
            # クイックソート実行
            self.quick_sort(0, self.num - 1)

        elif method == Sort.MERGE_SORT:
            # マージソート用のワークメモリを用意
            self.work = [0] * self.num

            # マージソート実行
            self.merge_sort(0, self.num - 1)

        elif method == Sort.INSERTION_SORT:
            # 挿入ソートの実行
            self.insertion_sort(self.data)


        for num in self.data:
            print(num)

        # 比較回数を返却
        return self.compare_num


    def selection_sort(self, data):
        '選択ソートを実行'
        print('Execute selection sort')
        for i in range(len(data)):
            minIdx = i  # 最小値の位置をセットする
            for j in range(i + 1, len(data)):  # 比較対象のインデックスの隣から探索開始
                if data[minIdx] > data[j]:  # 最小値と仮定している数字よりも小さい数を見つけた場合
                    minIdx = j  # 最小値のインデックスを更新
                self.compare_num += 1
            data[i], data[minIdx] = data[minIdx], data[i]  # 値を入れ変える
            self.view.draw_data(self.data)

    def quick_sort(self, left, right):
        'クイックソートを実行'

        if left >= right:
            # データ数１つ以下なのでソート終了
            return

        # pivot の決定
        pivot = self.data[left]

        i = left
        j = right

        # pivot以下の数字を配列の前半に、
        # pivot以上の数字を配列の後半に集める

        while True:
            # pivot以上の数字を左側から探索
            while self.data[i] < pivot:
                i += 1

                # 比較回数をインクリメント
                self.compare_num += 1

            # pivot以下の数字を右側から探索
            while self.data[j] > pivot:
                j -= 1

                # 比較回数をインクリメント
                self.compare_num += 1

            # i >= j になったということは、
            # 配列の左側にpivot以下の数字が、
            # 配列の右側にpivot以上の数字が集まったということ
            if i >= j:
                # 集合の分割処理は終了
                break

            # 探索した２つの数字を交換
            tmp = self.data[i]
            self.data[i] = self.data[j]
            self.data[j] = tmp

            # 交換後の数字の次から探索再開
            i += 1
            j -= 1

        # 現在のデータの並びを表示
        self.view.draw_data(self.data)

        # 小さい数字を集めた範囲に対してソート
        self.quick_sort(left, i - 1)

        # 大きい数字を集めた範囲に対してソート
        self.quick_sort(j + 1, right)

    def merge_sort(self, left, right):
        'マージソートを実行'

        if left == right:
            # データ数１つなのでソート終了
            return

        # 集合を中央で２つに分割する
        mid = (left + right) // 2

        # 分割後の各集合のデータをそれぞれソートする
        self.merge_sort(left, mid)
        self.merge_sort(mid + 1, right)

        # ソート済みの各集合をマージする
        self.merge(left, mid, right)

        # 現在のデータの並びを表示
        self.view.draw_data(self.data)

    def merge(self, left, mid, right):
        '集合をマージする'

        # １つ目の集合の開始点をセット
        i = left

        # ２つ目の集合の開始点をセット
        j = mid + 1

        # マージ先集合の開始点をセット
        k = 0

        # ２つの集合のどちらかが、
        # 全てマージ済みになるまでループ
        while i <= mid and j <= right:

            # 比較回数をインクリメント
            self.compare_num += 1

            # マージ済みデータを抜いた２つの集合の、
            # 先頭のデータの小さい方をマージ
            if (self.data[i] < self.data[j]):

                self.work[k] = self.data[i]

                # マージした集合のインデックスと、
                # マージ先集合のインデックスをインクリメント
                i += 1
                k += 1
            else:
                self.work[k] = self.data[j]
                # マージした集合のインデックスと、
                # マージ先集合のインデックスをインクリメント
                j += 1
                k += 1

        # マージ済みでないデータが残っている集合を、
        # マージ先集合にマージ
        while i <= mid:

            # 比較回数をインクリメント
            self.compare_num += 1

            self.work[k] = self.data[i]
            i += 1
            k += 1

        while j <= right:

            # 比較回数をインクリメント
            self.compare_num += 1

            self.work[k] = self.data[j]
            j += 1
            k += 1

        # マージ先集合をdataにコピー
        j = 0
        for i in range(left, right + 1):
            self.data[i] = self.work[j]
            j += 1

    def insertion_sort(self,data):
        print('Execute insertion sort')
        for i in range(1, len(data)):
            temp = data[i]  # 配列の左端のデータをソート済みとみなし、ソート開始位置の数をtempに記憶
            j = i - 1  # ソート済みの配列の右端のインデックスを抽出
            while (j >= 0 and data[j] > temp):
                '''
                このwhile文では
                1. インデックスIを境に左側がソート済み配列、右側がソート対象配列になる
                2. ソートが終わったとみなしている配列をインデックスJをデクリメントしつつ、インデックスiの値と比較
                3. もし2でdata[j] > data[i]を満たせば、場所を交換する。
                4. そのとき、data[j]を一つ後ろ、すなわちdata[j + 1]に移して、jをデクリメントしてから値をスワップする
                '''
                data[j + 1] = data[j]  # 要素を一つ後ろにずらす
                j -= 1
                self.compare_num += 1
            data[j + 1] = temp
            # 現在のデータの並びを表示
            self.view.draw_data(data)

