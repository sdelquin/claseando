# Configuración de python

El objetivo de esta sección es configurar nuestro servidor web para que responda a peticiones que procesen código *python*.

## Instalación

Desde la *máquina de producción* y como usuario *root*, lo primero será instalar el intérprete de *python*:

```console
root@hillvalley:~# apt-get install -y python3
...
root@hillvalley:~#
```

Una vez finalizada la instalación, podemos probarla, sin necesidad de ser *root*. Desde un usuario no privilegiado podemos ejecutar:

```console
sdelquin@hillvalley:~$ python3
Python 3.4.2 (default, Oct  8 2014, 10:45:20)
[GCC 4.9.1] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
sdelquin@hillvalley:~$
```

Se puede observar que la versión de *python* instalada es la `3.4.2`. De momento, todo está correcto.

* [x] `python` instalado.

### Gestión de paquetes

Existe una herramienta que permite instalar paquetes *python*. Se llama `pip`. Para su instalación hacemos lo siguiente:

```console
root@hillvalley:~# apt-get install -y python-pip
...
root@hillvalley:~#
```

Algunos paquetes de *python* necesitan compilarse previamente a su instalación. Para ello debemos instalar las librerías de desarrollo del lenguaje:

```console
root@hillvalley:~# apt-get install -y python3-dev
...
root@hillvalley:~#
```

* [x] `pip` instalado.

### Entornos virtuales

La forma más extendida de trabajar con aplicaciones *python* es usar entornos virtuales (*virtualenvs*). Se trata de un mecanismo para aislar las librerías y crear un ambiente de trabajo independiente.

```console
root@hillvalley:~# pip install virtualenv
Downloading/unpacking virtualenv
  Downloading virtualenv-15.0.3-py2.py3-none-any.whl (3.5MB): 3.5MB downloaded
Installing collected packages: virtualenv
Successfully installed virtualenv
Cleaning up...
root@hillvalley:~#
```

Desde un usuario no privilegiado, vamos a crear un directorio y un entorno virtual asociado, para poder crear nuestra pequeña aplicación en *python*:

```console
sdelquin@hillvalley:~/helloworld$ virtualenv -p python3 env
Running virtualenv with interpreter /usr/bin/python3
Using base prefix '/usr'
New python executable in /home/sdelquin/helloworld/env/bin/python3
Also creating executable in /home/sdelquin/helloworld/env/bin/python
Installing setuptools, pip, wheel...done.
sdelquin@hillvalley:~/helloworld$ source env/bin/activate
(env) sdelquin@hillvalley:~/helloworld$ python --version
Python 3.4.2
(env) sdelquin@hillvalley:~/helloworld$
```

### uWSGI

*uWSGI* es el encargado de procesar las peticiones *http* para aplicaciones con código *python*. Se puede ver como el *php-fpm* de *php*.

![](img/django_flask_work.png)

Para instalarlo, usamos el gestor de paquetes de python `pip`:

```console
(env)sdelquin@hillvalley:~/helloworld$ pip install uwsgi
...
(env)sdelquin@hillvalley:~/helloworld$ uwsgi --version
2.0.13.1
(env)sdelquin@hillvalley:~/helloworld$ deactivate
sdelquin@hillvalley:~/helloworld$
```

## Creación del "Hola Mundo"

```console
sdelquin@hillvalley:~/helloworld$ vi main.py
```

> Contenido
```python
def app(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/html")])
    return ["<h1 style='color:blue'>Hello World!</h1>"]
```

En este punto podemos lanzar el proceso que escuchará peticiones:

