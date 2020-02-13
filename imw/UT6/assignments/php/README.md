# UT6-A1: Introducción a PHP

Para varios ejercicios se necesita utilizar la función `mt_rand`, la cual recibe dos números y retorna, como resultado, un número aleatorio entre el primero y el segundo. Por ejemplo, `mt_rand(10, 20)` devuelve un número aleatorio entre 10 y 20 (ambos incluidos).

## Ejercicio 1: Imagen aleatoria

Crea una página PHP que muestre de forma aleatoria dos imágenes. Es decir, se muestra una u otra de forma aleatoria e impredecible.

> Ver función `mt_rand`: http://php.net/manual/es/function.mt-rand.php

## Ejercicio 2: Cálculo de salario

Lee el nombre, los apellidos, el salario (número con decimales) y la edad de una persona (un número) en un formulario. Recoge los datos y con ellos calcula un nuevo salario para esa persona en base a esta situación:

- Si el salario es mayor de 2000 euros, no cambiará.
- Si el salario está entre 1000 y 2000:
    + Si además la edad es mayor de 45 años, se sube un 3%.
    + Si la edad es menor de 45 o igual, se sube un 10%.
- Si el salario es menor de 1000:
    + Los menores de 30 años cobrarán, a partir de ahora, exactamente 1100 euros.
    + De 30 a 45 años, sube un 3%.
    + A los mayores de 45 años, sube un 15%.

## Ejercicio 3: Fondo aleatorio

Crea una página PHP que ponga de fondo un color aleatorio. Para ello recuerda que en CSS el color de fondo se puede realizar mediante la función `rgb()` a la que se le pasan tres números del 0 al 255, el primero es el nivel de rojo, el segundo el de verde y el tercero el de azul.

> Ver función `mt_rand`: http://php.net/manual/es/function.mt-rand.php

## Ejercicio 4: Creación de tabla

Crea un formulario que pida dos números (filas y columnas). Ambos tienen que valer 1 ó más, de no ser así se indica el error. El resultado será una tabla (se mostrará en la misma página del formulario) con el tamaño indicado.

## Subir los ejercicios a producción

Subir los ejercicios a la máquina de producción en estas URLs:
~~~
http://php.aluXXXX.me/ejer1/
http://php.aluXXXX.me/ejer2/
http://php.aluXXXX.me/ejer3/
http://php.aluXXXX.me/ejer4/
~~~

> Utiliza `index.php` como punto de entrada para cada uno de los ejercicios.

## Información a entregar

Se deberá entregar la **url al raíz de los ejercicios** junto a la **url al commit** en el repositorio privado *GitHub* de la asignatura *IMW*, apuntando a la carpeta que contiene los ficheros de código Php. La *url* debe tener la siguiente estructura:

```
https://github.com/<usuario>/imw/blob/<id del commit>/<ut>/<actividad>/
```

> ⚠️ Al subir la *url*, es importante crear un enlace. Es decir, poner un `href` a la *url* anterior, y no pegar el texto tal cual.
