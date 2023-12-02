
    


import re
# contained only 12 red cubes, 13 green cubes, and 14 blue cubes
document = open('day2/day2_input.txt', 'r')
lines = document.readlines()

id_count = []

# Example line: Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
# Game 99: 3 green, 2 blue, 1 red; 15 red, 8 blue, 7 green; 18 red, 12 blue, 2 green
def parse_line(line):
    # Regex expression to parse the game and its ID
    parse_game = re.compile('Game\s+(\d+):(.*)')
    game_id, rest = parse_game.search(line).groups()
    game_id = int(game_id)
    # parse the rest to extract the blocks
    rest = [x.split(",") for x in rest.split(';')]

    # flatten the list, convert the two list in a single one
    rest = [item for sublist in rest for item in sublist]
    
    # parse the blocks
    parse_block = re.compile('\s*(\d+)\s+(\w+)')
    dict_blocks = {"red": [], "green": [], "blue": []}
    for x in rest:
        v, k = parse_block.search(x).groups()
        dict_blocks[k].append(int(v))
    print(dict_blocks)
    
    max_dict = {}
    for k, v in dict_blocks.items():
        max_dict[k] = max(v)
    
    return max_dict["red"] *  max_dict["green"] * max_dict["blue"]
    

power_sets = 0
for line in lines:
    # sum of the power of these sets
    power_sets += parse_line(line)

print(power_sets)