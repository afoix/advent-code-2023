import sys

translation = {"zero" : 0, "0": 0, "one": 1, "1": 1, "two": 2, "2": 2, "three": 3, "3": 3, "four": 4, "4": 4, "five": 5, "5": 5, "six": 6, "6": 6, "seven": 7, "7": 7, "eight": 8, "8": 8, "nine": 9, "9": 9}

document = open('day1_input.txt', 'r')
lines = document.readlines()
total = 0

for line in lines:
    leftnum = None
    leftnums = {}
    leftposition = sys.maxsize

    for key in translation:
        leftnums[key] = line.find(key)
    for c in "0123456789":
        leftnums[str(c)] = line.find(str(c))
    
    for key, v in leftnums.items():
        if leftposition > v and v != -1:
            leftposition = v
            leftnum = translation[key]

    (rightnum) = None
    rightnums = {}
    rightposition = -1

    for key in translation:
        rightnums[key] = line.rfind(key)
    for c in "0123456789":
        rightnums[str(c)] = line.rfind(str(c))
    
    for key, v in rightnums.items():
        if rightposition < v and v != -1:
            rightposition = v
            rightnum = translation[key]

    num = leftnum * 10 + rightnum
    total += num

print(total)