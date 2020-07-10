# -*- coding:utf-8 -*-
import tkinter
from AlgorithmSimulator.view import main_view
from AlgorithmSimulator.controller import main_view_controller
from AlgorithmSimulator.model import sort

# アプリ生成
app = tkinter.Tk()
app.title("Algorithm Simulator")

# Viewオブジェクト生成
view = main_view.View(app)

# Sortオブジェクト生成
sort = sort.Sort(view)

# Controllerオブジェクト生成
controller = main_view_controller.Controller(view, sort)

# mainloopでイベント受付を待機
app.mainloop()