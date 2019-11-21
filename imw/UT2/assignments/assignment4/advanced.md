# UT2-A4 (avanzado): Secuenciando

Dada una serie de valores flotantes, se pide leer dichos valores por línea de comandos y calcular la menor distancia entre dos valores contiguos.

## Caso de uso

~~~console
$ python distances.py 4.3 1.2 3.9 3.2 9.2 11.1 0.12 3.2 8.91
La menor distancia es: 0.7
~~~

## Posible mejora

Incluir en la salida los valores que hacen que esa distancia se menor. En el ejemplo anterior:

~~~console
$ python distances.py 4.3 1.2 3.9 3.2 9.2 11.1 0.12 3.2 8.91
La menor distancia es: 0.7
Los valores son: 3.9 y 3.2
~~~

> Consejo:
> Usar bucle con `range`
