import os
import csv
from datetime import datetime

class ErrorFormatoFecha(Exception):
    """Excepcion para errores en el formato de fecha"""
    def __init__(self, mensaje="Formato de fecha invalido. Use DD/MM/AAAA."):
        super().__init__(mensaje)

class ErrorHabitacion(Exception):
    """Excepcion para errores relacionados con habitaciones"""
    def __init__(self, mensaje="Error en la gestion de habitaciones."):
        super().__init__(mensaje)

class ErrorReserva(Exception):
    """Excepcion para errores en las reservas"""
    def __init__(self, mensaje="Error en la gestion de reservas."):
        super().__init__(mensaje)

class Habitacion:
    def __init__(self, numero, tipo, precio_por_noche):
        self.numero = numero
        self.tipo = tipo
        self.precio_por_noche = precio_por_noche

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, valor):
        if not str(valor).isdigit():
            raise ErrorHabitacion("El numero de habitacion debe ser numerico.")
        self._numero = int(valor)

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, valor):
        if valor.lower() not in ["simple", "doble", "suite"]:
            raise ErrorHabitacion("Tipo de habitacion invalido. Use simple, doble o suite.")
        self._tipo = valor.lower()

    @property
    def precio_por_noche(self):
        return self._precio_por_noche

    @precio_por_noche.setter
    def precio_por_noche(self, valor):
        try:
            valor = float(valor)
        except ValueError:
            raise ErrorHabitacion("El precio debe ser un numero.")
        if valor <= 0:
            raise ErrorHabitacion("El precio debe ser mayor a 0.")
        self._precio_por_noche = valor

def validar_fecha(fecha_str):
    try:
        return datetime.strptime(fecha_str, "%d/%m/%Y")
    except ValueError:
        raise ErrorFormatoFecha()


def cargar_reservas(nombre_archivo="reservas.txt"):
    reservas = []
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            lector = csv.reader(f, delimiter=";")
            for fila in lector:
                if fila:
                    reservas.append(fila)
    return reservas


def guardar_reserva(datos, nombre_archivo="reservas.txt"):
    with open(nombre_archivo, "a", encoding="utf-8", newline="") as f:
        escritor = csv.writer(f, delimiter=";")
        escritor.writerow(datos)


def habitacion_disponible(numero, fecha_inicio, fecha_fin, reservas):
    for reserva in reservas:
        num_reservada, fecha_i, fecha_f, *_ = reserva
        if int(num_reservada) == int(numero):
            fi = datetime.strptime(fecha_i, "%d/%m/%Y")
            ff = datetime.strptime(fecha_f, "%d/%m/%Y")
            if (fecha_inicio <= ff and fecha_fin >= fi):
                return False
    return True


def generar_factura(nombre_cliente, habitacion, dias, fecha_inicio, fecha_fin):
    total = habitacion.precio_por_noche * dias
    factura = f"""
    ===== FACTURA HOTEL =====
    Cliente: {nombre_cliente}
    Habitacion: {habitacion.numero} ({habitacion.tipo})
    Precio por noche: ${habitacion.precio_por_noche:.2f}
    Fecha ingreso: {fecha_inicio.strftime('%d/%m/%Y')}
    Fecha salida: {fecha_fin.strftime('%d/%m/%Y')}
    Total noches: {dias}
    -------------------------
    TOTAL A PAGAR: ${total:.2f}
    """
    return factura

def menu():
    habitaciones = [
        Habitacion(101, "simple", 50),
        Habitacion(102, "doble", 80),
        Habitacion(201, "suite", 150),
    ]

    while True:
        print("\n===== SISTEMA DE RESERVAS DE HOTEL =====")
        print("1. Realizar reserva")
        print("2. Verificar disponibilidad")
        print("3. Generar factura")
        print("4. Salir")
        opcion = input("Seleccione una opcion: ")

        try:
            if opcion == "1":
                nombre_cliente = input("Ingrese el nombre del cliente: ").strip()
                numero = input("Ingrese numero de habitacion: ")
                habitacion = next((h for h in habitaciones if h.numero == int(numero)), None)
                if not habitacion:
                    raise ErrorHabitacion("La habitacion no existe.")

                fecha_inicio = validar_fecha(input("Ingrese fecha de ingreso (DD/MM/AAAA): "))
                fecha_fin = validar_fecha(input("Ingrese fecha de salida (DD/MM/AAAA): "))

                if fecha_fin <= fecha_inicio:
                    raise ErrorReserva("La fecha de salida debe ser posterior a la de ingreso.")

                reservas = cargar_reservas()
                if not habitacion_disponible(numero, fecha_inicio, fecha_fin, reservas):
                    raise ErrorReserva("La habitacion no esta disponible en ese rango de fechas.")

                dias = (fecha_fin - fecha_inicio).days
                guardar_reserva([numero, fecha_inicio.strftime("%d/%m/%Y"),
                                fecha_fin.strftime("%d/%m/%Y"), nombre_cliente])
                print("Reserva realizada con exito.")

            elif opcion == "2":
                numero = input("Ingrese numero de habitacion: ")
                fecha_inicio = validar_fecha(input("Ingrese fecha de ingreso (DD/MM/AAAA): "))
                fecha_fin = validar_fecha(input("Ingrese fecha de salida (DD/MM/AAAA): "))

                reservas = cargar_reservas()
                if habitacion_disponible(numero, fecha_inicio, fecha_fin, reservas):
                    print("La habitacion esta disponible.")
                else:
                    print("La habitacion NO esta disponible en esas fechas.")

            elif opcion == "3":
                nombre_cliente = input("Ingrese el nombre del cliente: ").strip()
                numero = input("Ingrese numero de habitacion: ")
                habitacion = next((h for h in habitaciones if h.numero == int(numero)), None)
                if not habitacion:
                    raise ErrorHabitacion("La habitacion no existe.")

                fecha_inicio = validar_fecha(input("Ingrese fecha de ingreso (DD/MM/AAAA): "))
                fecha_fin = validar_fecha(input("Ingrese fecha de salida (DD/MM/AAAA): "))

                dias = (fecha_fin - fecha_inicio).days
                print(generar_factura(nombre_cliente, habitacion, dias, fecha_inicio, fecha_fin))

            elif opcion == "4":
                print("Saliendo del sistema...")
                break

            else:
                print("Opcion invalida, intente nuevamente.")

        except (ErrorFormatoFecha, ErrorHabitacion, ErrorReserva, ValueError) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")


if __name__ == "__main__":
    menu()
