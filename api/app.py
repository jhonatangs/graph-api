from fastapi import FastAPI

from database.database import init_db
from routes.graph_routes import router as GraphRouter


app = FastAPI()


@app.on_event("startup")
async def start_db():
    await init_db()


@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to Graph API."}


app.include_router(GraphRouter, tags=["Graph"])
