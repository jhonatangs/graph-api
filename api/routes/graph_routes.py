from typing import Optional
from collections import defaultdict

from fastapi import APIRouter, Response, status
from beanie import PydanticObjectId

from models.graph import Graph
from core.core import (
    add_graph,
    get_graph,
    get_all_paths,
    get_shortest_path,
)
from serializers import GraphOut, DistanceOut, RouteOut

router = APIRouter()


@router.post("/graph", response_model=GraphOut)
async def create_graph(graph_in: Graph, response: Response):
    response.status_code = status.HTTP_201_CREATED
    graph_out = await add_graph(graph_in)
    return graph_out


@router.get("/graph/{graph_id}", response_model=GraphOut)
async def read_graph(graph_id: PydanticObjectId, response: Response):
    graph = await get_graph(graph_id)
    if graph:
        response.status_code = status.HTTP_200_OK
        return graph
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {
            "status_code": 404,
            "response_type": "error",
            "description": "Graph not found",
        }


@router.get(
    "/routes/{graph_id}/from/{town1}/to/{town2}",
    response_model=RouteOut,
)
async def get_all_routes(
    graph_id: PydanticObjectId,
    town1: str,
    town2: str,
    response: Response,
    max_stops: Optional[int] = None,
):
    graph = await get_graph(graph_id)

    if graph:
        routes_aux = get_all_paths(graph, town1, town2, max_stops)
        if routes_aux:
            routes_ans = defaultdict(list)

            for route in routes_aux:
                routes_ans["routes"].append(
                    {"route": "".join(route), "stops": len(route) - 1}
                )

            response.status_code = status.HTTP_200_OK
            return routes_ans

        else:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {
                "status_code": 404,
                "response_type": "error",
                "description": "Routes not found",
            }
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {
            "status_code": 404,
            "response_type": "error",
            "description": "Graph not found",
        }


@router.get(
    "/distance/{graph_id}/from/{town1}/to/{town2}", response_model=DistanceOut
)
async def get_distance(
    graph_id: PydanticObjectId, town1: str, town2: str, response: Response
):
    graph = await get_graph(graph_id)

    if graph:
        distance, path = get_shortest_path(graph, town1, town2)

        if path:
            response.status_code = status.HTTP_200_OK
            return {
                "distance": distance,
                "path": path,
            }
        else:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {
                "status_code": 404,
                "response_type": "error",
                "description": "Routes not found",
            }
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {
            "status_code": 404,
            "response_type": "error",
            "description": "Graph not found",
        }
