'''
This module provides a function for drawing cells in a
1- or 2-dimensional Game of Life.

The function draw_cells is meant to be used in conjunction
with the textbook module stddraw. The caller should call

stddraw.show()

after calling draw_cells; however, this causes the program
to enter the Pygame event loop. See the example programs:

glider_life2.py
gosper_gun2.py
random_life2.py

to see how to close the Pygame window.
'''
import stddraw

def draw_cells(cells):
    '''
    Draw the cells of a 1- or 2-dimensional Game of Life.

    Alive cells are drawn in red and dead cells are drawn in
    white.

    For a 1-dimensional Game of Life the cells are drawn
    as a single row centered in the image window.

    For a 2-dimensional Game of Life the cells occupy the
    entire canvas of the window.

    This function does nothing if `cells` is empty.

    Parameters
    ----------
    cells : list of bool or list-of-list of bool
        The cells in a Game of Life.
    '''

    if not cells:
        return
    n = len(cells)
    if type(cells[0]) is bool:
        stddraw.setXscale(0, n)
        stddraw.setYscale(-n / 2, n / 2)
        stddraw.clear(stddraw.WHITE)
        stddraw.setPenColor(stddraw.RED)
        for col in range(0, n):
            if cells[col]:
                stddraw.filledSquare(col + 0.5, 0, 0.5)
    else:
        stddraw.setXscale(0, n)
        stddraw.setYscale(0, n)
        stddraw.clear(stddraw.WHITE)
        stddraw.setPenColor(stddraw.RED)
        for row in range(0, n):
            for col in range(0, n):
                if cells[row][col]:
                    stddraw.filledSquare(col + 0.5, n - row - 0.5, 0.5)
