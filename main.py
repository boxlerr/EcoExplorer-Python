import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from app.experiencia import listar_experiencias, agregar_experiencia, actualizar_experiencia, eliminar_experiencia
from app.reserva import hacer_reserva, cancelar_reserva, listar_reservas
import app.db_setup as db_setup 

db_setup.create_tables()

# ventana principal
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

    # Estado de la disponibilidad (inicialmente "No")
    disponibilidad_estado = tk.StringVar(value="No")

    # Función para establecer la disponibilidad como "Sí"
    def set_disponibilidad_si():
        disponibilidad_estado.set("Sí")
        boton_si.config(bg="green", fg="white")
        boton_no.config(bg="lightgray", fg="black")

    # Función para establecer la disponibilidad como "No"
    def set_disponibilidad_no():
        disponibilidad_estado.set("No")
        boton_no.config(bg="red", fg="white")
        boton_si.config(bg="lightgray", fg="black")

    # Etiqueta para mostrar la disponibilidad
    disponibilidad_label = tk.Label(root, text="Disponibilidad:")
    disponibilidad_label.pack(pady=5)

    # Botones "Sí" y "No" para seleccionar disponibilidad
    botones_disponibilidad_frame = tk.Frame(root)
    botones_disponibilidad_frame.pack()

    # boton "Sí"
    boton_si = tk.Button(botones_disponibilidad_frame, text="Sí", command=set_disponibilidad_si, bg="lightgray", fg="black")
    boton_si.pack(side="left", padx=10)

    # boton "No"
    boton_no = tk.Button(botones_disponibilidad_frame, text="No", command=set_disponibilidad_no, bg="lightgray", fg="black")
    boton_no.pack(side="left", padx=10)

    # Establecer el estado inicial de los botones
    if disponibilidad_estado.get() == "Sí":
        boton_si.config(bg="green", fg="white")
        boton_no.config(bg="lightgray", fg="black")
    else:
        boton_no.config(bg="red", fg="white")
        boton_si.config(bg="lightgray", fg="black")

    tk.Label(root, text="Descripción:").pack()
    descripcion_entry = tk.Entry(root, width=50)
    descripcion_entry.pack()

    # botón agregar
    agregar_button = tk.Button(root, text="Agregar Experiencia", command=lambda: guardar_experiencia(
        nombre_entry.get(),
        ubicacion_entry.get(),
        dificultad_entry.get(),
        1 if disponibilidad_estado.get() == "Sí" else 0,  # Convertir "Sí"/"No" a 1/0
        descripcion_entry.get()
    ), bg="green", fg="white")
    agregar_button.pack(pady=10)

    # botón volver
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

        button_frame = tk.Frame(frame)
        button_frame.pack(anchor="e", padx=5, pady=5)

        # boton reserva
        if disponibilidad:
            reservar_button = tk.Button(button_frame, text="Reservar", command=lambda exp_id=exp_id: reservar_experiencia(exp_id), bg="green", fg="white")
            reservar_button.pack(side="left", padx=5)
        else:
            # Si no está disponible, mostramos un botón deshabilitado o un mensaje
            tk.Label(button_frame, text="No disponible", fg="red").pack(side="left", padx=5)

        # boton editar
        editar_button = tk.Button(button_frame, text="Editar", command=lambda exp_id=exp_id, exp=experiencia: editar_experiencia(exp_id, exp), bg="blue", fg="white")
        editar_button.pack(side="left", padx=5)

        # boton eliminar
        eliminar_button = tk.Button(button_frame, text="Eliminar", command=lambda exp_id=exp_id: eliminar_experiencia_confirmada(exp_id), bg="red", fg="white")
        eliminar_button.pack(side="left", padx=5)

    # volver
    volver_button = tk.Button(root, text="Volver", command=mostrar_menu_principal, bg="gray", fg="white")
    volver_button.pack(pady=10)

def eliminar_experiencia_confirmada(exp_id):
    """Muestra una ventana de confirmación para eliminar una experiencia."""
    respuesta = messagebox.askyesno("Eliminar Eco-Experiencia", "¿Estás seguro de que quieres eliminar esta experiencia?")
    if respuesta:
        eliminar_experiencia(exp_id)
        messagebox.showinfo("Eco-Experiencia", "Eco-Experiencia eliminada exitosamente.")
        mostrar_experiencias()

