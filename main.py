from subprocess import Popen, PIPE
from pprint import pprint


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
        graph += "\"{}\" -> \"{}\" [label=\"{}\"];".format(
            item, link[0], link[1])
    graph += "}"

    dot.communicate(graph.encode("utf8"))


drawn = {}
count = 4
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
    g.add_link(a, (sum, "+" + str(b)))

g.draw()

alphabet = "abcdefghijklmnopqrstuvwxyz"
commands = [
    "create message", "send_message_to_follower", "mute", "follow",
    "add_to_timeline", "unfollow", "like", "fanout", "unlike", "share",
    "stream", "upload", "fanout", "fanout", "fanout", "fanout", "fanout",
    "fanout", "fanout", "fanout", "fanout", "fanout", "fanout", "fanout",
    "fanout", "fanout", "fanout"
]
# how do you map addition to IO?
# need to get data to the right places in the most efficient way
inboxes = {}
for item in range(0, len(commands)):
  inboxes[item] = []
start = 0
event = 0
sequence = [0, 3, -3, 3, 2]


def run(event):
  for number in sequence:

    new_event = event + number
    print(new_event)
    print("{} {} -> {} {}".format(event, commands[event], new_event,
                                  commands[new_event]))
    inboxes[new_event].append(event)
    output = start
    coutput = start
    a = min(event, new_event)
    b = max(event, new_event)
    for intermediary in range(a, b):
      print("{} {} -> {} {}".format(new_event, commands[new_event],
                                    intermediary, commands[intermediary]))
      output = "{}({})".format(alphabet[intermediary], output)
      coutput = "{}({})".format(commands[intermediary], coutput)
    print(output)
    print(coutput)
    event = new_event


run(event)

pprint(inboxes)

# import itertools

# user_size = 20
# users = list(range(0, user_size))
# permutations = list(itertools.product([0, 1], repeat=user_size))
# print(len(permutations))
# print(permutations)

# import itertools
# print(list(itertools.product(["A", "B", "C"], repeat=3)))
