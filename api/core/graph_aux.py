import networkx as nx


def graph_model_to_networkx(graph_model):
    g = nx.DiGraph()

    for edge in graph_model.data:
        g.add_edge(edge.source, edge.target, weight=edge.distance)

    return g
