import tkinter as tk
from tkinter import messagebox
from app.experiencia import listar_experiencias, agregar_experiencia
from app.reserva import hacer_reserva, cancelar_reserva, listar_reservas
import app.db_setup as db_setup  # Para asegurarnos de que las tablas se creen al iniciar


db_setup.create_tables()

#ventana principal
root = tk.Tk()
root.title("Eco-Explorer")
root.geometry("500x500")

def mostrar_agregar_experiencia():
    limpiar_ventana()
    
    tk.Label(root, text="Agregar Eco-Experiencia", font=("Arial", 18)).pack(pady=10)
    
    # atributos de las expes
    tk.Label(root, text="Nombre:").pack()
    nombre_entry = tk.Entry(root, width=40)
    nombre_entry.pack()

    tk.Label(root, text="Ubicación:").pack()
    ubicacion_entry = tk.Entry(root, width=40)
    ubicacion_entry.pack()

    tk.Label(root, text="Dificultad:").pack()
    dificultad_entry = tk.Entry(root, width=40)
    dificultad_entry.pack()

    tk.Label(root, text="Disponibilidad (1 para disponible, 0 para no disponible):").pack()
    disponibilidad_entry = tk.Entry(root, width=40)
    disponibilidad_entry.pack()

    tk.Label(root, text="Descripción:").pack()
    descripcion_entry = tk.Entry(root, width=40)
    descripcion_entry.pack()

    # boton agregar
    agregar_button = tk.Button(root, text="Agregar Experiencia", command=lambda: guardar_experiencia(
        nombre_entry.get(),
        ubicacion_entry.get(),
        dificultad_entry.get(),
        int(disponibilidad_entry.get()),
        descripcion_entry.get()
    ), bg="green", fg="white")
    agregar_button.pack(pady=10)

    # boton volver
    volver_button = tk.Button(root, text="Volver", command=mostrar_menu_principal, bg="gray", fg="white")
    volver_button.pack(pady=10)

def guardar_experiencia(nombre, ubicacion, dificultad, disponibilidad, descripcion):
    agregar_experiencia(nombre, ubicacion, dificultad, disponibilidad, descripcion)
    messagebox.showinfo("Eco-Experiencia", "Eco-Experiencia agregada exitosamente.")
    mostrar_menu_principal()

def mostrar_experiencias():
    limpiar_ventana()

    # title
    tk.Label(root, text="Eco-Experiencias", font=("Arial", 18)).pack(pady=10)

    # listas expes
    experiencias = listar_experiencias()
    for experiencia in experiencias:
        exp_id, nombre, ubicacion, dificultad, disponibilidad, descripcion = experiencia

        frame = tk.Frame(root, relief=tk.RIDGE, borderwidth=2)
        frame.pack(fill="x", padx=10, pady=5)

        tk.Label(frame, text=f"Nombre: {nombre}", font=("Arial", 12, "bold")).pack(anchor="w")
        tk.Label(frame, text=f"Ubicación: {ubicacion}").pack(anchor="w")
        tk.Label(frame, text=f"Dificultad: {dificultad}").pack(anchor="w")
        tk.Label(frame, text=f"Disponibilidad: {'Sí' if disponibilidad else 'No'}").pack(anchor="w")
        tk.Label(frame, text=f"Descripción: {descripcion}").pack(anchor="w")

        # boton reserva
        reservar_button = tk.Button(frame, text="Reservar", command=lambda exp_id=exp_id: reservar_experiencia(exp_id), bg="green", fg="white")
        reservar_button.pack(anchor="e", padx=5, pady=5)

    # volver
    volver_button = tk.Button(root, text="Volver", command=mostrar_menu_principal, bg="gray", fg="white")
    volver_button.pack(pady=10)

def reservar_experiencia(experiencia_id):
    hacer_reserva(experiencia_id)
    messagebox.showinfo("Reserva", "Reserva realizada exitosamente.")
    mostrar_reservas()

def mostrar_reservas():
    limpiar_ventana()

    # title
    tk.Label(root, text="Mis Reservas", font=("Arial", 18)).pack(pady=10)

    # lista mis reservas
    reservas = listar_reservas()
    for reserva in reservas:
        reserva_id, nombre, fecha_reserva = reserva

        frame = tk.Frame(root, relief=tk.RIDGE, borderwidth=2)
        frame.pack(fill="x", padx=10, pady=5)

        tk.Label(frame, text=f"Experiencia: {nombre}", font=("Arial", 12, "bold")).pack(anchor="w")
        tk.Label(frame, text=f"Fecha de reserva: {fecha_reserva}").pack(anchor="w")

        # boton para cancelar reserva
        cancelar_button = tk.Button(frame, text="Cancelar Reserva", command=lambda reserva_id=reserva_id: cancelar_reserva_experiencia(reserva_id), bg="orange", fg="white")
        cancelar_button.pack(anchor="e", padx=5, pady=5)

    # boton volver
    volver_button = tk.Button(root, text="Volver", command=mostrar_menu_principal, bg="gray", fg="white")
    volver_button.pack(pady=10)

def cancelar_reserva_experiencia(reserva_id):
    cancelar_reserva(reserva_id)
    messagebox.showinfo("Reserva", "Reserva cancelada exitosamente.")
    mostrar_reservas()

def salir():
    root.quit()

def limpiar_ventana():
    for widget in root.winfo_children():
        widget.destroy()

def mostrar_menu_principal():
    limpiar_ventana()
    
    # botones menu
    boton_agregar_experiencia = tk.Button(root, text="Agregar Eco-Experiencia", command=mostrar_agregar_experiencia, width=20, height=2, bg="green", fg="white")
    boton_agregar_experiencia.pack(pady=10)

    boton_experiencias = tk.Button(root, text="Eco-Experiencias", command=mostrar_experiencias, width=20, height=2, bg="green", fg="white")
    boton_experiencias.pack(pady=10)

    boton_reservas = tk.Button(root, text="Mis Reservas", command=mostrar_reservas, width=20, height=2, bg="green", fg="white")
    boton_reservas.pack(pady=10)

    boton_salir = tk.Button(root, text="Salir", command=salir, width=20, height=2, bg="red", fg="white")
    boton_salir.pack(pady=10)


mostrar_menu_principal()

# iniciar app
root.mainloop()
