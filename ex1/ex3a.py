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

# Exemplo de acesso ao atributo "Country" de um nó (por exemplo, "Curitiba")
curitiba_country = G.nodes["Curitiba"]["Country"]
print(f"País onde Curitiba está localizada: {curitiba_country}")
