'''
This module provides functions for the 2-dimensional Game of Life.

The 2-dimensional Game of Life occurs on an n-by-n array of
cells where each cell is either alive or dead. The population of cells
evolves from one generation to the next according to three rules:

1. Any live cell survives into the next generation if it has 2 or 3
living neighbours in its 1-neighborhood (the cell itself does not
count towards the number of living neighbors).
2. Any dead cell becomes alive in the next generation if it has 3
living neighbours in its 1-neighborhood.
3. All other live cells die, and all other dead cells remain dead.

The rules are applied to each cell simultaneously to compute the
next generation of cells.

The 1-neighborhood of a cell consists of the cell itself and its
eight neighbours, which are the cells that are horizontally, vertically,
or diagonally adjacent (if those neighbors exist).
'''

import math
import sys


def test_indexes(cells, row, col, func_name):
    """
    Test if row and column indexes are valid for a square array.

    This function tests if `row` and `col` are both in the
    range 0 to (n - 1), inclusive, where n is equal to
    len(cells). Raises a ValueError if an index is out of
    range.

    Parameters
    ----------
    cells : list-of-list of bool
        The n-by-n cells of a 2D Game of Life.
    row : int
        A row index for cells.
    col : int
        A column index for cells.
    func_name : str
        The name of the function that called test_indexes

    Raises
    ------
    ValueError
        If `row` or `col` is out of range.
    """

    n = len(cells)
    if row < 0:
        raise ValueError(func_name, 'number of rows < 0, row = ', row)
    elif row >= n:
        raise ValueError(func_name, 'number of rows >= len(cells), row = ', row)
    if col < 0:
        raise ValueError(func_name, 'number of cols less than zero, col = ', col)
    elif col >= n:
        raise ValueError(func_name, 'number of cols >= len(cells), col = ', col)


def make_cells(rows, cols, val):
    """
    Return an array filled with a specified value.

    Parameters
    ----------
    rows : int
        The number of rows in the array.
    cols : int
        The number of columns in the array.
    val : bool
        The element to appear repeatedly in the returned list.

    Returns
    -------
    list
        A list-of-lists of `rows`-by-`cols` copies of `val`

    Raises
    ------
    ValueError
        If `rows` or `cols` is less than zero.
    """

    if rows < 0:
        raise ValueError('make_cells() size less than zero, rows = ', rows)
    if cols < 0:
        raise ValueError('make_cells() size less than zero, cols = ', cols)
    a = []
    for i in range(0, rows):
        row = [val] * cols
        a.append(row)
    return a


def print_cells(cells):
    """
    Prints a list-of-lists cells where the elements equal either True of False

    Parameters
    ----------
    cells : list
        The list of index containing either values True or False
    """
    for i in range(len(cells)):
        for j in range(len(cells[i])):
            if cells[i][j]:
                print("#", end="")  # end="" means it doesn't go to the next line
            else:
                print("-", end="")
        print()


def neighborhood(cells, row, col):
    """
    Returns a list-of-lists containing cells for cells[row][col]

    Parameters
    ----------
    cells : list
        The list containing values for row and col
    row : int
        The number of rows in the list
    col : int
        The number of columns in the list

    Returns
    -------
    list
        A list-of-lists for the neighbourhood for cells[row][col]

    Raises
    ------
    ValueError
        If row is less than 0 or col is less than 0
    """
    if row < 0 or col < 0:
        raise ValueError("Row or col value are less than 0")

    n_list = []
    r_list = []
    row_top_index = 0
    row_bot_index = 0
    col_left_index = 0
    col_right_index = 0

    row_top_index = max(0, row - 1)  # look to left of col if not 0
    col_left_index = max(0, col - 1)  # must look at previous row if not 0
    row_bot_index = min(len(cells) - 1, row + 1)
    col_right_index = min(len(cells[0]) - 1, col + 1)

    for i in range(row_top_index, row_bot_index + 1):
        r_list = cells[i][col_left_index: col_right_index + 1]
        n_list.append(r_list)
    return n_list


def evolve(cells):
    """
       Applies rules to 'evolve' cells to the next generation and replaces each current cell with a new one

       Parameters
       ----------
       cells : list
           The list containing values for row and col

       Raises
       ------
       ValueError
           If cells is empty
       """

    if not cells:
        raise ValueError("If cells is empty")

    cells_copy = [element[:] for element in cells]  # copying cells into a new list
    alive_count = 0
    n = []

    for i in range(len(cells)):

        for j in range(len(cells[i])):

            n = neighborhood(cells, i, j)
            alive_count = -cells[i][j]  # offsetting the count so it doesn't count itself

            for k in range(len(n)):
                alive_count += sum(n[k])
            if alive_count >= 3:  # becomes alive if 3 neighbours
                cells_copy[i][j] = True
            elif alive_count < 2:
                cells_copy[i][j] = False

    cells[:] = cells_copy


def glider(cells, top_row, left_col):
    """
       Applies a glider pattern to cells

       Parameters
       ----------
       cells : list
           The list containing values for row and col
       top_row : int
           Length of the top_row index
       left_col : int
           Length of hte left_col index

       Raises
       ------
       Exception
           If pattern does not fit into grid
       """

    if top_row + 5 > len(cells) or left_col + 5 > len(cells[0]):
        raise Exception("Glider pattern does not fit in the length of cells")

    cells[top_row: top_row + 6][left_col: left_col + 6] = 25 * [False]  # setting all cells to False
    cells[top_row + 1][left_col + 1] = True  # individually setting each True cell in glider pattern
    cells[top_row + 2][left_col + 2] = True
    cells[top_row + 2][left_col + 3] = True
    cells[top_row + 3][left_col + 1] = True
    cells[top_row + 3][left_col + 2] = True
