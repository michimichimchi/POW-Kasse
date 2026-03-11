import tkinter as tk
import backend as be
import pygubu

class BankingApp:
    def __init__(self):
        self.builder = pygubu.Builder()
        self.builder.add_from_file('gui.ui')
        self.mainwindow = self.builder.get_object('root')

        balance = be.view_balance()

        self.lbl = self.builder.get_object('lbl_balance')
        self.lbl.config(text=f"aktueller Kassenstand: {balance} €")

if __name__ == "__main__":
    app = BankingApp()
    app.mainwindow.mainloop()