from collections import Counter
ranks = {
    (5,):7,
    (1,4):6,
    (2,3):5,
    (1,1,3):4,
    (1,2,2):3,
    (1,1,1,2):2,
    (1,1,1,1,1):1
    }
def get_rank(card:str):
    return ranks[tuple(sorted((Counter(card).values())))]

labels = "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2".split(", ")

label_strength = {}
for l, s in zip(labels,range(13,-1,-1)):
    label_strength[l] = s
print(label_strength)

def compare_lines(l1,l2):
    card1,_ = l1.split(" ")
    card2,_ = l2.split(" ")
    return compare(card1,card2)
def compare(card1,card2):
    if get_rank(card1) > get_rank(card2):
        return -1
    if get_rank(card1) < get_rank(card2):
        return 1
    if card1 < card2:
        -1
    for i, j in zip(card1,card2):
        if label_strength[i] > label_strength[j]:
            return -1
        if label_strength[i] < label_strength[j]:
            return 1
    return 0

with open("input.txt","r") as f:
    lines = f.read().strip().split("\n")


for i in range(len(lines)-1):
    for j in range(i+1,len(lines)):
        if compare_lines(lines[i],lines[j]) < 0:
            lines[i],lines[j] = lines[j],lines[i]

# print(lines)
res = 0
for i,line in enumerate(lines,start=1):
    num = int(line.split()[1])
    # print(i,num)
    res += i*num
print(res)


