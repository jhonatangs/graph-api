from typing import List

from pydantic import BaseModel


class EdgeAux(BaseModel):
    source: str
    target: str
    distance: int


class GraphIn(BaseModel):
    data: List[EdgeAux]


class GraphOut(BaseModel):
    _id: str
    data: List[EdgeAux]


class RouteAux(BaseModel):
    route: str
    stops: int


class RouteOut(BaseModel):
    routes: List[RouteAux]


class DistanceOut(BaseModel):
    distance: int
    path: List[str]
