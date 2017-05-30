# UT1-A3: Trabajo con *virtual hosts*

La actividad consiste en configurar 4 sitios web (*virtual hosts*) en nuestro servidor web *Nginx*.

## Sitio web 1

- `http://imw.aula108.local`
    - Debe mostrar una página con la imagen de "Diagrama de unidades de trabajo" de *IMW* (ver *moodle* de la asignatura).
    - La imagen no debe ser enlazada en remoto, sino se debe descargar al directorio de trabajo en la máquina de producción, y luego usar un tag `<img>` apuntando a la ruta local.
- `http://imw.aula108.local/mec/`
    - Debe mostrar una página con un enlace al Real decreto del título de Administración de Sistemas Informáticos en Red - MEC (ver *moodle* de la asignatura).

## Sitio web 2

- `http://lib.local:9000`
- Debe mostrar el listado de ficheros y directorios de `/var/lib`

## Sitio web 3

- `https://locked.local` (ojo, es *https!*)
- Debe pedir usuario/clave. Los datos son:
    - USUARIO: `usuario1`
    - CLAVE: `aula108`
- Debe mostrar una página web con el nombre de todos los alumnos/as de clase.
- Se debe prohibir el acceso al fichero `.htpasswd`

## Sitio web 4

- `http://www.redirect.local`
- Se debe redirigir cualquier petición de este dominio a `http://redirect.local`
    + `http://www.redirect.local/probando` -> `http://redirect.local`
    + `http://www.redirect.local/hola` -> `http://redirect.local`  
    ...
- Al acceder a `http://redirect.local` se debe mostrar la página web siguiente [initializr.zip](https://dl.dropboxusercontent.com/u/3285051/imw/initializr.zip)
    + Para copiar y descomprimir el fichero `initializr.zip` se recomienda usar alguna de las siguientes herramientas: `wget`, `scp`, `unzip`.

- Los *logfiles* deben ser:
    + `/var/log/nginx/redirect/access.log`
    + `/var/log/nginx/redirect/error.log`

## Fichero a entregar

El fichero a entregar será un informe en formato *PDF*, donde expliques lo que has hecho, justificando tus decisiones.
