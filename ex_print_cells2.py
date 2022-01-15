import life2

c = life2.make_cells(3, 4, False)
c[0][0] = True
c[1][1] = True
c[2][2] = True
life2.print_cells(c)
