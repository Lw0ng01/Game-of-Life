import life1


cells = life1.make_cells(50, False)
s = '---##--##---####------####------#---#-#---#-#-#--#'
i = 0
for c in s:
    if c == '#':
        cells[i] = True
    i += 1

life1.print_cells(cells)
for i in range(0, 30):
    life1.evolve(cells)
    life1.print_cells(cells)
    
