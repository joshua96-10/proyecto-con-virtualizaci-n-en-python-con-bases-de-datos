import sqlite3

def conectar_db():
    """Conecta a la base de datos y retorna el objeto de conexión."""
    conn = sqlite3.connect('contactos.db')
    return conn

def crear_tabla():
    """Crea la tabla de contactos si no existe."""
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS contactos (
                        id INTEGER PRIMARY KEY,
                        nombre TEXT NOT NULL,
                        telefono TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def agregar_contacto(nombre, telefono):
    """Agrega un nuevo contacto a la base de datos."""
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO contactos (nombre, telefono) VALUES (?, ?)', (nombre, telefono))
    conn.commit()
    conn.close()

def obtener_contactos():
    """Obtiene todos los contactos de la base de datos."""
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contactos')
    contactos = cursor.fetchall()
    conn.close()
    return contactos

def eliminar_contacto(contacto_id):
    """Elimina un contacto de la base de datos por su ID."""
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM contactos WHERE id = ?', (contacto_id,))
    conn.commit()
    conn.close()
