# Preparación del entorno de desarrollo

Cuando programamos, lo hacemos desde la *máquina de desarrollo*. Es ahí donde se codifica y se prueba nuestro software, que posteriormente, pasará a la *máquina de producción*, en un proceso conocido como *despliegue*.

## Instalando python

### Intérprete de *python3*

```console
root@hillvalley:~# apt-get install -y python3
Leyendo lista de paquetes... Hecho
Creando árbol de dependencias
Leyendo la información de estado... Hecho
Los paquetes indicados a continuación se instalaron de forma automática y ya no son necesarios.
  python-colorama-whl python-distlib-whl python-html5lib-whl python-requests-whl python-setuptools-whl
  python-six-whl python-stevedore python-urllib3-whl virtualenv-clone
Utilice «apt-get autoremove» para eliminarlos.
Se instalarán los siguientes paquetes extras:
  dh-python
Paquetes sugeridos:
  python3-doc python3-tk python3-venv
Se instalarán los siguientes paquetes NUEVOS:
  dh-python python3
0 actualizados, 2 nuevos se instalarán, 0 para eliminar y 0 no actualizados.
Se necesita descargar 0 B/87,5 kB de archivos.
Se utilizarán 321 kB de espacio de disco adicional después de esta operación.
Seleccionando el paquete python3 previamente no seleccionado.
(Leyendo la base de datos ... 45435 ficheros o directorios instalados actualmente.)
Preparando para desempaquetar .../python3_3.4.2-2_amd64.deb ...
Desempaquetando python3 (3.4.2-2) ...
Seleccionando el paquete dh-python previamente no seleccionado.
Preparando para desempaquetar .../dh-python_1.20141111-2_all.deb ...
Desempaquetando dh-python (1.20141111-2) ...
Procesando disparadores para man-db (2.7.0.2-5) ...
Configurando dh-python (1.20141111-2) ...
Configurando python3 (3.4.2-2) ...
running python rtupdate hooks for python3.4...
running python post-rtupdate hooks for python3.4...
root@hillvalley:~#
```

Podemos comprobar la instalación de *python3*:

```console
root@hillvalley:~# python3
Python 3.4.2 (default, Oct  8 2014, 10:45:20)
[GCC 4.9.1] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
root@hillvalley:~#
```

### Gestor de paquetes de *python*

```console
root@hillvalley:~# apt-get install -y python-pip
Leyendo lista de paquetes... Hecho
Creando árbol de dependencias
Leyendo la información de estado... Hecho
Los paquetes indicados a continuación se instalaron de forma automática y ya no son necesarios.
  python-colorama-whl python-distlib-whl python-html5lib-whl python-requests-whl python-setuptools-whl
  python-six-whl python-stevedore python-urllib3-whl virtualenv-clone
Utilice «apt-get autoremove» para eliminarlos.
Paquetes recomendados:
  python-dev-all
Se instalarán los siguientes paquetes NUEVOS:
  python-pip
0 actualizados, 1 nuevos se instalarán, 0 para eliminar y 0 no actualizados.
Se necesita descargar 0 B/114 kB de archivos.
Se utilizarán 481 kB de espacio de disco adicional después de esta operación.
Seleccionando el paquete python-pip previamente no seleccionado.
(Leyendo la base de datos ... 45574 ficheros o directorios instalados actualmente.)
Preparando para desempaquetar .../python-pip_1.5.6-5_all.deb ...
Desempaquetando python-pip (1.5.6-5) ...
Procesando disparadores para man-db (2.7.0.2-5) ...
Configurando python-pip (1.5.6-5) ...
root@hillvalley:~#
```

Algunos paquetes de *python* necesitan compilarse previamente a su instalación. Para ello debemos instalar las librerías de desarrollo del lenguaje:

