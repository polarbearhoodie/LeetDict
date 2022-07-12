class Islands:
    def checkContain(self, grid, ch):
        for row in grid:
            for x in row:
                if x == ch:
                    return True
        return False

    def centerAndCorners(self, grid, xy):
        coords = []
        if 0 <= xy[0] <= grid.shape[0] and 0 <= xy[1] <= grid.shape[1]:
            if grid[x, y] == "1":
                grid[x, y] = "0"
                coords = [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]

        return grid, coords

    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 1
        while checkContain(grid, "1"):
            # pathfinding deletion of 1's
            paths = []

            # add initial island
            for i, row in enumerate(grid):
                for j, entry in enumerate(row):
                    if entry == "1":
                        paths.append([i, j])
                        break

            while len(paths) != 0:
                grid, coord = centerAndCorners(grid, paths.pop())
                for x in coord:
                    paths.append(x)

            islands += 1

        return islands


class Tomato:
    def daysTillRot(self, grid):
        # perform bfs and determine the max(minimum depth)
        if not grid:
            return 0

        # replace with better symbols
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i, j] == 2:
                    grid[i, j] = "R"
                if grid[i, j] == 1:
                    grid[i, j] = 99
                if grid[i, j] == 0:
                    grid[i, j] = "#"

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "R":
                    bfsRot(grid, i, j, 1)

        maxi = -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                v = grid[i][j]
                if type(v) == int and v > maxi:
                    maxi = v

        return maxi

    def bfsRot(self, grid, x, y, depth):
        if 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]:
            val = grid[x][y]
            if type(val) == int:
                grid[x][y] = min(val, depth)
                bfsRot(grid, x + 1, y, depth + 1)
                bfsRot(grid, x - 1, y, depth + 1)
                bfsRot(grid, x, y + 1, depth + 1)
                bfsRot(grid, x, y - 1, depth + 1)
