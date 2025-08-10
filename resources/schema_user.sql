CREATE TABLE socios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE,
    nombre TEXT,
    apellidos TEXT,
    alias TEXT,
    telefono TEXT,
    fecha_creacion TEXT NOT NULL DEFAULT (datetime('now')),
    fecha_modificacion TEXT NOT NULL DEFAULT (datetime('now')),
    password TEXT NOT NULL,
    asociacion_id INTEGER NOT NULL,
    FOREIGN KEY (asociacion_id) REFERENCES asociaciones(id)
);