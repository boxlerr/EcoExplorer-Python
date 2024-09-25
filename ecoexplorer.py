class EcoExperiencia:
    def __init__(self, nombre, ubicacion, dificultad, precio, descripcion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.dificultad = dificultad
        self.precio = precio
        self.descripcion = descripcion

    def obtener_detalles(self):
        return f"Nombre: {self.nombre}, Ubicación: {self.ubicacion}, Dificultad: {self.dificultad}, Precio: {self.precio}, Descripción: {self.descripcion}"


class Usuario:
    def __init__(self, nombre_usuario, email, contraseña):
        self.nombre_usuario = nombre_usuario
        self.email = email
        self.contraseña = contraseña
        self.reservas = []

    def registrar_usuario(self):
        # Implementar lógica para registrar el usuario
        pass

    def iniciar_sesion(self, email, contraseña):
        # Implementar lógica de inicio de sesión
        if self.email == email and self.contraseña == contraseña:
            return True
        return False

    def ver_reservas(self):
        return self.reservas


class Reserva:
    def __init__(self, usuario, experiencia, fecha_reserva):
        self.usuario = usuario
        self.experiencia = experiencia
        self.fecha_reserva = fecha_reserva
        self.estado_reserva = 'pendiente'

    def confirmar_reserva(self):
        self.estado_reserva = 'confirmada'

    def cancelar_reserva(self):
        self.estado_reserva = 'cancelada'


class Valoracion:
    def __init__(self, usuario, experiencia, calificacion, comentario):
        self.usuario = usuario
        self.experiencia = experiencia
        self.calificacion = calificacion
        self.comentario = comentario

    def dejar_valoracion(self):
        # Lógica para dejar una valoración
        pass

    def ver_valoraciones(self, experiencia):
        # Lógica para ver valoraciones de una experiencia
        pass


class Pago:
    def __init__(self, usuario, monto, metodo_pago):
        self.usuario = usuario
        self.monto = monto
        self.metodo_pago = metodo_pago
        self.estado_pago = 'pendiente'

    def procesar_pago(self):
        # Lógica para procesar el pago
        self.estado_pago = 'completado'

    def ver_historial_pagos(self):
        # Lógica para ver el historial de pagos
        pass
