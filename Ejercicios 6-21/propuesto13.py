import os
import csv
from datetime import datetime
from collections import defaultdict

class ErrorFormatoFecha(Exception):
    """Excepcion personalizada para errores de fecha"""

class ErrorMontoInvalido(Exception):
    """Excepcion personalizada para errores de monto"""

class Gasto:
    def __init__(self, descripcion: str, monto: float, fecha: str, categoria: str):
        self.descripcion = descripcion.strip()
        self._monto = None
        self._fecha = None
        self.set_monto(monto)
        self.set_fecha(fecha)
        self.categoria = categoria.strip().capitalize()

    def get_monto(self):
        return self._monto

    def set_monto(self, valor):
        try:
            valor = float(valor)
            if valor <= 0:
                raise ErrorMontoInvalido("El monto debe ser un numero positivo.")
            self._monto = valor
        except ValueError:
            raise ErrorMontoInvalido("El monto debe ser un numero valido.")

    monto = property(get_monto, set_monto)

    def get_fecha(self):
        return self._fecha

    def set_fecha(self, fecha_str: str):
        try:
            fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
            self._fecha = fecha
        except ValueError:
            raise ErrorFormatoFecha("La fecha debe tener el formato DD/MM/AAAA")

    fecha = property(get_fecha, set_fecha)

    def __str__(self):
        return f"{self.descripcion} | {self.monto:.2f} | {self.fecha.strftime('%d/%m/%Y')} | {self.categoria}"


class CalculadoraGastos:
    ARCHIVO = "gastos.txt"

    def __init__(self):
        self.gastos = []
        self.cargar_gastos()

    def cargar_gastos(self):
        if os.path.exists(self.ARCHIVO):
            try:
                with open(self.ARCHIVO, "r", encoding="utf-8") as f:
                    for linea in f:
                        datos = linea.strip().split(" | ")
                        if len(datos) == 4:
                            desc, monto, fecha_str, cat = datos
                            try:
                                gasto = Gasto(desc, monto, fecha_str, cat)
                                self.gastos.append(gasto)
                            except (ErrorFormatoFecha, ErrorMontoInvalido):
                                print(f"[Aviso] Se omitio un gasto invalido: {linea.strip()}")
            except Exception as e:
                print(f"[Error] No se pudo leer el archivo: {e}")

    def guardar_gastos(self):
        try:
            with open(self.ARCHIVO, "w", encoding="utf-8") as f:
                for gasto in self.gastos:
                    f.write(str(gasto) + "\n")
        except Exception as e:
            print(f"[Error] No se pudo guardar el archivo: {e}")

    def registrar_gasto(self, desc, monto, fecha_str, cat):
        try:
            nuevo_gasto = Gasto(desc, monto, fecha_str, cat)
            self.gastos.append(nuevo_gasto)
            self.guardar_gastos()
            print("Gasto registrado correctamente.")
        except (ErrorMontoInvalido, ErrorFormatoFecha) as e:
            print(f"[Error] {e}")

    def resumen_por_mes(self):
        resumen = defaultdict(float)
        for gasto in self.gastos:
            clave = gasto.fecha.strftime("%m/%Y")
            resumen[clave] += gasto.monto
        if resumen:
            print("\nResumen por mes:")
            for mes, total in resumen.items():
                print(f"{mes}: ${total:.2f}")
        else:
            print("No hay gastos registrados.")

    def resumen_por_categoria(self):
        resumen = defaultdict(float)
        for gasto in self.gastos:
            resumen[gasto.categoria] += gasto.monto
        if resumen:
            print("\nResumen por categoria:")
            for cat, total in resumen.items():
                print(f"{cat}: ${total:.2f}")
        else:
            print("No hay gastos registrados.")

    def exportar_csv(self, nombre_archivo="gastos_exportados.csv"):
        try:
            with open(nombre_archivo, "w", newline="", encoding="utf-8") as f:
                escritor = csv.writer(f)
                escritor.writerow(["Descripcion", "Monto", "Fecha", "Categoria"])
                for gasto in self.gastos:
                    escritor.writerow([gasto.descripcion, gasto.monto, gasto.fecha.strftime("%d/%m/%Y"), gasto.categoria])
            print(f"Gastos exportados correctamente a {nombre_archivo}")
        except Exception as e:
            print(f"[Error] No se pudo exportar a CSV: {e}")

def menu():
    gestor = CalculadoraGastos()
    while True:
        print("\n--- Menu Calculadora de Gastos ---")
        print("1) Registrar nuevo gasto")
        print("2) Ver resumen de gastos por mes")
        print("3) Ver resumen de gastos por categoria")
        print("4) Exportar datos a CSV")
        print("5) Salir")

        opcion = input("Elige una opcion: ").strip()
        if opcion == "1":
            desc = input("Descripcion del gasto: ").strip()
            monto = input("Monto: ").strip()
            fecha = input("Fecha (DD/MM/AAAA): ").strip()
            cat = input("Categoria: ").strip()
            gestor.registrar_gasto(desc, monto, fecha, cat)
        elif opcion == "2":
            gestor.resumen_por_mes()
        elif opcion == "3":
            gestor.resumen_por_categoria()
        elif opcion == "4":
            gestor.exportar_csv()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion invalida, intente de nuevo.")

if __name__ == "__main__":
    menu()
