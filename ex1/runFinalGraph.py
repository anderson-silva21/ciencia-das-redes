import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_gml("finalGraph.gml")

pos = nx.spring_layout(G)  # Define a posição dos nós para uma melhor visualização
nx.draw(G, pos, with_labels=True, node_size=500, font_size=10, font_color="black")
edge_labels = nx.get_edge_attributes(G, "Cost")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()