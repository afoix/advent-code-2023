import re

document = open('day3/day3_input.txt', 'r')
#document = open('day3/alex_input.txt', 'r')

lines = document.readlines()

numbers = []
symbols = []
for line in lines:
    # Find an ocurrance of a number in the line
    numbers.append([m for m in re.finditer('\d+', line)])
    symbols.append([m for m in re.finditer('\*', line)])
print(symbols)

result = 0
for i, syms in enumerate(symbols):
    for sym in syms:
        engine_num = []
        if i > 0:
            nums = numbers[i-1]
            for num in nums:
                if (sym.start() >= num.start() - 1) and (sym.start() <= num.end()):
                    engine_num.append(int(num.group()))
                    

        if i < len(numbers) - 1:
            print("entering below")
            nums = numbers[i+1]
            for num in nums:
                if (sym.start() >= (num.start() - 1)) and (sym.start() <= num.end()):
                    engine_num.append(int(num.group()))


        nums = numbers[i]
        for num in nums:
            if (sym.start() == num.start() - 1) or (sym.start() == num.end()):
                engine_num.append(int(num.group()))
        
        if len(engine_num) == 2:
            result += engine_num[0] * engine_num[1]
        

print(result)

    