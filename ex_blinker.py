import life1

c = life1.make_cells(12, False)
print('cells')
life1.print_cells(c)

life1.blinker(c, 3)
print('cells with blinker')
life1.print_cells(c)

for i in range(0, 10):
    life1.print_cells(c)
    life1.evolve(c)
