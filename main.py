from fastapi import FastAPI
from api.maintenance import router
from api.evaluation import router as evaluation_router

app = FastAPI()
app.include_router(router, prefix="/api/v1")
app.include_router(evaluation_router, prefix="/api/v1")
