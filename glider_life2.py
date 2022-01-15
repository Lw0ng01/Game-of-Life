import sys
import pygame
import stddraw
import a2
import life2


def main():
    '''
    Draw 50 generations of a glider in a 2-dimensional Game of Life.
    
    '''

    n = 20
    cells = life2.make_cells(n, n, False)
    life2.glider(cells, 3, 3)
    
    a2.draw_cells(cells)
    for i in range(0, 50):
        stddraw.show(200)
        life2.evolve(cells)
        a2.draw_cells(cells)

    pygame.display.quit()
    pygame.quit()
    sys.exit()


if __name__ == '__main__':  main()
