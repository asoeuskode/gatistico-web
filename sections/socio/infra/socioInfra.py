from fastapi import APIRouter, status, Depends
from sections.socio.application.socioApp import SocioApp
from sections.socio.model.socio import SocioCreate, SocioRead

socio_router = APIRouter()
socio_app = SocioApp()

def get_socio_app() -> SocioApp:
    return socio_app


@socio_router.post("/", status_code=status.HTTP_201_CREATED)
async def crear_socio(socio: SocioCreate, socio_app: SocioApp = Depends(get_socio_app)):
    return socio_app.insertar_socio(socio)


@socio_router.get("/", response_model=list[SocioRead])
async def listar_socios(socio_app: SocioApp = Depends(get_socio_app)):
    return socio_app.listar_socios()
