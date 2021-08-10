from tkinter import *
from MainWindow import *
from SolveSudoku import *

root = Tk()
root.geometry('275x283')       
        
# Matrix containing all stored numbers
number_bank = []
for i in range(1,10):
    number_bank += [[0,0,0,0,0,0,0,0,0]]
for i in range(0,9):
    for j in range(0,9):
        number_bank[i][j] = StringVar(root)


app = MainWindow(root)
root.mainloop()
