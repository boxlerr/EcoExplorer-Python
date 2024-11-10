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

def actualizar_experiencia(exp_id, nombre, ubicacion, dificultad, disponibilidad, descripcion):
    """Actualiza una experiencia existente en la base de datos."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
        UPDATE experiencias
        SET nombre = ?, ubicacion = ?, dificultad = ?, disponibilidad = ?, descripcion = ?
        WHERE id = ?
        ''', (nombre, ubicacion, dificultad, disponibilidad, descripcion, exp_id))
        
        conn.commit()
        print(f"Experiencia con ID {exp_id} actualizada exitosamente.")
    except sqlite3.Error as e:
        print(f"Error al actualizar la experiencia: {e}")
        conn.rollback()
    finally:
        conn.close()

def eliminar_experiencia(exp_id):
    """Elimina una experiencia de la base de datos por su ID."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    try:
        cursor.execute('DELETE FROM experiencias WHERE id = ?', (exp_id,))
        
        if cursor.rowcount > 0:
            conn.commit()
            print(f"Experiencia con ID {exp_id} eliminada exitosamente.")
        else:
            print(f"No se encontró ninguna experiencia con ID {exp_id}.")
    except sqlite3.Error as e:
        print(f"Error al eliminar la experiencia: {e}")
        conn.rollback()
    finally:
        conn.close()