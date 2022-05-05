from typing import List

from beanie import Document

from models.edge import Edge


class Graph(Document):
    data: List[Edge]
