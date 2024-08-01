from collections import deque
class Solution:
    def shortestDistance(self, N, M, A, X, Y):
        grid = A
        lengthOfGrid = len(grid)
        queue = deque([(0, 0, 1)])
        visited = set((0, 0))
        direct = [[0, 1], [1, 0], [0, -1], [-1, 0],
                  [1, 1], [-1, -1], [1, -1], [-1, 1]]
        while queue:
            row, column, lengthOfPosition = queue.popleft()
            if min(row, column) < 0 or max(row, column) >= lengthOfGrid or grid[row][column]:
                continue
            if row == lengthOfGrid - 1 and column == lengthOfGrid - 1:
                return lengthOfPosition
            for directRow, directColumn in direct:
                if (row + directRow, column + directColumn) not in visited:
                    queue.append((row + directRow, column + directColumn, lengthOfPosition + 1))
                    visited.add((row + directRow, column + directColumn))

        return -1

# Example usage:
solution_instance = Solution()
N, M = 3,4
A = [[1,0,0,0],[1,1,0,1],[0,1,1,1]]
X, Y = 2,3

result = solution_instance.shortestDistance(N, M, A, X, Y)
print(result)


