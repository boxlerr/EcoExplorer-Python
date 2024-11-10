import sqlite3
import unittest
from app.experiencia import agregar_experiencia

class TestAgregarExperiencia(unittest.TestCase):
    def test_agregar_experiencia(self):
        # Datos para la prueba
        nombre = "Experiencia Test"
        ubicacion = "Ubicacion Test"
        dificultad = "Fácil"
        disponibilidad = "Disponible"
        descripcion = "Descripción de la experiencia de prueba"  # Ajustado para coincidir con la base de datos

        # Llamar la función para agregar la experiencia
        agregar_experiencia(nombre, ubicacion, dificultad, disponibilidad, descripcion)

        # Verificar si la experiencia fue insertada correctamente en la base de datos real
        conn = sqlite3.connect("ecoexplorer.db")  # Conectar a la base de datos real
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM experiencias WHERE nombre = ?", (nombre,))
        experiencia = cursor.fetchone()
        conn.close()

        # Comprobar si la experiencia fue insertada
        self.assertIsNotNone(experiencia, "La experiencia no se insertó correctamente.")
        self.assertEqual(experiencia[1], nombre, "El nombre de la experiencia no es correcto.")
        self.assertEqual(experiencia[2], ubicacion, "La ubicación de la experiencia no es correcta.")
        self.assertEqual(experiencia[3], dificultad, "La dificultad de la experiencia no es correcta.")
        self.assertEqual(experiencia[4], disponibilidad, "La disponibilidad de la experiencia no es correcta.")
        self.assertEqual(experiencia[5], descripcion, "La descripción de la experiencia no es correcta.")

if __name__ == '__main__':
    unittest.main()
