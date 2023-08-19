import random
import time
from collections import deque

# Generate a random 3x3 grid with numbers from 1 to 8 and a blank space.
numbers = list(range(1, 9)) + ["B"]
random.shuffle(numbers)
initial_grid = [numbers[i:i+3] for i in range(0, 9, 3)]
target_grid = [[1, 2, 3], [4, 5, 6], [7, 8, 'B']]

def find_blank(grid):
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 'B':
                return i, j

def is_valid_move(x, y):
    return 0 <= x < 3 and 0 <= y < 3

def bfs(initial, target):
    visited = set()
    queue = deque([(initial, 0)])  # The grid and its depth
    while queue:
        state, depth = queue.popleft()
        if state == target:
            return depth
        visited.add(tuple(map(tuple, state)))
        x, y = find_blank(state)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Possible moves
            new_x, new_y = x + dx, y + dy
            if is_valid_move(new_x, new_y):
                new_state = [row[:] for row in state]
                new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
                if tuple(map(tuple, new_state)) not in visited:
                    queue.append((new_state, depth + 1))

def dfs(initial, target, depth=0, visited=None):
    if visited is None:
        visited = set()
    if initial == target:
        return depth
    visited.add(tuple(map(tuple, initial)))
    x, y = find_blank(initial)
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_x, new_y = x + dx, y + dy
        if is_valid_move(new_x, new_y):
            new_state = [row[:] for row in initial]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            if tuple(map(tuple, new_state)) not in visited:
                result = dfs(new_state, target, depth + 1, visited)
                if result:  # Stop at first found solution in DFS
                    return result

# Track BFS execution time
start_time = time.time()
bfs_steps = bfs(initial_grid, target_grid)
bfs_time = time.time() - start_time

# Track DFS execution time
start_time = time.time()
dfs_steps = dfs(initial_grid, target_grid)
dfs_time = time.time() - start_time

print(f"Initial grid:")
for row in initial_grid:
    print(row)

print(f"\nBFS steps: {bfs_steps}, Execution time: {bfs_time:.4f} seconds")
print(f"DFS steps: {dfs_steps}, Execution time: {dfs_time:.4f} seconds")
