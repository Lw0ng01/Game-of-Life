import life2

c = life2.make_cells(7, 7, False)
life2.glider(c, 0, 0)
print('cells')
life2.print_cells(c)

life2.evolve(c)
print('evolve')
life2.print_cells(c)

