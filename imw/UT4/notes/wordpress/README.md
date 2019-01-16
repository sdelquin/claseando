![](img/wp_logo.png)

## ¿Por qué Wordpress?

1. Tiene 16 años (se lanzó en 2003).
2. 423,759 líneas de código.
3. 58.55% del mercado de CMS.
4. 27% de páginas de internet están hechas con Wordpress ~ 75M sitios.
5. Wordpress 4.7 se ha descargado casi 20M de veces.
6. Contando todas las versiones, acumula casi 200M de descargas.
7. Wordpress está disponible en más de 50 idiomas.
8. El 14.7% de los 100 sitios web más influyentes del mundo están hechos en Wordpress.
9. `wordpress.com` tiene 175M de páginas vistas al mes.
10. Los usuarios de Wordpress publican 41.7M de nuevos posts cada mes.
11. En 2016, Wordpress publicó 117,939,148,357 palabras.
12. Wordpress supera los 5000 commits por más de 70 contribuidores.
13. Existen más de 3000 temas con licencia GPL.
14. Wordpress se puede instalar en menos de 5 minutos.
15. Hay más de 48500 plugins gratuitos para Wordpress.
16. Alrededor del 40% de las tiendas online usan Wordpress.
17. Jetpack fue instalado el último año en más de 2M de nuevos sitios Wordpress.
18. Akismet bloqueó 80B de comentarios spam.
19. Wordpress "sólo" tiene 532 empleados.

> Fuente: [WhoIsHostingThis](https://www.whoishostingthis.com/compare/wordpress/stats/)

## Instalación de Wordpress

A continuación vamos a instalar un sitio web Wordpress en nuestra **máquina de producción**.

## Estructura de la base de datos

El diagrama *Entidad-Relación* de la base de datos de Wordpress 4.4.2 es el siguiente:

![](img/WP4.4.2-ERD.png)

## Configuración de la base de datos

*Wordpress* necesita credenciales (usuario/contraseña) para acceder a una base de datos. Para ello, usaremos el intérprete de *MySQL*:

~~~console
sdelquin@claseando:~$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 157
Server version: 5.7.24-0ubuntu0.18.04.1 (Ubuntu)

Copyright (c) 2000, 2018, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
~~~

Tenemos que crear la base de datos, el usuario y asignar privilegios:

~~~sql
mysql> create database wpdatabase;
Query OK, 1 row affected (0.00 sec)

mysql> create user wpuser@localhost identified by 'Testing_1234';
Query OK, 0 rows affected (0.01 sec)

mysql> grant all privileges on wpdatabase.* to wpuser@localhost;
Query OK, 0 rows affected (0.00 sec)

mysql> exit;
Bye
~~~

## Descarga de código

Descargamos el código fuente de *Wordpress* desde su página web:

~~~console
sdelquin@claseando:~$ cd tmp/
sdelquin@claseando:~/tmp$ curl -O https://wordpress.org/latest.zip
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 10.8M  100 10.8M    0     0  6915k      0  0:00:01  0:00:01 --:--:-- 6911k
sdelquin@claseando:~/tmp$ ls -l latest.zip
-rw-rw-r-- 1 sdelquin sdelquin 11379765 ene  9 11:59 latest.zip
sdelquin@claseando:~/tmp$
~~~

A continuación descomprimimos el código y lo copiamos en `/usr/share`:

~~~console
sdelquin@claseando:~/tmp$ unzip latest.zip
...
...
...
sdelquin@claseando:~/tmp$ sudo cp -r wordpress /usr/share/
sdelquin@claseando:~/tmp$ ls -ld /usr/share/wordpress/
drwxr-xr-x 5 root root 4096 ene  9 12:01 /usr/share/wordpress/
sdelquin@claseando:~/tmp$
~~~

Ahora tenemos que establecer los permisos necesarios para que el usuario web `www-data` pueda usar estos ficheros:

~~~console
sdelquin@claseando:~/tmp$ sudo chown -R www-data:www-data /usr/share/wordpress/
sdelquin@claseando:~/tmp$
~~~

## Editar ficheros de configuración

Para una *configuración básica* de *WordPress* debemos especificar lo siguiente:

- El nombre de la base de datos.
- El usuario.
- La contraseña.

~~~console
sdelquin@claseando:~/tmp$ cd /usr/share/wordpress/
sdelquin@claseando:/usr/share/wordpress$ sudo cp wp-config-sample.php wp-config.php
sdelquin@claseando:/usr/share/wordpress$ sudo vi wp-config.php
...
~~~

Aproximadamente en la línea 23:

~~~php
...
// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define('DB_NAME', 'wpdatabase');

/** MySQL database username */
define('DB_USER', 'wpuser');

/** MySQL database password */
define('DB_PASSWORD', 'Testing_1234');

/** MySQL hostname */
define('DB_HOST', 'localhost');

/** Database Charset to use in creating database tables. */
define('DB_CHARSET', 'utf8mb4');

/** The Database Collate type. Don't change this if in doubt. */
define('DB_COLLATE', '');
...
~~~

## Acceso mediante Nginx

Para que nuestro sitio *Wordpress* sea accesible desde un navegador web, debemos incluir las directivas necesarias en la configuración del servidor web *Nginx*.

Supongamos que queremos acceder a nuestro *Wordpress* desde la url `wordpress.vps.claseando.es`. Para ello tendremos que crear un nuevo *virtual host* de la siguiente manera:

~~~console
sdelquin@claseando:~$ sudo vi /etc/nginx/sites-available/wordpress.vps.claseando.es
...
~~~

~~~nginx
server {
    server_name wordpress.vps.claseando.es;
    index index.php;
    root /usr/share/wordpress;
    location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/run/php/php7.2-fpm.sock;
    }
}
~~~

