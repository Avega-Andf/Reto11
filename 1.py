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
        fila = [] # Se inicia y se vacia la lista fila en cada iteracion
        for j in range(columnas1):
            n = int(input('Ingrese el elemento de la primera matriz (' + str(i+1)+',' +str(j+1) + '): ')) #Itera por cada elemento de la matriz
            fila.append(n) # # Agrega el elemento ingresado por el usuario
        matriz.append(fila) # Se añade la lista "lista" a la matriz
    imprimirmatriz(matriz)
    return matriz # Retorna una lista de listas


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


def sumadematrices(matriz1, matriz2, filas1, columnas1, filas2, columnas2):
    """
    Realiza la suma de dos matrices y devuelve el resultado si las dimensiones son iguales.
    Si las dimensiones no son iguales, muestra un mensaje de error.
    
    Args:
    - matriz1: primera matriz.
    - matriz2: segunda matriz.
    - filas1: número de filas de la primera matriz.
    - columnas1: número de columnas de la primera matriz.
    - filas2: número de filas de la segunda matriz.
    - columnas2: número de columnas de la segunda matriz.
    
    Returns:
    - matriz1: una lista de listas que representa la matriz resultante de la suma de las matrices si las dimensiones son iguales.
        Si las dimensiones no son iguales, retorna un mensaje de error.
    """
    if filas1 == filas2 and columnas1 == columnas2: # Revisa que las filas y columnas sean iguales (Requisito para que se puedan sumar las matrices)
        matrizsuma = [] # Crear una matriz vacía para almacenar el resultado de la suma
        for i in range(filas1):
            fila = []
            for j in range(columnas1):
                # Restar los elementos correspondientes de las matrices
                suma = matriz1[i][j] + matriz2[i][j]
                fila.append(suma)
            matrizsuma.append(fila)
        print("Matriz1 + Matriz2 =")
        imprimirmatriz(matrizsuma) # Imprimir el resultado obtenido
        return matrizsuma
    else: # Mensaje si no cumple la condición
        print("El número de filas y de columnas deben ser iguales para poder realizar la suma de matrices")

def restadematrices(matriz1, matriz2, filas1, columnas1, filas2, columnas2):
    """
    Realiza la resta de dos matrices y devuelve el resultado si las dimensiones son iguales.
    Si las dimensiones no son iguales, muestra un mensaje de error.
    
    Args:
    - matriz1: primera matriz.
    - matriz2: segunda matriz.
    - filas1: número de filas de la primera matriz.
    - columnas1: número de columnas de la primera matriz.
    - filas2: número de filas de la segunda matriz.
    - columnas2: número de columnas de la segunda matriz.
    
    Returns:
    - matrizresultante: una lista de listas que representa la matriz resultante de la resta de las matrices si las dimensiones son iguales.
      Si las dimensiones no son iguales, retorna un mensaje de error.
    """
    if filas1 == filas2 and columnas1 == columnas2: # Revisa que las filas y columnas sean iguales (Requisito para que se puedan restar las matrices)
        matrizresta = [] # Crear una matriz vacía para almacenar el resultado de la resta
        for i in range(filas1):
            fila = []
            for j in range(columnas1):
                # Restar los elementos correspondientes de las matrices
                resta = matriz1[i][j] - matriz2[i][j]
                fila.append(resta)
            matrizresta.append(fila)
        print("Matriz1 - Matriz2 =")
        imprimirmatriz(matrizresta) # Imprimir el resultado obtenido
        return matrizresta
    else: # Mensaje si no cumple la condición
        print("El número de filas y de columnas deben ser iguales para poder realizar la resta de matrices")

if __name__ == "__main__":
    # Se llaman las funciones, y se imprimen las matrices
    filas1 = int(input("ingrese el numero de filas de la primera matriz: "))
    columnas1 = int(input("ingrese el numero de filas de la segunda amtriz: "))
    print("Matriz 1:")
    matriz1 = primeramatriz(filas1, columnas1)
    
    filas2 = int(input("ingrese el numero de filas de la segunda matriz: "))
    columnas2 = int(input("ingrese el numero de filas de la segund matriz: "))
    print("Matriz 2:")
    matriz2 = segundamatriz(filas2, columnas2)
    
    suma = sumadematrices(matriz1, matriz2, filas1, columnas1, filas2, columnas2)
    resta = restadematrices(matriz1, matriz2, filas1, columnas1, filas2, columnas2)