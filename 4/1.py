with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

res = 0
for line in lines:
    _, cards = line.split(":")
    winning_cards_str, my_cards_str = cards.split("|")
    winning_cards = set(winning_cards_str.strip().split())
    my_cards = set(my_cards_str.strip().split())
    intersection = winning_cards.intersection(my_cards)
    if intersection:
        res+=1<<(len(intersection)-1)
print(res)