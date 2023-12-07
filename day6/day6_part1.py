import re
 

def parse_input(file_name):
    file = open(file_name, 'r')
    lines = file.readlines()
    return list(zip(list(map(int, lines[0].split()[1:])), 
           list(map(int, lines[1].split()[1:]))))

if __name__ == '__main__':
    races = parse_input('day6/day6_input.txt')
    print(races)
    possibilities = [[(i, i*(t-1)) for i in range(t+1)] for t, d in races]
    wins = [[(i, i*(t-1)) for i in range(t+1) if (i*(t-i)) > d] 
                     for t, d in races]
    
    nbwins = list(map(len, wins))
    prod = 1
    for n in nbwins:
        prod *= n
    print("product of nbwins: " + str(prod))
