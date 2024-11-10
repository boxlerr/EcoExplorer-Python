import sqlite3

def create_tables():
    # coneta la bd
    conn = sqlite3.connect("ecoexplorer.db")
    cursor = conn.cursor()

    # tabla expes
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS experiencias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        ubicacion TEXT NOT NULL,
        dificultad TEXT NOT NULL,
        disponibilidad BOOLEAN NOT NULL,
        descripcion TEXT
    )
    ''')

    # tabla reservas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS reservas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        experiencia_id INTEGER,
        fecha_reserva TEXT NOT NULL,
        FOREIGN KEY (experiencia_id) REFERENCES experiencias(id) ON DELETE CASCADE
    )
    ''')

    # confirma los cambios
    conn.commit()
    conn.close()
    print("Tablas creadas exitosamente.")

#funcion para crear las tablass
if __name__ == "__main__":
    create_tables()
