import tkinter as tk
import backend as be
import pygubu

class BankingApp:
    def __init__(self):
        self.builder = pygubu.Builder()
        self.builder.add_from_file('gui.ui')
        self.mainwindow = self.builder.get_object('root')
        self.builder.connect_callbacks(self)
        self.tree = self.builder.get_object('tree_transactions')
        self.lbl = self.builder.get_object('lbl_balance')

        self.tree.configure(columns=('id', 'date', 'amount', 'purpose', 'comment'), show='headings')
        self.tree.heading('id', text='ID')
        self.tree.heading('date', text='Datum')
        self.tree.heading('amount', text='Betrag (€)')
        self.tree.heading('purpose', text='Zweck')
        self.tree.heading('comment', text='Kommentar')
        self.tree.column('id', width=40)
        self.tree.column('date', width=100)
        self.tree.column('amount', width=100)
        self.tree.column('purpose', width=100)
        self.tree.column('comment', width=300)

        try:
            balance = be.view_balance()
        except Exception: pass

        self.lbl.config(text=f"aktueller Kassenstand: {balance} €")

    def view_transactions(self):
        self.offset = 0
        self.update_treeview()

    def next_page(self):
        if self.offset > 0:
            self.offset -= 10
        self.update_treeview()

    def prev_page(self):
        self.offset += 10
        self.update_treeview()

    def update_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        df = be.view_transactions(self.offset)
        print(df)

        for item in df:
            self.tree.insert("", "end", values=item)


if __name__ == "__main__":
    be.create_db()
    app = BankingApp()
    app.mainwindow.mainloop()
