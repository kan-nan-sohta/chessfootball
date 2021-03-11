import matplotlib.pyplot as plt
from IPython.display import clear_output
import random
from time import sleep
import numpy as np
import math
import tkinter as tk

# rootメインウィンドウの設定
root = tk.Tk()
root.title("application")
root.geometry("700x700")

# メインフレームの作成と設置
frame = tk.Frame(root)
frame.pack(fill = tk.BOTH, padx=20,pady=10)

# 画像ファイルをインスタンス変数に代入
light_green = tk.PhotoImage(file="img/light_green.png")
deep_green = tk.PhotoImage(file="img/deep_green.png")
red = tk.PhotoImage(file="img/red.png")
blue = tk.PhotoImage(file="img/blue.png")

# 画像のリサイズ
small_img = light_green.subsample(2, 1)
big_img = light_green.zoom(2, 2)

#ウィジェットの作成
buttons = [[tk.Button() for _ in range(5)] for _ in range(7)]
print(len(buttons), len(buttons[0]))

#buttonsの色付け
for i in range(7):
    for j in range(5):
        if i == 0:
            buttons[i][j] = tk.Button(frame, image=red)
        elif i == 6:
            buttons[i][j] = tk.Button(frame, image=blue)
        elif (i+j)%2 == 0:
            buttons[i][j] = tk.Button(frame, image=deep_green)
        else:
            buttons[i][j] = tk.Button(frame, image=light_green)
        
        # 各種ウィジェットの設置
        buttons[i][j].grid(row=i, column=j, padx=0.5, pady=0.5)

root.mainloop()