from datetime import datetime

def validar_nombre_apellido(valor, campo):
    if not valor.strip():
        raise ValueError(f"El {campo} no puede estar vacío.")

    partes = valor.strip().split()
    for p in partes:
        if not p.isalpha():
            raise ValueError(f"El {campo} contiene caracteres inválidos: {valor}")

    return " ".join([p.capitalize() for p in partes])

def procesar_linea(linea):
    partes = linea.strip().split(";")
    
    if len(partes) != 5:
        raise ValueError(f"Línea con formato incorrecto: {linea}")
    
    id_str, nombre, apellido, celular, fecha_nac = partes

    if not id_str.isdigit():
        raise ValueError(f"ID no válido: {id_str}")

    if not celular.isdigit() or len(celular) != 9 or celular.startswith("0"):
        raise ValueError(f"Celular no válido: {celular}")

    nombre = validar_nombre_apellido(nombre, "nombre")
    apellido = validar_nombre_apellido(apellido, "apellido")

    try:
        fecha_obj = datetime.strptime(fecha_nac, "%d/%m/%Y")
        anio_actual = datetime.now().year
        if fecha_obj.year < 1900 or fecha_obj.year > anio_actual:
            raise ValueError(f"Año fuera de rango válido: {fecha_nac}")
        if fecha_obj > datetime.now():
            raise ValueError(f"La fecha no puede ser futura: {fecha_nac}")
    except ValueError:
        raise ValueError(f"Fecha de nacimiento inválida: {fecha_nac}")

    return {
        "id": int(id_str),
        "nombre": nombre,
        "apellido": apellido,
        "celular": celular,
        "fecha_nacimiento": fecha_nac
    }

def main():
    directorio = []
    try:
        ruta = input("Ingrese el nombre del archivo: ").strip()
        with open(ruta+".txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                try:
                    persona = procesar_linea(linea)
                    directorio.append(persona)
                except ValueError as ve:
                    print("Error en registro:", ve)
        
        if directorio:
            print("\nDirectorio cargado exitosamente:\n")
            for p in directorio:
                print(p)
        else:
            print("No se pudo cargar ningún registro válido.")
    
    except FileNotFoundError:
        print("Error: El archivo 'directorio.txt' no fue encontrado.")
    except Exception as e:
        print("Error inesperado:", e)

if __name__ == "__main__":
    main()
