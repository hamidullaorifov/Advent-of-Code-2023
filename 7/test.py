from collections import defaultdict,Counter
a = "22959"

def get_rank(card: str):
    counter = defaultdict(int)
    for c in card:
        counter[c] += 1
    sorted_vals = sorted(counter.items(),key=lambda x:x[1])
    if len(sorted_vals) == 1:
      return (5,)
    if sorted_vals[-1][0] == 'J':
      most_common = sorted_vals[-2][0]
      
    else:
      most_common = sorted_vals[-1][0]
    if 'J' in counter:
      counter[most_common] += counter['J']
      del counter['J']

    return tuple(sorted(counter.values()))

def strength(hand, part2=True):
    a = hand
    hand = hand.replace('T', chr(ord('9')+1))
    hand = hand.replace('J', chr(ord('2')-1) if part2 else chr(ord('9')+2))
    hand = hand.replace('Q', chr(ord('9')+3))
    hand = hand.replace('K', chr(ord('9')+4))
    hand = hand.replace('A', chr(ord('9')+5))

    C = Counter(hand)
    if part2:
        target = list(C.keys())[0]
        for k in C:
            if k != '1':
                if C[k] > C[target] or target == '1':
                    target = k
        assert target != '1' or list(C.keys()) == ['1']
        if '1' in C and target != '1':
            C[target] += C['1']
            del C['1']
        assert '1' not in C or list(C.keys()) == ['1'], f'{C} {hand}'
    # res2[a] = tuple(sorted(C.values()))
    # res2.append(tuple(a))
    if sorted(C.values()) == [5]:
        return (10, hand)
    elif sorted(C.values()) == [1, 4]:
        return (9, hand)
    elif sorted(C.values()) == [2, 3]:
        return (8, hand)
    elif sorted(C.values()) == [1, 1, 3]:
        return (7, hand)
    elif sorted(C.values()) == [1, 2, 2]:
        return (6, hand)
    elif sorted(C.values()) == [1, 1, 1, 2]:
        return (5, hand)
    elif sorted(C.values()) == [1, 1, 1, 1, 1]:
        return (4, hand)
    else:
        assert False, f'{C} {hand} {sorted(C.values())}'

print(get_rank(a))
print(strength(a))