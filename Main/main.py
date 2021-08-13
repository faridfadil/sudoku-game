from tkinter import *
import random

# constant that stores the size of the grid. 
GRID_SIZE = 9
# creating the main tkinter window for the GUI application named root.
root = Tk()    

# main class to handle GUI. 
class MainWindow():
    
    # constructor of the MainWindow that takes in the root window, the width and the height of the window
    def __init__(self, gui, width, height):

        #constants for the status of sudoku grid- whether it is solved or not solved. Variables are here to improve readability. 
        self.SOLVED, self.NOT_SOLVED, self.INCORRECT = "Solved", "Not Solved", "Incorrect!"
        # setting the solution status of the grid (mainly used for player feedback on the GUI to say whether they got the correct solution or not)
        self.solution_status = StringVar(gui)
        # setting GUI title and settings.
        self.gui = gui
        gui.title("Sudoku Solver by Farid & Jerin")
        #setting gui dimensions
        self.width, self.height = width, height
        gui.geometry(f'{width}x{height}')  

        #setting font used in GUI
        font = ('Arial', 18)
        #setting background colour of GUI. 
        color = 'white'

        # creating label below the grid in the GUI for instructions for player controls. 
        Label(root, text = "Press File in the top left corner for commands",font = ('Helvetica 9 bold')).place( x = 5, y = 290)
        Label(root, textvariable = self.solution_status, fg='gray',font = ('Helvetica 9 bold')).place( x = self.width/4-20, y = self.height-30)

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

        # correct solution grid used to validate player inputted sulution. 
        self.correct_solution_grid = [
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

                if (row < 3 or row > 5) and (column < 3 or column > 5):
                    color = 'light sky blue'
                elif row in [3,4,5] and column in [3,4,5]:
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
        menu = Menu(self.gui)
        self.gui.config(menu = menu)
       
        file = Menu(menu)
        menu.add_cascade(label = 'File', menu = file)
        file.add_command(label = 'Exit', command = gui.quit)
        file.add_command(label = 'Check Solution', command = self.check_solution)
        file.add_command(label = 'New Grid', command = self.generate_new_grid)

        # generate new grid function
        self.generate_new_grid()     


    # ammend the cells in the grid if values are incorrect. 
    def ammend_grid(self, event):
        for row in range(GRID_SIZE):
            for column in range(GRID_SIZE):
                if main_sudoku_grid[row][column].get() == '':
                    continue
                #if the number in the cell is a 2 digit number or is not in the choices of numbers from 1-9, then set the cell as empty. 
                if len(main_sudoku_grid[row][column].get()) > 1 or main_sudoku_grid[row][column].get() not in ['1','2','3','4','5','6','7','8','9']:
                    main_sudoku_grid[row][column].set('')


    # clear grid. Set all cells to empty. 
    def clear_grid(self):
        for row in range(GRID_SIZE):
            for column in range(GRID_SIZE):
                main_sudoku_grid[row][column].set('')

    # generate a new grid
    def generate_new_grid(self):
        self.clear_grid()
        self.randomize_top_row()
        self.solve_grid()
        self.save_grid()
        self.hide_solution()
        self.solution_status.set(f"Game State: {self.NOT_SOLVED}")

    # Calls the class SolveSudoku
    def solve_grid(self):
        solution = SolveSudoku()  
    
    # randomize the top row so the solutions are random each time.
    def randomize_top_row(self):
        number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        number_choice = random.sample(number_list, len(number_list))

        for n in range(GRID_SIZE):
            main_sudoku_grid[0][n].set(number_choice[n])
    
    # replace slots that are chosen at random with empty cells. 
    def hide_solution(self):
        CHANCE_TO_HIDE = 85 # how frequent should the cells be made empty per loop iteration?
        for column in range(GRID_SIZE):
            for row in range(GRID_SIZE):
                #random number generator from 1 to 100
                random_roll = random.randint(0, 100)
                #if number rolled is less than given chance
                if random_roll < CHANCE_TO_HIDE:
                    # then set the current cell to be none
                    main_sudoku_grid[row][column].set('')

    # save the grid so that the check_solution() function can check if the player input when juxtaposed with the correct solution is valid.
    def save_grid(self):
        for row in range(GRID_SIZE):
            for column in range(GRID_SIZE):
                self.correct_solution_grid[row][column] = main_sudoku_grid[row][column].get()

    # boolean function that returns true if every player input in each cell matches exactly with the correct solution
    def is_correct_grid(self):
        for row in range(GRID_SIZE):
            for column in range(GRID_SIZE):
                if main_sudoku_grid[row][column].get() != self.correct_solution_grid[row][column]:
                    return False
        return True
    
    # checking the solution and changing the solution status.
    def check_solution(self):
        if self.is_correct_grid():
            self.solution_status.set(f"Game State: {self.SOLVED}")
        else:
            self.solution_status.set(f"Game State: {self.INCORRECT}")
            

    

# main class with sudoku solver backtracking 
class SolveSudoku():
    
    def __init__(self):
        self.set_all_zero()
        self.sudoku_solve()


    # set all the empty cells to zero
    def set_all_zero(self):
        for row in range(GRID_SIZE):
            for column in range(GRID_SIZE):
                if main_sudoku_grid[row][column].get() not in ['1','2','3','4','5','6','7','8','9']:
                    main_sudoku_grid[row][column].set(0)


    
    # MAIN BACKTRACKING ALGORITHM
    def sudoku_solve(self, i=0, j=0):
        i,j = self.fill_next_cell(i, j)

        # if i is -1, then the grid is solved, return true. 
        if i == -1:
            return True
        for e in range(1,10):
            if self.is_valid_cell(i,j,e):
                main_sudoku_grid[i][j].set(e)
                if self.sudoku_solve(i, j):
                    return True
                # set back to 0 for backtracking. 
                main_sudoku_grid[i][j].set(0)
        return False


    # find the nearest cell to fill
    def fill_next_cell(self, i, j):
        for row in range(i, GRID_SIZE):
            for column in range(j, GRID_SIZE):
                if main_sudoku_grid[row][column].get() == '0':
                    return row,column

        for row in range(0, GRID_SIZE):
            for column in range(0, GRID_SIZE):
                if main_sudoku_grid[row][column].get() == '0':
                    return row,column

        return -1,-1


    # checking if main_sudoku_grid[row][column] is valid. 
    def is_valid_cell(self, row, column, e):
        # checking every row
        for x in range(GRID_SIZE):
            if main_sudoku_grid[row][x].get() == str(e):
                return False
        #checking every column
        for x in range(GRID_SIZE):
            if main_sudoku_grid[x][column].get() == str(e):
                return False

        # checking the individual 3x3 boxes in the grid.   
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

# Setting all the cells in the grid to be StringVar class so we can use .set() and .get() on each grid to fill in values on the GUI.
for row in range(GRID_SIZE):
    for column in range(GRID_SIZE):
        main_sudoku_grid[row][column] = StringVar(root)

# passing the main root window into the MainWindow class for actual GUI construction. 
sudoku_application = MainWindow(root, 270, 340)

# running tkinter mainloop to display GUI
root.mainloop()



