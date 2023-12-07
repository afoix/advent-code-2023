
#def parse_input(filename):
#  file = open(filename, 'r')
#  lines = file.readlines()
#  return list(zip( list(map(int, lines[0].split()[1:]))
#                 , list(map(int, lines[1].split()[1:]))))
#
#if __name__ == '__main__':
#  races = parse_input('input.txt')
#  print(races)
#  possibilities = [ [(i, i*(t-i)) for i in range(t+1)]
#                    for t, d in races ]
#  wins = [ [(i, i*(t-i)) for i in range(t+1) if (i*(t-i)) > d]
#           for t, d in races ]
#  #print("------------------------")
#  #print(possibilities)
#  #print("------------------------")
#  #print(wins)
#  nbwins = list(map(len, wins))
#  prod = 1
#  for n in nbwins:
#    prod *= n
#  print(f"product of nbwins: {prod}")

def parse_input(filename):
  file = open(filename, 'r')
  lines = file.readlines()
  time = int(''.join(lines[0].split()[1:]))
  distance = int(''.join(lines[1].split()[1:]))
  return (time, distance)

def searchFirstWin(left_t, right_t, race_t, target_d):
  offset = int((right_t - left_t) / 2)
  t = left_t + offset
  left_d = (t-1)*(race_t-(t-1))
  d = t*(race_t-t)
  #print(f'({left_t}, {right_t}, {target_d}), t: {t}, left_d: {left_d}, d:{d}')
  if left_d <= target_d and d > target_d:
    return t
  elif d > target_d:
    return searchFirstWin(left_t, right_t - offset, race_t, target_d)
  else:
    return searchFirstWin(left_t + offset, right_t, race_t, target_d)

def searchLastWin(left_t, right_t, race_t, target_d):
  offset = int((right_t - left_t) / 2)
  t = left_t + offset
  right_d = (t+1)*(race_t-(t+1))
  d = t*(race_t-t)
  #print(f'({left_t}, {right_t}, {target_d}), t: {t}, right_d: {right_d}, d:{d}')
  if right_d <= target_d and d > target_d:
    return t
  elif d > target_d:
    return searchLastWin(left_t + offset, right_t, race_t, target_d)
  else:
    return searchLastWin(left_t, right_t - offset, race_t, target_d)

if __name__ == '__main__':
  #time, distance = parse_input('day6_input.txt')
  time, distance = parse_input('day6/day6_input.txt')
  print(time, distance)
  firstWin = searchFirstWin(0, time, time, distance)
  print(firstWin)
  lastWin = searchLastWin(0, time, time, distance)
  print(lastWin)
  print(f'nbwins: {lastWin - firstWin + 1}')
