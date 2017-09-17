# Máquina de producción

Vamos a intentar tener una máquina en producción a través de los servicios ofrecidos por [Digital Ocean](https://www.digitalocean.com/) . Para ello, vamos a tratar de conseguir crédito solicitando el *Student Developer Pack* de *GitHub*.

## Cuenta de correo del centro

En primer lugar necesitamos tener una cuenta de correo del IES Puerto de la Cruz - Telesforo Bravo. Han sido creadas cuentas para todo el alumnado de esta asignatura, en la forma:

> `aluXXXX@iespuertodelacruz.es`  

, donde XXXX es el número de expediente.

Para entrar en la cuenta, accedemos desde una navegador a [gmail.com](https://gmail.com) utilizando las siguientes credenciales:

- USUARIO: **cuenta de correo con dominio incluido**.
- CONTRASEÑA: tu **DNI** con la letra en mayúsculas.

## Cuenta en GitHub

`GitHub` es una plataforma de desarrollo colaborativo para alojar proyectos utilizando el sistema de control de versiones *Git*. [GitHub tiene actualmente cerca de 20 millones de repositorios de código](https://octoverse.github.com/).

![GitHub](img/github-octocat.png) 

Necesitamos una cuenta en *GitHub* para poder acceder al *Student Developer Pack*. Para ello nos registramos en su página utilizando el correo del centro.

![Join GitHub](img/join_github.png) 

## Solicitud del `Student Developer Pack`

Accedemos a [la página del `Student Developer Pack` de *GitHub*](https://education.github.com/pack/join).

![Student Developer Pack](img/sdp.png) 

Indicamos que somos estudiantes:

![YesStudent](img/iamstudent.png) 

Rellenar el formulario teniendo en cuenta lo siguiente:

- **Name**: tu nombre y apellidos.
- **school-issued email address**: tu dirección de correo del centro.
- **School name**: IES Puerto de la Cruz - Telesforo Bravo
- **Graduation year**: 2017
- **How do you plan to use GitHub?**: I want to use GitHub for my lessons at the school, and, of course, for my future code projects.

Si todo va bien, en poco tiempo recibiremos un correo confirmando la aprobación del `Student Developer Pack`.

## Digital Ocean

*Digital Ocean* es un plataforma que da **servicios de hosting**.

Lo primero que debemos hacer es registrarnos en [Digital Ocean](https://cloud.digitalocean.com/registrations/new), utilizando la cuenta de correo del centro.

![DigitalOcean](img/digital-ocean.jpg) 

Una vez que completemos el registro, debemos acceder a la [configuración de pagos](https://cloud.digitalocean.com/settings/billing), e introducir el `Promo Code` que sacaremos del `Student Developer Pack`.

### Creación de un droplet

Tendremos que crear un **droplet** (*máquina virtual*) con las siguientes características:

- Ubuntu 16.04.3 x64.
- 5$/mo
- 512MB
- 1 CPU
- 20GB SSD disk
- 1000GB transfer
- Datacenter region: Frankfurt
- Hostname: `alu<expediente>`

Cuando hayamos terminado este proceso, tendremos una máquina disponible con una *IP pública* apuntando a la misma.

## Namecheap

*Namecheap* es una plataforma que da **servicios de nombres de dominio**.

![Namecheap](img/namecheap.png) 

Antes de nada, es necesario crear una cuenta en [Namecheap](https://www.namecheap.com/myaccount/signup.aspx) utilizando el correo electrónico del centro.

A continuación, regresamos al `Student Developer Pack` y accedemos a la sección de `Namecheap` para poder hacer uso del dominio gratuito.

### Creación de un dominio

El objetivo es crear un dominio que apunte a la máquina que hemos creado en *Digital Ocean*.

El nombre de dominio deberá ser: `alu<expediente>.me`

Una vez creado el dominio, debemos establecer los DNS de la siguiente forma:

![Namecheap DNS](img/namecheap-dns.png) 
