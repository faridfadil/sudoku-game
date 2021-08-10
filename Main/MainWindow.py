
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
                    color = 'gray'
                elif i in [3,4,5] and j in [3,4,5]:
                    color = 'gray'
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