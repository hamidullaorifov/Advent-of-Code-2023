with open('input.txt','r') as f:
    data = f.readlines()
s = 0
for row in data:
    i, j = 0,len(row)-1
    while i<=j and not row[i].isdigit():
        i +=1
    while i<=j and not row[j].isdigit():
        j -=1
    s+= int(row[i]+row[j])
print(s)

78915902