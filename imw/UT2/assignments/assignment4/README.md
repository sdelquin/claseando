# UT2-A4: Secuenciando!

La actividad consiste en hacer varios programas *python*:

## Programa1

El programa debe cumplir con las siguientes especificaciones:

1. Leer un número de DNI por línea de comandos. (Sólo el número sin letra!)
2. La última letra del DNI puede calcularse a partir de sus números. Para ello sólo tienes que dividir el número por *23*, y quedarte con el resto. El resto es un número entre 0 y 22. La letra que corresponde a cada número la tienes en esta tabla:
![](img/DNI_letters.png)
3. La salida del programa debe ser el número del DNI más la letra calculada. Todo junto! Es decir, 12345678Y (por ejemplo)

> NOTA: Hacer este programa usando sólo cadenas! No se permite el uso de listas.

### Ejemplo de comprobación

Puedes comprobar el programa con tu propio DNI.

## Programa2

El programa debe cumplir con las siguientes especificaciones:

1. Pon el siguiente código al principio de tu programa:
    ```python
    import random

    NUCLEOBASES = "ATGC"
    DNA_SIZE = 100

    sequence = "".join([random.choice(NUCLEOBASES) for i in range(DNA_SIZE)])
    ```

2. Mostrar por pantalla el número de bases de cada tipo, recorriendo la variable `sequence`. Es decir, habrá que mostrar:

- `Adenine: XX`
- `Guanine: XX`
- `Cytosine: XX`
- `Thymine: XX`

## Programa3

El programa debe cumplir con las siguientes especificaciones:

1. Leer un número `k` (enteros positivo) y una cadena, por línea de comandos.
2. Emitir un error si el número introducido no es positivo, y salir del programa.
3. Decir cuántas palabras tienen longitud igual a `k`.

### Ejemplo de comprobación

```console
$> python3 programa3.py 4 "esto es una cadena de prueba para probar mi programa"
```

Salida: `Hay 2 palabras de tamaño 4`

## Programa4

El programa debe cumplir con las siguientes especificaciones:

1. Leer un número `h`(entero positivo) por línea de comandos.
2. Emitir un error si el número no es positivo, y salir del programa.
3. Pedir `h` valores numéricos flotantes por teclado, e introducirlos en una lista.
4. Calcular la media de los valores de la lista.
5. Mostrar la media calculada.

### Ejemplo de comprobación

Datos de entrada:

- `h` = 6
- Valores: `7, 4, 8, 10, 9, 1`

Salida: `6.5`

> No se pueden utilizar funciones predefinidas como `sum`.

## Ficheros a entregar

Se deberán subir 2 ficheros:

1. `<fichero>.zip` con los ficheros `.py` que contienen el código de tus programas.
2. `<fichero>.pdf` con el código fuente de tus programas.
