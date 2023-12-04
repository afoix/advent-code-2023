import re
document = open('day4/day4_input.txt', 'r')
#document = open('day4/input_alex.txt', 'r')
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
        

winners = []
gottens = []
matches = []
scores = []
for line in lines:
    groups = re.split('[:|]', line)
    line_winners = [int(x) for x in re.findall("\d+", groups[1])]
    line_gottens = [int(x) for x in re.findall("\d+", groups[2])]
    winners.append(line_winners)
    gottens.append(line_gottens)
    matched = match_winners(line_winners, line_gottens)
    matches.append(matched)
    scores.append(score_matches(matched))


print(sum(scores))

    

