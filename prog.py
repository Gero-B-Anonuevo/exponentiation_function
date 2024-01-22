import tkinter as tk 
from tkinter import simpledialog

base_number = tk.simpledialog.askinteger("Hello", "What is your base number: ")
exponent_number = tk.simpledialog.askinteger("Hello", "What is your exponent: ")


def exponent(base, exp):
    print("base = ", base)
    print("exponent = ", exp)
    end_product = base ** exp
    print(base, " raises to the power of ", exp, " is: ", end_product)
    
exponent(base_number, exponent_number)