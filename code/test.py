import numpy as np
import pandas as pd


box_width = 100  # Example dimension
box_height = 50  # Example dimension
large_square_size = 10  # Size of the large square
small_square_size = 5   # Size of the small square

squares = []

def add_square(x1, y1, x2, y2, size):
    squares.append({
        'x1': x1,
        'y1': y1,
        'x2': x2,
        'y2': y2,
        'size': size
    })

for x in range(0, box_width, large_square_size):
    for y in range(0, box_height, large_square_size):
        x2 = min(x + large_square_size, box_width)
        y2 = min(y + large_square_size, box_height)
        add_square(x, y, x2, y2, large_square_size)

for x in range(0, box_width, large_square_size):
    for y in range(0, box_height, large_square_size):
        if y + large_square_size < box_height:
            continue
        overflow_y_start = box_height - (box_height % large_square_size)
        for small_x in range(x, x + large_square_size, small_square_size):
            for small_y in range(overflow_y_start, box_height, small_square_size):
                small_x2 = min(small_x + small_square_size, box_width)
                small_y2 = min(small_y + small_square_size, box_height)
                add_square(small_x, small_y, small_x2, small_y2, small_square_size)

for y in range(0, box_height, large_square_size):
    for x in range(0, box_width, large_square_size):
        if x + large_square_size < box_width:
            continue
        overflow_x_start = box_width - (box_width % large_square_size)
        for small_x in range(overflow_x_start, box_width, small_square_size):
            for small_y in range(y, y + large_square_size, small_square_size):
                small_x2 = min(small_x + small_square_size, box_width)
                small_y2 = min(small_y + small_square_size, box_height)
                add_square(small_x, small_y, small_x2, small_y2, small_square_size)

squares_df = pd.DataFrame(squares)

squares_df.to_csv('FilledBoxSquares.csv', index=False)

print("Box filling complete. Squares details saved to 'FilledBoxSquares.csv'.")
