# Agenda Básica con Flask
## Se trata de un proyecto realizado por Vicente Igarza
Agenda básica usando Python-Flask; contiene logueo y funciones como edición y borrado de contacto.

La app conecta a una base de datos
![Vista BD](https://github.com/IgnacioIgarza/agenda-basica-flask/blob/main/static/img/vistaBD.bmp)

## Tiene registro y autenticación
![Vista autenticación](https://github.com/IgnacioIgarza/agenda-basica-flask/blob/main/static/img/pantallaAutenticacion.bmp)
![Vista registro](https://github.com/IgnacioIgarza/agenda-basica-flask/blob/main/static/img/pantallaRegistro.bmp)

## Tiene un perfil de Administrador que le permite:
- cear nuevos contactos, editarlos o borrarlos,
- buscar usuarios,
- ver todos los usuarios y editar su contraseña o borrarlo (excepto el usuario admin) y
- ver todos los contactos.
- (ver nota al final del ReadMe)
![Vista Admin](https://github.com/IgnacioIgarza/agenda-basica-flask/blob/main/static/img/pantallaAdmin.bmp)

## Tiene un perfil de Usuario Común que le permite:
- ver sus propios contactos,
- editarlos o borrarlos.
![Vista Usuario](https://github.com/IgnacioIgarza/agenda-basica-flask/blob/main/static/img/pantallaUsuario.bmp)

## Para iniciar 
### Activar la base de datos que debe tener la sig. estructura:
### root, con contraseña "" (un string vacío)
### base de datos llamada flask_contacto
### la base de datos tiene 2 tablas:
- usuarios con las columnas id, usuario y contraseña (ver nota al final del ReadMe)
- contactos con las columnas id, nombre, apellido, fecha_nacimiento, telefono, email, usuario_id


### luego desde la consola inicie la aplición:
``` bash
python app.py
```
En un navegador inicie la app en:
localhost:5000/


- nota: el usuario admin es un usuario especial que accede a un menú específico, como se explica arriba. Además no se puede borrar, pero es importante que en el códico, lo que permite no borrarlo es su id (en el caso del que se realizó inicialmente, el id 7 es el del admin, y no se puede borrar)
