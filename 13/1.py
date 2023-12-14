with open("input.txt",'r') as f:
    D = f.read().strip()
    L = D.split('\n')
    parts = D.split('\n\n')
    # print(len(parts))



rc = [0,0]


G = [[c for c in row] for row in L]

for part2 in [False, True]:
  ans = 0
  for grid in D.split('\n\n'):
    G = [[c for c in row] for row in grid.split('\n')]
    R = len(G)
    C = len(G[0])
    # vertical symmetry
    for c in range(C-1):
      badness = 0
      for dc in range(C):
        left = c-dc
        right = c+1+dc
        if 0<=left<right<C:
          for r in range(R):
            if G[r][left] != G[r][right]:
              badness += 1
      if badness == (1 if part2 else 0):
        ans += c+1
        rc[1]+=c+1
    for r in range(R-1):
      badness = 0
      for dr in range(R):
        up = r-dr
        down = r+1+dr
        if 0<=up<down<R:
          for c in range(C):
            if G[up][c] != G[down][c]:
              badness += 1
      if badness == (1 if part2 else 0):
        rc[0]+=r+1
        ans += 100*(r+1)
  print(ans)

print(rc)
rows_cols = [0, 0]
def get_mirror(part):
    lines = part.strip().split('\n')
    for i in range(0,len(lines[0])-1):
        is_mirror = True
        for k,line in enumerate(lines):
            length = min(i+1,len(line)-i-1)
            if line[i-length+1:i+1] != "".join(reversed(line[i+1:i+length+1])):
                is_mirror = False
                break
        if is_mirror:
            rows_cols[1]+=i+1
    for i in range(0,len(lines)-1):
        is_mirror = True
        j = i
        k = i+1
        for p in range(len(lines[0])):
            while j >=0 and k < len(lines):
                if lines[j][p] != lines[k][p]:
                    is_mirror = False
                    break
                j-=1
                k+=1
        if is_mirror:
            rows_cols[0]+=i+1

    # return 0,0







for part in parts:
    try:
       get_mirror(part)
        # print(mirror,i)
    except:
        print(part)
        break
print(rows_cols)

print(rows_cols[0]*100+rows_cols[1])