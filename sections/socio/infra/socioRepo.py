import sqlite3
from fastapi import HTTPException


class SocioRepo:
    def __init__(self):
        pass

    def get_db_connection(self):
        conn = sqlite3.connect("resources/gatistico.db")
        conn.row_factory = sqlite3.Row
        return conn

    def insertar_socio(self, email, nombre, apellidos, alias, telefono, password_cifrada, asociacion_id) -> dict:
        #make connection to the database
        conn = self.get_db_connection()


        cursor = conn.cursor()
        try:
            cursor.execute(
            """
            INSERT INTO socios (email, nombre, apellidos, alias, telefono, password, asociacion_id)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (email, nombre, apellidos, alias, telefono, password_cifrada, asociacion_id)
            )
            conn.commit()
        except sqlite3.IntegrityError as e:
            conn.close()
            raise HTTPException(status_code=400, detail=f"Error al insertar socio: {e}")
        
        conn.close()
        return {"message": "Socio creado exitosamente", "alias": alias}


    def listar_socios(self) -> dict:
        """
        Lista todos los socios registrados.
        Nota: no se retorna la contraseña.
        """
        conn = self.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, email, nombre, apellidos, alias, telefono, fecha_creacion, fecha_modificacion, asociacion_id FROM socios")
        socios = cursor.fetchall()
        conn.close()
        return list(socios)

    def asociacion_existe(self, asociacion_id: int) -> bool:
        """
        Verifica si una asociación existe en la base de datos.
        """
        conn = self.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM asociaciones WHERE id = ?", (asociacion_id,))
        existe = cursor.fetchone()[0] > 0
        conn.close()
        return existe
    
    def email_existe(self, email: str) -> bool:
        """
        Verifica si un email ya está registrado en la base de datos.
        """
        conn = self.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM socios WHERE email = ?", (email,))
        existe = cursor.fetchone() is not None
        conn.close()
        return existe