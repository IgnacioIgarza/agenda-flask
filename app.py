"""
Ejercicio: Aplicación Web de Agenda de Contactos con Flask 
1. Objetivo 
Desarrollar una aplicación web completa utilizando el microframework Flask (Python) que permita la autenticación de usuarios y la gestión de una agenda de contactos personal. La aplicación debe correr en el entorno local ( 127.0.0.1:5000 ). 
2. Condiciones Generales 
Modalidad: Trabajo individual. 
Evaluación: No se valorará la estética visual (CSS, colores, ni maquetación avanzada). La nota se centrará exclusivamente en: 
La correcta lógica de negocio (autenticación, permisos y CRUD). 
La claridad y legibilidad del código (Python, HTML y manejo de rutas). La claridad funcional de cómo se presenta la información en las pantallas (que los mensajes del servidor sean visibles y los formularios sean entendibles). 
Tecnologías permitidas: Flask, Jinja2 (plantillas HTML), y MySQL/MariaDB para la base de datos. 
3. Diseño de la Base de Datos 
Debes crear una base de datos llamada agenda que contenga las siguientes dos tablas con sus respectivas relaciones: 
Tabla usuarios : 
id (Integer, Clave Primaria, Auto-incremental) 
username (String, ÚNICO - no se permiten nombres de usuario duplicados) 
password (String, almacenamiento en texto plano o hasheado, según prefieras) 
Tabla contactos : 
id (Integer, Clave Primaria, Auto-incremental) 
nombre (String)
apellido (String) 
fecha_nacimiento (String o Date) 
email (String) 
usuario_id (Integer, Clave Foránea referenciando a usuarios.id ) 
Relación: Un usuario puede tener muchos contactos (relación 1 a N). Cada contacto está asociado estrictamente al usuario que lo creó. 
4. Requisitos Funcionales Detallados 
4.1. Pantalla de Login (Pública) 
Debe mostrar un formulario con los campos: Usuario y Contraseña, y un botón de envío etiquetado como "Ingresar". 
Manejo de mensajes: La vista debe mostrar mensajes enviados desde el servidor mediante un elemento HTML (ej. un <div> de alerta). 
Si las credenciales son correctas: debe mostrar "login correcto" y redirigir al panel correspondiente. 
Si fallan: debe mostrar "usuario y/o contraseña inválida". 
4.2. Rol: Administrador 
El sistema debe contar con un usuario admin (puede ser creado manualmente en la base de datos o mediante un script de inicialización). Al iniciar sesión, este usuario accede a un panel de administración con las siguientes capacidades: 
1. Gestión de su propia cuenta: 
Un enlace o botón para "Cambiar Contraseña" (propia). 
Un botón para "Cerrar Sesión" (Logout). 
2. Creación de nuevos usuarios del sistema: 
Formulario con dos campos: "Nombre de Usuario" y "Contraseña", más un botón "Crear". 
Debe validar que el nombre de usuario no exista previamente en la base de datos. Al crearse correctamente, debe mostrar el mensaje: "usuario creado con éxito". 3. Búsqueda de usuarios: 
Un único campo de texto para buscar por nombre de usuario y un botón "Buscar". 4. Gestión de resultados de búsqueda: 
Los usuarios encontrados deben mostrarse en una lista o tabla. 
Cada resultado debe presentarse como un formulario que permita:
Modificar únicamente la contraseña del usuario buscado (con un botón "Editar"). 
Eliminar completamente al usuario (con un botón "Borrar"). 
Nota: El admin NO debe poder editar el nombre de usuario, solo la contraseña. 4.3. Rol: Usuario Estándar 
Cualquier usuario no administrador (ej. jperez , mrodriguez ) accede a su panel personal. Importante: Cada usuario solo puede ver y gestionar los contactos que él mismo haya creado (asociados a su usuario_id ). Las funcionalidades son: 
1. Gestión de su propia cuenta: 
Un enlace o botón para "Cambiar Contraseña" (propia). 
Un botón para "Cerrar Sesión" (Logout). 
2. Creación de nuevos contactos: 
Formulario con 4 campos: Nombre, Apellido, Fecha de Nacimiento y Email, más un botón "Crear Contacto". 
3. Búsqueda de contactos: 
Un único campo de texto para buscar por nombre o apellido y un botón "Buscar". La búsqueda debe filtrar exclusivamente entre los contactos del usuario logueado. 4. Gestión de resultados de búsqueda: 
Los contactos encontrados deben mostrarse en una lista o tabla. 
Cada resultado debe presentarse como un formulario donde se puedan editar todos los campos (Nombre, Apellido, Fecha Nacimiento, Email) simultáneamente, con un botón "Editar" para aplicar los cambios. 
Cada resultado debe tener también un botón "Borrar" para eliminar ese contacto específico. 
5. Aspectos Técnicos y de Implementación 
Rutas: Debes definir claramente las rutas en Flask (ej. / , /login , /admin , /dashboard , /logout , etc.) utilizando los métodos HTTP adecuados ( GET y POST ). Sesiones: Utiliza flask.session para mantener la sesión del usuario logueado y restringir el acceso a las vistas según el rol. 
Mensajes Flash: Se recomienda usar session o flash() de Flask para gestionar los mensajes entre el servidor y las plantillas (ej. "login correcto", "usuario creado con éxito"), mostrándolos en un bloque HTML visible. 
Seguridad básica: Aunque no es el foco principal, asegúrate de que un usuario estándar no pueda acceder al panel de administración mediante la manipulación de
URLs. 

"""

