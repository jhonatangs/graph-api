from beanie import Document


class Edge(Document):
    source: str
    target: str
    distance: int
