import networkx as NX
import csv
import matplotlib.pyplot as plt
from networkx.algorithms.community.centrality import girvan_newman
import numpy as np

filename = './watermargin.csv'
characters=[]
color_map = []
with open(filename) as f:
    reader = csv.reader(f)
    head_row = next(reader)
    for row in reader:
        characters.append(row[0])
g = NX.Graph()
for character in characters:
    g.add_node(character)


with open(filename) as f:
    reader = csv.reader(f)
    head_row = next(reader)
    for row in reader:
        for friend in row:
            if friend != row[0]:
                g.add_edge(row[0], friend)


d = dict(g.degree)

print([node for (node, val) in sorted(g.degree(), key=lambda pair: pair[1])])
print([val for (node, val) in sorted(g.degree(), key=lambda pair: pair[1])])

b = NX.betweenness_centrality(g, normalized=True)
print(b)
print(sorted(b.items(), key = lambda kv:(kv[1], kv[0])))

e = NX.eigenvector_centrality(g)
print(e)
print(sorted(e.items(), key = lambda kv:(kv[1], kv[0])))

node_groups = []
comm = girvan_newman(g)
for com in next(comm):
  node_groups.append(list(com))


print(node_groups)
color_map = []
print(len(node_groups[0]))
print(len(node_groups[1]))
print(len(node_groups[2]))
print(len(node_groups[3]))
print(len(node_groups[4]))

for node in g:
    if node in node_groups[0]:
        color_map.append('blue')
    elif node in node_groups[1]:
        color_map.append('red')
    elif node in node_groups[2]:
        color_map.append('yellow')
    elif node in node_groups[3]:
        color_map.append('grey')
    else:
        color_map.append('green')
NX.draw(g, node_color=color_map, node_size=[v * 10 for v in d.values()])
plt.show()


#
# NX.draw(g, nodelist=d.keys(), node_size=[v * 10 for v in d.values()])
# plt.show()

