def main():
    directorio = []
    try:
        with open("directorio.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                partes = linea.strip().split(";")
                
                if len(partes) != 5:
                    raise ValueError(f"Línea con formato incorrecto: {linea}")
                
                persona = {
                    "id": partes[0],
                    "nombre": partes[1],
                    "apellido": partes[2],
                    "celular": partes[3],
                    "fecha_nacimiento": partes[4]
                }
                
                directorio.append(persona)
        
        print("Directorio cargado:")
        for p in directorio:
            print(p)
    
    except FileNotFoundError:
        print("El archivo 'directorio.txt' no existe en la carpeta actual.")
    except ValueError as ve:
        print("Error en los datos:", ve)
    except Exception as e:
        print("Error inesperado:", e)

if __name__ == "__main__":
    main()
