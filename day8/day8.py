import re
import math

def lcm(a, b):
  return abs(a*b) // math.gcd(a, b)

def parseInput(fname):
  path = []
  graph = {}
  with open(fname, 'r') as f:
    lines = f.readlines()
    # convert L/R to 0/1 index
    path = [0 if x == 'L' else 1 for x in lines[0][:-1]]
    # build the graph as a dict of tuples
    for line in lines[2:]:
      node, lnode, rnode = [x for x in re.split('\s|=|,|\(|\)', line) if x]
      graph[node] = (lnode, rnode)
  return path, graph

def repeat(xs):
  while True:
    for x in xs:
      yield x

def walkPath(directions, graph, start='AAA', dest_str_re='..Z'):
  dest_re = re.compile(dest_str_re)
  walkedPath = [start]
  for direction in repeat(directions):
    walkedPath.append(graph[walkedPath[-1]][direction])
    if dest_re.match(walkedPath[-1]):
      return walkedPath

def walkPaths(directions, graph, start_re='..A', dest_str_re='..Z'):
  starts = [x for x in graph.keys() if re.match(start_re, x)]
  walkedPaths = []
  for start in starts:
    walkedPaths.append(walkPath(directions, graph, start, dest_str_re))
  return walkedPaths

def countSteps(directions, graph, start_str_re='..A', dest_str_re='..Z'):
  walkedPaths = walkPaths(directions, graph, start_str_re, dest_str_re)
  return math.lcm(*map(lambda x: len(x)-1, walkedPaths))

if __name__ == "__main__":
  #path, graph = parseInput("test_input")
  path, graph = parseInput("input")
  walkedPath = walkPath(path, graph)
  print(f'part1, number of steps taken: {len(walkedPath)-1}')
  #walkedPaths = walkPaths(path, graph)
  #print(*walkedPaths, sep='\n')
  #count = len(walkedPaths[0])-1
  count = countSteps(path, graph)
  print(f'part2, number of steps taken: {count}')
