# Candidate 1294 | Task One | April 19 2022 #

from tkinter import *

# Calculate the future value #
def calculate():
    present_value = float(pvdbox.get(1.0, "end-1c"))
    time = int(noybox.get(1.0, 'end-1c'))
    x = present_value
    resultlabel.config(text= f'Future Value Dollars = {round(pow(x, time), 2)}')
    return

# Clears Screen #
def clear():
    pvdbox.delete('1.0', END)
    noybox.delete('1.0', END)
    resultlabel.config(text='Future Value Dollars = ')
    return

# Sets either yearly or montly #
def setym():
    return 

# Initialize a graphical environment #
root = Tk()
root.title('Future Value Calculator Program | 1294 | Task One')
root.resizable(False, False)

# Title Label #
titlelabel = Label(root , text='Future Value Calculator Program | Candidate 1294 | Task One')
titlelabel.pack()

# Present Value Dollars Input Box #
pvdlabel = Label(root , text='Present Value Dollars')
pvdlabel.pack()
pvdbox = Text(root, height=1, width=20)
pvdbox.pack() 

# Number of Years Input Box #
noylabel = Label(root , text='Number of Years')
noylabel.pack()
noybox = Text(root, height=1, width=20)
noybox.pack() 

# Compounding Period Dropdown Menu # 
cplabel = Label(root , text='Compounding Period (Y/M)')
cplabel.pack()
clicked = StringVar()
clicked.set('Y (Yearly)')
options = [
    'Y (Yearly)',
    'M (Monthly)'
]
drop = OptionMenu(root, clicked, *options, command=None) 
drop.pack()

# Separator #
sep= Label(root , text=' ')
sep.pack()

# Calculate Button #
calcbutton = Button(root, text='Calculate FVD', command=calculate)
calcbutton.pack()
resultlabel = Label(root, text='Future Value Dollars = ') 
resultlabel.pack()

# Clear Button #
clearbutton = Button(root, text='Clear Text', command=clear)
clearbutton.pack()

# Exit Button #
exitbutton = Button(root, text='Exit Program', command=exit)
exitbutton.pack()

root.mainloop()
