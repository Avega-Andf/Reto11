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


def sumar_columna(matriz, columnasumar, filas ):
    """
    Calcula la suma de una columna específica en una matriz.

    Args:
    - matriz: una lista de listas que representa la matriz.
    - columnasumar: el índice de la columna a sumar (se resta 1 para ajustar a índices base 0).
    - filas: el número de filas de la matriz.

    Returns:
    - suma: la suma de los elementos de la columna especificada.
      Si la columna especificada no es válida, se imprime un mensaje de error y se devuelve el mensaje como retorno.
    """
    suma = 0
    columnasumar -= 1
    # Verificar si la columna escrita por el usuario es válida
    if columnasumar < 0 or columnasumar >= len(matriz[0]):
        mensaje = "Error: La columna especificada no es válida."
        print(mensaje)
        return mensaje

    # Sumar los elementos de la columna especificada
    for i in range(filas):
        suma += matriz[i][columnasumar]
    print("La suma de la columna " + str(columnasumar + 1)+ " es: "+ str(suma) )
    return suma


    
    
if __name__ == "__main__":
    # Se llama las funciones y se imprimen las amtrices
    filas = int(input("Ingrese el número de filas de la  matriz: "))
    columnas = int(input("Ingrese el número de columnas de la matriz: "))
    columnasumar = int(input("Ingrese la columna que quiere sumar, tomando la primera columna como 1: "))
    print("Matriz:")
    matriz = crearmatriz(filas, columnas)
    
    suma_columna = sumar_columna(matriz, columnasumar, filas)
