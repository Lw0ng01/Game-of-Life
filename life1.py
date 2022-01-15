'''
This module provides functions for the 1-dimensional Game of Life.

The 1-dimensional Game of Life occurs on a list of cells where each
cell is either alive or dead. The population of cells evolves from
one generation to the next according to three rules:

1. Any live cell survives into the next generation if it has 2 or 4
living neighbours in its 2-neighborhood.
2. Any dead cell becomes alive in the next generation if it has 2 or 3
living neighbours in its 2-neighborhood.
3. All other live cells die and all other dead cells remain dead.

The rules are applied to each cell simultaneously to compute the
next generation of cells.

The 2-neighborhood of a cell consists of the cell itself and its
two neighbors to the left and two neighbors to the right of the cell
(if those neighbors exist).
'''


def make_cells(n, val):
    """
    Return a list filled with a specified value.

    Parameters
    ----------
    n : int
        The number of elements in the returned list.
    val : bool
        The element to appear repeatedly in the returned list.

    Returns
    -------
    list
        A list of `n` copies of `val`

    Raises
    ------
    ValueError
        If `n` is less than zero.
    """

    if n < 0:
        raise ValueError('make_cells() number of elements less than zero, n = ' + str(n))
    a = [val] * n
    return a


def print_cells(cells):
    """
    Prints a list of cells

    Parameters
    ----------
    cells : list
        The list containing the values True or False
    """

    for c in cells:
        if c:
            print("#", end="")  # end="" means it doesn't go to the next line
        else:
            print("-", end="")
    print()


def neighborhood(cells, index):
    """
    Returns a list containing cells

    Parameters
    ----------
    cells : list
        The list containing cells[index]
    index : int
        The element in the list containing values

    Returns
    -------
    list
        A list of cells that includes the left most and right most elements of a neighbourhood

    Raises
    ------
    ValueError
        If index is less than 0
    """

    if index < 0:
        raise ValueError("Index is less than 0")

    left_index = index - 2  # defining left and right index
    if left_index < 0:  # if left_index goes negative, set it to 0
        left_index = 0
    right_index = index + 3
    if right_index > len(cells):  # if right_index becomes bigger than size of list, set it to same size as list
        right_index = len(cells)

    left_index = max(0, index - 2)
    right_index = min(len(cells), index + 3)

    return cells[left_index: right_index]  # 3 because slice does not include last element


def evolve(cells):
    """
    Applies rules to 'evolve' each cell to the next generation

    Parameters
    ----------
    cells : list
        The list containing the cells value

    Raises
    ------
    ValueError
        If cells is empty
    """

    if not cells:
        raise ValueError("Cells is empty")
    cells_copy = cells[:]  # copying cells into a new list

    for i in range(len(cells)):
        n = neighborhood(cells, i)
        if cells[i]:
            if sum(n) > 2:
                cells_copy[i] = True
            else:
                cells_copy[i] = False
        else:
            if sum(n) > 1:
                cells_copy[i] = True
            else:
                cells_copy[i] = False

    cells[:] = cells_copy  # copying cells into a new list


def blinker(cells, index):
    """
    Inserts a blinker pattern into the list cells

    Parameters
    ----------
    cells : list
        The list containing the values True or False for the neighbourhood
    index : int
        The element value contained in the list cells

    Raises
    ------
    ValueError
        If index is less than 0 or the length of cells is less than index + 5
    """

    if index < 0 or len(cells) < index + 5:
        raise ValueError("Index is less than - or the length of cells is less than index + 5")
    else:  # starts blinker pattern wherever the cells start
        cells[index] = False  # setting each value to False for blinker pattern for 1 through 5
        cells[index + 1] = False
        cells[index + 2] = True
        cells[index + 3] = True
        cells[index + 4] = False
        cells[index + 5] = False




