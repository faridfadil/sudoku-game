from tkinter import *

class MainWindow():
    
    def __init__(self, gui):
        # setting GUI title and settings 
        self.gui = gui
        gui.title("Sudoku Solver by Farid & Jerin")
        gui.geometry('270x320')  
        #setting font used in GUI
        font = ('Arial', 18)
        #setting background colour of GUI. 
        color = 'white'

        # the grid that will be displayed on the GUI
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

        #setting the colours of the grid
        for row in range(GRID_SIZE):
            for column in range(GRID_SIZE):

                if (column < 3 or column > 5) and (row < 3 or row > 5):
                    color = 'light sky blue'
                elif column in [3,4,5] and row in [3,4,5]:
                    color = 'light sky blue'
                else:
                    color = 'white'
                
                self.gui_grid[row][column] = Entry(gui, width = 2, font = font, bg = color, cursor = 'arrow', borderwidth = 0,
                                                 highlightcolor = 'red', highlightthickness = 1, highlightbackground = 'black',
                                                 textvar = main_sudoku_grid[row][column])
                self.gui_grid[row][column].bind('<Motion>', self.ammend_grid)
                self.gui_grid[row][column].bind('<FocusIn>', self.ammend_grid)
                self.gui_grid[row][column].bind('<Button-1>', self.ammend_grid)
                self.gui_grid[row][column].grid(row=row, column=column)


        # menu dropdown for the commands in the top left corner. 
        menu = Menu(gui)
        gui.config(menu = menu)
       
        file = Menu(menu)
        menu.add_cascade(label = 'File', menu = file)
        file.add_command(label = 'Exit', command = gui.quit)
        file.add_command(label = 'Solve', command = self.solve_grid)
        file.add_command(label = 'Clear', command = self.clear_grid)


    # ammend the cells in the grid if values are incorrect. 
    def ammend_grid(self, event):
        for row in range(9):
            for column in range(9):
                if main_sudoku_grid[row][column].get() == '':
                    continue
                #if the number in the cell is a 2 digit number or is not in the choices of numbers from 1-9, then set the cell as empty. 
                if len(main_sudoku_grid[row][column].get()) > 1 or main_sudoku_grid[row][column].get() not in ['1','2','3','4','5','6','7','8','9']:
                    main_sudoku_grid[row][column].set('')


    # clear grid.
    def clear_grid(self):
        for row in range(9):
            for column in range(9):
                main_sudoku_grid[row][column].set('')


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
        for row in range(GRID_SIZE):
            for column in range(GRID_SIZE):
                    main_sudoku_grid[row][column].set(0)


    # Start the Algorithm
    def sudoku_solve(self, row=0, column=0):
        row, column = self.fill_next_cell(row, column)

        # If row == -1 the position is Ok or the Sudoku is Solved
        if row == -1:
            return True

        for e in range(GRID_SIZE):
            if self.is_valid_cell(row, column, e):
                main_sudoku_grid[row][column].set(e)
                if self.sudoku_solve(row, column):
                    return True
                # Undo the current cell for backtracking
                main_sudoku_grid[row][column].set(0)
        return False


    # Search the Nearest Cell to fill
    def fill_next_cell(self, i, j):
        for row in range(i, GRID_SIZE):
            for column in range(j, GRID_SIZE):
                if main_sudoku_grid[row][column].get() == '0':
                    return row,column

        return -1,-1


    # Check the Validity of main_sudoku_grid[i][j]
    def is_valid_cell(self, row, column, e):

        for x in range(9):
            if main_sudoku_grid[row][x].get() == str(e):
                return False

        for x in range(9):
            if main_sudoku_grid[x][column].get() == str(e):
                return False

        # Finding the Top x,y Co-ordinates of the section containing the i,j cell    
        secTopX, secTopY = 3 *int((row/3)), 3 *int((column/3))
        for row in range(secTopX, secTopX+3):
            for column in range(secTopY, secTopY+3):
                if main_sudoku_grid[row][column].get() == str(e):
                    return False
        
        return True

main_sudoku_grid = [
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
Label(root, text = "Press File in the top left corner for commands",font = ('Helvetica 9 bold')).place( x = 5, y = 290)
# Setting all the cells in the grid to be StringVar class so we can use .set() and .get() on each grid 
# to fill in values. 
for row in range(0,9):
    for column in range(0,9):
        main_sudoku_grid[row][column] = StringVar(root)

GRID_SIZE = 9

sudoku_application = MainWindow(root)
root.mainloop()



