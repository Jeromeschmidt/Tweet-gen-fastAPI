from fastapi import FastAPI

from core.routes.tweets import router as TweetRouter

app = FastAPI()

app.include_router(TweetRouter, tags=["Tweet"], prefix="/tweets")

@app.get("/", tags=["Root"])
async def read_root():
    return {"msg": "Hello World"}
