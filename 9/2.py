# s = 0
def func(nums):
    next_nums = []
    for i in range(1,len(nums)):
        next_nums.append(nums[i]-nums[i-1])
    if len(set(next_nums))==1:
        prev = nums[0] - next_nums[0]
        return prev
    return nums[0] - func(next_nums)

with open('input.txt','r') as f:
    lines = f.read().strip().split('\n')

res = 0
for line in lines:
    nums = map(int,(x for x in line.split() if x))
    res += func(tuple(nums))
print(res)