Enlazamos la configuración para que el *virtual host* esté disponible:

~~~console
sdelquin@claseando:~$ sudo ln -s /etc/nginx/sites-available/wordpress.vps.claseando.es /etc/nginx/sites-enabled/
sdelquin@claseando:~$ ls -l /etc/nginx/sites-enabled/wordpress.vps.claseando.es
lrwxrwxrwx 1 root root 53 ene  9 12:11 /etc/nginx/sites-enabled/wordpress.vps.claseando.es -> /etc/nginx/sites-available/wordpress.vps.claseando.es
sdelquin@claseando:~$
~~~

Recargamos el servidor web *Nginx* para que los cambios sean efectivos:

~~~console
sdelquin@claseando:~$ sudo systemctl reload nginx
sdelquin@claseando:~$
~~~

## Configuración del sitio vía web

Ahora podemos acceder a la dirección de nuestro servidor para configurar nuestro *Wordpress* vía web.

Cuando accedemos a `http://wordpress.vps.claseando.me` nos redirige a `http://wordpress.vps.claseando.me/wp-admin/install.php`:

![](img/wp01.png)

Elegimos el idioma *Español* y le damos a <kbd>Continuar</kbd>:

![](img/wp02.png)

Rellenamos los campos que nos piden y pulsamos <kbd>Instalar Wordpress</kbd>:

![](img/wp03.png)

Pulsamos en el botón <kbd>Acceder</kbd> e ingresamos nuestras credenciales:

![](img/wp04.png)

Así habremos podido acceder a la interfaz administrativa de Wordpress:

![](img/wp05.png)

## Ajuste de permalinks

En primer lugar activamos esta opción dentro de la interfaz administrativa de Wordpress:

![AjustesPermalinks1](img/wp06.png) 

Seleccionamos el ajuste **Día y nombre**. Pulsamos en <kbd>Guardar cambios</kbd>.

![AjustesPermalinks2](img/wp07.png) 

Ahora debemos indicar a Nginx que procese estas URLs:

~~~console
sdelquin@claseando:~$ sudo vi /etc/nginx/sites-available/wordpress.vps.claseando.es
~~~

> Añadir lo siguiente:

~~~nginx
location / {
    try_files $uri $uri/ /index.php?$args;
}
~~~

No olvidarnos de recargar la configuración de Nginx:

~~~console
sdelquin@claseando:~$ sudo systemctl reload nginx
sdelquin@claseando:~$
~~~