```console
root@hillvalley:~# apt-get install -y python3-dev
Leyendo lista de paquetes... Hecho
Creando árbol de dependencias
Leyendo la información de estado... Hecho
Los paquetes indicados a continuación se instalaron de forma automática y ya no son necesarios.
  python-colorama-whl python-distlib-whl python-html5lib-whl python-requests-whl python-setuptools-whl
  python-six-whl python-stevedore python-urllib3-whl virtualenv-clone
Utilice «apt-get autoremove» para eliminarlos.
Se instalarán los siguientes paquetes extras:
  libpython3-dev libpython3.4 libpython3.4-dev python3.4-dev
Se instalarán los siguientes paquetes NUEVOS:
  libpython3-dev libpython3.4 libpython3.4-dev python3-dev python3.4-dev
0 actualizados, 5 nuevos se instalarán, 0 para eliminar y 0 no actualizados.
Se necesita descargar 41,3 MB de archivos.
Se utilizarán 59,5 MB de espacio de disco adicional después de esta operación.
Des:1 http://ftp.es.debian.org/debian/ jessie/main libpython3.4 amd64 3.4.2-1 [1.315 kB]
Des:2 http://ftp.es.debian.org/debian/ jessie/main libpython3.4-dev amd64 3.4.2-1 [39,5 MB]
Des:3 http://ftp.es.debian.org/debian/ jessie/main libpython3-dev amd64 3.4.2-2 [18,2 kB]
Des:4 http://ftp.es.debian.org/debian/ jessie/main python3.4-dev amd64 3.4.2-1 [420 kB]
Des:5 http://ftp.es.debian.org/debian/ jessie/main python3-dev amd64 3.4.2-2 [1.198 B]
Descargados 41,3 MB en 1s (22,2 MB/s)
Seleccionando el paquete libpython3.4:amd64 previamente no seleccionado.
(Leyendo la base de datos ... 45497 ficheros o directorios instalados actualmente.)
Preparando para desempaquetar .../libpython3.4_3.4.2-1_amd64.deb ...
Desempaquetando libpython3.4:amd64 (3.4.2-1) ...
Seleccionando el paquete libpython3.4-dev:amd64 previamente no seleccionado.
Preparando para desempaquetar .../libpython3.4-dev_3.4.2-1_amd64.deb ...
Desempaquetando libpython3.4-dev:amd64 (3.4.2-1) ...
Seleccionando el paquete libpython3-dev:amd64 previamente no seleccionado.
Preparando para desempaquetar .../libpython3-dev_3.4.2-2_amd64.deb ...
Desempaquetando libpython3-dev:amd64 (3.4.2-2) ...
Seleccionando el paquete python3.4-dev previamente no seleccionado.
Preparando para desempaquetar .../python3.4-dev_3.4.2-1_amd64.deb ...
Desempaquetando python3.4-dev (3.4.2-1) ...
Seleccionando el paquete python3-dev previamente no seleccionado.
Preparando para desempaquetar .../python3-dev_3.4.2-2_amd64.deb ...
Desempaquetando python3-dev (3.4.2-2) ...
Procesando disparadores para man-db (2.7.0.2-5) ...
Configurando libpython3.4:amd64 (3.4.2-1) ...
Configurando libpython3.4-dev:amd64 (3.4.2-1) ...
Configurando libpython3-dev:amd64 (3.4.2-2) ...
Configurando python3.4-dev (3.4.2-1) ...
Configurando python3-dev (3.4.2-2) ...
Procesando disparadores para libc-bin (2.19-18+deb8u4) ...
root@hillvalley:~#
```

## Mejorando los entornos virtuales

Existe una paquete *python* denominado `virtualenvwrapper`, que en realidad es un conjunto de herramientas para gestionar nuestros entornos virtuales, de una manera mucho más sencilla y funcional. Desde la *máquina de desarrollo*, y como usuario `root` ejecutamos lo siguiente:

