def leer_numeros(nombre):
    try:
        with open(nombre, 'r', encoding="utf-8") as archi:
            suma = 0
            contador = 0

            for i, ln in enumerate(archi, start=1):
                try:
                    numero = int(ln.strip())
                    suma += numero
                    contador += 1
                except ValueError:
                    print(f"Error en línea {i}: '{ln.strip()}' no es un número válido")

        if contador > 0:
            print("\nResultados:")
            print(f"uma total: {suma}")
            print(f"Promedio: {suma/contador:.2f}")
        else:
            print("No se encontraron números válidos en el archivo.")

    except FileNotFoundError:
        print(f"No existe el archivo llamado '{nombre}'.")

nombre = input("Digite nombre del archivo completo (ejemplo.txt): ")
leer_numeros(nombre)
