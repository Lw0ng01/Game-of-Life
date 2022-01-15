import life1

c = life1.make_cells(7, False)
c[3] = True
c[5] = True
print('cells')
life1.print_cells(c)

print('neighborhood(c, 0)')
n = life1.neighborhood(c, 0)
life1.print_cells(n)

print('neighborhood(c, 1)')
n = life1.neighborhood(c, 1)
life1.print_cells(n)

print('neighborhood(c, 3)')
n = life1.neighborhood(c, 3)
life1.print_cells(n)

print('neighborhood(c, 6)')
n = life1.neighborhood(c, 6)
life1.print_cells(n)
