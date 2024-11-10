import sqlite3

# ruta bd
DB_PATH = "ecoexplorer.db"

def listar_experiencias():
    """Obtiene todas las experiencias de la base de datos."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM experiencias")
    experiencias = cursor.fetchall()
    
    conn.close()
    return experiencias

def agregar_experiencia(nombre, ubicacion, dificultad, disponibilidad, descripcion):
    """Agrega una nueva experiencia a la base de datos."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO experiencias (nombre, ubicacion, dificultad, disponibilidad, descripcion)
    VALUES (?, ?, ?, ?, ?)
    ''', (nombre, ubicacion, dificultad, disponibilidad, descripcion))
    
    conn.commit()
    conn.close()
    print("Experiencia agregada exitosamente.")
