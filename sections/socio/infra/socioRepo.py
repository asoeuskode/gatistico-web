import sqlite3
from fastapi import HTTPException


class SocioRepo:
    def __init__(self):
        pass

    def get_db_connection():
        conn = sqlite3.connect("gatistico.db")
        conn.row_factory = sqlite3.Row
        return conn

    def insertar_socio(self, nombre, apellidos, alias, password_cifrada) -> dict:
        #make connection to the database
        conn = self.get_db_connection()


        cursor = conn.cursor()
        try:
            cursor.execute(
                """
                INSERT INTO socios (nombre, apellidos, alias, password)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (nombre, apellidos, alias, password_cifrada)
            )
            conn.commit()
        except sqlite3.IntegrityError as e:
            conn.close()
            raise HTTPException(status_code=400, detail=f"Error al insertar socio: {e}")
        
        conn.close()
        return {"message": "Socio creado exitosamente", "alias": alias}


    def listar_socios(self) -> list:
        """
        Lista todos los socios registrados.
        Nota: no se retorna la contraseña.
        """
        conn = self.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, apellidos, alias, fecha_creacion, fecha_modificacion FROM socios")
        socios = cursor.fetchall()
        conn.close()
        return {"socios": [dict(socio) for socio in socios]}

