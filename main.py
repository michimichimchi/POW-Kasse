import tkinter as tk
import backend as be
import pygubu

root = tk.Tk()

root.title("POW Kasse")

root.geometry("1000x700")

label = tk.Label(root, text = "testestest")
label.place(x = 110, y= 40)

view_balance = tk.Button(root, text = "Kontostand ansehen", command=be.view_balance)
view_balance.place(x=110, y= 80)

root.mainloop()