class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        queue = []
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    queue.append([i+1,j])
                    queue.append([i-1,j])
                    queue.append([i,j+1])
                    queue.append([i,j-1])
                    grid[i][j] = "0"
                    while (queue):
                        y,x = queue.pop()
                        
                        if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]) or grid[y][x] == "0":
                            continue
                        
                        if grid[y][x] == "1":
                            queue.append([y+1,x])
                            queue.append([y-1,x])
                            queue.append([y,x+1])
                            queue.append([y,x-1])
                        grid[y][x] = "0"
        return count

                        




        