Una ventaja que tiene este método es que podemos acceder a la **zona administrativa** utilizando la siguiente URL: http://wordpress.vps.claseando.es/admin

## Límite de tamaño en la subida de archivos

Por defecto, el límite de subida de archivos para aplicaciones *PHP* suele ser bastante bajo, en torno a los 2MB.

Para incrementarlo, debemos hacer lo siguiente, como *root* en la máquina de producción:

~~~console
sdelquin@claseando:~$ sudo vi /etc/php/7.2/fpm/php.ini
~~~

Buscar y modificar sólo las siguientes líneas...

> Contenido:
~~~ini
upload_max_filesize = 64M
post_max_size = 64M
max_execution_time = 300
~~~

Ahora reinciamos el servicio `php-fpm`:

~~~console
sdelquin@claseando:~$ sudo systemctl restart php7.2-fpm.service
sdelquin@claseando:~$
~~~

Además de esto, debemos añadir una línea en el fichero de configuración de *Nginx*:

~~~console
sdelquin@cloud:~$ sudo vi /etc/nginx/nginx.conf
~~~

> Contenido:
~~~nginx
http {

    ##
    # Custom settings
    ##

    client_max_body_size 64M;

    ...
~~~

A continuación reiniciamos el servidor web *Nginx* para que tengan efectos los cambios realizados en el fichero de configuración:

~~~console
sdelquin@claseando:~$ sudo systemctl reload nginx
sdelquin@claseando:~$
~~~

## Seguridad

- Crear contraseñas complicadas (más de 8 caracteres con letras, números y signos de puntuación.).
- No utilizar el nombre de usuario "Admin".
- Limitar los intentos de login fallidos (plugin [Limit Login Attempts](https://wordpress.org/extend/plugins/limit-login-attempts/)).
- Controlar el *spam* (plugin [Akismet](http://wordpress.org/plugins/akismet/))
- No instalar muchos plugins.
- Buscar código malicioso en los archivos de tu *theme*.
- Añadir un firewall.
- Hacer un backup de la instalación periódicamente (plugin [Updraft Plus](http://wordpress.org/plugins/updraftplus/)).
- Mantener actualizados themes, plugins y software de Wordpress.
- Usar un plugin como [iThemes Security](https://wordpress.org/plugins/better-wp-security/).

## Estructura de ficheros

~~~console
sdelquin@claseando:~$ cd /usr/share/wordpress/wp-content/
sdelquin@claseando:/usr/share/wordpress/wp-content$ ls
index.php  languages  plugins  themes  upgrade  uploads
sdelquin@claseando:/usr/share/wordpress/wp-content$ tree -d
.
├── languages
│   ├── plugins
│   └── themes
├── plugins
│   └── akismet
│       ├── _inc
│       │   └── img
│       └── views
├── themes
│   ├── twentynineteen
│   │   ├── classes
│   │   ├── fonts
│   │   ├── inc
│   │   ├── js
│   │   ├── sass
│   │   │   ├── blocks
│   │   │   ├── elements
│   │   │   ├── forms
│   │   │   ├── layout
│   │   │   ├── media
│   │   │   ├── mixins
│   │   │   ├── modules
│   │   │   ├── navigation
│   │   │   ├── site
│   │   │   │   ├── footer
│   │   │   │   ├── header
│   │   │   │   ├── primary
│   │   │   │   └── secondary
│   │   │   ├── typography
│   │   │   └── variables-site
│   │   └── template-parts
│   │       ├── content
│   │       ├── footer
│   │       ├── header
│   │       └── post
│   ├── twentyseventeen
│   │   ├── assets
│   │   │   ├── css
│   │   │   ├── images
│   │   │   └── js
│   │   ├── inc
│   │   └── template-parts
│   │       ├── footer
│   │       ├── header
│   │       ├── navigation
│   │       ├── page
│   │       └── post
│   └── twentysixteen
│       ├── css
│       ├── genericons
│       ├── inc
│       ├── js
│       └── template-parts
├── upgrade
└── uploads
    └── 2019
        └── 01

57 directories
sdelquin@claseando:/usr/share/wordpress/wp-content$
~~~
