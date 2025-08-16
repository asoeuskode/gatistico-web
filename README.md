# Presentación
Gatístico es una plataforma integral diseñada para la gestión de socios y actividades de asociaciones felinas.
El proyecto combina una aplicación web, una API y una aplicación móvil, ofreciendo una solución completa y accesible tanto para administradores como para socios.

Con una interfaz intuitiva en la web y en la app móvil, y una API robusta que sirve de base para la integración, Gatístico busca modernizar y simplificar la gestión de comunidades felinas.

# Objetivos

## Gestión de socios

Permitir registrar, modificar y eliminar información de los socios.
Asignar cada socio a una asociación específica.
Garantizar el almacenamiento seguro de datos personales y contraseñas.

## Gestión de asociaciones

Registrar y administrar asociaciones felinas.
Permitir a los administradores visualizar y gestionar sus socios.

## Aplicación web

Proporcionar un panel de administración accesible desde navegador.
Facilitar la consulta rápida de socios y asociaciones.
Ofrecer estadísticas y reportes básicos.

## API

Proveer endpoints seguros para la comunicación entre sistemas.
Servir como base para la aplicación móvil y posibles integraciones futuras.

## Aplicación móvil

Permitir a los socios registrarse y actualizar sus datos desde el móvil.
Consultar información de asociaciones y actividades en tiempo real.
Notificar a los usuarios sobre eventos o actualizaciones.

## Seguridad y usabilidad

Implementar encriptación de contraseñas y buenas prácticas de autenticación.
Diseñar interfaces intuitivas para usuarios técnicos y no técnicos.

## Escalabilidad futura

Dejar la arquitectura lista para integrar nuevas funcionalidades (eventos, donaciones, gestión de adopciones).
Facilitar la interoperabilidad con otras plataformas mediante la API.

# Alcance inicial

## Gestion de asociaciones

- Crear y administrar asociaciones.
- Visualizar Asociaciones registradas.
- Tener panel de Asociación.

## Gestion de socios

- Registro basico de socios.
- Listar asociados a cada asociación.
- Editar y eliminar socios.
- Tener tipos de socios

## Gestion de animales

- Registrar basico de animales.
- Editar y eliminar animal.
- Asignar animal a socio.
- Listar animales registrados.
- Listar animales asignado a cada socio.

## Gestion de refugios o casa de acogida

- Asignar animales a refugio.
- Asignar tareas de refugio.
- Asignar socio de refugio.

## Aplicacion web

- Panel de administacion
- Login

## Aplicacion mobile

- Login
- Visualizacion de asociacion a la que pertenece
- Visualizacion de mascotas a su cargo
- Visualizacion y check de tareas
- Actualizacion de datos de socio

# Alcance futuro

## Eventos de asociaciones
## Display de estadisticas de asociacion

# Tecnologias a utilizar

- Lenguaje: Python - se hara debido a la robustes del lenguaje, la facilidad de añadir nuevas herramientas y la comodidad de encontrar gente que lo puedas aprender. Ademas de la buena perspectiva de futuro del mismo lenguaje.
- Framework: FastApi, Android Nativo.
- DDBB: SQLite - Debido a que no se espera que las asociaciones cuenten con programadores y una una bbdd liviana y facil de configurar.
-  