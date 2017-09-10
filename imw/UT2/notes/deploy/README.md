# Despliegue

El **despliegue** es el mecanismo que permite pasar un proyecto de software, desde la *máquina de desarrollo* al *servidor de producción*.

Supongamos que vamos a desplegar un proyecto cuya carpeta raíz se denomina `hogwarts`.

## Preparación del entorno en la máquina de producción

Hay que seguir los pasos descritos en [los apuntes de la UT1](http://imw.claseando.es/UT1/pythonconf/).

### Notas

1. Tener en cuenta que habrá que sustituir la carpeta `helloworld` por `hogwarts`.
2. En vez de hacer el apartado *Creación del "Hola Mundo"*, tendríamos que copiar el código de nuestro proyecto desde la máquina de desarrollo a la máquina de producción:

    ```console
    ~|🍺  cd hogwarts
    ~/hogwarts|🍺  scp -r * hillvalley.home:~/imw/hogwarts
    vm.cpython-35.pyc                                                          100% 2617     2.6KB/s   00:00
    main.py                                                                    100%  996     1.0KB/s   00:00
    nginx.conf                                                                 100%  204     0.2KB/s   00:00
    run.sh                                                                     100%  114     0.1KB/s   00:00
    style.css                                                                  100%  495     0.5KB/s   00:00
    supervisor.conf                                                            100%  258     0.3KB/s   00:00
    index.html                                                                 100% 1436     1.4KB/s   00:00
    run_process.html                                                           100%  874     0.9KB/s   00:00
    uwsgi.ini                                                                  100%  145     0.1KB/s   00:00
    vm.py                                                                      100% 1616     1.6KB/s   00:00
    ~/hogwarts|🍺
    ```
3. Recordar la instalación, en la *máquina de producción* y con el entorno virtual *activado*, los siguientes paquetes:

    ```console
    (hogwarts) sdelquin@hillvalley:~/imw/hogwarts$ pip install flask uwsgi
    Collecting flask
      Using cached Flask-0.11.1-py2.py3-none-any.whl
    Collecting uwsgi
    Collecting Jinja2>=2.4 (from flask)
      Using cached Jinja2-2.8-py2.py3-none-any.whl
    Collecting Werkzeug>=0.7 (from flask)
      Using cached Werkzeug-0.11.11-py2.py3-none-any.whl
    Collecting click>=2.0 (from flask)
      Using cached click-6.6-py2.py3-none-any.whl
    Collecting itsdangerous>=0.21 (from flask)
    Collecting MarkupSafe (from Jinja2>=2.4->flask)
    Installing collected packages: MarkupSafe, Jinja2, Werkzeug, click, itsdangerous, flask, uwsgi
    Successfully installed Jinja2-2.8 MarkupSafe-0.23 Werkzeug-0.11.11 click-6.6 flask-0.11.1 itsdangerous-0.24 uwsgi-2.0.14
    (hogwarts) sdelquin@hillvalley:~/imw/hogwarts$
    ```

## Automatizando el despliegue

Para no estar utilizando continuamente el comando `scp`, existen herramientas que permiten automatizar la copia y las acciones posteriores que se quieran llevar a cabo.

Una de esas herramientas es `fabric3`. Se trata de un paquete *Python*. Procedemos a su instalación, en la **máquina de desarrollo** y con el entorno virtual `hogwarts` activado:

```console
~|🍺  workon hogwarts
(hogwarts) ~|🍺  cd hogwarts
(hogwarts) ~/hogwarts|🍺  pip install fabric3
Collecting fabric3
  Using cached Fabric3-1.12.post1-py3-none-any.whl
Requirement already satisfied: six>=1.10.0 in /Users/sdelquin/.virtualenvs/hogwarts/lib/python3.5/site-packages (from fabric3)
Collecting paramiko<2.0,>=1.17.2 (from fabric3)
  Downloading paramiko-1.18.1-py2.py3-none-any.whl (172kB)
    100% |████████████████████████████████| 174kB 1.6MB/s
Collecting pycrypto!=2.4,<3.0,>=2.1 (from paramiko<2.0,>=1.17.2->fabric3)
Collecting ecdsa<2.0,>=0.11 (from paramiko<2.0,>=1.17.2->fabric3)
  Using cached ecdsa-0.13-py2.py3-none-any.whl
Installing collected packages: pycrypto, ecdsa, paramiko, fabric3
Successfully installed ecdsa-0.13 fabric3-1.12.post1 paramiko-1.18.1 pycrypto-2.6.1
(hogwarts) ~/hogwarts|🍺
```

A continuación tendremos que crear un fichero denominado `fabfile.py`:

```console
(hogwarts) ~/hogwarts|🍺  vi fabfile.py
```

> Contenido:
> ```python
> from fabric.api import env, cd, put, run
> 
> # nombre de la máquina de producción
> env.hosts = ["hillvalley.home"]
> # env.user
> # env.password
> 
> # ruta al proyecto en la máquina de producción
> PROJECT_PATH = "/home/sdelquin/imw/hogwarts"
> 
> 
> def deploy():
>     put("*", PROJECT_PATH)
>     run("supervisorctl restart hogwarts")
> ``

Esto nos va a permitir desplegar con el siguiente comando:

```console
(hogwarts) ~/hogwarts|🍺  fab deploy
```