```console
root@hillvalley:~# pip install virtualenvwrapper
Downloading/unpacking virtualenvwrapper
  Downloading virtualenvwrapper-4.7.2.tar.gz (90kB): 90kB downloaded
  Running setup.py (path:/tmp/pip-build-uqNyR1/virtualenvwrapper/setup.py) egg_info for package virtualenvwrapper

    Installed /tmp/pip-build-uqNyR1/virtualenvwrapper/pbr-1.10.0-py2.7.egg
    [pbr] Processing SOURCES.txt
    warning: LocalManifestMaker: standard file '-c' not found

    warning: no previously-included files found matching '.gitignore'
    warning: no previously-included files found matching '.gitreview'
    warning: no previously-included files matching '*.pyc' found anywhere in distribution
    warning: no files found matching '*.html' under directory 'docs'
    warning: no files found matching '*.css' under directory 'docs'
    warning: no files found matching '*.js' under directory 'docs'
    warning: no files found matching '*.png' under directory 'docs'
Requirement already satisfied (use --upgrade to upgrade): virtualenv in /usr/local/lib/python2.7/dist-packages (from virtualenvwrapper)
Requirement already satisfied (use --upgrade to upgrade): virtualenv-clone in /usr/lib/python2.7/dist-packages (from virtualenvwrapper)
Requirement already satisfied (use --upgrade to upgrade): stevedore in /usr/lib/python2.7/dist-packages (from virtualenvwrapper)
Installing collected packages: virtualenvwrapper
  Running setup.py install for virtualenvwrapper
    [pbr] Generating AUTHORS
    [pbr] AUTHORS complete (0.0s)
    [pbr] Reusing existing SOURCES.txt
    changing mode of build/scripts-2.7/virtualenvwrapper.sh from 644 to 755
    changing mode of build/scripts-2.7/virtualenvwrapper_lazy.sh from 644 to 755
    Skipping installation of /usr/local/lib/python2.7/dist-packages/virtualenvwrapper/__init__.py (namespace package)
    Installing /usr/local/lib/python2.7/dist-packages/virtualenvwrapper-4.7.2-nspkg.pth
    changing mode of /usr/local/bin/virtualenvwrapper.sh to 755
    changing mode of /usr/local/bin/virtualenvwrapper_lazy.sh to 755
Successfully installed virtualenvwrapper
Cleaning up...
root@hillvalley:~#
```

Vamos a hacer que nuestros entornos virtuales residan en la carpeta `~/.virtualenvs`. Para ello, desde la *máquina de desarrollo* y como *usuario no privilegiado*, haremos lo siguiente:

```console
sdelquin@hillvalley:~$ mkdir .virtualenvs
sdelquin@hillvalley:~$ vi .bashrc
```

(añadir al final del fichero)

> Contenido
```bash
...
export WORKON_HOME=~/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
...
```

Guardamos y salimos. A continuación ejecutamos:

```console
sdelquin@hillvalley:~$ source .bashrc
virtualenvwrapper.user_scripts creating /home/sdelquin/.virtualenvs/premkproject
virtualenvwrapper.user_scripts creating /home/sdelquin/.virtualenvs/postmkproject
virtualenvwrapper.user_scripts creating /home/sdelquin/.virtualenvs/initialize
virtualenvwrapper.user_scripts creating /home/sdelquin/.virtualenvs/premkvirtualenv
virtualenvwrapper.user_scripts creating /home/sdelquin/.virtualenvs/postmkvirtualenv
virtualenvwrapper.user_scripts creating /home/sdelquin/.virtualenvs/prermvirtualenv
virtualenvwrapper.user_scripts creating /home/sdelquin/.virtualenvs/postrmvirtualenv
virtualenvwrapper.user_scripts creating /home/sdelquin/.virtualenvs/predeactivate
virtualenvwrapper.user_scripts creating /home/sdelquin/.virtualenvs/postdeactivate
virtualenvwrapper.user_scripts creating /home/sdelquin/.virtualenvs/preactivate
virtualenvwrapper.user_scripts creating /home/sdelquin/.virtualenvs/postactivate
virtualenvwrapper.user_scripts creating /home/sdelquin/.virtualenvs/get_env_details
sdelquin@hillvalley:~$
```

## Creando entornos virtuales con *python3* 

Vamos a suponer que nuestros proyectos de *python* van a "colgar" de la carpeta `$HOME/imw`. Para ello, lo primero que haremos es crear dicha carpeta, como *usuario no privilegiado* desde la *máquina de desarrollo*:

```console
sdelquin@hillvalley:~$ mkdir imw
sdelquin@hillvalley:~$ ls -ld imw
drwxr-xr-x 2 sdelquin sdelquin 4096 oct 22 20:04 imw
sdelquin@hillvalley:~$ cd imw/
sdelquin@hillvalley:~/imw$ pwd
/home/sdelquin/imw
sdelquin@hillvalley:~/imw$
```

Ahora vamos a escribir un script *bash* que nos facilite la creación de nuestros entornos virtuales con *python3*.

```console
sdelquin@hillvalley:~$ mkdir bin
sdelquin@hillvalley:~$ cd bin/
sdelquin@hillvalley:~/bin$ vi mkv3
```

> Contenido:
> ```bash
> PROJECTS_DIR=$HOME/imw
> PYTHON3_PATH=`which python3`
> VIRTUALENVWRAPPER_PATH=/usr/local/bin/virtualenvwrapper.sh
> 
> mkdir $PROJECTS_DIR/$1
> source $VIRTUALENVWRAPPER_PATH
> mkvirtualenv --python=$PYTHON3_PATH -a $PROJECTS_DIR/$1 $1
> ```

Añadimos permisos de ejecución para nuestro script:

```console
sdelquin@hillvalley:~/bin$ chmod +x mkv3
sdelquin@hillvalley:~/bin$
```

Para poder ejecutar nuestro script desde cualquier ruta del sistema, tenemos que añadirlo al `PATH`. Para ello haremos lo siguiente:

```console
sdelquin@hillvalley:~$ vi .bashrc
sdelquin@hillvalley:~$
```

>  Contenido:
```bash
...
export PATH=$PATH:.:$HOME/bin
...
```

Para que los cambios hechos surtan efecto, tenemos que reparsear el fichero:

```console
sdelquin@hillvalley:~$ source .bashrc
sdelquin@hillvalley:~$
```

### Creando un entorno virtual de prueba

Vamos a crear un entorno virtual de prueba con *python3*. Lo llamaremos `test1`, y nuestro script hará lo siguiente:
1. Crear el directorio `/home/<usuario>/imw/test1`
2. Activar los comandos de `virtualenvwrapper`.
3. Crear el entorno virtual en `/home/<usuario>/.virtualenvs/test1`
4. Instalar en el entorno virtual *python3* y la librería estándar.

```console
sdelquin@hillvalley:~$ mkv3 test1
Running virtualenv with interpreter /usr/bin/python3
Using base prefix '/usr'
New python executable in /home/sdelquin/.virtualenvs/test1/bin/python3
Not overwriting existing python script /home/sdelquin/.virtualenvs/test1/bin/python (you must use /home/sdelquin/.virtualenvs/test1/bin/python3)
Installing setuptools, pip, wheel...done.
Setting project for test1 to /home/sdelquin/imw/test1
sdelquin@hillvalley:~$
```

Ahora ya podemos activar el entorno virtual con el siguiente comando:

```console
sdelquin@hillvalley:~$ workon test1
(test1) sdelquin@hillvalley:~/imw/test1$ python --version
Python 3.4.2
(test1) sdelquin@hillvalley:~/imw/test1$
```

Cuando el entorno virtual está activado aparece `(test1)` delante del prompt, y además hemos comprobado que la versión de *python* que estamos usando es la 3.

Igualmente, con el entorno virtual activado, podemos ejecutar otros comandos interesantes:
* `deactivate` (desactivar el entorno virtual)
* `rmvirtualenv` (borrar un entorno virtual)
* `cdproject` (nos lleva al directorio base de nuestro proyecto)
* `cdvirtualenv` (nos lleva al directorio base del entorno virtual)

### Ejecutando un programa de prueba

Como **usuario no privilegiado** ejecutamos lo siguiente:

```console
(test1) sdelquin@hillvalley:~/imw/test1$ vi main.py
```

> Contenido
```python
print("Esto funciona! " * 3)
```

Guardamos, salimos, y ejecutamos:

```console
(test1) sdelquin@hillvalley:~/imw/test1$ python main.py
Esto funciona! Esto funciona! Esto funciona!
(test1) sdelquin@hillvalley:~/imw/test1$
```

* [x] Vemos que todo está funcionando correctamente.

## Instalación del editor de código

