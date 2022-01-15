import life1

c = life1.make_cells(7, False)
c[3] = True
c[5] = True
c[6] = True
print('cells')
life1.print_cells(c)
life1.evolve(c)
print('evolve')
life1.print_cells(c)

