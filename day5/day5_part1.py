import re

document = open('day5/day5_input.txt', 'r')
#document = open('day5/alex_input.txt', 'r')

class MapRange:
    def __init__(self, dest_start, src_start, size):
        self.dest_start = dest_start
        self.src_start = src_start
        self.size = size

    def lookup(self, src):
        if src >= self.src_start and src < (self.src_start + self.size):
            return self.dest_start + (src - self.src_start)
        else: 
            return None
        
    def __str__(self):
        return "dest_start: {dest_start}, src_start: {src_start}, size: {size}".format(dest_start=self.dest_start, src_start=self.src_start, size=self.size)

def lookupRangeMap(ranges, src):
    ret = src
    for r in ranges:
        dest = r.lookup(src)
        if dest:
            ret = dest
            break
    return ret


def getLineRanges(line):
    dest, src, sz = list(map(int, line.split()))
    return MapRange(dest, src, sz)

lines = document.readlines()

# get seeds
seeds = list(map(int, lines[0].split()[1:]))

seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []

for line in lines[1:]:
    if line.startswith('seed-to-soil'):
        current_map = seed_to_soil
    elif line.startswith('soil-to-fertilizer'):
        current_map = soil_to_fertilizer
    elif line.startswith('fertilizer-to-water'):
        current_map = fertilizer_to_water
    elif line.startswith('water-to-light'):
        current_map = water_to_light
    elif line.startswith('light-to-temperature'):
        current_map = light_to_temperature
    elif line.startswith('temperature-to-humidity'):
        current_map = temperature_to_humidity
    elif line.startswith('humidity-to-location'):
        current_map = humidity_to_location
    # skip empty lines
    elif line == '\n' or not line:
        continue
    else:
        print(line)
        current_map.append(getLineRanges(line))

# Look up for each seed
seed_locations = []
for seed in seeds:
    soil = lookupRangeMap(seed_to_soil, seed)
    fertilizer = lookupRangeMap(soil_to_fertilizer, soil)
    water = lookupRangeMap(fertilizer_to_water, fertilizer)
    light = lookupRangeMap(water_to_light, water)
    temperature = lookupRangeMap(light_to_temperature, light)
    humidity = lookupRangeMap(temperature_to_humidity, temperature)
    location = lookupRangeMap(humidity_to_location, humidity)
    seed_locations[seed] = location

print(min(seed_locations))

    




