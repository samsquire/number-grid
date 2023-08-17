from subprocess import Popen, PIPE


class Graph:

  def __init__(self, name):
    self.name = name
    self.adjacency = {}

  def add_link(self, left, right):
    if left not in self.adjacency:
      self.adjacency[left] = []
    if right not in self.adjacency:
      self.adjacency[right] = []
    self.adjacency[left].append(right)

  def draw(self):
    dot = Popen(["dot", "-Tpng", "-o", "graphs/{}.png".format(self.name)],
                stdin=PIPE,
                stdout=PIPE)
    graph = "digraph G {"
    for item, value in self.adjacency.items():
      for link in value:
        graph += "\"{}\" -> \"{}\" [label=\"{}\"];".format(item, link[0], link[1])
    graph += "}"

    dot.communicate(graph.encode("utf8"))

drawn = {}
count = 5
g = Graph("numbers")
for a in range(0, count):
  for b in range(0, count):
    if b == a:
      continue
    
    if a not in drawn:
      drawn[a] = []
    if b in drawn[a]:
      continue
    drawn[a].append(b)
    # diff = a - b
    #g.add_link(a, (b, str(diff)))
    sum = a + b
    g.add_link(a, (sum, "+"+str(b)))

g.draw()
  