from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL


# Configuración de la aplicación Flask y la base de datos MySQL
app = Flask(__name__)  # aca se crea la aplicacion flask
app.config['MYSQL_HOST'] = 'localhost' # aca se configura el host de la base de datos, en este caso localhost
app.config['MYSQL_USER'] = 'root' # aca se configura el usuario de la base de datos, en este caso root
app.config['MYSQL_PASSWORD'] = ''  # aca se configura la contraseña de la base de datos, en este caso vacia
app.config['MYSQL_DB'] = 'flask_contacto'  # aca se configura el nombre de la base de datos, en este caso flask_contacto
mysql = MySQL(app) # aca se crea la conexion a la base de datos

# Configuración de la clave secreta para la sesión
app.secret_key = 'millavesecreta'  # esto fue necesario para poder usar flash y session, ya que flask necesita una clave secreta para poder encriptar la informacion de la sesion



@app.route('/registro') 
def registro():
    return render_template('registro.html') # render_template es una funcion de flask que permite renderizar un template html, en este caso registro.html




@app.route('/añadir_usuario', methods=['GET','POST'])
def add_usuario():
    cur = mysql.connection.cursor()  # aca se conecta a la base de datos
    cur.execute('SELECT * FROM usuarios')  # aca se ejecuta la consulta a la base de datos, en este caso se seleccionan todos los contactos
    data = cur.fetchall()  # aca se guardan los datos obtenidos de la consulta
    # print(data)  # aca se imprime en consola los datos obtenidos de la consulta
    if request.method == 'POST': # aca se valida que el metodo sea POST
        usuario_ingresado = request.form['usuario']
        contraseña = request.form['contraseña']
        for usuario in data:
            if usuario[1] == usuario_ingresado:  # aca se valida que el nombre de usuario no exista previamente en la base de datos
                flash('El nombre de usuario ya existe. Elija otro.')
                return redirect(url_for('registro'))  # redirecciona a la ruta registro
        cur = mysql.connection.cursor() # aca se conecta a la base de datos
        cur.execute('INSERT INTO usuarios (usuario, contraseña) VALUES (%s, %s)', (usuario_ingresado, contraseña))
        mysql.connection.commit()  # aca se guarda en la base de datos
        flash('Usuario creado correctamente')  # flash es una funcion de flask que permite enviar mensajes al template html, en este caso se envia un mensaje de contacto agregado correctamente
        return redirect(url_for('autenticacion'))  # redirecciona a la ruta autenticacion
        

