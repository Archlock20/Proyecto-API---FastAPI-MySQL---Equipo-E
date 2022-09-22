from fastapi import FastAPI
from routes.user import user

app = FastAPI(
    openapi_tags=[{
        "name": "users",
        "description": "Rutas para la API de estudiantes"
    }]
)

app.include_router(user)
