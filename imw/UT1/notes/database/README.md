# Base de datos

El sistema gestor de bases de datos que vamos a utilizar es **MySQL**.

![MySQL Logo](img/mysql_logo.png) 

## Instalación

En primer lugar actualizamos los repositorios:

~~~console
sdelquin@claseando:~$ sudo apt update
[sudo] password for sdelquin:
Obj:1 http://ppa.launchpad.net/certbot/certbot/ubuntu bionic InRelease
Des:2 http://security.ubuntu.com/ubuntu bionic-security InRelease [83,2 kB]
Obj:3 http://mirrors.digitalocean.com/ubuntu bionic InRelease
Des:4 http://mirrors.digitalocean.com/ubuntu bionic-updates InRelease [88,7 kB]
Des:5 http://mirrors.digitalocean.com/ubuntu bionic-backports InRelease [74,6 kB]
Des:6 http://security.ubuntu.com/ubuntu bionic-security/main Sources [51,0 kB]
Des:7 http://security.ubuntu.com/ubuntu bionic-security/main amd64 Packages [179 kB]
Des:8 http://security.ubuntu.com/ubuntu bionic-security/main Translation-en [69,7 kB]
Des:9 http://security.ubuntu.com/ubuntu bionic-security/universe amd64 Packages [85,2 kB]
Des:10 http://security.ubuntu.com/ubuntu bionic-security/universe Translation-en [46,8 kB]
Des:11 http://mirrors.digitalocean.com/ubuntu bionic-updates/main Sources [193 kB]
Des:12 http://mirrors.digitalocean.com/ubuntu bionic-updates/universe Sources [87,5 kB]
Des:13 http://mirrors.digitalocean.com/ubuntu bionic-updates/main amd64 Packages [396 kB]
Des:14 http://mirrors.digitalocean.com/ubuntu bionic-updates/main Translation-en [147 kB]
Des:15 http://mirrors.digitalocean.com/ubuntu bionic-updates/universe amd64 Packages [558 kB]
Des:16 http://mirrors.digitalocean.com/ubuntu bionic-updates/universe Translation-en [144 kB]
Descargados 2.204 kB en 1s (1.817 kB/s)
Leyendo lista de paquetes... Hecho
Creando árbol de dependencias
Leyendo la información de estado... Hecho
Se pueden actualizar 48 paquetes. Ejecute «apt list --upgradable» para verlos.
sdelquin@claseando:~$
~~~

Para la instalación vamos a usar el paquete preparado para ello:

