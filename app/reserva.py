import sqlite3
from datetime import datetime


DB_PATH = "ecoexplorer.db"

def hacer_reserva(experiencia_id):
    """Crea una nueva reserva para una experiencia específica."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    fecha_reserva = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute('''
    INSERT INTO reservas (experiencia_id, fecha_reserva)
    VALUES (?, ?)
    ''', (experiencia_id, fecha_reserva))
    
    conn.commit()
    conn.close()
    print("Reserva realizada exitosamente.")

def cancelar_reserva(reserva_id):
    """Elimina una reserva específica de la base de datos."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM reservas WHERE id = ?", (reserva_id,))
    
    conn.commit()
    conn.close()
    print("Reserva cancelada exitosamente.")

def listar_reservas():
    """Obtiene todas las reservas actuales de la base de datos."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT reservas.id, experiencias.nombre, reservas.fecha_reserva
    FROM reservas
    JOIN experiencias ON reservas.experiencia_id = experiencias.id
    ''')
    reservas = cursor.fetchall()
    
    conn.close()
    return reservas