```console
sdelquin@hillvalley:~/helloworld$ source env/bin/activate
(env)sdelquin@hillvalley:~/helloworld$ uwsgi --socket 0.0.0.0:8080 --protocol=http -w main:app
*** Starting uWSGI 2.0.13.1 (64bit) on [Sun Aug 28 13:51:15 2016] ***
compiled with version: 4.9.2 on 28 August 2016 13:31:54
os: Linux-3.16.0-4-amd64 #1 SMP Debian 3.16.7-ckt25-2+deb8u3 (2016-07-02)
nodename: hillvalley
machine: x86_64
clock source: unix
detected number of CPU cores: 1
current working directory: /home/sdelquin/helloworld
detected binary path: /home/sdelquin/helloworld/env/bin/uwsgi
!!! no internal routing support, rebuild with pcre support !!!
*** WARNING: you are running uWSGI without its master process manager ***
your processes number limit is 1858
your memory page size is 4096 bytes
detected max file descriptor number: 65536
lock engine: pthread robust mutexes
thunder lock: disabled (you can enable it with --thunder-lock)
uwsgi socket 0 bound to TCP address 0.0.0.0:8080 fd 3
Python version: 2.7.9 (default, Mar  1 2015, 13:01:26)  [GCC 4.9.2]
*** Python threads support is disabled. You can enable it with --enable-threads ***
Python main interpreter initialized at 0x2084d10
your server socket listen backlog is limited to 100 connections
your mercy for graceful operations on workers is 60 seconds
mapped 72760 bytes (71 KB) for 1 cores
*** Operational MODE: single process ***
WSGI app 0 (mountpoint='') ready in 0 seconds on interpreter 0x2084d10 pid: 21061 (default app)
*** uWSGI is running in multiple interpreter mode ***
spawned uWSGI worker 1 (and the only) (pid: 21061, cores: 1)
```

Si ahora accedemos con un navegador a la dirección IP de nuestro servidor y al puerto 8080, veremos lo siguiente:

![](img/uwsgi_test.png)

## Configuración del servidor web

### `uWSGI`

En primer lugar debemos crear un fichero de configuración para *uWSGI*:

```console
(env)sdelquin@hillvalley:~/helloworld$ deactivate   #podemos desactivar el entorno virtual
sdelquin@hillvalley:~/helloworld$ vi uwsgi.ini
```

> Contenido
>```ini
>[uwsgi]
>chdir = /home/sdelquin/helloworld
>module = main:app
>master = true
>processes = 4
>socket = /tmp/helloworld.sock
>chmod-socket = 666
>vacuum = true
>```

- `chdir`: ruta al directorio del proyecto
- `module`: `<fichero.py>:<callable>
- `master`: `crea un proceso maestro`
- `processes`: número de workers para atender peticiones
- `socket`: ruta hasta el socket
- `chmod-socket`: permisos del socket
- `vacuum`: limpieza del socket al finalizar

Hay que tener en cuenta lo siguiente:

> NOTA: Es importante fijarse que la línea `module = main:app` nos indica que el módulo que se va a ejecutar está en el fichero `main.py` y que se llama `app`. En este caso es una función, pero podría ser cualquier *callable* de *Python*.

Ahora tenemos que crear un pequeño script que será el encargado de activar el entorno virtual de nuestra aplicación y de lanzar el proceso `uwsgi` para que escuche peticiones en el socket especificado:

```console
sdelquin@hillvalley:~/helloworld$ vi run.sh
```

> Contenido

> ```bash
> #!/bin/bash
> 
> source /home/sdelquin/helloworld/env/bin/activate
> uwsgi --ini /home/sdelquin/helloworld/uwsgi.ini
> ```

Ahora le damos permisos de ejecución al script que hemos creado:

```console
sdelquin@hillvalley:~/helloworld$ chmod +x run.sh
sdelquin@hillvalley:~/helloworld$ ls -lh run.sh
-rwxr--r-- 1 sdelquin sdelquin 90 ago 28 16:29 run.sh
sdelquin@hillvalley:~/helloworld$
```

### `Nginx`

Vamos a crear un *virtual host* para nuestra aplicación *python*. Queremos que responda a peticiones a la url `http://helloworld.local`. Para ello haremos lo siguiente como *root* desde la *máquina de producción*:

```console
root@hillvalley:~# vi /etc/nginx/sites-available/helloworld
```

> Contenido
> ```nginx
> server {
>     server_name helloworld.local;
> 
>     location / {
>         include uwsgi_params;
>         uwsgi_pass unix:/tmp/helloworld.sock;   # socket definido previamente
>     }
>     
>     location /static {
>         root /home/sdelquin/helloworld;         # para servir ficheros estáticos
>     }
> }
```

Enlazamos el *virtual host* para habilitarlo:

```console
root@hillvalley:~# cd /etc/nginx/sites-enabled/
root@hillvalley:/etc/nginx/sites-enabled# ln -s ../sites-available/helloworld
root@hillvalley:/etc/nginx/sites-enabled# ls -l helloworld
lrwxrwxrwx 1 root root 29 oct  1 18:58 helloworld -> ../sites-available/helloworld
root@hillvalley:/etc/nginx/sites-enabled#
```

Ahora recargamos el servidor web:

