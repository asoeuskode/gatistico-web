from fastapi import HTTPException, status
from sections.socio.infra.socioRepo import SocioRepo
import bcrypt

from sections.socio.model.socio import SocioCreate


class SocioApp:
    """
    SocioApp is a FastAPI application that provides endpoints for managing socios.
    It includes routes for creating and listing socios.
    """

    def __init__(self):
        self.socio_repo = SocioRepo()

    def insertar_socio(self, socio: SocioCreate):

        try:
            self.validar_socio(socio)
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        
        try:
            socio.password = bcrypt.hashpw(socio.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al cifrar la contraseña.")

        return self.socio_repo.insertar_socio(socio)

    def validar_socio(self, socio: SocioCreate):
        
        # Validar que el alias no esté vacío
        if not socio.alias:
            raise ValueError("El alias no puede estar vacío.")

        # Validar que la contraseña tenga al menos 8 caracteres
        if len(socio.password) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres.")
        # Validar que el nombre y apellidos no estén vacíos
        if not socio.nombre or not socio.apellidos:
            raise ValueError("El nombre y los apellidos no pueden estar vacíos.")
        # Validar que el nombre y apellidos no contengan caracteres especiales
        if not socio.nombre.isalnum() or not socio.apellidos.isalnum():
            raise ValueError("El nombre y los apellidos solo pueden contener letras y números.")
        # Validar que el alias no contenga caracteres especiales
        if not socio.alias.isalnum():
            raise ValueError("El alias solo puede contener letras y números.")
        # Validar que la contraseña no contenga caracteres especiales
        if not socio.password.isalnum():
            raise ValueError("La contraseña solo puede contener letras y números.")
        # Validar que el teléfono sea un número válido
        if socio.telefono and not socio.telefono.isdigit():
            raise ValueError("El teléfono debe ser un número válido.")
        # Validar que el email no esté vacío
        if not socio.email:
            raise ValueError("El email no puede estar vacío.")
        # Validar que el email tenga un formato válido
        if not isinstance(socio.email, str) or "@" not in socio.email:
            raise ValueError("El email debe tener un formato válido.")
        # Validar que el ID de la asociación sea un número entero positivo
        if not isinstance(socio.asociacion_id, int) or socio.asociacion_id <= 0:
            raise ValueError("El ID de la asociación debe ser un número entero positivo.")
        
        # Validar que el ID de la asociación exista en la base de datos
        if not self.socio_repo.asociacion_existe(socio.asociacion_id):
            raise ValueError("El ID de la asociación no existe.")
        # Validar que el email no esté ya registrado
        if self.socio_repo.email_existe(socio.email):
            raise ValueError("El email ya está registrado.")
        

        


    def listar_socios(self):
        return self.socio_repo.listar_socios()