import matplotlib.pyplot as form
from matplotlib.colors import ListedColormap
from matplotlib.patches import Rectangle
import numpy as np

from EightQueensProblem import EightQueensProblem
from CSP_Solver import CSP_Solver

solver = CSP_Solver()

eight_queens_problem = EightQueensProblem()
solver.train(eight_queens_problem)
eight_queens_result = solver.solve()
print(eight_queens_result)

chessboard = np.zeros((8,8))
chessboard[1::2,0::2] = 1
chessboard[0::2,1::2] = 1


cmap = ListedColormap(['white', '#ADD8E6'])
form.axis('off')
form.imshow(chessboard, cmap=cmap)

for i in range(8):
    for j in range(8):
        color = cmap(chessboard[i][j])
        rect = Rectangle((j - 0.5, i - 0.5), 1, 1, linewidth=1, edgecolor='black', facecolor=color)
        form.gca().add_patch(rect)

for y, x in eight_queens_result.items():
    form.text(y-1, x-1, '♚', fontsize=35,
             horizontalalignment='center',
             verticalalignment='center')

form.show()