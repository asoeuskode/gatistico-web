from pydantic import BaseModel

class SocioCreate(BaseModel):
    email: str
    nombre: str = None
    apellidos: str = None
    alias: str = None
    telefono: str = None
    password: str
    asociacion_id: int

class SocioRead(BaseModel):
    id: int
    email: str
    nombre: str
    apellidos: str
    alias: str
    telefono: str
    fecha_creacion: str
    fecha_modificacion: str
    asociacion_id: int