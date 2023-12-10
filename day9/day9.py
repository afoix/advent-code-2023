def diff_extrapolate_line(numbers_line):
    if all(value == 0 for value in numbers_line):
        return 0
    else: 
        sihfted_number = numbers_line[1:]
        pairwise_list = list(zip(numbers_line, sihfted_number))
        diff = []
        for x, y in pairwise_list:
            diff.append(y - x)

        # recursive, return an extrapolate value
        extrapolate = diff_extrapolate_line(diff)
        return extrapolate + numbers_line[-1]

with open('day9/day9_input.txt', 'r') as f:
    lines = list(map(lambda x: list(map(int, x.split())), f.readlines()))
    result = [diff_extrapolate_line(line) for line in lines]
    print('Part 1: ' + str(sum(result)))