import networkx as nx

G = nx.read_gml("createGraph.gml")

# Coeficiente de clusterização de um nó específico (Curitiba)
curitiba_clustering = nx.clustering(G, "Curitiba")
print(f"Coeficiente de clusterização de Curitiba: {curitiba_clustering}")

# Coeficiente de clusterização da rede geral
network_clustering = nx.average_clustering(G)
print(f"Coeficiente de clusterização da rede geral: {network_clustering}")
