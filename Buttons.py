import tkinter as tk
import Calculations as calc

def layout():

    container = []

    def on_click(value):
        entry.config(state="normal")
        if ord(value) not in [45, 43, 61, 47, 42, 67]:
            entry.insert(tk.END, value)
        else:
            final = collect(value)
            entry.delete(0, tk.END)
        if ord(value) == 61:
            entry.insert(tk.END, final)
        entry.config(state="readonly")    

    def collect(value):
        container.append(entry.get())
        if ord(value) in [45, 43, 61, 47, 42]:
            container.append(value)
        elif ord(value) == 67:
            container.clear()
        print(container)
        return calc.calculate(container)

    root = tk.Tk()
    root.title("Calculator")

    entry = tk.Entry(root, font=20, textvariable="info", state="readonly", justify=tk.CENTER)
    entry.grid(column=0, row=0, columnspan=4)
    
    clr = tk.Button(root, text="C", font=20, command=lambda:on_click('C'))
    clr.grid(column=0, row=1, sticky='nesw')

    divider = tk.Button(root, text="/", font=20, command=lambda:[on_click('/')])
    divider.grid(column=1, row=1, sticky='nesw')

    multiplier = tk.Button(root, text="*", font=20, command=lambda:on_click('*'))
    multiplier.grid(column=2, row=1, sticky='nesw')

    minus = tk.Button(root, text="-", font=20, command=lambda:[on_click('-')])
    minus.grid(column=3, row=1, sticky='nesw')

    one = tk.Button(root, text="1", font=20, command=lambda:on_click('1'))
    one.grid(column=0, row=2, sticky='nesw')

    two = tk.Button(root, text="2", font=20, command=lambda:on_click('2'))
    two.grid(column=1, row=2, sticky='nesw')

    three = tk.Button(root, text="3", font=20, command=lambda:on_click('3'))
    three.grid(column=2, row=2, sticky='nesw')

    plus = tk.Button(root, text="+", font=20, command=lambda:[on_click('+')])
    plus.grid(column=3, row=2, rowspan=2, sticky='nesw')

    four = tk.Button(root, text="4", font=20, command=lambda:on_click('4'))
    four.grid(column=0, row=3, sticky='nesw')

    five = tk.Button(root, text="5", font=20, command=lambda:on_click('5'))
    five.grid(column=1, row=3, sticky='nesw')

    six = tk.Button(root, text="6", font=20, command=lambda:on_click('6'))
    six.grid(column=2, row=3, sticky='nesw')

    seven = tk.Button(root, text="7", font=20, command=lambda:on_click('7'))
    seven.grid(column=0, row=4, sticky='nesw')

    eight = tk.Button(root, text="8", font=20, command=lambda:on_click('8'))
    eight.grid(column=1, row=4, sticky='nesw')

    nine = tk.Button(root, text="9", font=20, command=lambda:on_click('9'))
    nine.grid(column=2, row=4, sticky='nesw')

    equals = tk.Button(root, text="=", font=20, command=lambda:on_click('='))
    equals.grid(column=3, row=4, rowspan=2, sticky='nesw')

    zero = tk.Button(root, text="0", font=20, command=lambda:on_click('0'))
    zero.grid(column=0, row=5, columnspan=3, sticky='nesw')

    #exit = tk.Button(fg="red", bg="blue", font=14, text="Quit Calculator", command=root.destroy, height=3, width=15).grid()
    root.mainloop()