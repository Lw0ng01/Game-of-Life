import life2

c = life2.make_cells(5, 5, False)
c[0][0] = True
c[1][1] = True
c[2][2] = True
c[3][3] = True
c[4][4] = True

print('cells')
life2.print_cells(c)

print('neighborhood(c, 0, 0)')
n = life2.neighborhood(c, 0, 0)
life2.print_cells(n)

print('neighborhood(c, 0, 2)')
n = life2.neighborhood(c, 0, 2)
life2.print_cells(n)

print('neighborhood(c, 2, 2)')
n = life2.neighborhood(c, 2, 2)
life2.print_cells(n)

print('neighborhood(c, 3, 4)')
n = life2.neighborhood(c, 3, 4)
life2.print_cells(n)
