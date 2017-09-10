# Flask

[Flask](http://flask.pocoo.org/) es una librería de *python*, que se define como un *microframework* para el desarrollo de aplicaciones web.

## Instalación

Primero, como siempre, creamos un nuevo *entorno virtual*:

```console
~|🍺  mkv3 myweb
Running virtualenv with interpreter /usr/local/bin/python3
Using base prefix "/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5"
New python executable in /Users/sdelquin/.virtualenvs/myweb/bin/python3.5
Also creating executable in /Users/sdelquin/.virtualenvs/myweb/bin/python
Installing setuptools, pip, wheel...done.
virtualenvwrapper.user_scripts creating /Users/sdelquin/.virtualenvs/myweb/bin/predeactivate
virtualenvwrapper.user_scripts creating /Users/sdelquin/.virtualenvs/myweb/bin/postdeactivate
virtualenvwrapper.user_scripts creating /Users/sdelquin/.virtualenvs/myweb/bin/preactivate
virtualenvwrapper.user_scripts creating /Users/sdelquin/.virtualenvs/myweb/bin/postactivate
virtualenvwrapper.user_scripts creating /Users/sdelquin/.virtualenvs/myweb/bin/get_env_details
Requirement already up-to-date: pip in ./.virtualenvs/myweb/lib/python3.5/site-packages
Collecting ipython
  Using cached ipython-5.1.0-py3-none-any.whl
Collecting appnope; sys_platform == "darwin" (from ipython)
  Using cached appnope-0.1.0-py2.py3-none-any.whl
Collecting traitlets>=4.2 (from ipython)
  Using cached traitlets-4.3.1-py2.py3-none-any.whl
Collecting pexpect; sys_platform != "win32" (from ipython)
  Using cached pexpect-4.2.1-py2.py3-none-any.whl
Collecting prompt-toolkit<2.0.0,>=1.0.3 (from ipython)
  Using cached prompt_toolkit-1.0.9-py3-none-any.whl
Requirement already up-to-date: setuptools>=18.5 in ./.virtualenvs/myweb/lib/python3.5/site-packages (from ipython)
Collecting simplegeneric>0.8 (from ipython)
Collecting pickleshare (from ipython)
  Using cached pickleshare-0.7.4-py2.py3-none-any.whl
Collecting decorator (from ipython)
  Using cached decorator-4.0.10-py2.py3-none-any.whl
Collecting pygments (from ipython)
  Using cached Pygments-2.1.3-py2.py3-none-any.whl
Collecting six (from traitlets>=4.2->ipython)
  Using cached six-1.10.0-py2.py3-none-any.whl
Collecting ipython-genutils (from traitlets>=4.2->ipython)
  Using cached ipython_genutils-0.1.0-py2.py3-none-any.whl
Collecting ptyprocess>=0.5 (from pexpect; sys_platform != "win32"->ipython)
  Using cached ptyprocess-0.5.1-py2.py3-none-any.whl
Collecting wcwidth (from prompt-toolkit<2.0.0,>=1.0.3->ipython)
  Using cached wcwidth-0.1.7-py2.py3-none-any.whl
Installing collected packages: appnope, six, ipython-genutils, decorator, traitlets, ptyprocess, pexpect, wcwidth, prompt-toolkit, simplegeneric, pickleshare, pygments, ipython
Successfully installed appnope-0.1.0 decorator-4.0.10 ipython-5.1.0 ipython-genutils-0.1.0 pexpect-4.2.1 pickleshare-0.7.4 prompt-toolkit-1.0.9 ptyprocess-0.5.1 pygments-2.1.3 simplegeneric-0.8.1 six-1.10.0 traitlets-4.3.1 wcwidth-0.1.7
Requirement already up-to-date: wheel in ./.virtualenvs/myweb/lib/python3.5/site-packages
~|🍺
```

Ahora instalamos la librería:

```console
~|🍺  workon myweb
(myweb) ~/Dropbox/Code/myweb|🍺
(myweb) ~/Dropbox/Code/myweb|🍺  pip install flask
Collecting flask
  Using cached Flask-0.11.1-py2.py3-none-any.whl
Collecting click>=2.0 (from flask)
  Downloading click-6.6-py2.py3-none-any.whl (71kB)
    100% |████████████████████████████████| 71kB 479kB/s
Collecting Jinja2>=2.4 (from flask)
  Using cached Jinja2-2.8-py2.py3-none-any.whl
Collecting Werkzeug>=0.7 (from flask)
  Using cached Werkzeug-0.11.11-py2.py3-none-any.whl
Collecting itsdangerous>=0.21 (from flask)
Collecting MarkupSafe (from Jinja2>=2.4->flask)
Installing collected packages: click, MarkupSafe, Jinja2, Werkzeug, itsdangerous, flask
Successfully installed Jinja2-2.8 MarkupSafe-0.23 Werkzeug-0.11.11 click-6.6 flask-0.11.1 itsdangerous-0.24
(myweb) ~/Dropbox/Code/myweb|🍺
```

## Primera aplicación *Flask*

```console
(myweb) ~/Dropbox/Code/myweb|🍺  vi main.py
```

> Contenido:
> ```python
> from flask import Flask
> 
> app = Flask(__name__)
> 
> @app.route("/")
> def hello():
>     return "Hello World!"
> 
> if __name__ == "__main__":
>     app.run(debug=True)
> ```

Lanzamos nuestra aplicación:

```console
(myweb) ~/Dropbox/Code/myweb|🍺  python main.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger pin code: 203-004-358
```

Si ahora accedemos en el navegador a la dirección que nos indica `http://127.0.0.1:5000/`

![](img/flask01.png)

## Mejorando las URLs

El [enrutamiento](http://flask.pocoo.org/docs/0.11/quickstart/#routing) es el mecanismo que nos permite vincular *URLs* con funciones *python*.

```python
@app.route("/")
def index():
    return "Index Page"

@app.route("/hello")
def hello():
    return "Hello, World"

@app.route("/user/<username>")
def show_user_profile(username):
    return "User {}".format(username)

@app.route("/post/<post_id>")
def show_post(post_id):
    return "Post {}".format(post_id)
```

## Petición POST

Por defecto, *Flask* entiende las peticiones *HTTP* como peticiones tipo *GET*. Si queremos enviar un formulario vía [POST](http://flask.pocoo.org/docs/0.11/quickstart/#http-methods), tenemos que hacer lo siguiente:

```python
from flask import request

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        do_the_login(
            request.form["username"],   # el campo del formulario debe tener name="username"
            request.form["password"]    # el campo del formulario debe tener name="password"
        )
    else:
        show_the_login_form()
```

## Plantillas

Para que nuestra aplicación esté bien organizada, tendremos que poner el código de [las plantillas](http://flask.pocoo.org/docs/0.11/quickstart/#rendering-templates) en ficheros separados:

```python
from flask import render_template

@app.route("/hello/<name>")
def hello(name=None):
    return render_template("hello.html", name=name)
```

Las plantillas deben estar dentro de la carpeta `templates`. Con esto, la estructura de nuestra aplicación podría quedar así:

```console
/main.py
/templates
    /hello.html
```

Las plantillas utilizan el lenguaje [Jinja2](http://jinja.pocoo.org/docs/dev/templates/). Vamos a ver cómo sería el código de nuestra plantilla `hello.html`:

```html+jinja
Hola {{ name }}!!
```

Un ejemplo de plantilla algo más elaborada, utilizando un bucle, sería la siguiente:

```html+jinja
<!DOCTYPE html>
<html lang="en">
<head>
    <title>My Webpage</title>
</head>
<body>
    <ul id="navigation">
    {% for item in navigation %}
        <li><a href="{{ item.href }}">{{ item.caption }}</a></li>
    {% endfor %}
    </ul>

    <h1>My Webpage</h1>
    {{ a_variable }}

    {# a comment #}
</body>
</html>
```
