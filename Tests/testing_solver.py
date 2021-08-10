# Python file for testing code. 
# NOTE: The contents of this file does not follow convention and is only for prototyping certain code structures/algorithms. 

#nested for loop
# for x in range(1, 10):
#     for y in range(1, 10):
#         print(f"column (x): {x}, row (y): {y}")


grid = [
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

max_loop_n = 30000
loop_range = range(1, max_loop_n)

chance = 70
hit_count, no_hit_count = 0, 0

import random

print("Processing...")
for x in loop_range:
    random_roll = random.randint(0, 100)
    if random_roll >= chance:
        # print(f"hit! {random_roll}")
        hit_count += 1
    else: 
        # print(f"no hit! {random_roll}")
        no_hit_count += 1

print(f"Hit percentage = %{(hit_count/max_loop_n)*100}")
print(f"No-Hit percentage = %{(no_hit_count/max_loop_n)*100}")

# for column in loop_range:
#     for row in loop_range:
        





