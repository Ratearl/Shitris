import pygame
import sys
import random
from copy import deepcopy

frame_width = 500
frame_height = 1000
block_size = 50
idk = 0
fall = 0
lr = 0
score = 0

pygame.init()
pygame.display.set_caption("Shitris")

game_display = pygame.display.set_mode((frame_width, frame_height))
clock = pygame.time.Clock()

shapes = [
    [
        [
            [3 * block_size, -2 * block_size],
            [4 * block_size, -2 * block_size],  # Line
            [5 * block_size, -2 * block_size],
            [6 * block_size, -2 * block_size]
        ],
        [
            [4 * block_size, -1 * block_size],
            [4 * block_size, -2 * block_size],  # Line
            [4 * block_size, -3 * block_size],
            [4 * block_size, -4 * block_size]
        ],
        [
            [3 * block_size, -3 * block_size],
            [4 * block_size, -3 * block_size],  # Line
            [5 * block_size, -3 * block_size],
            [6 * block_size, -3 * block_size]
        ],
        [
            [5 * block_size, -1 * block_size],
            [5 * block_size, -2 * block_size],  # Line
            [5 * block_size, -3 * block_size],
            [5 * block_size, -4 * block_size]
        ],
    ],
    [
        [
            [4 * block_size, -3 * block_size],
            [4 * block_size, -2 * block_size],  # L
            [4 * block_size, -1 * block_size],
            [5 * block_size, -1 * block_size]
        ],
        [
            [3 * block_size, -2 * block_size],
            [4 * block_size, -2 * block_size],  # L
            [5 * block_size, -2 * block_size],
            [3 * block_size, -1 * block_size]
        ],
        [
            [5 * block_size, -3 * block_size],
            [5 * block_size, -2 * block_size],  # L
            [5 * block_size, -1 * block_size],
            [4 * block_size, -3 * block_size]
        ],
        [
            [3 * block_size, -1 * block_size],
            [4 * block_size, -1 * block_size],  # L
            [5 * block_size, -1 * block_size],
            [5 * block_size, -2 * block_size]
        ],
    ],
    [
        [
            [4 * block_size, -3 * block_size],
            [4 * block_size, -2 * block_size],  # S
            [5 * block_size, -2 * block_size],
            [5 * block_size, -1 * block_size]
        ],
        [
            [5 * block_size, -2 * block_size],
            [4 * block_size, -2 * block_size],  # S
            [4 * block_size, -1 * block_size],
            [3 * block_size, -1 * block_size]
        ],
        [
            [4 * block_size, -1 * block_size],
            [4 * block_size, -2 * block_size],  # S
            [5 * block_size, -2 * block_size],
            [5 * block_size, -3 * block_size]
        ],
        [
            [3 * block_size, -2 * block_size],
            [4 * block_size, -2 * block_size],  # S
            [4 * block_size, -1 * block_size],
            [5 * block_size, -1 * block_size]
        ],
    ],
    [
        [
            [4 * block_size, -3 * block_size],
            [4 * block_size, -2 * block_size],  # T
            [4 * block_size, -1 * block_size],
            [5 * block_size, -2 * block_size]
        ],
        [
            [3 * block_size, -2 * block_size],
            [4 * block_size, -2 * block_size],  # T
            [5 * block_size, -2 * block_size],
            [4 * block_size, -1 * block_size]
        ],
        [
            [5 * block_size, -3 * block_size],
            [5 * block_size, -2 * block_size],  # T
            [5 * block_size, -1 * block_size],
            [4 * block_size, -2 * block_size]
        ],
        [
            [3 * block_size, -1 * block_size],
            [4 * block_size, -1 * block_size],  # T
            [5 * block_size, -1 * block_size],
            [4 * block_size, -2 * block_size]
        ],
    ],
    [
        [
            [4 * block_size, -1 * block_size],
            [4 * block_size, -2 * block_size],  # Sq
            [5 * block_size, -1 * block_size],
            [5 * block_size, -2 * block_size]
        ],
    ]
]

colors = [
    pygame.Color(3, 65, 174),
    pygame.Color(114, 203, 59),
    pygame.Color(255, 213, 0),
    pygame.Color(255, 151, 28),
    pygame.Color(255, 50, 19)
]

field_squares = []
field_colors = {}

rand_shape_index = random.randint(0, len(shapes) - 1)  # Random Shopon Picker
curr_shape_index = random.randint(0, len(shapes[rand_shape_index]) - 1)  # Random Orientation
curr_shape = deepcopy(shapes[rand_shape_index][curr_shape_index])  # Instance of Random Shape & Orientation


# Check if there a two siamese shitris tiles
def in_field_squares(field_squares, sq):
    for fs in field_squares:
        if fs[0] == sq:
            return True
    return False

# Generate a newborn shitris shape
def new_shape(shape, rsi):
    for sq in shape:
        field_squares.append([sq, rsi])
    fall = 0
    lr = 0
    rand_shape_index = random.randint(0, len(shapes) - 1)
    curr_shape_index = random.randint(0, len(shapes[rand_shape_index]) - 1)
    curr_shape = deepcopy(shapes[rand_shape_index][curr_shape_index])
    return rand_shape_index, curr_shape_index, curr_shape, fall, lr

while True:
    q = 0

    game_display.fill(pygame.Color(0, 0, 0))

    for sq in curr_shape:
        if not in_field_squares(field_squares, [sq[0], sq[1] + block_size]) and sq[1] + block_size != frame_height:
            q += 1

    # Check stuff idk
    if q == 4:
        for sq in curr_shape:
            sq[0] += idk
            sq[1] += block_size
        fall += block_size
        lr += idk
    else:
        rand_shape_index, curr_shape_index, curr_shape, fall, lr = new_shape(curr_shape, rand_shape_index)

    # Draw Shitris shape
    for sq in curr_shape:
        pygame.draw.rect(game_display, colors[rand_shape_index], pygame.Rect(sq[0], sq[1], block_size, block_size))

    # Draw placed shitris tiles
    for sh in field_squares:
        pygame.draw.rect(game_display, colors[sh[1]], pygame.Rect(sh[0][0], sh[0][1], block_size, block_size))

    # Draw cage line 1
    for i in range(frame_height // block_size):
        pygame.draw.line(game_display, pygame.Color(20, 20, 20), (0, i * block_size), (frame_width, i * block_size), 1)

    # Draw cage line 2
    for j in range(frame_width // block_size):
        pygame.draw.line(game_display, pygame.Color(20, 20, 20), (j * block_size, 0), (j * block_size, frame_height), 1)

    pygame.display.update()
    clock.tick(6)