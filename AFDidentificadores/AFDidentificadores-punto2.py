def afd_identificador(cadena):
    estado = 0 # 0: Inicio, 1: Estado de Aceptación, 2: Error
    
    for char in cadena:
        if estado == 0:
            if char.isalpha():
                estado = 1
            else:
                estado = 2
                break
        elif estado == 1:
            if char.isalnum():
                estado = 1
            else:
                estado = 2
                break
                
    return "ACEPTE" if estado == 1 else "NO ACEPTE"

# Pruebas solicitadas
pruebas = ["miVariable", "ID2026", "A", "123error", "var_con_error"]
print("--- Pruebas de Identificadores ---")
for p in pruebas:
    print(f"ID: {p:15} | Resultado: {afd_identificador(p)}")