```console
root@hillvalley:~# /etc/init.d/nginx reload
[ ok ] Reloading nginx configuration (via systemctl): nginx.service.
root@hillvalley:~#
```

En este momento, las peticiones que lleguen a nuestro servidor *Nginx* en la url definida serán derivados a un servicio que debería estar escuchando en el socket `/tmp/helloworld.sock`. Si probamos a acceder en este momento a nuestro servidor web, nos aparece lo siguiente:

![](img/bad_gateway.png)

Se debe a que nos falta lanzar nuestra aplicación *uWSGI* para que escuche en el socket especificado y devuelva el sencillo *html* que hemos preparado en nuestra aplicación *python*:

```console
sdelquin@hillvalley:~/helloworld$ run.sh
[uWSGI] getting INI configuration from /home/sdelquin/helloworld/uwsgi.ini
*** Starting uWSGI 2.0.13.1 (64bit) on [Sun Aug 28 17:13:08 2016] ***
compiled with version: 4.9.2 on 28 August 2016 13:31:54
os: Linux-3.16.0-4-amd64 #1 SMP Debian 3.16.7-ckt25-2+deb8u3 (2016-07-02)
nodename: hillvalley
machine: x86_64
clock source: unix
detected number of CPU cores: 1
current working directory: /home/sdelquin/helloworld
detected binary path: /home/sdelquin/helloworld/env/bin/uwsgi
!!! no internal routing support, rebuild with pcre support !!!
your processes number limit is 1858
your memory page size is 4096 bytes
detected max file descriptor number: 65536
lock engine: pthread robust mutexes
thunder lock: disabled (you can enable it with --thunder-lock)
uwsgi socket 0 bound to UNIX address /tmp/helloworld.sock fd 3
Python version: 2.7.9 (default, Mar  1 2015, 13:01:26)  [GCC 4.9.2]
*** Python threads support is disabled. You can enable it with --enable-threads ***
Python main interpreter initialized at 0xc8aab0
your server socket listen backlog is limited to 100 connections
your mercy for graceful operations on workers is 60 seconds
mapped 363800 bytes (355 KB) for 4 cores
*** Operational MODE: preforking ***
WSGI app 0 (mountpoint='') ready in 0 seconds on interpreter 0xc8aab0 pid: 22091 (default app)
*** uWSGI is running in multiple interpreter mode ***
spawned uWSGI master process (pid: 22091)
spawned uWSGI worker 1 (pid: 22092, cores: 1)
spawned uWSGI worker 2 (pid: 22093, cores: 1)
spawned uWSGI worker 3 (pid: 22094, cores: 1)
spawned uWSGI worker 4 (pid: 22095, cores: 1)
```

Sin parar de ejecutar el comando anterior, volvemos a probar el acceso a través del navegador, y obtenemos lo siguiente:

![](img/uwsgi_nginx.png)

* [x] Configuración `uWSGI` + `Nginx` completada.

## Supervisor

