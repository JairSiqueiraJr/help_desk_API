from fastapi import FastAPI
from app.routers import analytics, chamados

app = FastAPI(title="HelpDesk Analytics API")

app.include_router(analytics.router)
app.include_router(chamados.router)

@app.get("/")
def root():
    return {"message": "API rodando"}