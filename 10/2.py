with open("test_input.txt",'r') as f:
    lines = f.read().strip().split('\n')

res = 0
for i , line in enumerate(lines):
    inner = False
    for t in line:
        if t == '|':
            inner = not inner
        elif t == '.' and inner:
            res += 1

print(res)