# Login
@app.route('/')
def autenticacion():
    return(render_template('autenticacion.html'))

@app.route('/inicio_sesion',methods=['GET','POST'])
def inicio_sesion():
    cur = mysql.connection.cursor()  # aca se conecta a la base de datos
    cur.execute('SELECT * FROM usuarios')  # aca se ejecuta la consulta a la base de datos, en este caso se seleccionan todos los contactos
    data = cur.fetchall()  # aca se guardan los datos obtenidos de la consulta
    print(data)  # aca se imprime en consola los datos obtenidos de la consulta
    if request.method == 'POST': # aca se valida que el metodo sea POST
        usuario_ingresado = request.form['usuario_ingresado']
        contraseña_ingresada = request.form['contraseña_ingresada']
    print(usuario_ingresado)
    print(contraseña_ingresada)
    
    for usuario in data:
        if usuario_ingresado == 'admin' and contraseña_ingresada == usuario[2] and usuario[1] == 'admin':
            return (redirect(url_for('Index')))
        if usuario_ingresado == usuario[1] and contraseña_ingresada == usuario[2]:
            session['usuario_id'] = usuario[0]
            session['usuario'] = usuario[1]
            return(redirect(url_for('agenda_usuarios')))
    flash('Usuario y/o contraseña inválida')
    return(redirect(url_for('autenticacion')))








# Rutas de la aplicación
@app.route('/administrador') # aca se define la ruta principal de la aplicacion, en este caso es la raiz del sitio web
def Index():
    cur = mysql.connection.cursor()  # aca se conecta a la base de datos
    cur.execute('SELECT * FROM contactos')  # aca se ejecuta la consulta a la base de datos, en este caso se seleccionan todos los contactos
    data = cur.fetchall()  # aca se guardan los datos obtenidos de la consulta
    # print(data)  # aca se imprime en consola los datos obtenidos de la consulta
    
    cur.execute('SELECT * FROM usuarios')  # aca se ejecuta la consulta a la base de datos, en este caso se seleccionan todos los contactos
    data_usuarios = cur.fetchall()  # aca se guardan los datos obtenidos de la consulta
    # print(data_usuarios)  # aca se imprime en consola los datos obtenidos de la consulta
    
    return render_template('administrador.html', contactos = data, usuarios = data_usuarios) # render_template es una funcion de flask que permite renderizar un template html, en este caso index.html

