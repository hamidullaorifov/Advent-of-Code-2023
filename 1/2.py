with open('input.txt','r') as f:
    data = f.readlines()
s = 0
digits = "one, two, three, four, five, six, seven, eight, nine"
digits = digits.split(", ")

for row in data:
    d1,d2 = None,None
    i, j = 0,len(row)-1
    while i<=j and not row[i].isdigit():
        i +=1
    while i<=j and not row[j].isdigit():
        j -=1
    digit1 = i
    digit2 = j
    for k in range(9):
        index = row.find(digits[k])
        if index != -1 and index<digit1:
            digit1 = index
            d1 = k+1
        index = row.rfind(digits[k])
        if index != -1 and index > digit2:
            digit2 = index
            d2 = k+1

    num = ''
    num += str(d1) if d1 else row[i]
    num += str(d2) if d2 else row[j]
    print(num)
    s+=int(num)
print(s)

