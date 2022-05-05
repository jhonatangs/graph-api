from typing import List, Optional, Tuple

import networkx as nx
from beanie import PydanticObjectId

from core.graph_aux import graph_model_to_networkx
from models.graph import Graph

graph_collection = Graph


async def add_graph(new_graph: Graph) -> Graph:
    graph = await new_graph.create()
    return graph


async def get_graph(id: PydanticObjectId) -> Graph:
    graph = await graph_collection.get(id)

    if graph:
        return graph


def get_all_paths(
    graph: Graph, s: str, d: str, max_stops: Optional[int] = None
) -> List[List[str]]:
    g = graph_model_to_networkx(graph)

    if max_stops:
        return nx.all_simple_paths(g, source=s, target=d, cutoff=max_stops)
    else:
        return nx.all_simple_paths(g, source=s, target=d)


def get_shortest_path(graph: Graph, s: str, d: str) -> Tuple[int, List[str]]:
    g = graph_model_to_networkx(graph)
    return nx.dijkstra_path_length(g, source=s, target=d), nx.dijkstra_path(
        g, source=s, target=d
    )
