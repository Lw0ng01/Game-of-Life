import life2

c = life2.make_cells(5, 5, False)
c[0][0] = True
c[1][1] = True
c[1][2] = True
c[2][2] = True
c[3][3] = True
c[4][4] = True

print('cells')
life2.print_cells(c)

life2.evolve(c)
print('evolve')
life2.print_cells(c)

