def main():
    try:
        entrada = input("Ingrese un número entero entre 1 y 10: ")
        
        if not entrada.isdigit():
            raise ValueError("Debe ingresar un valor numérico entero.")
        
        numero = int(entrada)
        if numero < 1 or numero > 10:
            raise ValueError("El número debe estar dentro del rango 1 a 10.")
        
        with open("tabla_propuesto.txt", "w", encoding="utf-8") as archivo:
            archivo.write(f"Tabla de multiplicar del {numero}\n")
            archivo.write("-" * 30 + "\n")
            for i in range(1, 13):
                archivo.write(f"{numero} x {i} = {numero * i}\n")
        
        print("El archivo 'tabla_propuesto.txt' fue generado correctamente.")
    
    except ValueError as ve:
        print("Error de validación:", ve)
    except IOError:
        print("No fue posible escribir en el archivo de salida.")
    except Exception as e:
        print("Error inesperado:", e)

if __name__ == "__main__":
    main()
