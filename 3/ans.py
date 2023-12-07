from collections import defaultdict
with open('input.txt','r') as f:
    D = f.read().strip()


lines = D.split('\n')
G = [[c for c in line] for line in lines]
R = len(G)
C = len(G[0])
print(len(lines))
p1 = 0
nums = defaultdict(list)
for r in range(len(G)):
  gears = set() # positions of '*' characters next to the current number
  n = 0
  has_part = False
  for c in range(len(G[r])+1):
    if c<C and G[r][c].isdigit():
      n = n*10+int(G[r][c])
      for rr in [-1,0,1]:
        for cc in [-1,0,1]:
          if 0<=r+rr<R and 0<=c+cc<C:
            ch = G[r+rr][c+cc]
            if not ch.isdigit() and ch != '.':
              has_part = True
            if ch=='*':
              gears.add((r+rr, c+cc))
    elif n>0:
      for gear in gears:
        nums[gear].append(n)
      if has_part:
        p1 += n
      n = 0
      has_part = False
      gears = set()

print(p1)
data = lines

nums_positions = []


for i, line in enumerate(data):
    # nums_length = 0
    num = ''
    j = 0
    while j<len(line):
        if line[j].isdigit():
            k = j
            while j < len(line) and line[j].isdigit() :
                num+=line[j]
                j+=1
            if num:
                nums_positions.append((num,i,k))
                num = ''
        j+=1
# print(nums_positions)



s = 0
for p in nums_positions:
    num, i, j = p
    is_part = False
    if j+len(num) < len(data[i]) and data[i][j+len(num)]!='.' and not data[i][j+len(num)].isdigit():
        is_part = True
    if j > 0 and data[i][j-1]!='.' and not data[i][j-1].isdigit():
        is_part = True
    if i > 0:
        if j > 0 and not data[i-1][j-1].isdigit() and data[i-1][j-1]!='.':
            is_part = True
        if j + len(num) < len(data[i]) and data[i-1][j+len(num)]!='.' and not data[i-1][j+len(num)].isdigit():
            is_part = True
        # if data[i-1][j] != '.' or (j + len(num)-1<len(data[i]) and data[i-1][j+len(num)-1]!='.'):
        #     is_part = True
        for k in range(j,j+len(num)):
            if data[i-1][k] != '.' and not data[i-1][j+len(num)].isdigit():
                is_part = True
                break
    if i < len(data)-1:
        if j > 0 and data[i+1][j-1]!='.' and not data[i+1][j-1].isdigit():
            is_part = True
        if j + len(num) < len(data[i]) and data[i+1][j+len(num)]!='.' and not data[i+1][j+len(num)].isdigit():
            
            is_part = True
        # if data[i+1][j] !='.' or (j+len(num)-1 < len(data[i]) and data[i+1][j+len(num)-1] != '.'):
        #     is_part = True
        # else:
        #     print("A",num,i+1,j+1+len(num))
        for k in range(j,j+len(num)):
            if data[i+1][k] != '.' and not data[i+1][k].isdigit():
                is_part = True
                break
    if is_part:
        s+=int(num)
    # else:
    #     print(num,is_part)
print(s)
        

# p2 = 0
# for k,v in nums.items():
#   if len(v)==2:
#     p2 += v[0]*v[1]
# print(p2)