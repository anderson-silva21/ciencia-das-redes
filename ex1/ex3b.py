import networkx as nx

G = nx.read_gml("createGraph.gml")

# Adicione o atributo "Cost" às arestas
for edge in G.edges():
    source = edge[0]
    target = edge[1]
    
    source_country = G.nodes[source]["Country"]
    target_country = G.nodes[target]["Country"]
    
    if source_country != target_country:
        cost = 5  # Voo internacional
    else:
        cost = 1  # Voo nacional
    
    G.edges[source, target]["Cost"] = cost

# Exemplo de acesso ao atributo "Cost" de uma aresta (por exemplo, entre "Albuquerque" e "Atlanta")
cost_albuquerque_to_atlanta = G.edges["Albuquerque", "Atlanta"]["Cost"]
print(f"Custo entre Albuquerque e Atlanta: {cost_albuquerque_to_atlanta}")
