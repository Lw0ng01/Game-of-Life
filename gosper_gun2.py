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

    s = '''........................O
......................O.O
............OO......OO............OO
...........O...O....OO............OO
OO........O.....O...OO
OO........O...O.OO....O.O
..........O.....O.......O
...........O...O
............OO'''
    t = s.split()

    c = life2.make_cells(50, 50, False)
    row = 3
    for cell_row in t:
        col = 3
        for cell in cell_row:
            if cell == 'O':
               c[row][col] = True
            col += 1
        row += 1

    for i in range(0, 1000):
        stddraw.show(10)
        life2.evolve(c)
        a2.draw_cells(c)
        
    pygame.display.quit()
    pygame.quit()
    sys.exit()



if __name__ == '__main__':  main()
