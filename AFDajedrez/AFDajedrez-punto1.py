import re

class AFDAjedrez:
    def __init__(self):
        # q0: inicio, q1: pos orígen, q2: acción, q3: destino
        self.estado_aceptacion = "q_acc"

    def validar_movimiento(self, cadena):

        patron = r'^([a-zA-Z0-9]+)\s*(->|[xX]|\s)\s*([a-zA-Z0-9]+)$'
        if re.match(patron, cadena.strip()):
            return "ACEPTADO"
        return "RECHAZADO"

if __name__ == "__main__":
    pruebas = ["p->k4", "kbp X qn", "Qxe5", "e2 e4"]
    print("Movimientos Ajedrez")
    for p in pruebas:
        print(f"Entrada: {p:10} | Resultado: {AFDAjedrez().validar_movimiento(p)}")
