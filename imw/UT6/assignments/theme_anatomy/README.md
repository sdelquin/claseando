# UT6-A2: Anatomía de un tema Wordpress

La actividad consiste en personalizar un tema de *Wordpress*.

1. Partir de una instalación limpia de Wordpress, o resetearla utilizando algún plugin al efecto.
1. Instalar el tema "Sparkling".
2. Crear un tema hijo llamado "MySparkling" y activarlo. Es necesario que aparezca el nombre del tema en el menú de *Apariencia* de Wordpress.  
![](img/theme.png)
3. Poner de fondo de página el siguiente patrón (cogido de la página https://www.toptal.com/designers/subtlepatterns/).
![](img/background.png)
4. En la página inicial de *Wordpress*, las entradas se deben ver de la siguiente manera:  
![](img/post.png)  
Ojo a los siguientes detalles:
    + Icono antes del título.
    + Autor de la entrada.
    + Borde rojo con esquinas curvas en imágenes.
    + Borde gris a toda la entrada.
5. Una vez que se haga click en cada entrada, se deben ver de la siguiente manera:  
![](img/whole_post.png)  
Ojo a los siguientes detalles:
    + Icono antes del título.
    + Enlace corto de la entrada.
    + Borde rojo con esquinas curvas en imágenes.
    + Borde gris a toda la entrada.
6. Se debe crear un panel en la barra lateral derecha con esta forma:
![](img/subscribe1.png)
7. El panel debe controlar que no se deje el *email* vacío y también que el *email* sea válido:  
![](img/subscribe2.png)
![](img/subscribe3.png)
8. Al pulsar en *SUSCRIBIRME!* se debe enviar la petición a un fichero `/wp-content/themes/MySparkling/subscribe.php` que debe hacer 3 cosas:
    - Mostrar un *alert* con el siguiente aspecto:  
    ![](img/subscribe4.png)
    - Guardar el email pasado por `POST` en un fichero `subscribers.txt`.
    - Redirigir la página a `"/"`. Utilizar: `header("refresh:0;url=/");`
9. Crear una cabecera con el siguiente aspecto:  
![](img/header.png)
    - La imagen debe tener 100px de ancho/alto.
    - La url de la imagen es: http://www.wordpresstrainingandclasses.com/wp-content/uploads/2013/05/wordpress-logo-730x584.png
10. El aspecto global de la web debería ser el siguiente:  
![](img/wireframe.png)

## Comprobación del formulario

Supongamos que la ruta al fichero de suscripción es:

`/usr/share/wordpress/wp-content/themes/MySparkling/subscribers.txt`

Incluir la siguiente directiva en el *virtual-host* de Nginx:

~~~nginx
location /contacts {
    alias /usr/share/wordpress/wp-content/themes/MySparkling/subscribers.txt
}
~~~

De esta forma, al acceder a http://customwp.aluXXXX.me/contacts podremos ver el fichero de suscripción y comprobar que está funcionando bien mediante el formulario.

## Notas

> Todas las modificaciones de estilo deben incluirse bien en el fichero `style.css` ó bien en un nuevo fichero creado para ello. Es decir, no se permiten reglas de estilo dentro de los propios ficheros *php*/*html*.

> Ojo con los permisos de los ficheros. El usuario que utiliza Nginx es `www-data`, por lo tanto debemos asegurarnos que los ficheros tienen permiso de lectura para *"others"*. Lo más fácil sería utilizar la máscara 755.

> Una manera sencilla de modificar los ficheros del tema es utilizando el editor visual de código integrado en el propio Wordpress.

## Enlaces

- [Añadir líneas a un fichero de texto en PHP](http://stackoverflow.com/a/24972441)
- [Mostrar un `alert` a través de PHP](http://stackoverflow.com/a/13851576)
- [Iconos de Font Awesome](http://fontawesome.io/icons/)
- [Bootstrap](http://getbootstrap.com/)

## Información a entregar

No es necesario entregar informe. Únicamente habrá que subir la URL del blog: `http://customwp.aluXXXX.me`.
