import re

document = open('day3/day3_input.txt', 'r')

lines = document.readlines()

numbers = []
symbols = []
for line in lines:
    # Find an ocurrance of a number in the line
    numbers.append([m for m in re.finditer('\d+', line)])
    symbols.append([m for m in re.finditer('[^.\d\n]', line)])

engine_num = []
for i, nums in enumerate(numbers):
    for num in nums:
        done = False
        if not done and i > 0:
            print("entering above")
            syms = symbols[i-1]
            for sym in syms:
                if (sym.start() >= num.start() - 1) and (sym.start() <= num.end()):
                    engine_num.append(int(num.group()))
                    done = True
                    print("adjacent from above: {num} and {sym}".format(num=num, sym=sym))
                    break

        if not done and i < len(numbers) - 1:
            print("entering below")
            syms = symbols[i+1]
            for sym in syms:
                if (sym.start() >= (num.start() - 1)) and (sym.start() <= num.end()):
                    engine_num.append(int(num.group()))
                    done = True
                    print("adjacent from below: {num} and {sym}".format(num=num, sym=sym))
                    break

        if not done:
            print("entering side")
            syms = symbols[i]
            for sym in syms:
               if (sym.start() == num.start() - 1) or (sym.start() == num.end()):
                    engine_num.append(int(num.group()))
                    print("adjacent from side: {num} and {sym}".format(num=num, sym=sym))
                    break
        

print(sum(engine_num))

