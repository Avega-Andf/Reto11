def imprimirmatriz(mat):
    """
    Imprime la matriz en formato de matriz.

    Args:
    - mat: una lista de listas que representa una matriz.

    """
    for i in range(len(mat)):
        print(mat[i])

def crearmatriz(filas1, columnas1):
    """
    Crea una matriz con los elementos ingresados por el usuario
    Args:
    - filas1: número de filas de la matriz.
    - columnas1: número de columnas de la matriz.

    Returns:
    - matriz: una lista de listas que representa la matriz creada a partir de la entrada del usuario.
      La matriz también se imprime utilizando la función imprimirmatriz(mat) antes de ser retornada.

    """
    matriz = []
    for i in range(filas1):
        fila = []
        for j in range(columnas1):
            n = int(input('Ingrese el elemento (' + str(i+1)+',' +str(j+1) + '): '))
            fila.append(n)
        matriz.append(fila)
    imprimirmatriz(matriz)
    return matriz


def sumar_fila(matriz, filasumar, filas ):
    """
    Calcula la suma de una fila específica en una matriz.

    Args:
    - matriz: una lista de listas que representa la matriz.
    - filasumar: el índice de la fila a sumar (se resta 1 para ajustar a índices base 0).
    - filas: el número de filas de la matriz.

    Returns:
    - suma: la suma de los elementos de la fila especificada.
      Si la fila especificada no es válida, se imprime un mensaje de error y se devuelve el mensaje como retorno.
    """
    suma = 0
    filasumar -= 1
    # Verificar si la fila es válida
    if filasumar < 0 or filasumar >= len(matriz[0]):
        mensaje = "Error: La fila especificada no es válida."
        print(mensaje)
        return mensaje

    # Sumar los elementos de la fila
    for j in range(filas):
        suma += matriz[filasumar][j]
    print("La suma de la fila " + str(filasumar + 1 )+ " es: "+ str(suma) )
    return suma


    
    
if __name__ == "__main__":
    # Se llama las funciones y se imprimen las amtrices
    filas = int(input("Ingrese el número de filas de la  matriz: "))
    columnas = int(input("Ingrese el número de columnas de la matriz: "))
    filasumar = int(input("Ingrese la fila que quiere sumar, tomando la primera fila como 1: "))
    print("Matriz:")
    matriz = crearmatriz(filas, columnas)
    
    suma_fila = sumar_fila(matriz, filasumar, filas)