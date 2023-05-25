def imprimirmatriz(mat):
    """
    Imprime la matriz en formato de matriz.

    Args:
    - mat: una lista de listas que representa una matriz.

    """
    for i in range(len(mat)):
        print(mat[i])

def primeramatriz(filas1, columnas1):
    """
    Solicita al usuario ingresar los elementos de la primera matriz y la devuelve.

    Args:
    - filas1: número de filas de la primera matriz.
    - columnas1: número de columnas de la primera matriz.

    Returns:
    - matriz: una lista de listas que representa la primera matriz ingresada por el usuario.
    """
    matriz = []
    for i in range(filas1):
        fila = []
        for j in range(columnas1):
            n = int(input('Ingrese el elemento de la primera matriz (' + str(i+1)+',' +str(j+1) + '): '))
            fila.append(n)
        matriz.append(fila)
    imprimirmatriz(matriz)
    return matriz

def segundamatriz(filas2, columnas2):
    """
    Solicita al usuario ingresar los elementos de la segunda matriz y la devuelve.

    Args:
    - filas2: número de filas de la segunda matriz.
    - columnas2: número de columnas de la segunda matriz.

    Returns:
    - matriz: una lista de listas que representa la segunda matriz ingresada por el usuario.
    """
    matriz = []
    for i in range(filas2):
        fila = []
        for j in range(columnas2):
            n = int(input('Ingrese el elemento de la segunda matriz (' + str(i+1)+',' +str(j+1) + '): '))
            fila.append(n)
        matriz.append(fila)
    imprimirmatriz(matriz)
    return matriz

def productodematrices(matriz1, matriz2, columnas1, filas1, columnas2, filas2):
    """
    Realiza la multiplicación de dos matrices y devuelve el resultado si la columna de la primera matriz es del mismo tamaño que la fila de la segunda matriz.
    Si las dimensiones no son válidas, muestra un mensaje de error.

    Args:
    - matriz1: primera matriz.
    - matriz2: segunda matriz.
    - columnas1: número de columnas de la primera matriz.
    - filas1: número de filas de la primera matriz.
    - columnas2: número de columnas de la segunda matriz.
    - filas2: número de filas de la segunda matriz.

    Returns:
    - resultado: una lista de listas que representa la matriz resultante de la multiplicación de las matrices si las dimensiones son válidas.
      Si las dimensiones no son válidas, retorna None.
    """
    if columnas1 == filas2: # Para poder realizar el producto de matrices se debe cumplir esta condicion, el numero de columnas de la primera matriz debe ser igual al numero de filas de la segunda matriz
        resultado = [] # Se crea una lista para almacenar la matriz resultado
        for i in range(filas1): # Bucle que recorre las filas de la primera matriz
            fila = [] # Se crea una lista vacia para crear la matriz
            for j in range(columnas2): # Se recorre las columnas de la matriz 2
                elemento = 0
                for k in range(filas2): # Se multiplica fila de la matriz 1 por columna de la matriz 2, (valor por valor), y se van sumando los resultados, se hace por cada fila de la segunda matriz
                    elemento += matriz1[i][k] * matriz2[k][j]
                fila.append(elemento) # Se va creando una lista por cada iteracion
            resultado.append(fila) # Cada lista se ve añadiendo a la matriz
    else: 
        print("El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz")
        return None
    
    print("El resultado de la multiplicación de matrices es:")
    imprimirmatriz(resultado)
    return resultado


if __name__ == "__main__":
    # Se llaman las funciones, y se imprimen las matrices
    filas1 = int(input("Ingrese el número de filas de la primera matriz: "))
    columnas1 = int(input("Ingrese el número de columnas de la primera matriz: "))
    print("Matriz 1:")
    matriz1 = primeramatriz(filas1, columnas1)

    filas2 = int(input("Ingrese el número de filas de la segunda matriz: "))
    columnas2 = int(input("Ingrese el número de columnas de la segunda matriz: "))
    print("Matriz 2:")
    matriz2 = segundamatriz(filas2, columnas2)

    productodematrices(matriz1, matriz2, columnas1, filas1, columnas2, filas2)