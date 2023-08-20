import networkx as nx

G = nx.read_gml("createGraph.gml")

def max_hops_between_cities(graph, source_city, target_city):
    distances = nx.shortest_path_length(graph, source=source_city, target=target_city)
    if distances:
        return distances[target_city]
    else:
        return None

source_city = "Albuquerque"  # partida
target_city = "Sao Paulo"    # destino

max_hops = max_hops_between_cities(G, source_city, target_city)
if max_hops is not None:
    print(f"Número máximo de saltos entre {source_city} e {target_city}: {max_hops}")
else:
    print(f"Não há conexão direta entre {source_city} e {target_city}.")
