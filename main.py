import tkinter as tk
import tkinter.ttk as ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('StockGuru')
        self.attributes('-fullscreen', True)
        self.mainloop()

if __name__ == "__main__":
    App()