```console
sdelquin@claseando:~$ sudo apt install -y mysql-server
Leyendo lista de paquetes... Hecho
Creando árbol de dependencias
Leyendo la información de estado... Hecho
El paquete indicado a continuación se instaló de forma automática y ya no es necesario.
  grub-pc-bin
Utilice «sudo apt autoremove» para eliminarlo.
Se instalarán los siguientes paquetes adicionales:
  libaio1 libcgi-fast-perl libcgi-pm-perl libencode-locale-perl libevent-core-2.1-6 libfcgi-perl
  libhtml-parser-perl libhtml-tagset-perl libhtml-template-perl libhttp-date-perl libhttp-message-perl
  libio-html-perl liblwp-mediatypes-perl libtimedate-perl liburi-perl mysql-client-5.7 mysql-client-core-5.7
  mysql-common mysql-server-5.7 mysql-server-core-5.7
Paquetes sugeridos:
  libdata-dump-perl libipc-sharedcache-perl libwww-perl mailx tinyca
Se instalarán los siguientes paquetes NUEVOS:
  libaio1 libcgi-fast-perl libcgi-pm-perl libencode-locale-perl libevent-core-2.1-6 libfcgi-perl
  libhtml-parser-perl libhtml-tagset-perl libhtml-template-perl libhttp-date-perl libhttp-message-perl
  libio-html-perl liblwp-mediatypes-perl libtimedate-perl liburi-perl mysql-client-5.7 mysql-client-core-5.7
  mysql-common mysql-server mysql-server-5.7 mysql-server-core-5.7
0 actualizados, 21 nuevos se instalarán, 0 para eliminar y 48 no actualizados.
Se necesita descargar 21,0 MB de archivos.
Se utilizarán 162 MB de espacio de disco adicional después de esta operación.
Des:1 http://ams2.mirrors.digitalocean.com/ubuntu bionic/main amd64 mysql-common all 5.8+1.0.4 [7.308 B]
Des:2 http://ams2.mirrors.digitalocean.com/ubuntu bionic/main amd64 libaio1 amd64 0.3.110-5 [6.448 B]
Des:3 http://ams2.mirrors.digitalocean.com/ubuntu bionic-updates/main amd64 mysql-client-core-5.7 amd64 5.7.23-0ubuntu0.18.04.1 [6.985 kB]
Des:4 http://ams2.mirrors.digitalocean.com/ubuntu bionic-updates/main amd64 mysql-client-5.7 amd64 5.7.23-0ubuntu0.18.04.1 [2.312 kB]
Des:5 http://ams2.mirrors.digitalocean.com/ubuntu bionic-updates/main amd64 mysql-server-core-5.7 amd64 5.7.23-0ubuntu0.18.04.1 [7.777 kB]
Des:6 http://ams2.mirrors.digitalocean.com/ubuntu bionic/main amd64 libevent-core-2.1-6 amd64 2.1.8-stable-4build1 [85,9 kB]
Configurando liburi-perl (1.73-1) ...
Procesando disparadores para systemd (237-3ubuntu10.3) ...
Configurando libhtml-parser-perl (3.72-3build1) ...
Configurando libcgi-pm-perl (4.38-1) ...
Procesando disparadores para man-db (2.8.3-2) ...
Configurando mysql-client-core-5.7 (5.7.23-0ubuntu0.18.04.1) ...
Configurando libfcgi-perl (0.78-2build1) ...
Configurando libhttp-date-perl (6.02-1) ...
Configurando libhtml-template-perl (2.97-1) ...
Configurando mysql-server-core-5.7 (5.7.23-0ubuntu0.18.04.1) ...
Configurando libcgi-fast-perl (1:2.13-1) ...
Configurando libhttp-message-perl (6.14-1) ...
Configurando mysql-client-5.7 (5.7.23-0ubuntu0.18.04.1) ...
Configurando mysql-server-5.7 (5.7.23-0ubuntu0.18.04.1) ...
update-alternatives: utilizando /etc/mysql/mysql.cnf para proveer /etc/mysql/my.cnf (my.cnf) en modo automático
Renaming removed key_buffer and myisam-recover options (if present)
Created symlink /etc/systemd/system/multi-user.target.wants/mysql.service → /lib/systemd/system/mysql.service.
Configurando mysql-server (5.7.23-0ubuntu0.18.04.1) ...
Procesando disparadores para libc-bin (2.27-3ubuntu1) ...
Procesando disparadores para ureadahead (0.100.0-20) ...
Procesando disparadores para systemd (237-3ubuntu10.3) ...
sdelquin@claseando:~$
```

Comprobamos que el servicio se esté ejecutando correctamente:

~~~console
sdelquin@claseando:~$ sudo systemctl status mysql
● mysql.service - MySQL Community Server
   Loaded: loaded (/lib/systemd/system/mysql.service; enabled; vendor preset: enabled)
   Active: active (running) since Fri 2018-10-05 08:17:07 UTC; 1min 28s ago
 Main PID: 21845 (mysqld)
    Tasks: 27 (limit: 1152)
   CGroup: /system.slice/mysql.service
           └─21845 /usr/sbin/mysqld --daemonize --pid-file=/run/mysqld/mysqld.pid

oct 05 08:17:06 claseando systemd[1]: Starting MySQL Community Server...
oct 05 08:17:07 claseando systemd[1]: Started MySQL Community Server.
sdelquin@claseando:~$
~~~

### Uso de memoria

*MySQL* es un proceso (o conjunto de procesos) que consume bastante memoria RAM. Para ver el consumo hacemos:

