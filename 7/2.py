from collections import Counter, defaultdict
ranks = {
    (5,): 7,
    (1, 4): 6,
    (2, 3): 5,
    (1, 1, 3): 4,
    (1, 2, 2): 3,
    (1, 1, 1, 2): 2,
    (1, 1, 1, 1, 1): 1
}


def get_rank(card: str):
    counter = defaultdict(int)
    for c in card:
        counter[c] += 1
    sorted_vals = sorted(counter.items(),key=lambda x:x[1])
    if len(sorted_vals) == 1:
      return (5,)
    if sorted_vals[-1][0] == 'J':
      most_common = sorted_vals[-2][0]
      # return tuple(sorted(counter.values()))
    else:
      most_common = sorted_vals[-1][0]
    if 'J' in counter:
      counter[most_common] += counter['J']
      del counter['J']

    return tuple(sorted(counter.values()))


labels = "A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J".split(", ")
numeral_system = len(labels)
label_strength = {}
for l, s in zip(labels, range(numeral_system, -1, -1)):
    label_strength[l] = s

def get_strength(line):
    card = line.split()[0]
    k = numeral_system**5
    s = 0
    for c in card:
        s+=k*label_strength[c]
        k//=numeral_system
    return ranks[get_rank(card)]*10000000 + s



with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")



lines.sort(key=lambda x:get_strength(x))



res = 0
for i, line in enumerate(lines, start=1):
    num = int(line.split()[1])
    res += i*num
print(res)

