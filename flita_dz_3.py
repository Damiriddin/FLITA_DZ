import networkx as nx
import matplotlib.pyplot as plt


with open(r"C:\Users\Дамириддин\Desktop\ФЛиТА\dz_flita\DZ_2\graphs\outputs\adjacency_matrix_0.txt") as file:
    data = file.read().strip()
    s = []

    for line in data.split('\n'):
        lst = []
        for dig in line.strip().split(' '):
            lst.append(int(dig))
        s.append(lst)

print(s)

G = nx.Graph()

n = len(s)

for i in range(n):
    G.add_node(i)

for i in range(n):
    for j in range(n):
        if s[i][j] >= 1:
            G.add_edge(i, j)

print(G)

if len(G.edges) > (len(G.nodes)-1)*(len(G.nodes)-2)*0.5:
    print("связный")
else:
    print("несвязный")

nx.draw(G, with_labels=True)
plt.show()