Para mantener nuestra aplicación "viva" y poder gestionar su arranque/parada de manera sencilla, necesitamos un proceso coordinador. Para este cometido, se ha desarrollado [supervisor](http://supervisord.org/).

### Instalación

```console
root@hillvalley:~# apt-get install -y supervisor
Leyendo lista de paquetes... Hecho
Creando árbol de dependencias
Leyendo la información de estado... Hecho
Se instalarán los siguientes paquetes NUEVOS:
  supervisor
0 actualizados, 1 nuevos se instalarán, 0 para eliminar y 0 no actualizados.
Se necesita descargar 0 B/267 kB de archivos.
Se utilizarán 1.352 kB de espacio de disco adicional después de esta operación.
Seleccionando el paquete supervisor previamente no seleccionado.
(Leyendo la base de datos ... 44016 ficheros o directorios instalados actualmente.)
Preparando para desempaquetar .../supervisor_3.0r1-1_all.deb ...
Desempaquetando supervisor (3.0r1-1) ...
Procesando disparadores para systemd (215-17+deb8u4) ...
Configurando supervisor (3.0r1-1) ...
Procesando disparadores para systemd (215-17+deb8u4) ...
root@hillvalley:~#
```

Comprobamos que el servicio está correctamente instalado y funcionando:

```console
root@hillvalley:~# /etc/init.d/supervisor status
● supervisor.service - LSB: Start/stop supervisor
   Loaded: loaded (/etc/init.d/supervisor)
   Active: active (running) since sáb 2016-10-01 18:42:00 WEST; 11s ago
  Process: 6272 ExecStop=/etc/init.d/supervisor stop (code=exited, status=0/SUCCESS)
  Process: 6276 ExecStart=/etc/init.d/supervisor start (code=exited, status=0/SUCCESS)
   CGroup: /system.slice/supervisor.service
           └─6281 /usr/bin/python /usr/bin/supervisord -c /etc/supervisor/supervisord.conf

oct 01 18:42:00 hillvalley supervisor[6276]: Starting supervisor: supervisord.
root@hillvalley:~#
```

## Configuración

Para que nuestro programa `helloworld` sea gestionado por *supervisor*, debemos añadir un fichero de configuración:

```console
root@hillvalley:~# vi /etc/supervisor/conf.d/helloworld.conf
```

> Contenido

```ini
[program:helloworld]
user = sdelquin
command = /home/sdelquin/helloworld/run.sh
autostart = true
autorestart = true
stopsignal = INT
killasgroup = true
stderr_logfile = /home/sdelquin/helloworld/helloworld.err.log
stdout_logfile = /home/sdelquin/helloworld/helloworld.out.log
```

### Permitir la gestión de procesos por usuarios no privilegiados

Nos puede interesar que los usuarios no privilegiados controlen sus propios procesos. Para controlar el arranque/parada/consulta de los procesos, existe una herramienta de *supervisor* llamada `supervisorctl`. Si un usuario no privilegiado intenta ejecutarla, pasa lo siguiente:

```console
sdelquin@hillvalley:~$ supervisorctl status
error: <class 'socket.error'>, [Errno 13] Permission denied: file: /usr/lib/python2.7/socket.py line: 224
sdelquin@hillvalley:~$
```

Esto es así porque el *socket* que usa *supervisord* para funcionar, no permite su lectura a usuarios no privilegiados. Para solucionar esto debemos seguir varios pasos. La idea es crear un grupo `supervisor` en el que incluiremos a todos aquellos "desarrolladores":

```console
root@hillvalley:~# groupadd supervisor
root@hillvalley:~#
```

Ahora debemos modificar la configuración inicial de *supervisor*. Como usuario *root* hacemos lo siguiente:

```console
root@hillvalley:~# vi /etc/supervisor/supervisord.conf
```

> Cambiar estas dos líneas
```nginx
...
chmod=0770               ; socket file mode (default 0700)
chown=root:supervisor    ; grupo 'supervisor' para usuarios no privilegiados
...
```

Reiniciamos el servicios para que surtan efectos los cambios realizados:

```console
root@hillvalley:~# /etc/init.d/supervisor restart
[ ok ] Restarting supervisor (via systemctl): supervisor.service.
root@hillvalley:~#
```

A continuación tenemos que añadir al usuario de la aplicación (`sdelquin`) al grupo que hemos creado para supervisord (`supervisor`):

```console
root@hillvalley:~# usermod -a -G supervisor sdelquin
root@hillvalley:~#
```

> Para que el cambio de grupo sea efectivo, habrá que salir y volver a entrar en la sesión de `sdelquin`.

Ahora, desde la *máquina de producción*, pero con un usuario no privilegiado, vemos que ya podemos hacer uso de la gestión de nuestros procesos:

```console
sdelquin@hillvalley:~$ supervisorctl status
helloworld                       RUNNING    pid 6804, uptime 0:01:08
sdelquin@hillvalley:~$
```

## Control de la aplicación

```console
sdelquin@hillvalley:~$ supervisorctl start helloworld
helloworld: ERROR (already started)
sdelquin@hillvalley:~$ supervisorctl stop helloworld
helloworld: stopped
sdelquin@hillvalley:~$ supervisorctl start helloworld
helloworld: started
sdelquin@hillvalley:~$ supervisorctl status helloworld
helloworld                       RUNNING   pid 5704, uptime 0:00:14
sdelquin@hillvalley:~$ supervisorctl restart helloworld
helloworld: stopped
helloworld: started
sdelquin@hillvalley:~$
```

Si accedemos al servidor y a la ruta especificada, tendremos disponible nuestra aplicación.

> NOTA: En el caso de que se añadan nuevos procesos que controlar con `supervisor`, tendremos que reiniciar el servicio, tras añadir la nueva configuración `/etc/supervisor/conf.d/<proceso>.conf`. Para ello, siendo *root* en la *máquina de producción*:

> `$> /etc/init.d/supervisor restart`

* [x] Configuración de `supervisor`.
