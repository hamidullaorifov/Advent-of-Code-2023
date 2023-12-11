from collections import deque
with open("input.txt",'r') as f:
    lines = f.read().strip().split('\n')

start = (0,0)
for i, line in enumerate(lines):
    index = line.find("S")
    # print(line,index)
    if index >= 0:
        start = (i,index)
        break
distances = [[0]*len(lines[0]) for i in range(len(lines))]
max_distance = 0


visited = set() # List for visited nodes.
queue = deque()    #Initialize a queue

directions = {
    '|':((1,0),(-1,0)),
    '-':((0,1),(0,-1)),
    'F':((0,1),(1,0)),
    'J':((-1,0),(0,-1)),
    'L':((-1,0),(0,1)),
    '7':((0,-1),(1,0)),
    'S':((0,1),(1,0),(-1,0),(0,-1))
    
}

# match ={
#     'S':'LF-|J7',
#     'L':
# }
coords = {
    (0,-1):'-LF',
    (-1,0):'|7F',
    (0,1):'-7J',
    (1,0):'|JL'
}

def is_valid_coord(row,col):
    return 0<=row<len(lines) and 0 <= col < len(lines[0])

visited.add(start)


queue.append(start)



while queue:          # Creating loop to visit each node
    row,col = pos = queue.popleft() 
    for (i,j) in directions[lines[row][col]]:
        next_row,next_col = row + i, col + j
        if is_valid_coord(next_row,next_col) and (next_row,next_col) not in visited and lines[next_row][next_col] in coords[(i,j)]:
            distances[next_row][next_col] = max(distances[next_row][next_col],distances[row][col]+1)
            max_distance = max(max_distance,distances[next_row][next_col])
            visited.add((next_row,next_col))
            queue.append((next_row,next_col))



print(max_distance)
    

    

# Driver Code
# print("Following is the Breadth-First Search")
# bfs(visited, graph, '5')