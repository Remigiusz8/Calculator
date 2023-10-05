from tkinter import *
from tkinter import ttk

def layout():
    '''
    This function creates our layout with buttons
    '''

    root = Tk()

    def on_click(value):
        print(value)
        
    #entry.clear(0, 'end')
    #root = ttk.Frame(root, padding=100)
    #root.grid()
    entry = Entry(root, state='readonly', font=20).grid(column=0, row=0, columnspan=4)
    #ttk.Label(root, text="Hello world").grid(column=0, row=1)
    clr = Button(root, text="clr", font=20, command=lambda:on_click('test'))
    clr.grid(column=0, row=1, sticky='nesw')

    divider = Button(root, text="/", font=20, command=lambda:on_click('/'))
    divider.grid(column=1, row=1, sticky='nesw')

    multiplier = Button(root, text="*", font=20, command=lambda:on_click('*'))
    multiplier.grid(column=2, row=1, sticky='nesw')

    minus = Button(root, text="-", font=20, command=lambda:on_click('-'))
    minus.grid(column=3, row=1, sticky='nesw')

    one = Button(root, text="1", font=20, command=lambda:on_click(1))
    one.grid(column=0, row=2, sticky='nesw')

    two = Button(root, text="2", font=20, command=lambda:on_click(2))
    two.grid(column=1, row=2, sticky='nesw')

    three = Button(root, text="3", font=20, command=lambda:on_click(3))
    three.grid(column=2, row=2, sticky='nesw')

    plus = Button(root, text="+", font=20, command=lambda:on_click('+'))
    plus.grid(column=3, row=2, rowspan=2, sticky='nesw')

    four = Button(root, text="4", font=20, command=lambda:on_click(4))
    four.grid(column=0, row=3, sticky='nesw')

    five = Button(root, text="5", font=20, command=lambda:on_click(5))
    five.grid(column=1, row=3, sticky='nesw')

    six = Button(root, text="6", font=20, command=lambda:on_click(6))
    six.grid(column=2, row=3, sticky='nesw')

    seven = Button(root, text="7", font=20, command=lambda:on_click(7))
    seven.grid(column=0, row=4, sticky='nesw')

    eight = Button(root, text="8", font=20, command=lambda:on_click(8))
    eight.grid(column=1, row=4, sticky='nesw')

    nine = Button(root, text="9", font=20, command=lambda:on_click(9))
    nine.grid(column=2, row=4, sticky='nesw')

    equals = Button(root, text="=", font=20, command=lambda:on_click('='))
    equals.grid(column=3, row=4, rowspan=2, sticky='nesw')

    zero = Button(root, text="0", font=20, command=lambda:on_click(0))
    zero.grid(column=0, row=5, columnspan=3, sticky='nesw')

    #exit = Button(fg="red", bg="blue", font=14, text="Quit Calculator", command=root.destroy, height=3, width=15).grid()
    root.mainloop()