```console
sdelquin@claseando:~$ ps -ax -o pid,command,rss | grep mysql
21845 /usr/sbin/mysqld --daemoniz 174516
22283 grep --color=auto mysql      1084
sdelquin@claseando:~$ python3 -c 'print(174516 / 1024, "MB")'
170.42578125 MB
sdelquin@claseando:~$
```

Existe una web que permite tener una aproximación de la memoria que va a usar el servicio *MySQL* en función de ciertos parámetros de configuración: [MySQL Calculator](http://www.mysqlcalculator.com/).

## Instalación segura

La instalación por defecto de *MySQL* deja una base de datos de test y algunas cuentas extrañas de usuario, que pueden ser origen de problemas de seguridad. Vamos a intentar solucionar estos problemas usando el comando `mysql_secure_installation`:

~~~console
sdelquin@claseando:~$ sudo mysql_secure_installation
[sudo] password for sdelquin:

Securing the MySQL server deployment.

Connecting to MySQL using a blank password.

VALIDATE PASSWORD PLUGIN can be used to test passwords
and improve security. It checks the strength of password
and allows the users to set only those passwords which are
secure enough. Would you like to setup VALIDATE PASSWORD plugin?

Press y|Y for Yes, any other key for No: y

There are three levels of password validation policy:

LOW    Length >= 8
MEDIUM Length >= 8, numeric, mixed case, and special characters
STRONG Length >= 8, numeric, mixed case, special characters and dictionary                  file

Please enter 0 = LOW, 1 = MEDIUM and 2 = STRONG: 0
Please set the password for root here.

New password:

Re-enter new password:

Estimated strength of the password: 50
Do you wish to continue with the password provided?(Press y|Y for Yes, any other key for No) : y
By default, a MySQL installation has an anonymous user,
allowing anyone to log into MySQL without having to have
a user account created for them. This is intended only for
testing, and to make the installation go a bit smoother.
You should remove them before moving into a production
environment.

Remove anonymous users? (Press y|Y for Yes, any other key for No) : y
Success.


Normally, root should only be allowed to connect from
'localhost'. This ensures that someone cannot guess at
the root password from the network.

Disallow root login remotely? (Press y|Y for Yes, any other key for No) : y
Success.

By default, MySQL comes with a database named 'test' that
anyone can access. This is also intended only for testing,
and should be removed before moving into a production
environment.


Remove test database and access to it? (Press y|Y for Yes, any other key for No) : y
 - Dropping test database...
Success.

 - Removing privileges on test database...
Success.

Reloading the privilege tables will ensure that all changes
made so far will take effect immediately.

Reload privilege tables now? (Press y|Y for Yes, any other key for No) : y
Success.

All done!
sdelquin@claseando:~$
~~~

## Acceso al gestor de bases de datos

El comando que nos permite gestionar las bases de datos **MySQL** es, aunque parezca increíble `mysql` 😉

```console
sdelquin@claseando:~$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 14
Server version: 5.7.23-0ubuntu0.18.04.1 (Ubuntu)

Copyright (c) 2000, 2018, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```

Con `sudo mysql` estamos accediendo al gestor como usuario `root`.

## Política de contraseñas

Supongamos que queremos pasar de una política de contraseñas de nivel MEDIO a una de nivel BAJO. Haríamos lo siguiente:

~~~console
sdelquin@claseando:~$ sudo mysql
[sudo] password for sdelquin:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 3
Server version: 5.7.23-0ubuntu0.18.04.1 (Ubuntu)

Copyright (c) 2000, 2018, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
~~~

Ejecutamos la siguiente instrucción **SQL**:

~~~sql
mysql> SHOW VARIABLES LIKE 'validate_password%';
+--------------------------------------+--------+
| Variable_name                        | Value  |
+--------------------------------------+--------+
| validate_password_check_user_name    | OFF    |
| validate_password_dictionary_file    |        |
| validate_password_length             | 8      |
| validate_password_mixed_case_count   | 1      |
| validate_password_number_count       | 1      |
| validate_password_policy             | MEDIUM |
| validate_password_special_char_count | 1      |
+--------------------------------------+--------+
7 rows in set (0.01 sec)

mysql>
~~~

Podemos ver que tenemos el nivel **MEDIO** de seguridad en contraseñas, con lo que deberíamos cumplir con lo siguiente:

- La longitud de la contraseña debe ser de 8 o más caracteres.
- Deben incluir, al menos, uno de los siguientes caracteres:
  + Letras en mayúsculas.
  + Letras en minúsculas.
  + Dígitos.
  + Caracteres especiales ("!", "@", "$", etc.).

Si queremos modificar el nivel de seguridad en contraseñas, podemos hacer lo siguiente:

~~~sql
mysql> SET GLOBAL validate_password_policy=LOW;
Query OK, 0 rows affected (0.00 sec)

mysql>
~~~

Volvemos a comprobar el nivel:

~~~sql
mysql> SHOW VARIABLES LIKE 'validate_password%';
+--------------------------------------+-------+
| Variable_name                        | Value |
+--------------------------------------+-------+
| validate_password_check_user_name    | OFF   |
| validate_password_dictionary_file    |       |
| validate_password_length             | 8     |
| validate_password_mixed_case_count   | 1     |
| validate_password_number_count       | 1     |
| validate_password_policy             | LOW   |
| validate_password_special_char_count | 1     |
+--------------------------------------+-------+
7 rows in set (0.00 sec)

mysql>
~~~

## Ajuste de codificaciones

*MySQL* maneja una gran cantidad de variables globales, que configuran su comportamiento. Se pueden ver utilizando el comando `show variables;` dentro de una sesión en el intérprete.

Es importante ajustar las codificaciones que utiliza el sistema gestor. Primero vemos el valor que tienen utilizando el siguiente comando:

```sql
mysql> SHOW VARIABLES WHERE Variable_name LIKE 'character\_set\_%' OR Variable_name LIKE 'collation%';
+--------------------------+-------------------+
| Variable_name            | Value             |
+--------------------------+-------------------+
| character_set_client     | utf8              |
| character_set_connection | utf8              |
| character_set_database   | latin1            |
| character_set_filesystem | binary            |
| character_set_results    | utf8              |
| character_set_server     | latin1            |
| character_set_system     | utf8              |
| collation_connection     | utf8_general_ci   |
| collation_database       | latin1_swedish_ci |
| collation_server         | latin1_swedish_ci |
+--------------------------+-------------------+
10 rows in set (0.00 sec)
mysql>
```

Lo que queremos, es que todas las variables de codificación estén fijadas a `utf8mb4`.

El fichero de configuración de **MySQL** se encuentra en: `/etc/mysql/my.cnf`, pero se pueden incluir ficheros de configuración en la ruta: `/etc/mysql/conf.d/`

```console
sdelquin@claseando:~$ sudo vi /etc/mysql/conf.d/utf8mb4.cnf
```

>Contenido
```ini
[mysqld]
character-set-client-handshake = FALSE
character-set-server = utf8mb4
collation-server = utf8mb4_unicode_ci
```

Reiniciamos el servidor:

```console
sdelquin@claseando:~$ sudo systemctl restart mysql
sdelquin@claseando:~$
```

Accedemos de nuevo al intérprete SQL de **MySQL** para comprobar de nuevo las variables:

```sql
mysql> SHOW VARIABLES WHERE Variable_name LIKE 'character\_set\_%' OR Variable_name LIKE 'collation%';
+--------------------------+--------------------+
| Variable_name            | Value              |
+--------------------------+--------------------+
| character_set_client     | utf8mb4            |
| character_set_connection | utf8mb4            |
| character_set_database   | utf8mb4            |
| character_set_filesystem | binary             |
| character_set_results    | utf8mb4            |
| character_set_server     | utf8mb4            |
| character_set_system     | utf8               |
| collation_connection     | utf8mb4_unicode_ci |
| collation_database       | utf8mb4_unicode_ci |
| collation_server         | utf8mb4_unicode_ci |
+--------------------------+--------------------+
10 rows in set (0.00 sec)

mysql> Bye
```

> En el intérprete de MYSQL también funcionan los cursores para acceder a comandos ya ejecutados.
