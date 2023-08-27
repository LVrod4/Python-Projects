from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import tkinter as tk

calculation = ''

def add_calc(symbol):
    global calculation
    calculation += str(symbol)
    text_resul.delete(1.0, 'end')
    text_resul.insert(1.0, calculation)

def evaluate_cal():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ''
        text_resul.delete(1.0, 'end')
        text_resul.insert(1.0, result)
    except:
        clear()
        text_resul.insert(1.0, 'Error')    

def clear():
    global calculation
    calculation = ''
    text_resul.delete(1.0, 'end')

def open_popup():
   top = Toplevel(root)
   top.geometry('300x120')
   top.title('Information')
   top.configure(bg='#003459')
   Label(top, text='GUI Calculator made on Tkinter\nMade by Ing. Laura Rodriguez\nVenezuela, 2023', font=('FreeSerif', 14),foreground='white', background='#003459').place(x=25, y=20)


root = tk.Tk()
root.title('Calculator')
root.geometry('360x360')
root.configure(bg='#003459')

style = ttk.Style()
style.configure('Btn_Style.TButton', background='#007EA7', font=('FreeSerif', 20), width=5, relief='flat')
style.map('Btn_Style.TButton', background=[('active', '#00A8E8')])

text_resul = tk.Text(root, height=1, width=17, font=('FreeSerif', 28), bg='#a2d2ff', relief='flat')
text_resul.grid(columnspan=4, padx=12, pady=15)


# OPERATION BUTTONS 
btn_paren_left = ttk.Button(root, text='(', command=lambda: add_calc('('), style='Btn_Style.TButton')
btn_paren_left.grid(row=1, column=0, pady=5)

btn_paren_right = ttk.Button(root, text=')', command=lambda:add_calc(')'), style='Btn_Style.TButton')
btn_paren_right.grid(row=1, column=1,pady=5)

btn_plus = ttk.Button(root, text='+', command=lambda:add_calc('+'), style='Btn_Style.TButton')
btn_plus.grid(row=1, column=3,pady=5)

btn_subs = ttk.Button(root, text='-', command=lambda:add_calc('-'), style='Btn_Style.TButton')
btn_subs.grid(row=2, column=3,pady=5)

btn_multi = ttk.Button(root, text='*', command=lambda:add_calc('*'), style='Btn_Style.TButton')
btn_multi.grid(row=3, column=3,pady=5)

btn_divid = ttk.Button(root, text='/', command=lambda:add_calc('/'), style='Btn_Style.TButton')
btn_divid.grid(row=4, column=3,pady=5)

btn_result = ttk.Button(root, text='=', command=lambda:evaluate_cal(), style='Btn_Style.TButton')
btn_result.grid(row=5, column=3,pady=5)

btn_clear = ttk.Button(root, text='⇽', command=clear, style='Btn_Style.TButton')
btn_clear.grid(row=1, column=2,pady=5)

btn_info = ttk.Button(root, text='Info', command=open_popup, style='Btn_Style.TButton')
btn_info.grid(row=5, column=0,pady=5)


# NUMERIC BUTTONS
for i in range(9, 0, -1):
    btn = ttk.Button(root, text=i, command=lambda num=i: add_calc(num), style='Btn_Style.TButton')
    btn.grid(row=(9-i)//3+2, column=(9-i)%3, pady=5)

btn_zero = ttk.Button(root, text='0', command=lambda:add_calc('0'), style='Btn_Style.TButton')
btn_zero.grid(row=5, column=1,pady=5)


# OTHER BUTTONS
btn_coma = ttk.Button(root, text=',', command=lambda:add_calc(','), style='Btn_Style.TButton')
btn_coma.grid(row=5, column=2,pady=5)


root.mainloop()