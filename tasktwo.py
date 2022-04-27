# Candidate 1294 | Task Two | April 19 2022 #

from tkinter import *

# Function to calculate and output the values requested #
def calculate():
    global output
    columnslabel = Label(root, text='Year\tBeginning value\tDeprecation Amount\tEnding Value')
    noyrstodepreciate = 0
    endingvalue = 0 
    salvagevalue = 0
    # Validate values entered #
    try:
        noyrstodepreciate = int(nydbox.get(1.0, 'end-1c'))
        salvagevalue = float(salbox.get(1.0, 'end-1c')) 
        endingvalue = float(savbox.get(1.0, 'end-1c')) 
    except:
        error = Label(root, text='Please eneter valid values!', bg='red') 
        error.pack()
        return
    # Calculate and display values for each year #
    year = 2022 + noyrstodepreciate
    while noyrstodepreciate > 0:
        beginningvalue = endingvalue
        depamt = round((beginningvalue - salvagevalue) / noyrstodepreciate, 2) 
        endingvalue = round(beginningvalue - depamt, 2) 
        noyrstodepreciate -= 1
        output += f'{year-noyrstodepreciate}\t\t{beginningvalue}\t\t{depamt}\t\t{endingvalue}\n'
        outputlabel.config(text=output)
        outputlabel.pack()
    return

# Function to clear Screen #
def clear():
    astnmbox.delete('1.0', END)
    savbox.delete('1.0', END)
    salbox.delete('1.0', END)
    nydbox.delete('1.0', END)
    global output
    output = ''
    outputlabel.config(text='')
    return


# Initialize a graphical environment #
root = Tk()
root.title('Future Value Calculator Program | 1294 | Task One')
root.resizable(False, False)
output = ''

# Title Label #
titlelabel = Label(root , text='Future Value Calculator Program | Candidate 1294 | Task One')
titlelabel.pack()

# Asset Name Input # 
astnmlabel = Label(root , text='Asset Name')
astnmlabel.pack()
astnmbox = Text(root, height=1, width=20)
astnmbox.pack() 

# Starting Asset Value Input # 
savlabel = Label(root , text='Starting Asset Value')
savlabel.pack()
savbox = Text(root, height=1, width=20)
savbox.pack() 

# Number of Years to Depreciate Input # 
nydlabel = Label(root , text='No. Years to Depreciate')
nydlabel.pack()
nydbox = Text(root, height=1, width=20)
nydbox.pack() 

# Salvage Value Input #
sallabel = Label(root , text='Salvage Value')
sallabel.pack()
salbox = Text(root, height=1, width=20)
salbox.pack() 

# Separator #
sep= Label(root , text=' ')
sep.pack()

# Calculate Button #
calcbutton = Button(root, text='Calculate Yearly Depreciation', command=calculate)
calcbutton.pack()

# Clear Button #
clearbutton = Button(root, text='Clear Text', command=clear)
clearbutton.pack()

# Exit Button #
exitbutton = Button(root, text='Exit Program', command=exit)
exitbutton.pack()

# Separator #
sep= Label(root , text=' ')
sep.pack()

# Output #
resultlabel = Label(root, text='Depreciation Schedule') 
columnslabel = Label(root, text='Year\tBeginning value\tDeprecation Amount\tEnding Value')
outputlabel = Label(root, text=output) 
resultlabel.pack()
columnslabel.pack() 

root.mainloop()
