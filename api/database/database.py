from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from config import settings
from models.edge import Edge
from models.graph import Graph


async def init_db():
    client = AsyncIOMotorClient(settings.database.url)

    await init_beanie(database=client.graph_db, document_models=[Edge, Graph])
