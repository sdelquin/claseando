# UT2 - Las mates molan!

La actividad consiste en hacer varios programas *Python*:

## Programa 1

Las ecuaciones de segundo grado tienen la forma:

$$ ax^2 + bx + c = 0 $$

El programa debe cumplir con las siguientes especificaciones:

1. Leer los coeficientes *a*, *b* y *c* desde la línea de comandos.
2. Controlar los siguientes casos:
    - Si $a=0$ entonces la ecuación ya no es de segundo grado, y su solución es: $x=\frac{-c}{b}$
    - Si el discriminante $b^2-4ac < 0$ entonces la ecuación no tiene solución real.
3. Imprimir las dos soluciones que tiene la ecuación, según estas fórmulas:

$$ x_1 = \frac{-b + \sqrt{b^2 - 4ac}}{2a} $$
$$ x_2 = \frac{-b - \sqrt{b^2 - 4ac}}{2a} $$

### Ejemplo de comprobación

#### Entrada

~~~console
python programa1.py 1 -5 6
~~~

#### Salida

~~~
x1 = 3
x2 = 2
~~~
