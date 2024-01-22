import tkinter as tk 
from tkinter import simpledialog

base_number = tk.simpledialog.askinteger("Hello", "What is your base number: ")
exponent_number = tk.simpledialog.askinteger("Hello", "What is your exponent: ")


def exponent(base, exp):
    print("base = ", base)
    print("exponent = ", exp)
    end_product = base ** exp
    ender = = end_product
    print(base, " raises to the power of ", exp, " is: ", end_product)
    for num in range(exponent_number):
        num = base_number
        print(num, end='  *')
    return ender

print(exponent(base_number, exponent_number))