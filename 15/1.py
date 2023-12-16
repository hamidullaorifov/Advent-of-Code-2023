with open('input.txt','r') as f:
    data = f.read().split(',')




def hash(s):
    start = 0
    for i in s:
        cur = start + ord(i)
        start = cur * 17 % 256
    return start

# res = 0
# for i in data:
#     res+=hash(i)

print(hash("pc"))


        
