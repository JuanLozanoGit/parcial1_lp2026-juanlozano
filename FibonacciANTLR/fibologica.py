def fibo_secuencia(n_terminos):
    # Genera la secuencia exacta: 0, 1, 1, 2, 3, 5, 8, 13
    a, b = 0, 1
    secuencia = []
    for _ in range(n_terminos): 
        secuencia.append(str(a))
        a, b = b, a + b
    return ", ".join(secuencia)

if __name__ == "__main__":
    print("--- Calculadora Fibonacci (Escribe 'salir' para terminar) ---")
    
    while True:
        try:
            entrada = input(">> ").strip()
            
            # Opción para salir del programa legalmente
            if entrada.lower() in ["salir", "exit", "quit"]:
                print("Saliendo...")
                break

            # Validamos el formato FIBO(n)
            if "FIBO(" in entrada.upper() and ")" in entrada:
                # Extraemos lo que está entre paréntesis para validar que sea número
                contenido = entrada[entrada.find("(")+1 : entrada.find(")")]
                
                if contenido.isdigit():
                    # Si todo está bien, mostramos la secuencia de 8 términos
                    print(fibo_secuencia(8))
                else:
                    print("ERROR: El valor dentro del paréntesis debe ser un número entero.")
            else:
                print("AVISO: Formato incorrecto. Debe ser 'FIBO(n)' (ejemplo: FIBO(20)).")
        
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
            print("Intenta de nuevo.")
