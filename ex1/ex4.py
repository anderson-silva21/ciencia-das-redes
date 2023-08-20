import networkx as nx

G = nx.read_gml("createGraph.gml")

# Adicione o atributo "Country" aos nós
country_mapping = {
    "Albuquerque": "EUA",
    "Atlanta": "EUA",
    "Chicago": "EUA",
    "New York": "EUA",
    "Pinhais": "Brasil",
    "Curitiba": "Brasil",
    "Miami": "EUA",
    "Sao Paulo": "Brasil",
    "Londrina": "Brasil",
    "Foz": "Brasil",
    "Maringa": "Brasil",
    "Cleveland": "EUA",
    "Denver": "EUA",
    "Philadelphia": "EUA",
    "Minneapolis": "EUA",
    "Phoenix": "EUA",
    "Ponta Grossa": "Brasil",
    "Boston": "EUA",
    "Tulsa": "EUA",
}
nx.set_node_attributes(G, country_mapping, "Country")

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

# Exporte a rede final no formato .GML
nx.write_gml(G, "finalGraph.gml")
