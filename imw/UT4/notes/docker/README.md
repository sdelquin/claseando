# Docker

![Docker Logo](img/docker_logo.png) 

## ¿Qué es Docker?

- Docker es un proyecto de **código abierto**.
- Automatiza el despliegue de aplicaciones dentro de **contenedores** de software.
- Proporciona una **capa adicional de abstracción** y automatización de virtualización a nivel de sistema operativo en Linux.
- Utiliza características de aislamiento de recursos del kernel Linux.
- Permite que "contenedores" independientes se ejecuten dentro de **una sola instancia de Linux**, evitando la sobrecarga de iniciar y mantener máquinas virtuales.

![Docker Tech](img/docker_tech.png) 

Docker provee dos *sabores* de su plataforma:

- [Docker Community Edition](https://www.docker.com/community-edition) enfocado a desarrolladores y pequeños equipos de trabajo. Es *gratuito*. Conocido como `Docker CE`.
- [Docker Entreprise Edition](https://www.docker.com/enterprise-edition) es una plataforma con infraestructura, contenedores y plugins totalmente certificados. Es *de pago*. Conocido como `Docker EE`.

## Instalación de Docker

Desde la máquina de producción, haremos lo siguiente:

Eliminar las versiones previas de Docker que pudieran existir:

~~~console
sdelquin@cloud:~$ sudo apt remove docker docker-engine docker.io
[sudo] password for sdelquin:
Leyendo lista de paquetes... Hecho
Creando árbol de dependencias
Leyendo la información de estado... Hecho
El paquete «docker-engine» no está instalado, no se eliminará
El paquete «docker» no está instalado, no se eliminará
El paquete «docker.io» no está instalado, no se eliminará
Los paquetes indicados a continuación se instalaron de forma automática y ya no son necesarios.
  linux-headers-4.4.0-101 linux-headers-4.4.0-101-generic linux-headers-4.4.0-103
  linux-headers-4.4.0-103-generic linux-headers-4.4.0-104 linux-headers-4.4.0-104-generic
  linux-headers-4.4.0-93 linux-headers-4.4.0-93-generic linux-headers-4.4.0-97 linux-headers-4.4.0-97-generic
  linux-headers-4.4.0-98 linux-headers-4.4.0-98-generic linux-image-4.4.0-101-generic
  linux-image-4.4.0-103-generic linux-image-4.4.0-104-generic linux-image-4.4.0-93-generic
  linux-image-4.4.0-97-generic linux-image-4.4.0-98-generic
Utilice «sudo apt autoremove» para eliminarlos.
0 actualizados, 0 nuevos se instalarán, 0 para eliminar y 105 no actualizados.
sdelquin@cloud:~$
~~~

Actualizamos el listado de paquetes:

~~~console
sdelquin@cloud:~$ sudo apt update
Obj:1 http://ppa.launchpad.net/jonathonf/python-3.6/ubuntu xenial InRelease
Des:2 http://security.ubuntu.com/ubuntu xenial-security InRelease [102 kB]
Obj:3 http://ams2.mirrors.digitalocean.com/ubuntu xenial InRelease
Des:5 http://security.ubuntu.com/ubuntu xenial-security/main Sources [106 kB]
Des:7 http://security.ubuntu.com/ubuntu xenial-security/main amd64 Packages [424 kB]
Des:8 http://security.ubuntu.com/ubuntu xenial-security/main Translation-en [186 kB]
Des:4 http://ams2.mirrors.digitalocean.com/ubuntu xenial-updates InRelease [102 kB]
Des:6 http://ams2.mirrors.digitalocean.com/ubuntu xenial-backports InRelease [102 kB]
Des:9 http://ams2.mirrors.digitalocean.com/ubuntu xenial-updates/main amd64 Packages [699 kB]
Des:10 http://ams2.mirrors.digitalocean.com/ubuntu xenial-updates/universe amd64 Packages [572 kB]
Descargados 2.293 kB en 2s (997 kB/s)
Leyendo lista de paquetes... Hecho
~~~

Instalamos los paquetes necesarios para que `apt` pueda usar repositorios sobre HTTPS:

~~~console
sdelquin@cloud:~$ sudo apt install apt-transport-https ca-certificates curl software-properties-common
Leyendo lista de paquetes... Hecho
Creando árbol de dependencias
Leyendo la información de estado... Hecho
apt-transport-https ya está en su versión más reciente (1.2.24).
ca-certificates ya está en su versión más reciente (20170717~16.04.1).
curl ya está en su versión más reciente (7.47.0-1ubuntu2.5).
software-properties-common ya está en su versión más reciente (0.96.20.7).
Los paquetes indicados a continuación se instalaron de forma automática y ya no son necesarios.
  linux-headers-4.4.0-101 linux-headers-4.4.0-101-generic linux-headers-4.4.0-103
  linux-headers-4.4.0-103-generic linux-headers-4.4.0-104 linux-headers-4.4.0-104-generic
  linux-headers-4.4.0-93 linux-headers-4.4.0-93-generic linux-headers-4.4.0-97 linux-headers-4.4.0-97-generic
  linux-headers-4.4.0-98 linux-headers-4.4.0-98-generic linux-image-4.4.0-101-generic
  linux-image-4.4.0-103-generic linux-image-4.4.0-104-generic linux-image-4.4.0-93-generic
  linux-image-4.4.0-97-generic linux-image-4.4.0-98-generic
Utilice «sudo apt autoremove» para eliminarlos.
0 actualizados, 0 nuevos se instalarán, 0 para eliminar y 105 no actualizados.
sdelquin@cloud:~$
~~~

Añadimos la clave oficial GPG de Docker:

~~~console
sdelquin@cloud:~$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
OK
sdelquin@cloud:~$
~~~

Comprobación de clave:

~~~console
sdelquin@cloud:~$ sudo apt-key fingerprint 0EBFCD88
pub   4096R/0EBFCD88 2017-02-22
      Key fingerprint = 9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88
uid                  Docker Release (CE deb) <docker@docker.com>
sub   4096R/F273FCD8 2017-02-22

sdelquin@cloud:~$
~~~

Añadimos el repositorio de Docker y actualizamos el listado de paquetes:

~~~console
sdelquin@cloud:~$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sdelquin@cloud:~$ sudo apt update
Obj:1 http://ppa.launchpad.net/jonathonf/python-3.6/ubuntu xenial InRelease
Obj:3 http://security.ubuntu.com/ubuntu xenial-security InRelease
Obj:2 http://ams2.mirrors.digitalocean.com/ubuntu xenial InRelease
Des:4 http://ams2.mirrors.digitalocean.com/ubuntu xenial-updates InRelease [102 kB]
Des:5 http://ams2.mirrors.digitalocean.com/ubuntu xenial-backports InRelease [102 kB]
Des:6 https://download.docker.com/linux/ubuntu xenial InRelease [49,8 kB]
Des:7 https://download.docker.com/linux/ubuntu xenial/stable amd64 Packages [3.150 B]
Descargados 257 kB en 0s (393 kB/s)
Leyendo lista de paquetes... Hecho
Creando árbol de dependencias
Leyendo la información de estado... Hecho
Se pueden actualizar 105 paquetes. Ejecute «apt list --upgradable» para verlos.
sdelquin@cloud:~$
~~~

Instalamos el paquete:

~~~console
sdelquin@cloud:~$ sudo apt install -y docker-ce
Preparando para desempaquetar .../aufs-tools_1%3a3.2+20130722-1.1ubuntu1_amd64.deb ...
Desempaquetando aufs-tools (1:3.2+20130722-1.1ubuntu1) ...
Seleccionando el paquete cgroupfs-mount previamente no seleccionado.
Preparando para desempaquetar .../cgroupfs-mount_1.2_all.deb ...
Desempaquetando cgroupfs-mount (1.2) ...
Seleccionando el paquete libltdl7:amd64 previamente no seleccionado.
Preparando para desempaquetar .../libltdl7_2.4.6-0.1_amd64.deb ...
Desempaquetando libltdl7:amd64 (2.4.6-0.1) ...
Seleccionando el paquete docker-ce previamente no seleccionado.
Preparando para desempaquetar .../docker-ce_17.12.0~ce-0~ubuntu_amd64.deb ...
Desempaquetando docker-ce (17.12.0~ce-0~ubuntu) ...
Procesando disparadores para libc-bin (2.23-0ubuntu9) ...
Procesando disparadores para man-db (2.7.5-1) ...
Procesando disparadores para ureadahead (0.100.0-19) ...
Procesando disparadores para systemd (229-4ubuntu19) ...
Configurando aufs-tools (1:3.2+20130722-1.1ubuntu1) ...
Configurando cgroupfs-mount (1.2) ...
Configurando libltdl7:amd64 (2.4.6-0.1) ...
Configurando docker-ce (17.12.0~ce-0~ubuntu) ...
Procesando disparadores para libc-bin (2.23-0ubuntu9) ...
Procesando disparadores para systemd (229-4ubuntu19) ...
Procesando disparadores para ureadahead (0.100.0-19) ...
sdelquin@cloud:~$
~~~

Verificamos que todo se ha instalado correctamente lanzando un contenedor de ejemplo:

~~~console
sdelquin@cloud:~$ sudo docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
ca4f61b1923c: Pull complete
Digest: sha256:66ef312bbac49c39a89aa9bcc3cb4f3c9e7de3788c944158df3ee0176d32b751
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://cloud.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/engine/userguide/

sdelquin@cloud:~$
~~~

[Tutorial oficial de instalación de Ubuntu CE para Ubuntu](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/) 

## Instalación de Docker Compose

Docker Compose es una herramienta que permite levantar y gestionar microservicios Docker conectados entre sí de manera sencilla.

Descargamos el ejecutable:

~~~console
sdelquin@cloud:~$ sudo curl -L https://github.com/docker/compose/releases/download/1.18.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
[sudo] password for sdelquin:
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   617    0   617    0     0    800      0 --:--:-- --:--:-- --:--:--   800
100 8280k  100 8280k    0     0  1229k      0  0:00:06  0:00:06 --:--:-- 1757k
sdelquin@cloud:~$
~~~

Damos permisos de ejecución:

~~~console
sdelquin@cloud:~$ sudo chmod +x /usr/local/bin/docker-compose
sdelquin@cloud:~$
~~~

Testeamos la instalación:

~~~console
sdelquin@cloud:~$ docker-compose --version
docker-compose version 1.18.0, build 8dd22a9
sdelquin@cloud:~$
~~~

[Tutorial oficial de instalación de Docker Compose](https://docs.docker.com/compose/install/) 

## Pasos después de la instalación

Por defecto, `docker` sólo puede ser utilizado por el usuario `root`. Vamos a permitir que otros usuarios no privilegiados puedan utilizarlo.

Creamos el grupo `docker`:

~~~console
sdelquin@cloud:~$ sudo groupadd docker
[sudo] password for sdelquin:
groupadd: group 'docker' already exists
sdelquin@cloud:~$
~~~

Añadimos el usuario actual a dicho grupo:

~~~console
sdelquin@cloud:~$ sudo usermod -aG docker $USER
sdelquin@cloud:~$
~~~

Ahora debemos salir de la sesión y volver a entrar para que los cambios surtan efecto:

~~~console
sdelquin@cloud:~$ exit
logout
Connection to cloud closed.
sdelquin@imw:~$ ssh cloud
Welcome to Ubuntu 16.04.3 LTS (GNU/Linux 4.4.0-96-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

Pueden actualizarse 105 paquetes.
0 actualizaciones son de seguridad.


*** Es necesario reiniciar el sistema ***
Last login: Sat Jan 13 11:58:44 2018 from 83.35.202.251
sdelquin@cloud:~$
~~~

Ahora comprobamos que podemos usar el comando `docker` desde un usuario no privilegiado:

~~~console
sdelquin@cloud:~$ docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://cloud.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/engine/userguide/

sdelquin@cloud:~$
~~~

[Tutorial para post-instalación de Docker en Linux](https://docs.docker.com/engine/installation/linux/linux-postinstall/) 
