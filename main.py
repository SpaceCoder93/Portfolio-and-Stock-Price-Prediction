import tkinter as tk
import tkinter.ttk as ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('StockGuru')
        self.state('zoomed')
        self.mainloop()

class LoginPage(tk.Frame):
    def __init__(self):
        pass
class CreatePage(tk.Frame):
    def __init__(self):
        pass
class Verification(tk.Frame):
    def __init__(self):
        pass
class DashBoard(tk.Frame):
    def __init__(self):
        pass
class Prediction(tk.Frame):
    def __init__(self):
        pass

if __name__ == "__main__":
    App()