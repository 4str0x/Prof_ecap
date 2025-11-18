from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from config.database import init_db
from config.routes import router
from config.config import settings

app = FastAPI(title="Api - Netescola")

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")  # type: ignore
async def startup_event():
    await init_db()

# Rota para GET e HEAD
@app.api_route("/", methods=["GET", "HEAD"])
async def root():
    return JSONResponse(content={"status": "OK"}, status_code=200)


# Inclusão do roteador
app.include_router(router, prefix="")

# Inicialização do servidor com Uvicorn
if __name__ == "__main__":
    import uvicorn
    
    if settings.DEV_MODE:
        uvicorn.run("main:app" , host=settings.HOST, port=settings.PORT, reload=True)
    
    uvicorn.run("main:app" , host=settings.HOST, port=settings.PORT)