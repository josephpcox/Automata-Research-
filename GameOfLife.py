
import pygame
import numpy as np
from time import sleep

# This sets the number of cells 
N = 150
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 30
HEIGHT = 30
#WIDTH = 7
#HEIGHT = 7
# This sets the margin between each cell
MARGIN = 4
 

def updateGrid(grid,N):
    newGrid =grid.copy()
    for i in range(N): 
        for j in range(N): 
  
            # compute 8-neghbor sum 
            # using boundary conditions - x and y wrap around  
            total =  (grid[i][(j-1)%N]+ grid[i][(j+1)%N] + 
                         grid[(i-1)%N] [j] + grid[(i+1)%N][j] + 
                         grid[(i-1)%N] [(j-1)%N] + grid[(i-1)%N] [(j+1)%N] + 
                         grid[(i+1)%N] [(j-1)%N]+ grid[(i+1)%N][(j+1)%N])
  
            # apply Conway's rules 
            if grid[i] [j]  == 1: 
                if (total < 2) or (total > 3): 
                    newGrid[i] [j] = 0 
            else: 
                if total == 3: 
                    newGrid[i] [j] = 1

    return newGrid 
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = np.random.randint(2, size=(N, N))
 
# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [N*6, N*6]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("The Game of Life")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the grid
    for row in range(N):
        for column in range(N):
            color = WHITE
            if grid[row][column] == 1:
                color = BLACK
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
 
    # Limit to 60 frames per second
    clock.tick(30)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    grid = updateGrid(grid,N)
    print(grid)
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
