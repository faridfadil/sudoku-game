from tkinter import *

class MainWindow():
    
    # Set Title, Grid and Menu
    def __init__(self, gui):
        # Title and settings
        self.gui = gui
        gui.title("Sudoku Solver by Farid & Jerin")

        font = ('Arial', 18)
        color = 'white'
        # px, py = 0, 0

        # Front-end Grid
        self.gui_grid = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        #setting the colour of the grid
        for column in range(GRID_SIZE):
            for row in range(GRID_SIZE):

                if (column < 3 or column > 5) and (row < 3 or row > 5):
                    color = 'light sky blue'
                elif column in [3,4,5] and row in [3,4,5]:
                    color = 'light sky blue'
                else:
                    color = 'white'
                
                self.gui_grid[row][column] = Entry(gui, width = 2, font = font, bg = color, cursor = 'arrow', borderwidth = 0,
                                                 highlightcolor = 'red', highlightthickness = 1, highlightbackground = 'black',
                                                 textvar = number_bank[i][j])
                self.gui_grid[row][column].bind('<Motion>', self.ammend_grid)
                self.gui_grid[row][column].bind('<FocusIn>', self.ammend_grid)
                self.gui_grid[row][column].bind('<Button-1>', self.ammend_grid)
                self.gui_grid[row][column].grid(row=row, column=column)


        # Menu at the top left corner. 
        menu = Menu(gui)
        gui.config(menu = menu)
       
        file = Menu(menu)
        menu.add_cascade(label = 'File', menu = file)
        file.add_command(label = 'Exit', command = gui.quit)
        file.add_command(label = 'Solve', command = self.solve_grid)
        file.add_command(label = 'Clear', command = self.clear_grid)


    # Correct the Grid if inputs are incorrect.
    def ammend_grid(self, event):
        for column in range(9):
            for row in range(9):
                if number_bank[row][column].get() == '':
                    continue
                if len(number_bank[row][column].get()) > 1 or number_bank[row][column].get() not in ['1','2','3','4','5','6','7','8','9']:
                    number_bank[row][column].set('')


    # Clear the Grid
    def clear_grid(self):
        for column in range(9):
            for row in range(9):
                number_bank[row][column].set('')


    # Calls the class SolveSudoku
    def solve_grid(self):
        solution = SolveSudoku()  

# Class containing Sudoku Solver backtacking algorithm 
class SolveSudoku():
    
    def __init__(self):
        self.set_all_zero()
        self.sudoku_solve()


    # set all the empty cells to zero first
    #NOTE this could be used to generate the random numbers
    def set_all_zero(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
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

number_bank = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

root = Tk()
root.geometry('270x500')  
Label(root, text = "Python Sudoku Solver",font = ('Helvetica 16 bold')).place( x = 20, y = 300)
Label(root, text = "Press File in the top left corner for commands",font = ('Helvetica 9 bold')).place( x = 5, y = 350)
# Setting all the cells in the grid to be StringVar class so we can use .set() and .get() on each grid 
# to fill in values. 
for i in range(0,9):
    for j in range(0,9):
        number_bank[i][j] = StringVar(root)

GRID_SIZE = 9

sudoku_application = MainWindow(root)
root.mainloop()
from tkinter import *

class MainWindow():
    
    # Set Title, Grid and Menu
    def __init__(self, gui):
        # Title and settings
        self.gui = gui
        gui.title("Sudoku Solver by Farid & Jerin")

        font = ('Arial', 18)
        color = 'white'
        # px, py = 0, 0

        # Front-end Grid
        self.gui_grid = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        #setting the colour of the grid
        for column in range(GRID_SIZE):
            for row in range(GRID_SIZE):

                if (column < 3 or column > 5) and (row < 3 or row > 5):
                    color = 'light sky blue'
                elif column in [3,4,5] and row in [3,4,5]:
                    color = 'light sky blue'
                else:
                    color = 'white'
                
                self.gui_grid[row][column] = Entry(gui, width = 2, font = font, bg = color, cursor = 'arrow', borderwidth = 0,
                                                 highlightcolor = 'red', highlightthickness = 1, highlightbackground = 'black',
                                                 textvar = number_bank[i][j])
                self.gui_grid[row][column].bind('<Motion>', self.ammend_grid)
                self.gui_grid[row][column].bind('<FocusIn>', self.ammend_grid)
                self.gui_grid[row][column].bind('<Button-1>', self.ammend_grid)
                self.gui_grid[row][column].grid(row=row, column=column)


        # Menu at the top left corner. 
        menu = Menu(gui)
        gui.config(menu = menu)
       
        file = Menu(menu)
        menu.add_cascade(label = 'File', menu = file)
        file.add_command(label = 'Exit', command = gui.quit)
        file.add_command(label = 'Solve', command = self.solve_grid)
        file.add_command(label = 'Clear', command = self.clear_grid)


    # Correct the Grid if inputs are incorrect.
    def ammend_grid(self, event):
        for column in range(9):
            for row in range(9):
                if number_bank[row][column].get() == '':
                    continue
                if len(number_bank[row][column].get()) > 1 or number_bank[row][column].get() not in ['1','2','3','4','5','6','7','8','9']:
                    number_bank[row][column].set('')


    # Clear the Grid
    def clear_grid(self):
        for column in range(9):
            for row in range(9):
                number_bank[row][column].set('')


    # Calls the class SolveSudoku
    def solve_grid(self):
        solution = SolveSudoku()  

# Class containing Sudoku Solver backtacking algorithm 
class SolveSudoku():
    
    def __init__(self):
        self.set_all_zero()
        self.sudoku_solve()


    # set all the empty cells to zero first
    #NOTE this could be used to generate the random numbers
    def set_all_zero(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
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

number_bank = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

root = Tk()
root.geometry('270x500')  
Label(root, text = "Python Sudoku Solver",font = ('Helvetica 16 bold')).place( x = 20, y = 300)
Label(root, text = "Press File in the top left corner for commands",font = ('Helvetica 9 bold')).place( x = 5, y = 350)
# Setting all the cells in the grid to be StringVar class so we can use .set() and .get() on each grid 
# to fill in values. 
for i in range(0,9):
    for j in range(0,9):
        number_bank[i][j] = StringVar(root)

GRID_SIZE = 9

sudoku_application = MainWindow(root)
root.mainloop()
