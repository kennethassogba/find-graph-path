import networkx as netx
import matplotlib.pyplot as plt

"""
Draw our Cleaning.graph
We illustrate with Case_Aspi_R_2.txt
"""
# Without wall
"""
graph = {0: [-1, 4, 1, -1], 1: [0, 5, 2, -1], 2: [1, 6, 3, -1], 3: [2, 7, -1, -1], 4: [-1, 8, 5, 0], 5: [4, 9, 6, 1], 6: [5, 10, 7, 2], 7: [6, 11, -1, 3],
         8: [-1, 12, 9, 4], 9: [8, 13, 10, 5], 10: [9, 14, 11, 6], 11: [10, 15, -1, 7], 12: [-1, -1, 13, 8], 13: [12, -1, 14, 9], 14: [13, -1, 15, 10], 15: [14, -1, -1, 11]}
"""
# With murs
"""
graph = {0: [-1, 4, 1, -1], 1: [0, 5, 2, -1], 2: [1, 6, 3, -1], 3: [2, 7, -1, -1], 4: [-1, -1, 5, 0], 5: [4, -1, -1, 1], 6: [-1, 10, 7, 2], 7: [6, 11, -1, 3],
         8: [-1, 12, 9, -1], 9: [8, 13, -1, -1], 10: [-1, 14, 11, 6], 11: [10, 15, -1, 7], 12: [-1, -1, 13, 8], 13: [12, -1, 14, 9], 14: [13, -1, 15, 10], 15: [14, -1, -1, 11]}
"""
# With robots
graph = {0: [-1, 4, 1, -1], 1: [-1, 5, 2, -1], 2: [1, 6, 3, -1], 3: [2, 7, -1, -1], 4: [-1, -1, 5, -1], 5: [4, -1, -1, 1], 6: [-1, 10, 7, 2], 7: [6, 11, -1, 3],
         8: [-1, -1, 9, -1], 9: [8, 13, -1, -1], 10: [-1, 14, 11, 6], 11: [10, 15, -1, 7], 12: [-1, -1, 13, 8], 13: [-1, -1, 14, 9], 14: [13, -1, 15, 10], 15: [14, 11]}

robots = {'B': 0, 'R': 12}
val_map = {r: 'r' for r in list(robots.values())}
# val_map is used to change node colors.
# we set robot's positions to red

# Remove -1 value in the dict
for key in graph:
    val = graph[key]
    todel = val.count(-1)
    for i in range(todel):
        val.remove(-1)


nx = 4
ny = 4  # TODO:  use main.formatForClean()

# set node coordinates to have good visualisation
vertexPosition = {i: [] for i in range(nx*ny)}
for i in range(nx):
    for j in range(ny):
        vertex = i*ny+j
        tab = [j, -i]
        vertexPosition[vertex] = tab


G = netx.DiGraph(graph)  # Directed (Oriented) graph

# set color=blue if no robot at this node
color_values = [val_map.get(node, 'b') for node in G.nodes()]
# Draw
netx.draw_networkx(G, pos=vertexPosition, node_color=color_values, with_labels=True)
plt.savefig("C2.png")  # save as png
plt.show()

# Clean Boxes
cleanedBoxes = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
# We want to create animation to visualise the cleaning steps of the room but have no enough time to develop that
