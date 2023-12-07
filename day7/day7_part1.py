from functools import cmp_to_key

def cardScore(card):
  return {
    'A': 12
  , 'K': 11
  , 'Q': 10
  , 'J': 9
  , 'T': 8
  , '9': 7
  , '8': 6
  , '7': 5
  , '6': 4
  , '5': 3
  , '4': 2
  , '3': 1
  , '2': 0
  }.get(card, 0)

def handScore(handtype):
  return {
    'Five of a kind': 6
  , 'Four of a kind': 5
  , 'Full house': 4
  , 'Three of a kind': 3
  , 'Two pair': 2
  , 'One pair': 1
  , 'High card': 0
  }.get(handtype, 0)

def cmpHands(a, b):
  cmpPairs = list(zip(a, b))
  if len(cmpPairs) == 0:
    return 0
  else:
    if (cardScore(cmpPairs[0][0]) > cardScore(cmpPairs[0][1])):
      return 1
    elif (cardScore(cmpPairs[0][1]) > cardScore(cmpPairs[0][0])):
      return -1
    else:
      return cmpHands(*zip(*cmpPairs[1:]))

def classifyHand(hand):
  cardcount = {}
  for c in hand:
    try:
      cardcount[c] += 1
    except:
      cardcount[c] = 1
  cardtypes = len(cardcount)
  handtype = None
  if cardtypes == 1:
    handtype = 'Five of a kind'
  elif cardtypes == 2 and 1 in cardcount.values():
    handtype = 'Four of a kind'
  elif cardtypes == 2:
    handtype = 'Full house'
  elif cardtypes == 3 and 3 in cardcount.values():
    handtype = 'Three of a kind'
  elif cardtypes == 3:
    handtype = 'Two pair'
  elif cardtypes == 4:
    handtype = 'One pair'
  else:
    handtype = 'High card'
  return (handtype, cardcount)

def parse_input(filename):
  file = open(filename, 'r')
  hands = []
  for line in file.readlines():
    es = line.split()
    hands.append({
      'hand': es[0]
    , 'bid': int(es[1])
    , 'info': classifyHand(es[0])
    })
  return hands

def sortAllHands(allhands):
  allFiveOfAKind = [x for x in allhands if x['info'][0] == 'Five of a kind']
  allFourOfAKind = [x for x in allhands if x['info'][0] == 'Four of a kind']
  allFullHouse = [x for x in allhands if x['info'][0] == 'Full house']
  allThreeOfAKind = [x for x in allhands if x['info'][0] == 'Three of a kind']
  allTwoPair = [x for x in allhands if x['info'][0] == 'Two pair']
  allOnePair = [x for x in allhands if x['info'][0] == 'One pair']
  allHighCard = [x for x in allhands if x['info'][0] == 'High card']
  def cmp(a, b):
    return  cmpHands(a['hand'], b['hand'])
  allFiveOfAKind.sort(key=cmp_to_key(cmp))
  allFourOfAKind.sort(key=cmp_to_key(cmp))
  allFullHouse.sort(key=cmp_to_key(cmp))
  allThreeOfAKind.sort(key=cmp_to_key(cmp))
  allTwoPair.sort(key=cmp_to_key(cmp))
  allOnePair.sort(key=cmp_to_key(cmp))
  allHighCard.sort(key=cmp_to_key(cmp))
  return allHighCard + allOnePair + allTwoPair + allThreeOfAKind \
                     + allFullHouse + allFourOfAKind + allFiveOfAKind

if __name__ == '__main__':
  hands = sortAllHands(parse_input('day7/day7_input.txt'))
  print(*hands, sep='\n')
  print(sum([i*x for i, x in enumerate([hand['bid'] for hand in hands], 1)]))