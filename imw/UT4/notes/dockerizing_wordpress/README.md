# Dockerizando Wordpress

## Activación del Swap

Si estamos trabajando con una máquina de producción con poca memoria RAM, en este caso, sólo 512MB, debemos activar el Swap para no tener problemas con los servicios.

Podemos ver que actualmente **no está activado** el Swap:

~~~console
sdelquin@cloud:~$ free
              total        used        free      shared  buff/cache   available
Mem:         500048      319892       22244       27560      157912      120048
Swap:             0           0           0
sdelquin@cloud:~$
~~~

En primer lugar creamos el fichero de Swap:

~~~console
sdelquin@cloud:~$ cd /var/
sdelquin@cloud:/var$ sudo touch swap.img
[sudo] password for sdelquin:
sdelquin@cloud:/var$ sudo chmod 600 swap.img
sdelquin@cloud:/var$
~~~

A continuación redimensionamos el fichero de Swap. Normalmente se aconseja el doble del tamaño de la memoria RAM. En este caso le daremos un tamaño de 1GB:

~~~console
sdelquin@cloud:/var$ sudo dd if=/dev/zero of=/var/swap.img bs=1024k count=1000
1000+0 records in
1000+0 records out
1048576000 bytes (1,0 GB, 1000 MiB) copied, 1,74696 s, 600 MB/s
sdelquin@cloud:/var$
~~~

A continuación inicializamos el sistema de ficheros de Swap:

~~~console
sdelquin@cloud:~$ sudo mkswap /var/swap.img
Setting up swapspace version 1, size = 1000 MiB (1048571904 bytes)
no label, UUID=33723033-4415-4938-85ec-8884997af99e
sdelquin@cloud:~$
~~~

Una vez hecho esto, sólo nos queda activar el fichero de Swap:

~~~console
sdelquin@cloud:~$ sudo swapon /var/swap.img
sdelquin@cloud:~$ free
              total        used        free      shared  buff/cache   available
Mem:         500048      321404       11156       29040      167488      116188
Swap:       1023996           0     1023996
sdelquin@cloud:~$
~~~

En el caso de querer *deshabilitar* el Swap se puede hacer con el comando `swapoff /var/swap.img`.

[Cómo configurar memoria virtual (fichero Swap) en un VPS - DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-configure-virtual-memory-swap-file-on-a-vps) 

## Servicios con Docker

En primer lugar vamos a crear un fichero para componer nuestros contenedores:

~~~console
sdelquin@cloud:~$ mkdir wordpress
sdelquin@cloud:~$ cd wordpress
sdelquin@cloud:~/wordpress$ vi docker-compose.yml
~~~

> Contenido:

~~~yml
version: '3.1'

services:

  wordpress:
    image: wordpress
    restart: always
    ports:
      - 8080:80
    environment:
      WORDPRESS_DB_PASSWORD: mydocker2018

  mysql:
    image: mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: mydocker2018
~~~

Ahora lanzamos los servicios:

~~~console
sdelquin@cloud:~/wordpress$ docker-compose up
Creating wordpress_wordpress_1 ... done
Creating wordpress_mysql_1     ... done
Attaching to wordpress_mysql_1, wordpress_wordpress_1
...
...
...
~~~

Si accedemos al puerto `8080` en la dirección de nuestra máquina de producción, podremos ver que accedemos al instalador de Wordpress:

![Puerto 8080](img/wordpress_docker01.png) 

