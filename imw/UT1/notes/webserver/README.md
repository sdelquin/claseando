# Servidor Web

[Instalando Nginx](#instalando-nginx)  
[Server y Location](#server-y-location)  
[Rutas destacadas](#rutas-destacadas)  
[Listado de directorios](#listado-de-directorios)  
[Acceso restringido con clave](#acceso-restringido-con-clave)  
[Ficheros de log](#ficheros-de-log)  
[Configurando SSL](#configurando-ssl)  
[Redirecciones](#redirecciones)  
[Variables](#variables)

## Instalando Nginx

El servidor con el que vamos a trabajar será **Nginx**.

La instalación del servidor **Nginx** es muy sencilla. Lo único que debemos hacer es utilizar el paquete preparado al efecto.

Lo primero es cambiar a la cuenta de `root` y actualizar la lista de paquetes:

```console
sdelquin@cloud:~$ sudo apt-get update
[sudo] password for sdelquin:
Des:1 http://security.ubuntu.com/ubuntu xenial-security InRelease [102 kB]
Des:2 http://security.ubuntu.com/ubuntu xenial-security/main Sources [91,3 kB]
Des:3 http://security.ubuntu.com/ubuntu xenial-security/main amd64 Packages [354 kB]
Des:4 http://security.ubuntu.com/ubuntu xenial-security/universe amd64 Packages [169 kB]
Obj:5 http://ams2.mirrors.digitalocean.com/ubuntu xenial InRelease
Des:6 http://ams2.mirrors.digitalocean.com/ubuntu xenial-updates InRelease [102 kB]
Des:7 http://ams2.mirrors.digitalocean.com/ubuntu xenial-backports InRelease [102 kB]
Des:8 http://ams2.mirrors.digitalocean.com/ubuntu xenial-updates/main Sources [275 kB]
Des:9 http://ams2.mirrors.digitalocean.com/ubuntu xenial-updates/main amd64 Packages [631 kB]
Des:10 http://ams2.mirrors.digitalocean.com/ubuntu xenial-updates/universe amd64 Packages [536 kB]
Descargados 2.363 kB en 1s (1.595 kB/s)
Leyendo lista de paquetes... Hecho
sdelquin@cloud:~$
```

A continuación instalaremos el paquete `nginx`:

```console
sdelquin@cloud:~$ sudo apt-get install nginx
Leyendo lista de paquetes... Hecho
Creando árbol de dependencias
Leyendo la información de estado... Hecho
El paquete indicado a continuación se instaló de forma automática y ya no es necesario.
  grub-pc-bin
Utilice «sudo apt autoremove» para eliminarlo.
Se instalarán los siguientes paquetes adicionales:
  fontconfig-config fonts-dejavu-core libfontconfig1 libgd3 libjbig0 libjpeg-turbo8 libjpeg8 libtiff5
  libvpx3 libxpm4 libxslt1.1 nginx-common nginx-core
Paquetes sugeridos:
  libgd-tools fcgiwrap nginx-doc ssl-cert
Se instalarán los siguientes paquetes NUEVOS:
  fontconfig-config fonts-dejavu-core libfontconfig1 libgd3 libjbig0 libjpeg-turbo8 libjpeg8 libtiff5
  libvpx3 libxpm4 libxslt1.1 nginx nginx-common nginx-core
0 actualizados, 14 nuevos se instalarán, 0 para eliminar y 15 no actualizados.
Se necesita descargar 3.000 kB de archivos.
Se utilizarán 9.783 kB de espacio de disco adicional después de esta operación.
¿Desea continuar? [S/n]
Des:1 http://ams2.mirrors.digitalocean.com/ubuntu xenial/main amd64 libjpeg-turbo8 amd64 1.4.2-0ubuntu3 [111 kB]
Des:2 http://ams2.mirrors.digitalocean.com/ubuntu xenial/main amd64 libjbig0 amd64 2.1-3.1 [26,6 kB]
Des:3 http://ams2.mirrors.digitalocean.com/ubuntu xenial/main amd64 fonts-dejavu-core all 2.35-1 [1.039 kB]
Des:4 http://ams2.mirrors.digitalocean.com/ubuntu xenial-updates/main amd64 fontconfig-config all 2.11.94-0ubuntu1.1 [49,9 kB]
Des:5 http://ams2.mirrors.digitalocean.com/ubuntu xenial-updates/main amd64 libfontconfig1 amd64 2.11.94-0ubuntu1.1 [131 kB]
Des:6 http://ams2.mirrors.digitalocean.com/ubuntu xenial/main amd64 libjpeg8 amd64 8c-2ubuntu8 [2.194 B]
Des:7 http://ams2.mirrors.digitalocean.com/ubuntu xenial-updates/main amd64 libtiff5 amd64 4.0.6-1ubuntu0.2 [146 kB]
Des:8 http://ams2.mirrors.digitalocean.com/ubuntu xenial/main amd64 libvpx3 amd64 1.5.0-2ubuntu1 [732 kB]
Des:9 http://ams2.mirrors.digitalocean.com/ubuntu xenial-updates/main amd64 libxpm4 amd64 1:3.5.11-1ubuntu0.16.04.1 [33,8 kB]
Des:10 http://ams2.mirrors.digitalocean.com/ubuntu xenial-updates/main amd64 libgd3 amd64 2.1.1-4ubuntu0.16.04.8 [126 kB]
Des:11 http://ams2.mirrors.digitalocean.com/ubuntu xenial-updates/main amd64 libxslt1.1 amd64 1.1.28-2.1ubuntu0.1 [145 kB]
Des:12 http://ams2.mirrors.digitalocean.com/ubuntu xenial-updates/main amd64 nginx-common all 1.10.3-0ubuntu0.16.04.2 [26,6 kB]
Des:13 http://ams2.mirrors.digitalocean.com/ubuntu xenial-updates/main amd64 nginx-core amd64 1.10.3-0ubuntu0.16.04.2 [428 kB]
Des:14 http://ams2.mirrors.digitalocean.com/ubuntu xenial-updates/main amd64 nginx all 1.10.3-0ubuntu0.16.04.2 [3.490 B]
Descargados 3.000 kB en 1s (1.943 kB/s)
Preconfigurando paquetes ...
Seleccionando el paquete libjpeg-turbo8:amd64 previamente no seleccionado.
(Leyendo la base de datos ... 82162 ficheros o directorios instalados actualmente.)
Preparando para desempaquetar .../libjpeg-turbo8_1.4.2-0ubuntu3_amd64.deb ...
Desempaquetando libjpeg-turbo8:amd64 (1.4.2-0ubuntu3) ...
Seleccionando el paquete libjbig0:amd64 previamente no seleccionado.
Preparando para desempaquetar .../libjbig0_2.1-3.1_amd64.deb ...
Desempaquetando libjbig0:amd64 (2.1-3.1) ...
Seleccionando el paquete fonts-dejavu-core previamente no seleccionado.
Preparando para desempaquetar .../fonts-dejavu-core_2.35-1_all.deb ...
Desempaquetando fonts-dejavu-core (2.35-1) ...
Seleccionando el paquete fontconfig-config previamente no seleccionado.
Preparando para desempaquetar .../fontconfig-config_2.11.94-0ubuntu1.1_all.deb ...
Desempaquetando fontconfig-config (2.11.94-0ubuntu1.1) ...
Seleccionando el paquete libfontconfig1:amd64 previamente no seleccionado.
Preparando para desempaquetar .../libfontconfig1_2.11.94-0ubuntu1.1_amd64.deb ...
Desempaquetando libfontconfig1:amd64 (2.11.94-0ubuntu1.1) ...
Seleccionando el paquete libjpeg8:amd64 previamente no seleccionado.
Preparando para desempaquetar .../libjpeg8_8c-2ubuntu8_amd64.deb ...
Desempaquetando libjpeg8:amd64 (8c-2ubuntu8) ...
Seleccionando el paquete libtiff5:amd64 previamente no seleccionado.
Preparando para desempaquetar .../libtiff5_4.0.6-1ubuntu0.2_amd64.deb ...
Desempaquetando libtiff5:amd64 (4.0.6-1ubuntu0.2) ...
Seleccionando el paquete libvpx3:amd64 previamente no seleccionado.
Preparando para desempaquetar .../libvpx3_1.5.0-2ubuntu1_amd64.deb ...
Desempaquetando libvpx3:amd64 (1.5.0-2ubuntu1) ...
Seleccionando el paquete libxpm4:amd64 previamente no seleccionado.
Preparando para desempaquetar .../libxpm4_1%3a3.5.11-1ubuntu0.16.04.1_amd64.deb ...
Desempaquetando libxpm4:amd64 (1:3.5.11-1ubuntu0.16.04.1) ...
Seleccionando el paquete libgd3:amd64 previamente no seleccionado.
Preparando para desempaquetar .../libgd3_2.1.1-4ubuntu0.16.04.8_amd64.deb ...
Desempaquetando libgd3:amd64 (2.1.1-4ubuntu0.16.04.8) ...
Seleccionando el paquete libxslt1.1:amd64 previamente no seleccionado.
Preparando para desempaquetar .../libxslt1.1_1.1.28-2.1ubuntu0.1_amd64.deb ...
Desempaquetando libxslt1.1:amd64 (1.1.28-2.1ubuntu0.1) ...
Seleccionando el paquete nginx-common previamente no seleccionado.
Preparando para desempaquetar .../nginx-common_1.10.3-0ubuntu0.16.04.2_all.deb ...
Desempaquetando nginx-common (1.10.3-0ubuntu0.16.04.2) ...
Seleccionando el paquete nginx-core previamente no seleccionado.
Preparando para desempaquetar .../nginx-core_1.10.3-0ubuntu0.16.04.2_amd64.deb ...
Desempaquetando nginx-core (1.10.3-0ubuntu0.16.04.2) ...
Seleccionando el paquete nginx previamente no seleccionado.
Preparando para desempaquetar .../nginx_1.10.3-0ubuntu0.16.04.2_all.deb ...
Desempaquetando nginx (1.10.3-0ubuntu0.16.04.2) ...
Procesando disparadores para libc-bin (2.23-0ubuntu9) ...
Procesando disparadores para man-db (2.7.5-1) ...
Procesando disparadores para ureadahead (0.100.0-19) ...
Procesando disparadores para ufw (0.35-0ubuntu2) ...
Procesando disparadores para systemd (229-4ubuntu19) ...
Configurando libjpeg-turbo8:amd64 (1.4.2-0ubuntu3) ...
Configurando libjbig0:amd64 (2.1-3.1) ...
Configurando fonts-dejavu-core (2.35-1) ...
Configurando fontconfig-config (2.11.94-0ubuntu1.1) ...
Configurando libfontconfig1:amd64 (2.11.94-0ubuntu1.1) ...
Configurando libjpeg8:amd64 (8c-2ubuntu8) ...
Configurando libtiff5:amd64 (4.0.6-1ubuntu0.2) ...
Configurando libvpx3:amd64 (1.5.0-2ubuntu1) ...
Configurando libxpm4:amd64 (1:3.5.11-1ubuntu0.16.04.1) ...
Configurando libgd3:amd64 (2.1.1-4ubuntu0.16.04.8) ...
Configurando libxslt1.1:amd64 (1.1.28-2.1ubuntu0.1) ...
Configurando nginx-common (1.10.3-0ubuntu0.16.04.2) ...
Configurando nginx-core (1.10.3-0ubuntu0.16.04.2) ...
Configurando nginx (1.10.3-0ubuntu0.16.04.2) ...
Procesando disparadores para libc-bin (2.23-0ubuntu9) ...
Procesando disparadores para systemd (229-4ubuntu19) ...
Procesando disparadores para ureadahead (0.100.0-19) ...
Procesando disparadores para ufw (0.35-0ubuntu2) ...
sdelquin@cloud:~$
```

Con esto, en principio, debería estar instalado el servidor web **Nginx**. Podemos comprobarlo con el siguiente comando:

```console
sdelquin@cloud:~$ sudo systemctl status nginx
● nginx.service - A high performance web server and a reverse proxy server
   Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
   Active: active (running) since jue 2017-09-21 15:09:21 UTC; 26s ago
 Main PID: 28992 (nginx)
   CGroup: /system.slice/nginx.service
           ├─28992 nginx: master process /usr/sbin/nginx -g daemon on; master_process on
           └─28993 nginx: worker process

sep 21 15:09:21 cloud systemd[1]: Starting A high performance web server and a reverse proxy server...
sep 21 15:09:21 cloud systemd[1]: nginx.service: Failed to read PID from file /run/nginx.pid: Invalid argument
sep 21 15:09:21 cloud systemd[1]: Started A high performance web server and a reverse proxy server.
sdelquin@cloud:~$
```

Para comprobar nuestra instalación de **Nginx**, accedemos al nombre de la máquina:

![](img/nginx_test.png)

Igualmente, podemos acceder a la IP de la máquina, y la respuesta debe ser la misma:

```console
sdelquin@imw:~$ ping imwpto.me
PING imwpto.me (138.68.99.84) 56(84) bytes of data.
64 bytes from cloud (138.68.99.84): icmp_seq=1 ttl=55 time=66.0 ms
^C
--- imwpto.me ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 66.050/66.050/66.050/0.000 ms
sdelquin@imw:~$
```

![](img/nginx_test_by_ip.png)

## Rutas destacadas

El directorio *root* por defecto de Nginx es: `/var/www/html`. Si echamos un vistazo, vemos lo siguiente:

```console
sdelquin@cloud:~$ sudo ls -l /var/www/html/
total 4
-rw-r--r-- 1 root root 612 sep 21 15:09 index.nginx-debian.html
sdelquin@cloud:~$
```

Cuando accedemos a nuestra máquina de producción, lo que realmente está pasando es que Nginx trata de buscar un fichero índice en el *root*. De hecho si miramos el contenido del fichero `index.nginx-debian.html` podemos ver que su contenido coincide con lo que nos muestra el servidor web:

```console
sdelquin@cloud:~$ cat /var/www/html/index.nginx-debian.html
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
sdelquin@cloud:~$
```

### Ficheros de configuración

Podríamos decir que Nginx dispone de dos ficheros destacados de configuración:

* `/etc/nginx/nginx.conf`: para las configuraciones del servicio.
* `/etc/nginx/sites-enabled/default`: para las configuraciones del sitio web.

## Server y Location

*Nginx* se configura a través de bloques de mayor nivel llamados `server` (servidor ó *virtual host*) y de `location` (ubicaciones) dentro de esos servidores.

![](img/Nginx-Server-Location.png)

Cada vez que queramos incluir un nuevo *virtual host*, debemos incluir un fichero en la ruta `/etc/nginx/sites-available` y luego enlazar dicho fichero desde la ruta `/etc/nginx/sites-enabled`.

Supongamos que queremos mostrar una página web que hemos creado en la carpeta *home* del usuario *sdelquin*. Además queremos que se muestre esa página cuando se acceda en el navegador a la *url* `http://sdelquin.imwpto.me/`.

Añadimos el fichero de configuración de *Nginx* que tratará las peticiones que se hagan al nombre de dominio `sdelquin.imwpto.me`:

```console
sdelquin@cloud:~$ sudo vi /etc/nginx/sites-available/sdelquin
```

> Contenido
```nginx
server {
    server_name sdelquin.imwpto.me;
    root /home/sdelquin;
}
```

A continuación tenemos que enlazar el fichero que hemos creado para que esté disponible desde los `sites-enabled`:

```console
sdelquin@cloud:~$ cd /etc/nginx/sites-enabled/
sdelquin@cloud:/etc/nginx/sites-enabled$ sudo ln -s ../sites-available/sdelquin
sdelquin@cloud:/etc/nginx/sites-enabled$ ls -l ../sites-available/
total 8
-rw-r--r-- 1 root root 2074 feb 11  2017 default
-rw-r--r-- 1 root root   36 sep 21 15:20 sdelquin
sdelquin@cloud:/etc/nginx/sites-enabled$
```

Por último, tenemos que recargar la configuración de *Nginx* para que los cambios surtan efecto:

```console
sdelquin@cloud:/etc/nginx/sites-enabled$ sudo systemctl reload nginx
sdelquin@cloud:/etc/nginx/sites-enabled$
```

Ahora ya podemos escribir la página web en nuestro *home*:

```console
sdelquin@cloud:~$ vi index.html
```

> Contenido:
```html
Esto es un nuevo virtual host.<br>
By sdelquin.
```

Si ahora accedemos desde un navegador, deberíamos ver lo siguiente:

![](img/virtual_server.png)

Supongamos que ahora queremos, que cuando se acceda a `http://sdelquin.imwpto.me/blog/`, nos muestre la web que vamos a diseñar en el directorio `/home/sdelquin/webapps/blog`. Dado que se trata de un *location* dentro de un *virtual host*, tendremos que utilizar la siguiente directiva:

```console
sdelquin@cloud:~$ sudo vi /etc/nginx/sites-available/sdelquin
```

> Contenido
> ```nginx
> server {
>     server_name hv;
>     root /home/sdelquin;
> 
>     location /blog {
>         root /home/sdelquin/webapps;
>     }
> }
> ```

Una vez más, recargamos nuestro servidor para que los cambios surtan efecto:

```console
sdelquin@cloud:~$ sudo systemctl reload nginx
sdelquin@cloud:~$
```

Ahora, como usuario `sdelquin`, podemos desarrollar nuestro blog en la ruta `/home/sdelquin/webapps/blog`. Lo típico sería empezar por un fichero `index.html`:

```console
sdelquin@cloud:~$ mkdir -p webapps/blog
sdelquin@cloud:~$ echo "Brand new blog!" > webapps/blog/index.html
sdelquin@cloud:~$
```

Si accedemos mediante un navegador, deberíamos ver algo como lo siguiente:

![](img/blog.png)

## Listado de directorios

Existen multitud de parámetros que se pueden configurar para los sitios web que se definen en *Ningx*.

Uno de ellos es `autoindex` y nos permite *listar el contenido del directorio actual*, pudiendo implementar una especie de *FTP* a través del navegador.

Supongamos que tenemos una carpeta en nuestro *HOME* que queremos compartir con una serie de amigos. Vamos a ver cómo lo implementamos usando *Nginx*:





```console
sdelquin@cloud:~$ sudo vi /etc/nginx/sites-available/default
```

> Contenido
```nginx
...
location / {
    ...
    autoindex on;
    ...
}
...
```

Ahora recargamos el servidor para que los cambios tengan efecto:

```console
sdelquin@cloud:~$ sudo systemctl reload nginx
sdelquin@cloud:~$
```

> NOTA: Hay que tener mucho cuidado con el uso de esta configuración, pues dará acceso al contenido de los subdirectorios que cuelgan de `/var/www/html`

## Acceso restringido con clave

Es posible pedir usuario/clave al acceder a determinadas ubicaciones de nuestro servidor *Nginx*.

Supongamos que queremos tener acceso a la carpeta `/var/opt/admin`, pero que no nos interesa que sea pública, sino a través de un usuario/clave.

En primer lugar tendremos que generar el fichero `.htpasswd`. Este fichero tiene una estructura en el que cada línea identifica a un posible usuario en la forma:

```
username:encrypted-password:comment
```

Para generar nuestro *password* encriptado, podemos usar el lenguaje *perl* (que suele instalarse con el sistema base), utilizando el siguiente comando desde la *máquina de producción* como usuario `root`:

```console
root@hillvalley:~# perl -le 'print crypt("restringido", "salt-hash")'
saOQOMmS3k30w
root@hillvalley:~#
```

Lo que hemos hecho es encriptar el password `restringido`. Ahora podemos crear el fichero `.htpasswd`:

```console
root@hillvalley:~# cd /var/opt/
root@hillvalley:/var/opt# mkdir admin
root@hillvalley:/var/opt# vi .htpasswd
```

> Contenido
```
admin:saOQOMmS3k30w
```

Ahora añadimos el *location* correspondiente a nuestra configuración de *Nginx*:

```console
root@hillvalley:~# vi /etc/nginx/sites-enabled/hv
```

> Contenido
```nginx
server {
    server_name hv;
    ...
    location /admin {
        root /var/opt;
        auth_basic "Administrator Login";
        auth_basic_user_file /var/opt/admin/.htpasswd;
        autoindex on;
    }
    ...
}
...
```

Recargamos la configuración de *Nginx* y probamos el acceso. Al acceder a la ruta `http://hv/admin` vemos que nos aparece un cuadro de diálogo preguntándonos por el usuario/clave:

![](img/auth1.png)

Rellenamos los campos con las credenciales que pusimos anteriormente en el fichero de configuración: `admin` | `restringido`:

![](img/auth2.png)

Vemos que podemos acceder y se nos muestra el contenido del directorio, que ahora mismo, está vacío:

![](img/auth3.png)

Pero aún no hemos terminado la configuración. Si dejáramos el servidor tal cual, tendríamos un grave problema de seguridad, ya que podríamos acceder al fichero `.htpasswd` desde el navegador, simplemente accediendo a `http://hv/admin/.htpasswd`.

Para evitar eso debemos añadir un par de líneas de configuración en el fichero de configuración del *virtual host*:

```console
root@hillvalley:~# vi /etc/nginx/sites-enabled/hv
```

> Contenido
> ```nginx
> server {
>     server_name hv;
>     ...
>     location /admin {
>         root /var/opt;
>         auth_basic "Administrator Login";
>         auth_basic_user_file /var/opt/admin/.htpasswd;
>         autoindex on;
> 
>         location ~ .htpasswd {
>             deny all;
>         }
>     }
>     ...
> }
> ```

Si ahora recargamos la configuración de *Nginx* y queremos acceder al fichero de contraseñas, lo que obtenemos es un error *404*:

![](img/auth4.png)

## Ficheros de log

Es importante conocer la ubicación de los *logfiles* de *Nginx*. Por defecto, estos ficheros son los siguientes:

* `/var/log/nginx/access.log`
* `/var/log/nginx/error.log`

Además, para cada *virtual host* y/o para cada *location*, podemos definir *logfiles* propios. Para hacer esto habría que añadir las siguientes líneas a las secciones correspondientes:

```nginx
server {
    ...
    access_log /path/to/your/access.log;
    error_log /path/to/your/error.log;
    ...
}
```

## Configurando SSL

Cuando queremos que nuestro sitio web use *SSL* (Secure Sockets Layer), necesitamos configurar el servidor web *Nignx* con certificados de seguridad, específicamente creados para nuestro dominio. El procedimiento que se debe seguir para esto se explica a continuación:

![](img/SSL workflow.png)

Por lo tanto, necesitamos contar con 4 ficheros, más un quinto que se genera a partir de otros dos. Los ficheros serían los siguientes:

- `server.key`: clave privada.
- `server.crs`: solicitud de firma de certificado de seguridad.
- `SSL.crt`: certificado SSL.
- `intermediate.crt`: certificados intermedios.
- `SSL.final.crt`: certificado final resultante de la unión de `SSL.crt` y `intermediate.crt`

> Hoy en día, las entidades certificadoras facilitan la creación de todos estos ficheros, a través de sencillos asistentes. Una vez que obtengamos los citados ficheros, se suelen guardar en `/etc/ssl/`. Ejemplo: [DonDominio](http://dondominio.com)

Vamos a configurar un *virtual host* para que use *SSL*. Imaginemos que nuestro dominio es `probandossl.com`.

Lo primero que habría que hacer es generar los certificados, pero en vez de usar una entidad certificadora externa, vamos a generar unos certificados propios (sin validar). Desde la *máquina de producción*, y como `root` hacemos lo siguiente:

```console
root@hillvalley:~# openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/server.key -out /etc/ssl/SSL.final.crt
Generating a 2048 bit RSA private key
................................................+++
..+++
writing new private key to '/etc/ssl/server.key'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:
State or Province Name (full name) [Some-State]:
Locality Name (eg, city) []:
Organization Name (eg, company) [Internet Widgits Pty Ltd]:
Organizational Unit Name (eg, section) []:
Common Name (e.g. server FQDN or YOUR name) []:probandossl.com
Email Address []:
root@hillvalley:~#
```

Parámetros del comando anterior:

- `req -x509`: generar un certificado auto firmado, en vez de generar una solicitud de firma de certificado.
- `-nodes`: evita que se solicite un *passphrase* para el certificado.
- `-days 365`: cantidad de días que se considera válido el certificado.
- `-newkey rsa:2048`: crear un nuevo certificado y una nueva clave al mismo tiempo.
- `-keyout`: dónde guardar el fichero de clave privada.
- `-out`: dónde guardar el certificado generado.

El comando nos pide una serie de datos. El único campo que es importante (para estas pruebas) es `Common Name (e.g. server FQDN or YOUR name)`, donde tendremos que poner el nombre de dominio que vamos a utilizar. Cuando este comando finaliza ya tenemos a nuestra disposición los dos ficheros que nos van a permitir completar el fichero de configuración de nuestro *virtual host* en el servidor *Nginx*:

```console
root@hillvalley:~# vi /etc/nginx/sites-available/probandossl
```

> Contenido
> ```nginx
> server {
>     listen 443;
>     server_name probandossl.com;
>     root /var/www/html/probandossl;
> 
>     ssl on;
>     ssl_certificate /etc/ssl/SSL.final.crt;
>     ssl_certificate_key /etc/ssl/server.key;
> }
> ```

Ya sólo nos quedaría enlazar este *virtual host* en `sites-enabled`, y recargar la configuración de *Nginx* para que los cambios surtan efecto.

Cuando accedemos a nuestro *virtual host* desde un navegador, vemos lo siguiente:

![](img/ssl1.png)

Si pulsamos en *OPCIONES AVANZADAS* -> *Acceder a probandossl.com (sitio no seguro)*

![](img/ssl2.png)

Conseguimos acceder a la web que hemos preparado, y se nos muestra el contenido del `index.html` que se haya definido en el lugar correspondiente.

![](img/ssl3.png)

Si miramos el certificado de la página, podemos ver 3 cuestiones importantes:

1. Hay un error con el certificado, porque la *autoridad certificadora* es inválida.
2. La conexión es *TLS* (seguridad en la capa de transporte) con cifrado.
3. Todos los recursos de la página se sirven de forma segura.

![](img/ssl4.png)

## Redirecciones

Puede darse el caso de que queramos redireccionar ciertas *urls* a otras. De hecho, podría utilizarse como regla general, el hecho de trabajar siempre sobre la url `https://tudominio.com`.

```nginx
# Redirige de http://tudominio.com a https://tudominio.com
server {  
    listen 80;
    return 301 https://$host$request_uri;
}

# Redirige de http://www.tudominio.com a https://tudominio.com
server {  
    listen 80;
    server_name www.tudominio.com;
    return 301 https://tudominio.com$request_uri;
}

# Redirige de https://www.tudominio.com a https://tudominio.com
server {  
    listen 443;
    server_name www.tudominio.com;
    return 301 $scheme://tudominio.com$request_uri;
}
```

## Variables

*Nginx* dispone de multitud de **variables de configuración** que podemos usar según nos convengan, dentro de nuestros *virtual hosts*.

[Variables de configuración](http://nginx.org/en/docs/varindex.html)
