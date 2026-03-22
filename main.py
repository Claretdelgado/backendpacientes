from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router

app = FastAPI(title="API Gestión de Pacientes")

# configuración de CORS para permitir solicitudes desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# se incluyen las rutas en app/routes.py
app.include_router(router, prefix="/api")
# para ruta raíz para verificar que la API está funcionando
@app.get("/")
def root():
    return {"mensaje": "API Gestión de Pacientes funcionando"}