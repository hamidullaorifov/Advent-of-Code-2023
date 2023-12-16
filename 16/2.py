from collections import defaultdict

import sys

sys.setrecursionlimit(10000)
with open('input.txt','r') as f:
    data = f.read().strip()
    lines = data.split('\n')


grid = [list(s) for s in lines]



directions = defaultdict(set)



m = len(grid)
n = len(grid[0])

def func(d,r,c):
    if d in directions[(r,c)]:
        return
    directions[(r,c)].add(d)
    cur = grid[r][c]

    # right
    if d == 'r':
        if cur == '.' or cur == '-':
            if c == n-1:
                return
            func(d,r,c+1)
        elif cur == '|':
            if r > 0:
                func('u',r-1,c)
            if r < m-1:
                func('d',r+1,c)
        elif cur == '/':
            if r > 0:
                func('u',r-1,c)
        elif cur == '\\':
            if r < m-1:
                func('d',r+1,c)


    # down
    if d == 'd':
        if cur == '.' or cur == '|':
            if r == m-1:
                return
            func(d,r+1,c)
        elif cur == '-':
            if c > 0:
                func('l',r,c-1)
            if c < n-1:
                func('r',r,c+1)
        elif cur == '/':
            if c > 0:
                func('l',r,c-1)
        elif cur == '\\':
            if c < n-1:
                func('r',r,c+1)

    # left
    if d == 'l':
        if cur == '.' or cur == '-':
            if c == 0:
                return
            func(d,r,c-1)
        elif cur == '|':
            if r > 0:
                func('u',r-1,c)
            if r < m-1:
                func('d',r+1,c)
        elif cur == '\\':
            if r > 0:
                func('u',r-1,c)
        elif cur == '/':
            if r < m-1:
                func('d',r+1,c)

    # up
    if d == 'u':
        if cur == '.' or cur == '|':
            if r == 0:
                return
            func(d,r-1,c)
        elif cur == '-':
            if c > 0:
                func('l',r,c-1)
            if c < n-1:
                func('r',r,c+1)
        elif cur == '\\':
            if c > 0:
                func('l',r,c-1)
        elif cur == '/':
            if c < n-1:
                func('r',r,c+1)





# func('r',0,0)
res = 0
for i in range(m):
    for j in [0,n-1]:
        for d in 'rlud':
            directions = defaultdict(set)
            func(d,i,j)
            cur = 0
            for v in directions.values():
                if v:
                    cur+=1
            res = max(res,cur)
for i in [0,m-1]:
    for j in range(n):
        for d in 'rlud':
            directions = defaultdict(set)
            func(d,i,j)
            cur = 0
            for v in directions.values():
                if v:
                    cur+=1
            res = max(res,cur)







print(res)
