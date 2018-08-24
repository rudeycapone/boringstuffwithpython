#Chapter 4 final excercise number 2
#Reversing and then printing a grid

grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]

#Variable declaration
ySize = len(grid)
xSize = len(grid[0])

#With a nested for loop
#with a nested loop
for item in range(0, xSize):
    if item != 0:
        print('')
    for item2 in range(0, ySize):
        print(grid[item2][item], end='')

#While loop1
# while counter <= ySize - 1:
#     if x >= xSize:
#         exit()
#     print(grid[y][x], end='')
#     y += 1
#     counter += 1
#     if counter > ySize - 1:
#         print('')
#         x += 1
#         y = 0
#         counter = 0