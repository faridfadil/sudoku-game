from tkinter import *
import random

# main class to handle GUI. 
class MainWindow():
    
    def __init__(self, gui):
        # setting GUI title and settings.
        self.gui = gui
        gui.title("Sudoku Solver by Farid & Jerin")
        gui.geometry('270x320')  
        #setting font used in GUI
        font = ('Arial', 18)
        #setting background colour of GUI. 
        color = 'white'

        # the 9x9 grid that will be displayed on the GUI. This grid is different from main_sudoku_grid as it is the front-end component. 
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

        #setting the colours of the GUI grid.
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


        # menu dropdown for player controls in the top left corner. 
        menu = Menu(gui)
        gui.config(menu = menu)
       
        file = Menu(menu)
        menu.add_cascade(label = 'File', menu = file)
        file.add_command(label = 'Exit', command = gui.quit)
        file.add_command(label = 'Solve', command = self.solve_grid)
        file.add_command(label = 'Clear', command = self.clear_grid)

        #NOTE ammend this function so that VALID numbers are placed on the grid. 
        self.fill_grid(chance_to_place = 20)


    # ammend the cells in the grid if values are incorrect. 
    def ammend_grid(self, event):
        for row in range(GRID_SIZE):
            for column in range(GRID_SIZE):
                if main_sudoku_grid[row][column].get() == '':
                    continue
                #if the number in the cell is a 2 digit number or is not in the choices of numbers from 1-9, then set the cell as empty. 
                if len(main_sudoku_grid[row][column].get()) > 1 or main_sudoku_grid[row][column].get() not in ['1','2','3','4','5','6','7','8','9']:
                    main_sudoku_grid[row][column].set('')


    # clear grid.
    def clear_grid(self):
        for row in range(GRID_SIZE):
            for column in range(GRID_SIZE):
                main_sudoku_grid[row][column].set('')


    # Calls the class SolveSudoku
    def solve_grid(self):
        solution = SolveSudoku()  
    
    def fill_grid(self, chance_to_place = 0):
        number_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        #nested for loop for the 9x9 grid.
        for column in range(GRID_SIZE):
            for row in range(GRID_SIZE):
                #random number generator from 1 to 100
                random_roll = random.randint(0, 100)
                #if number rolled is less than given chance
                if random_roll < chance_to_place:
                    # then place a number randomly chosen from the number_choices.
                    main_sudoku_grid[row][column].set(random.choice(number_choices))
                else:
                    # otherwise, then put it in 0
                    main_sudoku_grid[row][column].set(0)

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

# our main 9x9 sudoku grid
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

# constant that stores the size of the grid. 
GRID_SIZE = 9

# creating the main tkinter window for the GUI application.
root = Tk()

# creating label below the grid in the GUI for instructions for player controls. 
Label(root, text = "Press File in the top left corner for commands",font = ('Helvetica 9 bold')).place( x = 5, y = 290)

# Setting all the cells in the grid to be StringVar class so we can use .set() and .get() on each grid to fill in values.
for row in range(GRID_SIZE):
    for column in range(GRID_SIZE):
        main_sudoku_grid[row][column] = StringVar(root)

# passing the main root window into the MainWindow class for actual GUI construction. 
sudoku_application = MainWindow(root)

# running tkinter mainloop to display GUI
root.mainloop()