@app.route('/editar_contraseña_usuario/<id>')  # en esta linea se define la ruta y el metodo que va a recibir, en este caso GET
def editar_contraseña_usuario(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM usuarios WHERE id = %s', (id,))
    datos = cur.fetchall()
    return render_template('editar_contraseña_usuario.html', usuario = datos[0])

@app.route('/borrar_usuario/<string:id>')
def delete_usuario(id):
    if id == '7':  # aca se valida que el id del usuario no sea 7, ya que ese es el id del usuario administrador
        flash('No se puede eliminar el usuario administrador')
        return redirect(url_for('Index')) # redirecciona a la ruta index
    cur = mysql.connection.cursor() # aca se conecta a la base de datos
    cur.execute('DELETE FROM usuarios WHERE id = {0}'.format(id)) # aca se ejecuta la consulta a la base de datos, en este caso se elimina el contacto con el id especificado
    mysql.connection.commit() # aca se guarda en la base de datos
    flash('Usuario eliminado correctamente')
    return redirect(url_for('Index')) # redirecciona a la ruta index



@app.route('/agenda') # aca se define la ruta principal de la aplicacion
def agenda_usuarios():
    usuario_id = session['usuario_id']
    cur = mysql.connection.cursor()  # aca se conecta a la base de datos
    cur.execute('SELECT * FROM contactos WHERE usuario_id = %s', (usuario_id,))  # aca se ejecuta la consulta a la base de datos, en este caso se seleccionan los contactos del usuaro que inició sesión
    data = cur.fetchall()  # aca se guardan los datos obtenidos de la consulta
    # print(data)  # aca se imprime en consola la tupla que tiene todos los datos asignados a data
    return render_template('agenda_usuarios.html', contactos = data) # render_template es una funcion de flask que permite renderizar un template html, en este caso agenda_usuarios.html

@app.route('/actualizar_contraseña_usuario/<string:id>', methods = ['POST']) # en esta linea se define la ruta y el metodo que va a recibir, en este caso POST
def actualizar_contraseña_usuario(id):
    if request.method == 'POST': # aca se valida que el metodo sea POST
        contraseña = request.form['contraseña'] # aca se obtiene la contraseña del formulario html
        cur = mysql.connection.cursor()
        cur.execute("""   
            UPDATE usuarios
            SET contraseña = %s
            WHERE id = %s
        """, (contraseña, id)) # aca se ejecuta la consulta a la base de datos, en este caso se actualiza la contraseña del usuario con el id especificado
        mysql.connection.commit()
        flash('Contraseña actualizada correctamente')
        return redirect(url_for('Index')) # redirecciona a la ruta index

@app.route('/añadir_contacto_admin', methods=['POST'])  # en esta linea se define la ruta y el metodo que va a recibir, en este caso POST
def add_contact_admin():
    if request.method == 'POST': # aca se valida que el metodo sea POST
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        fecha_nacimiento = request.form['fecha_nacimiento']
        telefono = request.form['telefono']
        email = request.form['email']
        usuario_id = session['usuario_id']
        # print(nombre, telefono, email)
        cur = mysql.connection.cursor() # aca se conecta a la base de datos
        cur.execute('INSERT INTO contactos (nombre, apellido, fecha_nacimiento, telefono, email, usuario_id) VALUES (%s, %s, %s, %s, %s, %s)', (nombre, apellido, fecha_nacimiento, telefono, email, usuario_id))
        mysql.connection.commit()  # aca se guarda en la base de datos
        flash('Contacto agregado correctamente')  # flash es una funcion de flask que permite enviar mensajes al template html, en este caso se envia un mensaje de contacto agregado correctamente
        return redirect(url_for('Index'))  # redirecciona a la ruta agenda_usuarios


@app.route('/añadir_contacto', methods=['POST'])  # en esta linea se define la ruta y el metodo que va a recibir, en este caso POST
def add_contact():
    if request.method == 'POST': # aca se valida que el metodo sea POST
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        fecha_nacimiento = request.form['fecha_nacimiento']
        telefono = request.form['telefono']
        email = request.form['email']
        usuario_id = session['usuario_id']
        # print(nombre, telefono, email)
        cur = mysql.connection.cursor() # aca se conecta a la base de datos
        cur.execute('INSERT INTO contactos (nombre, apellido, fecha_nacimiento, telefono, email, usuario_id) VALUES (%s, %s, %s, %s, %s, %s)', (nombre, apellido, fecha_nacimiento, telefono, email, usuario_id))
        mysql.connection.commit()  # aca se guarda en la base de datos
        flash('Contacto agregado correctamente')  # flash es una funcion de flask que permite enviar mensajes al template html, en este caso se envia un mensaje de contacto agregado correctamente
        return redirect(url_for('agenda_usuarios'))  # redirecciona a la ruta agenda_usuarios

@app.route('/editar_contacto/<id>')  # en esta linea se define la ruta y el metodo que va a recibir, en este caso GET
def editar_contacto(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contactos WHERE id = %s', (id,))
    datos = cur.fetchall()
    return render_template('editar_contacto.html', contacto = datos[0])

@app.route('/actualizar_contacto/<string:id>', methods = ['POST']) # en esta linea se define la ruta y el metodo que va a recibir, en este caso POST
def actualizar_contacto(id):
    if request.method == 'POST': # aca se valida que el metodo sea POST
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        fecha_nacimiento = request.form['fecha_nacimiento']
        telefono = request.form['telefono']
        email = request.form['email'] # aca se obtienen los datos del formulario html, en este caso nombre, apellido, fecha_nacimiento, telefono y email
        cur = mysql.connection.cursor()
        cur.execute("""   
            UPDATE contactos
            SET nombre = %s,
                apellido = %s,
                fecha_nacimiento = %s,
                telefono = %s,
                email = %s
            WHERE id = %s
        """, (nombre, apellido, fecha_nacimiento, telefono, email, id)) # aca se ejecuta la consulta a la base de datos, en este caso se actualiza el contacto con el id especificado
        mysql.connection.commit()
        flash('Contacto actualizado correctamente')
        return redirect(url_for('agenda_usuarios')) # redirecciona a la ruta agenda_usuarios

@app.route('/editar_contacto_admin/<id>')  # en esta linea se define la ruta y el metodo que va a recibir, en este caso GET
def editar_contacto_admin(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contactos WHERE id = %s', (id,))
    datos = cur.fetchall()
    return render_template('editar_contacto_admin.html', contacto = datos[0])

@app.route('/actualizar_contacto_admin/<string:id>', methods = ['POST']) # en esta linea se define la ruta y el metodo que va a recibir, en este caso POST
def actualizar_contacto_admin(id):
    if request.method == 'POST': # aca se valida que el metodo sea POST
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        fecha_nacimiento = request.form['fecha_nacimiento']
        telefono = request.form['telefono']
        email = request.form['email'] # aca se obtienen los datos del formulario html, en este caso nombre, apellido, fecha_nacimiento, telefono y email
        cur = mysql.connection.cursor()
        cur.execute("""   
            UPDATE contactos
            SET nombre = %s,
                apellido = %s,
                fecha_nacimiento = %s,
                telefono = %s,
                email = %s
            WHERE id = %s
        """, (nombre, apellido, fecha_nacimiento, telefono, email, id)) # aca se ejecuta la consulta a la base de datos, en este caso se actualiza el contacto con el id especificado
        mysql.connection.commit()
        flash('Contacto actualizado correctamente')
        return redirect(url_for('Index')) # redirecciona a la ruta Index(administrador)

@app.route('/borrar_contacto/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor() # aca se conecta a la base de datos
    cur.execute('DELETE FROM contactos WHERE id = {0}'.format(id)) # aca se ejecuta la consulta a la base de datos, en este caso se elimina el contacto con el id especificado
    mysql.connection.commit() # aca se guarda en la base de datos
    flash('Contacto eliminado correctamente')
    return redirect(url_for('agenda_usuarios')) # redirecciona a la ruta index

@app.route('/borrar_contacto_admin/<string:id>')
def delete_contact_admin(id):
    cur = mysql.connection.cursor() # aca se conecta a la base de datos
    cur.execute('DELETE FROM contactos WHERE id = {0}'.format(id)) # aca se ejecuta la consulta a la base de datos, en este caso se elimina el contacto con el id especificado
    mysql.connection.commit() # aca se guarda en la base de datos
    flash('Contacto eliminado correctamente')
    return redirect(url_for('Index')) # redirecciona a la ruta index

# prueba buscador de usuarios
@app.route('/buscar_usuario', methods=['POST'])
def buscar_usuario():
    if request.method == 'POST':
        termino_busqueda = request.form['termino_busqueda']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM usuarios WHERE usuario LIKE %s", ('%' + termino_busqueda + '%',))
        resultados = cur.fetchall()
   #     return redirect(url_for('Index', resultados=resultados, termino=termino_busqueda))
        return render_template('buscador_usuario_admin.html', resultados=resultados, termino=termino_busqueda)



if __name__ == '__main__':
    app.run(port = 5000, debug = True) # aca se ejecuta la aplicacion en el puerto 5000 y en modo debug, lo que permite ver los errores en la consola
