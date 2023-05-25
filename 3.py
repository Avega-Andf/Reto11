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


def matriztranspuesta(matriz,columnas, filas):
    """
    Calcula la matriz traspuesta de una matriz dada.

    Args:
    - matriz: una lista de listas que representa la matriz original.
    - columnas: número de columnas de la matriz original.
    - filas: número de filas de la matriz original.

    Returns:
    - matriztranspuesta: una lista de listas que representa la matriz traspuesta de la matriz original.
      La matriz traspuesta también se imprime utilizando la función imprimirmatriz(mat) antes de ser retornada.
    """
    matriztrans = [] # Se crea una lista vacia, que sera la matriz
    for j in range(columnas):
        filatrans = [] # Lista que se añade a la matriz
        for i in range(filas):
            filatrans.append(matriz[i][j]) #Cada elemento [i][j] pasa a ser el elemento [j][i] de la matriz
        matriztrans.append(filatrans)
    imprimirmatriz(matriztrans)
    return matriztrans
    


if __name__ == "__main__":
    # Se llaman las funciones y se imprimen las matrices
    filas = int(input("Ingrese el número de filas de la  matriz: "))
    columnas = int(input("Ingrese el número de columnas de la matriz: "))
    print("Matriz:")
    matriz = crearmatriz(filas, columnas)
    
    print("Matriz transpuesta: ")
    matrizt = matriztranspuesta(matriz, columnas, filas)