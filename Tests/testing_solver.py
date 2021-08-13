# Python file for testing code. 
# NOTE: The contents of this file does not follow convention and is only for prototyping certain code structures/algorithms. 

#nested for loop
# for x in range(1, 10):
#     for y i range(1, 10):
#         print(f"column (x): {x}, row (y): {y}")n
import random


def chance_test(change_chance):
    
    max_loop_n = 50000
    loop_range = range(1, max_loop_n)

    chance = change_chance
    hit_count, no_hit_count = 0, 0

    print("Processing...")
    for x in loop_range:
        random_roll = random.randint(0, 100)
        if random_roll <= chance:
            # print(f"hit! {random_roll}")
            hit_count += 1
        else: 
            # print(f"no hit! {random_roll}")
            no_hit_count += 1

    print(f"Hit percentage = %{(hit_count/max_loop_n)*100}")
    print(f"No-Hit percentage = %{(no_hit_count/max_loop_n)*100}")


def choice_sequence_test():
    sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(random.choice(sequence))

#sample sudoku grid
sudoku_grid = [
        [0, 1, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

#chance to place a number, higher the value, the easier it is for the sudoku to be solved
chance = 100
#choices of numbers 

#constant variable of grid size
GRID_SIZE = 9

def fill_grid(grid, chance_to_place):
    number_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #nested for loop for the 9x9 grid.
    for column in range(GRID_SIZE):
        for row in range(GRID_SIZE):
            #random number generator from 1 to 100
            random_roll = random.randint(0, 100)
            #if number rolled is less than given chance
            if random_roll < chance_to_place:
                # then place a number randomly chosen from the number_choices.
                grid[row][column] = random.choice(number_choices)
            else:
                # otherwise, then put it in 0
                grid[row][column] = 0
    return grid

def is_valid(grid, row, column):
    for n in range(GRID_SIZE):
        if grid[row][n] in number_choices or grid[n][column] in number_choices:
            return False

    return True
    
#testing random shuffle function to shuffle first row of sudoku grid
def random_shuffle():
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    number_choice = random.sample(number_list, len(number_list))
    return number_choice

#printing the result of the random_shuffle function
for x in range(10):
    print(random_shuffle())

            

        



