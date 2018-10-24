# UT2-A1: ¿Me da cambio por favor?

La actividad consiste en hacer un programa Python que:

1. Lea una cantidad (ENTERA) de euros como argumento desde la línea de comandos.
2. Devuelva la cantidad de billetes de 50€, 20€, 10€, 5€; y de monedas de 2€ y 1€.

> Detalles a tener en cuenta:
> 1. Si no hay billetes/monedas de alguna cantidad, **NO** mostrar esos mensajes.
> 2. El fichero se deberá llamar `main.py`.

**Ejemplo:**

`$> python main.py 313`

> Entrada: 313
> Salida:
>   * 6 billetes de 50€.
>   * 1 billete de 10€.
>   * 1 moneda de 2€.
>   * 1 moneda de 1€.

## Vinculación con el repositorio `imw`

Clonamos nuestro repositorio en la **máquina de desarrollo**:
~~~console
sdelquin@imw:~$ git clone git@github.com:sdelquin/imw.git
...
~~~

Creamos una estructura para las actividades de esta unidad:
~~~console
sdelquin@imw:~$ mkdir -p imw/ut2/a1
~~~

Creamos el entorno virtual para esta actividad:

~~~console
sdelquin@imw:~$ cd imw/ut2/a1/
sdelquin@imw:~/imw/ut2/a1$ pipenv install
Creating a virtualenv for this project…
Pipfile: /home/sdelquin/imw/ut2/a1/Pipfile
Using /usr/bin/python3.7 (3.7.0) to create virtualenv…
...
~~~

Creamos el fichero que contendrá el código de nuestro programa:

~~~console
sdelquin@imw:~/imw/ut2/a1$ touch main.py
sdelquin@imw:~/imw/ut2/a1$ tree
.
├── main.py
├── Pipfile
└── Pipfile.lock

0 directories, 3 files
sdelquin@imw:~/imw/ut2/a1$
~~~

Lanzamos *ATOM* en la carpeta actual para poder editar los ficheros con más facilidad:

~~~console
sdelquin@imw:~/imw/ut2/a1$ atom .
~~~

A medida que tengamos escrito código en el fichero `main.py` podemos ir ejecutando desde la *terminal* con los siguientes comandos:

~~~console
sdelquin@imw:~/imw/ut2/a1$ pipenv shell
Launching subshell in virtual environment…
sdelquin@imw:~/imw/ut2/a1$  . /home/sdelquin/.local/share/virtualenvs/a1-8YVffccZ/bin/activate
(a1) sdelquin@imw:~/imw/ut2/a1$
~~~

Desde ahí podemos lanzar nuestro programa cada vez que queramos con:

~~~console
(a1) sdelquin@imw:~/imw/ut2/a1$ python main.py
(a1) sdelquin@imw:~/imw/ut2/a1$
~~~

## Información a entregar

Se deberá entregar la *url* al commit en el repositorio privado *GitHub* de la asignatura *IMW*, apuntando al fichero que contiene el código Python. La *url* debe tener la siguiente estructura:

```
https://github.com/<usuario>/imw/blob/<id del commit>/<ut>/<actividad>/main.py
```

> ⚠️ Al subir la *url*, es importante crear un enlace. Es decir, poner un `href` a la *url* anterior, y no pegar el texto tal cual.
