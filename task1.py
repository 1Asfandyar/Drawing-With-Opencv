import networkx as nx
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

graph = {}

m = int(input("Enter number of vertices : "))
if m is None:
    print('Nothing Entered')
    exit(1)

values = []
print()
for x in range(0, m):
    # iterating till the range
    print()
    n = int(input(f"Enter number of elements of vector {x + 1}: "))
    print()
    lst = []
    for i in range(0, n):
        ele = int(input(f'Enter adjacent point {i + 1} for vector {x + 1}: '))
        lst.append(ele)  # adding the element
    values.append(lst)

print(values)
for x in range(1, m):
    graph[x + 1] = values[x]

print('Graph is: ', graph)



# compute Voronoi tesselation
vor = Voronoi(values)

# plot
voronoi_plot_2d(vor)

# colorize
for region in vor.regions:
    if not -1 in region:
        polygon = [vor.vertices[i] for i in region]
        plt.fill(*zip(*polygon))

# fix the range of axes
plt.xlim([0,1]), plt.ylim([0,1])

plt.show()


def main(G):
    fig = plt.figure()
    fig.show()

    graph = nx.DiGraph()

    for v in G.keys():
        graph.add_node(v)

    for delta in G.items():
        for w in delta[1]:
            graph.add_edge(delta[0], w)

    # posit = nx.shell_layout(G) #ISN'T NEEDED ANYMORE

    nx.draw_planar(graph, with_labels=True, alpha=0.8)  # NEW FUNCTION
    fig.canvas.draw()
    plt.show()


main(graph)

# graph-- = {
# '1': ['2','4'],
# '2': ['1','3','5'],
# '3': ['2','6'],
# '4': ['1','5','7'],
# '5': ['4','2', '6'],
# '6': ['5','3'],
# '7': ['4','8'],
# '8': ['7','5','9'],
# '9': ['8','6']
# }