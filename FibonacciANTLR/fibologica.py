def fibo_secuencia(n_terminos):
    # Secuencia
    a, b = 0, 1
    secuencia = []
    for _ in range(n_terminos): 
        secuencia.append(str(a))
        a, b = b, a + b
    return ", ".join(secuencia)

if __name__ == "__main__":
    print("Calculadora Fibonacci")
    
    while True:
        try:
            entrada = input(">> ").strip()
            
            # Salir
            if entrada.lower() in ["salir", "exit", "quit"]:
                print("Saliendo...")
                break

            # Validacion
            if "FIBO(" in entrada.upper() and ")" in entrada:
                # Contenido numero
                contenido = entrada[entrada.find("(")+1 : entrada.find(")")]
                
                if contenido.isdigit():
                    # Ejemoplo secuencia
                    print(fibo_secuencia(8))
                else:
                    print("ERROR: El valor tiene que ser un numero entero.")
            else:
                print("AVISO: Debe ser 'FIBO(n).")
        
        except Exception as e:
            print(f"Error {e}")
            print("Intenta de nuevo.")
