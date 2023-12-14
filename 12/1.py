filename = "input.txt"
test = False
if test:
    filename = "test_input.txt"


with open(filename,'r') as f:
    lines = f.read().strip().split('\n')
def is_valid(s,p):
    return [len(x) for x in s.split('.') if x] == p

def get_arrangements_count(s,arrangements,res=0):
    if '?' not in s and is_valid(s,arrangements):
        return 1
    index = s.find('?')
    if index >=0:
        left,right = s[:index],s[index+1:]
        return get_arrangements_count(left+'.'+right,arrangements) + get_arrangements_count(left+"#"+right,arrangements)
    return 0


print(get_arrangements_count('.###.##....#',[3,2,1]))
res = 0
    
    
for line in lines:
    s,nums_str = line.split()
    nums = list(map(int,nums_str.split(',')))
    t = get_arrangements_count(s,nums)
    # print(s,nums,t)

    res += t
print(res)
