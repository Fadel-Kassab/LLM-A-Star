import numpy as np
import random
import matplotlib.pyplot as plt

def generate_8d_maze(rows: int, cols: int) -> np.ndarray:
    # Predefined moves for 8-directional carving (dr, dc)
    DIRECTIONS = [(-2, 0), (2, 0), (0, -2), (0, 2),
                (-2, -2), (-2, 2), (2, -2), (2, 2)]

    # enforce minimum odd dimensions for full connectivity
    rows = max(3, rows | 1)
    cols = max(3, cols | 1)

    maze = np.ones((rows, cols), dtype=int)
    start = (1, 1)
    maze[start] = 0
    stack = [start]

    while stack:
        r, c = stack[-1]
        # shuffle neighbor order for randomness
        neighbors = [(r + dr, c + dc) for dr, dc in DIRECTIONS]
        random.shuffle(neighbors)
        for nr, nc in neighbors:
            if 1 <= nr < rows - 1 and 1 <= nc < cols - 1 and maze[nr, nc] == 1:
                # carve path between cells
                maze[(r + nr) // 2, (c + nc) // 2] = 0
                maze[nr, nc] = 0
                stack.append((nr, nc))
                break
        else:
            stack.pop()  # backtrack when no unvisited neighbor

    return maze

def show_grid(grid: np.ndarray):
    plt.imshow(grid, cmap='gray_r', interpolation='nearest')
    plt.xticks([])
    plt.yticks([])
    plt.show()

def show_grid_console(grid: np.ndarray):
    for row in grid:
        print(''.join('█' if cell == 1 else ' ' for cell in row))
