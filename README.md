# Agenda Básica con Flask
## Se trata de un proyecto realizado por Vicente Igarza
Agenda básica usando Python-Flask; contiene logueo y funciones como edición y borrado de contacto.

La app conecta a una base de datos
![Vista BD](https://github.com/IgnacioIgarza/agenda-basica-flask/blob/main/static/img/vistaBD.bmp)

## Tiene registro y autenticación
![Vista autenticación](https://github.com/IgnacioIgarza/agenda-basica-flask/blob/main/static/img/pantallaAutenticacion.bmp)
![Vista registro](https://github.com/IgnacioIgarza/agenda-basica-flask/blob/main/static/img/pantallaRegistro.bmp)

## Tiene un perfil de Administrador que le permite:
cear nuevos contactos, editarlos o borrarlos,
ver los usuarios y editar su contraseña,
y ver todos los contantos.
![Vista Admin](https://github.com/IgnacioIgarza/agenda-basica-flask/blob/main/static/img/pantallaAdmin.bmp)
## Tiene un perfil de usuario común que le permite:
ver sus propios contactos,
editarlos o borrarlos.
![Vista Usuario](https://github.com/IgnacioIgarza/agenda-basica-flask/blob/main/static/img/pantallaUsuario.bmp)

## Para iniciar 
Activar la base de datos que debe tener la sig. estructura:
...
luego desde la consola inicie la aplición:
``` bash
python app.py
```
En un navegador inicie la app en 
localhost:5000/
