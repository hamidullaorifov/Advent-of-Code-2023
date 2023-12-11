filename = 'input.txt'

with open(filename,'r') as f:
    lines = f.read().strip().split('\n')



def solution(part1):
    if part1:
        scale = 2
    else:
        scale = 1_000_000
    cols_involve_galaxy = [False] * len(lines[0])
    rows_involve_galaxy = [False] * len(lines)
    galaxies = []
    for i, line in enumerate(lines):
        for c,ch in enumerate(line):
            if ch == '#':
                cols_involve_galaxy[c] = True
                rows_involve_galaxy[i] = True
                galaxies.append((i,c))



    def get_distance(pos1,pos2):
        d = 0
        if pos1[1]<pos2[1]:
            for i in range(pos1[1]+1,pos2[1]+1):
                if cols_involve_galaxy[i] == True:
                    d+=1
                else:
                    d+=scale
        else:
            for i in range(pos1[1],pos2[1],-1):
                if cols_involve_galaxy[i] == True:
                    d+=1
                else:
                    d+=scale
        if pos1[0] < pos2[0]:
            for i in range(pos1[0]+1,pos2[0]+1):
                if rows_involve_galaxy[i]:
                    d+=1
                else:
                    d+=scale
        else:
            for i in range(pos1[0],pos2[0],-1):
                if rows_involve_galaxy[i] == True:
                    d+=1
                else:
                    d+=scale
        return d

    s = 0
    count = 0
    for i in range(len(galaxies)-1):
        for j in range(i+1,len(galaxies)):
            dist = get_distance(galaxies[i],galaxies[j])
            # print(galaxies[i],galaxies[j],dist)
            s+=dist

    return s
for part in [True,False]:
    print(solution(part))