Existen multitud de editores de código fuente, e incluso IDEs, pero nosotros vamos a usar **Sublime Text**. Para su instalación, desde la *máquina de desarrollo* y como usuario `root`, ejecutamos lo siguiente:

```console
root@hillvalley:~# mkdir tmp
root@hillvalley:~# cd tmp
root@hillvalley:~/tmp# wget https://download.sublimetext.com/sublime-text_build-3126_amd64.deb
--2016-10-16 14:35:39--  https://download.sublimetext.com/sublime-text_build-3126_amd64.deb
Resolviendo download.sublimetext.com (download.sublimetext.com)... 104.236.0.104
Conectando con download.sublimetext.com (download.sublimetext.com)[104.236.0.104]:443... conectado.
Petición HTTP enviada, esperando respuesta... 200 OK
Longitud: 7746994 (7,4M) [application/octet-stream]
Grabando a: “sublime-text_build-3126_amd64.deb”

sublime-text_build-3126_amd6 100%[=============================================>]   7,39M  4,85MB/s   en 1,5s

2016-10-16 14:35:42 (4,85 MB/s) - “sublime-text_build-3126_amd64.deb” guardado [7746994/7746994]

root@hillvalley:~/tmp# dpkg -i sublime-text_build-3126_amd64.deb
Seleccionando el paquete sublime-text previamente no seleccionado.
(Leyendo la base de datos ... 45464 ficheros o directorios instalados actualmente.)
Preparando para desempaquetar sublime-text_build-3126_amd64.deb ...
Desempaquetando sublime-text (3126) ...
Configurando sublime-text (3126) ...
Procesando disparadores para hicolor-icon-theme (0.13-1) ...
Procesando disparadores para mime-support (3.58) ...
root@hillvalley:~/tmp#
```

Miramos si se ha instalado correctamente, mostrando la versión de *Sublime Text*:

```console
root@hillvalley:~/tmp# subl --version
Sublime Text Build 3126
root@hillvalley:~/tmp#
```

### Instalación de `Package Control` para `Sublime Text`

Para ver la versión que tenemos instalada de *Sublime Text*:

![](img/SublimeText-Version.png)

Mostrar la consola de *Sublime Text*, pegar el código especificado en https://packagecontrol.io/installation (según versión del pograma) y pulsar ENTER:

![](img/SublimeText-Console.png)

Después de la instalación, deberían ver algo así:

![](img/SublimeText-PackageInstalled.png)

### Instalación del *linter* para *python*

En *Python* disponemos de una *guía de estilo*, que especifica cómo se debe escribir código fuente. Esta guía está definida en el [PEP8](http://www.recursospython.com/pep8es.pdf).

Para que nos sea más fácil la escritura de nuestro código *Python*, existe un paquete en *Sublime Text* que ya nos hace ese trabajo. Se denomina `Python Flake8 Lint`.

Pulsar `Mayús+Ctrl+P` para abrir el *Package Control*. Escribir `Package Control: Install Package`. A continuación buscar el siguiente paquete e instalarlo:

> Python Flake8 Lint

Este paquete permite chequear nuestro código *python* cada vez que guardemos (`CTRL-S`) y mostrar avisos para mejorar aquellas cuestiones sintácticas que no son correctas.

### Ajuste de las indentaciones

En *Python* son muy importante las **indentaciones** (bloques hacia adentro). Para evitar problemas, vamos a fijar que las indentaciones se hagan con espacios. Para ello hacemos lo siguiente:

![](img/SublimeText-IndentSpaces.png)

### Ignorar ciertos errores de Flake8

Existen ciertos errores del módulo `Flake8` que no nos interesa que nos salgan, porque no son especialmente importantes.

Para deshabilitarlos, lo que tenemos que hacer es acceder a los ajustes del paquete `Python Flake8 Lint` de la siguiente manera:

![](img/Flake8.png)

Y a continuación escribir el siguiente código:

```json
{
  "ignore": ["D100", "D101", "D102", "D103", "D105"],
}
```

Luego guardamos el fichero, y ya no tenemos que preocuparnos por los errores con los códigos que hemos especificado.
