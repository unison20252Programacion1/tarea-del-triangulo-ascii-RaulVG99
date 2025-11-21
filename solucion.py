# En este archivo debes implementar la función

def triangulo_simetrico(m: int, s: str) -> str:
    # TODO: validar altura mayor que 0 e imprimir "Error: La altura debe ser un entero positivo" y salir
    if m <= 0:
        print("Error: La altura debe ser un entero positivo")
        return
    else:
    # TODO: implementar la lógica para generar el triángulo simétrico en ASCII 
        n=2*m-1
        respuesta=""
        for i in range(n):
            respuesta=respuesta+s*(-abs(i-m+1)+m)+"\n"
        print(respuesta[0:-1])
