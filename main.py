import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import time
import threading

bg_color = '#1A1A1A'
fg_color = '#FFFFFF'

Monte_Font = Font(
    family='Montserrat Light',
    size=20,
)

Playfair_Font = Font(
    family='Playfair Display Regular',
    size=30
)

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