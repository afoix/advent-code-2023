
document = open('day1_input.txt', 'r')
lines = document.readlines()
total = 0

for line in lines:
    leftnum = None
    for c in line:
        if c in "0123456789":
            leftnum = int(c)
            break
    
    rightnum = None
    for i in range(len(line)-1, -1, -1):
        if line[i] in "0123456789":
            rightnum = int(line[i])
            break

    num = leftnum * 10 + rightnum
    total += num

print(total)

