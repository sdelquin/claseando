# Preparación del entorno de desarrollo

Cuando programamos, lo hacemos desde la *máquina de desarrollo*. Es ahí donde se codifica y se prueba nuestro software, que posteriormente, pasará a la *máquina de producción*, en un proceso conocido como *despliegue*.

## Instalando Python

Completa el apartado de `Instalación` de la [Configuración de Python](../../../UT1/notes/pythonconf/README.md) que hicimos en su momento, pero ahora **⚠️ SOBRE LA MÁQUINA DE DESARROLLO** (ignorar la creación del *primer entorno virtual* y la instalación de *uwsgi*).


## Ejecutando un programa de prueba

Vamos a hacer un mini programa que calcula el cuadrado de un número.

### Creación del entorno virtual

~~~console
sdelquin@imw:~$ mkdir -p webapps/square
sdelquin@imw:~$ cd webapps/square
sdelquin@imw:~/webapps/square$ pipenv install
Creating a virtualenv for this project…
Pipfile: /home/sdelquin/webapps/square/Pipfile
Using /usr/bin/python3.7 (3.7.0) to create virtualenv…
⠧Already using interpreter /usr/bin/python3.7
Using base prefix '/usr'
/usr/local/lib/python3.7/dist-packages/virtualenv.py:1041: DeprecationWarning: the imp module is deprecated in favour of importlib; see the module's documentation for alternative uses
  import imp
New python executable in /home/sdelquin/.local/share/virtualenvs/square-89hKHu9b/bin/python3.7
Also creating executable in /home/sdelquin/.local/share/virtualenvs/square-89hKHu9b/bin/python
Installing setuptools, pip, wheel...done.

Virtualenv location: /home/sdelquin/.local/share/virtualenvs/square-89hKHu9b
Creating a Pipfile for this project…
Pipfile.lock not found, creating…
Locking [dev-packages] dependencies…
Locking [packages] dependencies…
Updated Pipfile.lock (a65489)!
Installing dependencies from Pipfile.lock (a65489)…
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 0/0 — 00:00:00
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
sdelquin@imw:~/webapps/square$
~~~

### Escritura del código

~~~console
sdelquin@imw:~/webapps/square$ vi main.py
...
~~~

~~~python
import sys

print(int(sys.argv[1])**2)
~~~

Guardamos, salimos, y ejecutamos:

~~~console
sdelquin@imw:~/webapps/square$ pipenv run python main.py 3
9
sdelquin@imw:~/webapps/square$ pipenv run python main.py 7
49
sdelquin@imw:~/webapps/square$ pipenv run python main.py 231
53361
sdelquin@imw:~/webapps/square$
~~~

Otra alternativa es **activar la shell del entorno virtual de Python** y ejecutar de una forma más sencilla:

~~~console
(square) sdelquin@imw:~/webapps/square$ python main.py 3
9
(square) sdelquin@imw:~/webapps/square$ python main.py 7
49
(square) sdelquin@imw:~/webapps/square$ python main.py 231
53361
(square) sdelquin@imw:~/webapps/square$
~~~

## Instalación del editor de código

¿Atom? ¿Sublime-Text? ¿VSCode?
