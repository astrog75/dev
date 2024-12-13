##########################
#
#       Part 1
#
##########################

with open("input_6.txt", "r") as f:
    grid = f.read().splitlines()

n = len(grid)
# current position and direction
x, y, dir_ = 0, 0, "up"

for i in range(n):
    for j in range(n):
        if grid[i][j] == '^':
            x, y = i, j

seen = {(x,y)}      

while True:
    if dir_ == "up":
        if x > 0:
            if grid[x-1][y] != "#":
                x -= 1
            else:
                dir_ = "right"
        else:
            break
    
    if dir_ == "down":
        if x < n-1:
            if grid[x+1][y] != "#":
                x += 1
            else:
                dir_ = "left"
        else:
            break
    
    if dir_ == "left":
        if y > 0:
            if grid[x][y-1] != "#":
                y -= 1
            else:
                dir_ = "up"
        else:
            break
    
    if dir_ == "right":
        if y < n-1:
            if grid[x][y+1] != "#":
                y += 1
            else:
               dir_ = "down"
        else:
            break
    
    seen.add((x,y))

print(len(seen))


##########################
#
#       Part 2
#
##########################
    
class state:
    def __init__(self, x=0, y=0, dir="up"):
        self.x = x
        self.y = y
        self.dir = dir
    
    def __str__(self):
        return f"My position is {(self.x, self.y)} and i'm pointing towards {self.dir}"

with open("input_6.txt", "r") as f:
    grid = f.read().splitlines()
    
new_grid = []
for row in grid:
    new_grid.append(list(row))

grid = new_grid

# grid = """....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...""".splitlines()

n = len(grid)
curr = state()

for i in range(n):
    for j in range(n):
        if grid[i][j] == '^':
            curr.x, curr.y = i,j

start = state(curr.x, curr.y, curr.dir)

res = 0
for k in range(n):
    for l in range(n):
        # Place a new obstacle in grid[k][l]
        tmp = grid[k][l]
        grid[k][l] = "#"
        
        curr = state(start.x, start.y, start.dir)
        
        seen = set()      
        loop = False
        
        while True:
            (i,j) = curr.x, curr.y
            if curr.dir == "up":
                if curr.x > 0:
                    if grid[i-1][j] != "#":
                        curr.x -= 1
                    else:
                        curr.dir = "right"
                else:
                    break
            elif curr.dir == "down":
                if curr.x < n-1:
                    if grid[i+1][j] != "#":
                        curr.x += 1
                    else:
                        curr.dir = "left"
                else:
                    break
            elif curr.dir == "left":
                if curr.y > 0:
                    if grid[i][j-1] != "#":
                        curr.y -= 1
                    else:
                        curr.dir = "up"
                else:
                    break
            elif curr.dir == "right":
                if curr.y < n-1:
                    if grid[i][j+1] != "#":
                        curr.y += 1
                    else:
                        curr.dir = "down"
                else:
                    break
                 
            if (curr.x, curr.y, curr.dir) in seen:
                loop = True
                break
            else:
                seen.add((curr.x, curr.y, curr.dir))
        
        grid[k][l] = tmp
        
        if loop:
            res += 1
    
print(res)    
    
    