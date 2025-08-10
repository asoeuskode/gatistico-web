from sections.socio.infra.socioRepo import SocioRepo

class SocioApp:
    """
    SocioApp is a FastAPI application that provides endpoints for managing socios.
    It includes routes for creating and listing socios.
    """

    def __init__(self):
        self.socio_repo = SocioRepo()

    def insertar_socio(self, nombre: str, apellidos: str, alias: str, password_cifrada: str):

        self.socio_repo.insertar_socio(nombre, apellidos, alias, password_cifrada)


    def listar_socios(self):
        self.socio_repo.listar_socios()