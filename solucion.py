# En este archivo debes implementar la función

def triangulo_simetrico(m: int, s: str) -> str:
    # TODO: validar altura mayor que 0 e imprimir "Error: La altura debe ser un entero positivo" y salir
    if m <= 0:
        print("Error: La altura debe ser un entero positivo")
        return
    else:
    # TODO: implementar la lógica para generar el triángulo simétrico en ASCII 
        for i in range(1,m+1):
            print(s*i)
        for i in range(m-1,0,-1):
            print(s*i)
