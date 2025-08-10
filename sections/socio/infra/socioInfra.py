from fastapi import APIRouter, HTTPException, status, Depends
import bcrypt
from sections.socio.application.socioApp import SocioApp
from sections.socio.model.socio import SocioCreate, SocioRead

socio_router = APIRouter()

class SocioAppDependency:
    def __init__(self):
        self.socio_app = SocioApp()

    def __call__(self):
        return self.socio_app

socio_app_dependency = SocioAppDependency()

@socio_router.post("/", status_code=status.HTTP_201_CREATED)
async def crear_socio(socio: SocioCreate, socio_app: SocioApp = Depends(socio_app_dependency)):
    password_cifrada = bcrypt.hashpw(socio.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    print(f"Password cifrada: {password_cifrada}")

    
    return socio_app.insertar_socio(socio.nombre, socio.apellidos, socio.alias, password_cifrada)


@socio_router.get("/", response_model=list[SocioRead])
async def listar_socios(socio_app: SocioApp = Depends(socio_app_dependency)):
    return socio_app.listar_socios()
