from copy import deepcopy
with open('input.txt','r') as f:
    grid = [list(line) for line in f.read().strip().split('\n')]
initial_condition = deepcopy(grid)
#UP - North
N = 10**9
def cycle():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'O':
                k = i
                while k > 0 and grid[k-1][j] == '.':
                    grid[k][j] = '.'
                    k-=1
                grid[k][j] = 'O'



    for i in range(len(grid[0])):
        for j in range(len(grid)):
            if grid[j][i] == 'O':
                k = i
                while k > 0 and grid[j][k-1] == '.':
                    grid[j][k] = '.'
                    k-=1
                grid[j][k] = 'O'
    for i in range(len(grid)-1,-1,-1):
        for j in range(len(grid[0])):
            if grid[i][j] == 'O':
                k = i
                while k < len(grid)-1 and grid[k+1][j] == '.':
                    grid[k][j] = '.'
                    k+=1
                grid[k][j] = 'O'

    for i in range(len(grid[0])-1,-1,-1):
        for j in range(len(grid)):
            if grid[j][i] == 'O':
                k = i
                while k < len(grid[0])-1 and grid[j][k+1] == '.':
                    grid[j][k] = '.'
                    k+=1
                grid[j][k] = 'O'



def show(grid):
    for l in grid:
        print(''.join(l))
# conditions = [initial_condition]
conditions = {}
indexes = []
T = 0
for i in range(N):
    g = tuple(tuple(x) for x in grid)
    if g in conditions:
        break
    conditions[g] = i
    indexes.append(g)
    cycle()
    T+=1

reps = T - conditions[g]

final_grid = indexes[(N-conditions[g])%reps+conditions[g]]

# g = conditions[T]
print(T)

# for g in conditions:
#     show(g)
#     print('\n_____________________________________________')



n = len(grid)
res = 0
for i in final_grid:
    
    count = 0
    for j in i:
        if j == 'O':
            count+=1
    
    # print(n,count)
    res += n*count
    n-=1

print(res)
    
