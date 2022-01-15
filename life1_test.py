import life1
import pytest

cells = life1.make_cells(5, False)
print(cells)
life1.print_cells(cells)
cells[2] = True  # making middle cell true to test
life1.print_cells(cells)

neighborhood = life1.neighborhood(cells, 2)
print(neighborhood)
life1.print_cells(neighborhood)

"""
# testing pytest
def test_neighborhood_middle():
    cells = life1.make_cells(5, False)
    index = 2  # middle of cells
    n = life1.neighborhood(cells, index)

    expected_answer = [False, False, False, False, False]

    assert n == expected_answer  # assert (in python), confirms if value is true or false


def test_neighborhood_left():
    cells = life1.make_cells(5, False)
    index = 0  # first of cells
    n = life1.neighborhood(cells, index)

    expected_answer = [False, False, False]  # only first cell + 2 cells to the right

    assert n == expected_answer  # assert (in python), confirms if value is true or false


def test_neighborhood_right():
    cells = life1.make_cells(5, False)
    index = len(cells) - 1  # match length of cells, but -1 if it goes over
    n = life1.neighborhood(cells, index)

    expected_answer = [False, False, False]  # only first cell + 2 cells to the left
    assert n == expected_answer  # assert (in python), confirms if value is true or false
"""


def test_evolve():
    c = life1.make_cells(7, False)
    c[3] = True
    c[5] = True
    c[6] = True
    print('cells')
    life1.print_cells(c)
    life1.evolve(c)
    print('evolve')
    life1.print_cells(c)


# this is ex_blinker.py
c = life1.make_cells(12, False)
print('cells')
life1.print_cells(c)

life1.blinker(c, 3)
print('cells with blinker')
life1.print_cells(c)

for i in range(0, 10):
    life1.print_cells(c)
    life1.evolve(c)
