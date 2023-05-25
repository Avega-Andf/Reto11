# RETO 11 
### 1. Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

<details><summary>codigo</summary><p>

``` python
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
```
</p></details></br>

### 2. Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.


<details><summary>codigo</summary><p>

``` python
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
```
</p></details></br>

### 3. Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.
<details><summary>codigo</summary><p>

``` python
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
```
</p></details></br>

### 4. Desarrollar un programa que sume los elementos de una columna dada de una matriz.

<details><summary>codigo</summary><p>

``` python
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

```
</p></details></br>

### 5. Desarrollar un programa que sume los elementos de una fila dada de una matriz.
<details><summary>codigo</summary><p>

``` python
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
```
</p></details></br>


#### Gracias por leer :D
