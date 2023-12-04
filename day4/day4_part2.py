import re
document = open('day4/day4_input.txt', 'r')
lines = document.readlines()

def match_winners(ws, gs):
    ret = []
    for g in gs:
        if g in ws:
            ret.append(g)
    return ret

def score_matches(ws):
    ret = 1 if len(ws) > 0 else 0 
    for _ in ws[1:]:
        ret *= 2
    return ret

class CardInstance:
    def __init__(self, idx, winners, gottens, matches, instance_num):
        self.idx = idx
        self.winners = winners
        self.gottens = gottens
        self.matches = matches
        self.instance_num = instance_num
    
    def __str__(self):
        return "idx: {idx}, winners: {winners}, gottens: {gottens}, matches: {matches}, instance_num: {instance_num}".format(idx=self.idx, winners=self.winners, gottens=self.gottens, matches=self.matches, instance_num=self.instance_num)
    


winners = []
gottens = []
matches = []
scores = []
card_instances = []

for i, line in enumerate(lines):
    groups = re.split('[:|]', line)
    line_winners = [int(x) for x in re.findall("\d+", groups[1])]
    line_gottens = [int(x) for x in re.findall("\d+", groups[2])]
    winners.append(line_winners)
    gottens.append(line_gottens)
    matched = match_winners(line_winners, line_gottens)
    matches.append(matched)
    scores.append(score_matches(matched))
    card_instances.append(CardInstance(i, line_winners, line_gottens, matched, 1))

for i, card in enumerate(card_instances):
    for _ in range(card.instance_num):
        for j in range(1, len(card.matches)+1):
            card_instances[i+j].instance_num += 1

print(sum([card.instance_num for card in card_instances]))

#print(sum(scores))
#print(card_instances[0])

    

