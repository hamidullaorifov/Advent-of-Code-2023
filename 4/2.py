from collections import defaultdict
with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")



d = defaultdict(lambda:1)
res = 0
for i,line in enumerate(lines,start=1):
    _, cards = line.split(":")
    winning_cards_str, my_cards_str = cards.split("|")
    winning_cards = set(winning_cards_str.strip().split())
    my_cards = set(my_cards_str.strip().split())
    intersection = winning_cards.intersection(my_cards)
    
    if intersection:
        
        for j in range(i+1,i+len(intersection)+1):
            d[j] += d[i]
    if i not in d:
        d[i] = 1
# print(d)
print(sum(d.values()))
        
# print(res)