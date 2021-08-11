from tkinter import *



class MainWindow():
    
    # Set Title, Grid and Menu
    def __init__(self, gui):
  
        # Title and settings
        self.gui = gui
        gui.title("Sudoku Solver by Farid & Jerin")

        font = ('Arial', 18)
        color = 'white'
        px, py = 0, 0

        # Front-end Grid
        self.__table = []
        for i in range(1,10):
            self.__table += [[0,0,0,0,0,0,0,0,0]]

        for i in range(0,9):
            for j in range(0,9):
                
                if (i < 3 or i > 5) and (j < 3 or j > 5):
                    color = 'light sky blue'
                elif i in [3,4,5] and j in [3,4,5]:
                    color = 'light sky blue'
                else:
                    color = 'white'

                self.__table[i][j] = Entry(gui, width = 2, font = font, bg = color, cursor = 'arrow', borderwidth = 0,
                                          highlightcolor = 'yellow', highlightthickness = 1, highlightbackground = 'black',
                                          textvar = number_bank[i][j])
                self.__table[i][j].bind('<Motion>', self.ammend_grid)
                self.__table[i][j].bind('<FocusIn>', self.ammend_grid)
                self.__table[i][j].bind('<Button-1>', self.ammend_grid)
                self.__table[i][j].grid(row=i, column=j)


        # Front-End Menu
        menu = Menu(gui)
        gui.config(menu = menu)

        file = Menu(menu)
        menu.add_cascade(label = 'File', menu = file)
        file.add_command(label = 'Exit', command = gui.quit)
        file.add_command(label = 'Solve', command = self.solve_grid)
        file.add_command(label = 'Clear', command = self.clear_grid)


    # Correct the Grid if inputs are uncorrect
    def ammend_grid(self, event):
        for i in range(9):
            for j in range(9):
                if number_bank[i][j].get() == '':
                    continue
                if len(number_bank[i][j].get()) > 1 or number_bank[i][j].get() not in ['1','2','3','4','5','6','7','8','9']:
                    number_bank[i][j].set('')


    # Clear the Grid
    def clear_grid(self):
        for i in range(9):
            for j in range(9):
                number_bank[i][j].set('')


    # Calls the class SolveSudoku
    
    def solve_grid(self):
        solution = SolveSudoku()
class SolveSudoku():
    
    def __init__(self):
        self.set_all_zero()
        self.sudoku_solve()


    # set all the empty cells to zero first
    #NOTE this could be used to generate the random numbers
    def set_all_zero(self):
        number_range = range(1, 10)
        

        for i in range(number_range):
            for j in range(number_range):
                if number_bank[i][j].get() not in ['1','2','3','4','5','6','7','8','9']:
                    number_bank[i][j].set(0)


    # Start the Algorithm
    def sudoku_solve(self, i=0, j=0):
        i,j = self.fill_next_cell(i, j)

        # If i == -1 the position is Ok or the Sudoku is Solved
        if i == -1:
            return True
        for e in range(1,10):
            if self.is_valid_cell(i,j,e):
                number_bank[i][j].set(e)
                if self.sudoku_solve(i, j):
                    return True
                # Undo the current cell for backtracking
                number_bank[i][j].set(0)
        return False


    # Search the Nearest Cell to fill
    def fill_next_cell(self, i, j):

        for x in range(i,9):
            for y in range(j,9):
                if number_bank[x][y].get() == '0':
                    return x,y

        for x in range(0,9):
            for y in range(0,9):
                if number_bank[x][y].get() == '0':
                    return x,y

        return -1,-1


    # Check the Validity of number_bank[i][j]
    def is_valid_cell(self, i, j, e):

        for x in range(9):
            if number_bank[i][x].get() == str(e):
                return False

        for x in range(9):
            if number_bank[x][j].get() == str(e):
                return False

        # Finding the Top x,y Co-ordinates of the section containing the i,j cell    
        secTopX, secTopY = 3 *int((i/3)), 3 *int((j/3))
        for x in range(secTopX, secTopX+3):
            for y in range(secTopY, secTopY+3):
                if number_bank[x][y].get() == str(e):
                    return False
        
        return True

root = Tk()
root.geometry('600x600')
 

# Matrix containing all stored numbers
number_bank = []
for i in range(1,10):
    number_bank += [[0,0,0,0,0,0,0,0,0]]
for i in range(0,9):
    for j in range(0,9):
        number_bank[i][j] = StringVar(root)


app = MainWindow(root)
root.mainloop()
# Class containing Sudoku Solver backtacking algorithm 


