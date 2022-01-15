import random
import sys
import pygame
import stddraw
import a2
import life2


def main():
    '''
    Run 50 generations of a random 2-dimensional Game of Life
    
    '''
    
    n = 50
    cells = life2.make_cells(n, n, True)
    for row in range(0, n):
        for col in range(0, n):
            if random.randint(0, 1) == 0:
                cells[row][col] = False
    a2.draw_cells(cells)
    for i in range(0, n):
        stddraw.show(500)
        life2.evolve(cells)
        a2.draw_cells(cells)
        
    pygame.display.quit()
    pygame.quit()
    sys.exit()



if __name__ == '__main__':  main()
