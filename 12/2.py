from functools import cache
filename = "input.txt"
test = True
if test:
    filename = "test_input.txt"


with open(filename,'r') as f:
    lines = f.read().strip().split('\n')
def is_valid(s,p):
    return tuple(len(x) for x in s.split('.') if x) == p
@cache
def get_arrangements_count(s,arrangements,res=0):
    if '?' not in s and is_valid(s,arrangements):
        return 1
    parts = tuple(x for x in s.split('.') if x)
    if len(parts[0]) < arrangements[0]:
        return 0
    index = s.find('?')
    if index >=0:
        
        left,right = s[:index],s[index+1:]
        return get_arrangements_count(left+'.'+right,arrangements) + get_arrangements_count(left+"#"+right,arrangements)
    return 0


# print(get_arrangements_count('.###.##....#',[3,2,1]))
res = 0
    
    
for line in lines:
    s,nums_str = line.split()

    next_str = '?'.join([s]*5)
    
    nums = tuple(map(int,nums_str.split(',')))
    t = get_arrangements_count(next_str,nums*5)
    print(t)
    # print(s,nums,t)

    res += t
print(res)
