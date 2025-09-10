from fastapi import FastAPI
from app.api.v1 import routes


app = FastAPI(title="Task Tracker API")


app.include_router(routes.router, prefix="/api/v1")


@app.get("/healthz")
async def healthz():
return {"status": "ok"}