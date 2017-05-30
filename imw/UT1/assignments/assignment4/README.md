# UT1-A4: Sirviendo aplicaciones Php y Python

La actividad consiste en configurar 4 sitios web (*virtual hosts*) en nuestro servidor web *Nginx*, con las siguientes características.

## Sitio web 1

- `http://php.apps.local`
- Mostrar la aplicación [demo_php.zip](https://dl.dropboxusercontent.com/u/3285051/imw/demo_php.zip)

## Sitio web 2

- `http://python.apps.local`
- El código del programa *python* es el siguiente:

```python
import datetime

def application(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/html")])
    return [
    """
    <h1>Testing python over Nginx</h1>
    Today is: {today}
    <br>
    Now is: {now}
    """.format(
        today=datetime.datetime.now().strftime("%d/%m/%Y"),
        now=datetime.datetime.now().strftime("%H:%mh")
    )
    ]
```

- El código debe residir dentro de un directorio del *home* de un usuario no privilegiado.
- Se debe configurar *supervisor* para gestionar el proceso *uwsgi*, permitiendo que el usario no privilegiado lo administre.
- Se debe probar los siguientes comandos, y ver cómo es la respuesta del navegador al acceder a la web:
```console
$> supervisorctl status
$> supervisorctl start demo_python
$> supervisorctl stop demo_python
$> supervisorctl restart demo_python
```

## Fichero a entregar

El fichero a entregar será un informe en formato *PDF*, donde expliques lo que has hecho, justificando tus decisiones.
