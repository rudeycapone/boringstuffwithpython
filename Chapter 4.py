# Working with lists
import copy

spam = ['A', 'B', 'C', 'D', [1, 2, 3, 4]]
cheese = copy.copy(spam)
cheese[1] = 42
print(spam)
print(cheese)
print(cheese[4][2])