def editar_experiencia(exp_id, experiencia):
    limpiar_ventana()

    tk.Label(root, text="Editar Eco-Experiencia", font=("Arial", 18)).pack(pady=10)

    # atributos de las expes
    tk.Label(root, text="Nombre:").pack()
    nombre_entry = tk.Entry(root, width=40)
    nombre_entry.insert(0, experiencia[1])
    nombre_entry.pack()

    tk.Label(root, text="Ubicación:").pack()
    ubicacion_entry = tk.Entry(root, width=40)
    ubicacion_entry.insert(0, experiencia[2])
    ubicacion_entry.pack()

    tk.Label(root, text="Dificultad:").pack()
    dificultad_entry = tk.Entry(root, width=40)
    dificultad_entry.insert(0, experiencia[3])
    dificultad_entry.pack()

    # estado dispo
    disponibilidad_estado = tk.StringVar(value="Sí" if experiencia[4] else "No")

    # Función para establecer la disponibilidad como "Sí"
    def set_disponibilidad_si():
        disponibilidad_estado.set("Sí")
        boton_si.config(bg="green", fg="white")
        boton_no.config(bg="lightgray", fg="black")

    # Función para establecer la disponibilidad como "No"
    def set_disponibilidad_no():
        disponibilidad_estado.set("No")
        boton_no.config(bg="red", fg="white")
        boton_si.config(bg="lightgray", fg="black")

    # mostrar dispo
    disponibilidad_label = tk.Label(root, text="Disponibilidad:")
    disponibilidad_label.pack(pady=5)

    # Botones "Sí" y "No" para seleccionar disponibilidad
    botones_disponibilidad_frame = tk.Frame(root)
    botones_disponibilidad_frame.pack()

    # boton "Sí"
    boton_si = tk.Button(botones_disponibilidad_frame, text="Sí", command=set_disponibilidad_si, bg="green" if experiencia[4] else "lightgray", fg="white" if experiencia[4] else "black")
    boton_si.pack(side="left", padx=10)

    # boton "No"
    boton_no = tk.Button(botones_disponibilidad_frame, text="No", command=set_disponibilidad_no, bg="red" if not experiencia[4] else "lightgray", fg="white" if not experiencia[4] else "black")
    boton_no.pack(side="left", padx=10)

    tk.Label(root, text="Descripción:").pack()
    descripcion_entry = tk.Entry(root, width=40)
    descripcion_entry.insert(0, experiencia[5])
    descripcion_entry.pack()

    # boton guardar
    guardar_button = tk.Button(root, text="Guardar Cambios", command=lambda: guardar_edicion_experiencia(
        exp_id,
        nombre_entry.get(),
        ubicacion_entry.get(),
        dificultad_entry.get(),
        1 if disponibilidad_estado.get() == "Sí" else 0,
        descripcion_entry.get()
    ), bg="green", fg="white")
    guardar_button.pack(pady=10)

    # boton volver
    volver_button = tk.Button(root, text="Volver", command=mostrar_experiencias, bg="gray", fg="white")
    volver_button.pack(pady=10)

def guardar_edicion_experiencia(exp_id, nombre, ubicacion, dificultad, disponibilidad, descripcion):
    actualizar_experiencia(exp_id, nombre, ubicacion, dificultad, disponibilidad, descripcion)
    messagebox.showinfo("Eco-Experiencia", "Eco-Experiencia actualizada exitosamente.")
    mostrar_experiencias()


def reservar_experiencia(experiencia_id):
    hacer_reserva(experiencia_id)
    messagebox.showinfo("Reserva", "Reserva realizada exitosamente.")
    mostrar_reservas()


def mostrar_reservas():
    limpiar_ventana()

    # title
    tk.Label(root, text="Reservas", font=("Arial", 18)).pack(pady=10)

    # lista reservas
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

    # logo
    logo_img = PhotoImage(file="img/logo.png") 
    logo_label = tk.Label(root, image=logo_img)
    logo_label.image = logo_img 
    logo_label.pack(pady=10)

    # botones menu
    boton_agregar_experiencia = tk.Button(root, text="Agregar Eco-Experiencia", command=mostrar_agregar_experiencia, width=20, height=2, bg="green", fg="white")
    boton_agregar_experiencia.pack(pady=10)

    boton_experiencias = tk.Button(root, text="Eco-Experiencias", command=mostrar_experiencias, width=20, height=2, bg="green", fg="white")
    boton_experiencias.pack(pady=10)

    boton_reservas = tk.Button(root, text="Reservas", command=mostrar_reservas, width=20, height=2, bg="green", fg="white")
    boton_reservas.pack(pady=10)

    boton_salir = tk.Button(root, text="Salir", command=salir, width=20, height=2, bg="red", fg="white")
    boton_salir.pack(pady=10)


mostrar_menu_principal()

# iniciar app
root.mainloop()
