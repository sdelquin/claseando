# Misc

## Configuración de la interfaz de red

Si vamos a trabajar en el instituto y en casa, tendremos que poder acceder a la máquina de origen desde las dos localizaciones.

### Asignar una IP fija

#### `/etc/interfaces`

Dado que tenemos redes diferentes en el instituto y en casa, vamos a configurar la interfaz de red en la máquina de origen, para que asuma 2 direcciones de red diferentes, y podamos acceder a ella desde ambas localizaciones.

> NOTA:
> El adaptador de red debe configurarse en modo *bridge* o *puente*.

```bash
sdelquin@imwprofe:~$
sdelquin@imwprofe:~$ sudo vi /etc/network/interfaces
```

> Contenido:

```bash
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

source /etc/network/interfaces.d/*

# The loopback network interface
auto lo
iface lo inet loopback

# school interface
auto ens33:0
iface ens33:0 inet static
    address 172.18.<tu_numero>.<lo_que_quieras>    # pon una dirección de tu rango
    netmask 255.255.0.0
    broadcast 172.18.255.255
    post-up route add default gw 172.18.0.1
    dns-nameservers 1.1.1.1 1.0.0.1

# home interface
auto ens33:1
iface ens33:1 inet static
    address 192.168.1.118
    netmask 255.255.255.0
    broadcast 192.168.1.255
    post-up route add default gw 192.168.1.1
    dns-nameservers 1.1.1.1 1.0.0.1
```

Ahora debemos reiniciar nuestra máquina, para que todos estos cambios tengan efecto. Ejecutamos como **root**:

```bash
sdelquin@imwprofe:~$ sudo reboot
```

Una vez termine el reinicio, comprobamos que la máquina tiene salida hacia internet:

```bash
sdelquin@hillvalley:~$ ping -c4 google.com
PING google.com (216.58.211.238) 56(84) bytes of data.
64 bytes from mad01s24-in-f14.1e100.net (216.58.211.238): icmp_seq=1 ttl=56 time=28.5 ms
64 bytes from mad01s24-in-f14.1e100.net (216.58.211.238): icmp_seq=2 ttl=56 time=28.8 ms
64 bytes from mad01s24-in-f14.1e100.net (216.58.211.238): icmp_seq=3 ttl=56 time=28.7 ms
64 bytes from mad01s24-in-f14.1e100.net (216.58.211.238): icmp_seq=4 ttl=56 time=28.6 ms

--- google.com ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3006ms
rtt min/avg/max/mdev = 28.584/28.696/28.879/0.114 ms
sdelquin@hillvalley:~$
```

#### `/etc/netplan`

Dado que tenemos redes diferentes en el instituto y en casa, vamos a configurar la interfaz de red en la máquina de desarrollo, para que asuma 2 direcciones de red diferentes, y podamos acceder a ella desde ambas localizaciones.

> NOTA:
> El adaptador de red debe configurarse en modo *bridge* o *puente*.

Lo primero de todo es deshabilitar la configuración por defecto que activa el *DHCP*:

~~~console
sdelquin@imw:~$ sudo vi /etc/netplan/50-cloud-init.yaml
...
~~~

    # This file is generated from information provided by
    # the datasource.  Changes to it will not persist across an instance.
    # To disable cloud-init's network configuration capabilities, write a file
    # /etc/cloud/cloud.cfg.d/99-disable-network-config.cfg with the following:
    # network: {config: disabled}
    #network:
    #    ethernets:
    #        ens33:
    #            addresses: []
    #            dhcp4: true
    #    version: 2

A continuación vamos a crear un nuevo fichero de configuración para asignar la configuración estática a nuestra interfaz:

~~~console
sdelquin@imw:~$ sudo vi /etc/netplan/01-netcfg.yaml
...
~~~

~~~yaml
network:
  version: 2
  ethernets:
    ens33:  # este identificador debe ser el mismo que el del fichero 50-cloud-init.yaml
      addresses:
        - 192.168.1.120/24  # especifica un valor propio
        - 172.19.144.23/16  # especifica un valor propio
      routes:
        - to: 0.0.0.0/0
          via: 192.168.1.1
        - to: 0.0.0.0/0
          via: 172.19.0.1
      nameservers:
        addresses: [1.1.1.1, 1.0.0.1]
~~~

Ahora aplicamos la configuración:

~~~console
sdelquin@imw:~$ sudo netplan apply
~~~

Comprobamos la configuración del adaptador de red:

~~~console
sdelquin@imw:~$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: ens33: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 00:0c:29:4e:59:3e brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.120/24 brd 192.168.1.255 scope global ens33
       valid_lft forever preferred_lft forever
    inet 172.19.144.23/16 brd 172.19.255.255 scope global ens33
       valid_lft forever preferred_lft forever
    inet6 fe80::20c:29ff:fe4e:593e/64 scope link
       valid_lft forever preferred_lft forever
sdelquin@imw:~$
~~~

Si queremos ver los "saltos" que da la conexión de salida, podemos hacer una prueba con la herramienta `mtr`:

~~~console
                                            My traceroute  [v0.92]
imw (192.168.1.120)                                                                  2018-09-16T09:33:14+0000
Keys:  Help   Display mode   Restart statistics   Order of fields   quit
                                                                     Packets               Pings
 Host                                                              Loss%   Snt   Last   Avg  Best  Wrst StDev
 1. 192.168.1.1                                                     0.0%    50    0.8   0.7   0.5   1.1   0.1
 2. 192.168.144.1                                                   0.0%    50    5.6   8.4   5.2  41.0   7.7
 3. ???
 4. 81.46.0.121                                                     0.0%    50   29.6  32.7  29.4  71.6   7.5
 5. 80.58.96.117                                                    0.0%    50   29.1  30.2  28.9  52.5   3.5
 6. 213.140.51.56                                                   0.0%    50   29.1  30.8  29.0  38.8   2.5
 7. 5.53.7.225                                                      0.0%    50   36.2  35.6  29.9  89.7   9.5
 8. 213.140.36.146                                                  0.0%    50   29.9  30.1  29.7  31.5   0.4
 9. 94.142.97.138                                                   0.0%    50   30.0  29.8  29.5  30.7   0.3
10. 94.142.107.37                                                   0.0%    50   29.9  30.1  29.6  37.1   1.1
11. 89.149.187.150                                                  0.0%    50   29.6  32.7  29.3  85.6  10.2
12. 77.67.94.246                                                    0.0%    50   30.2  30.5  30.0  35.0   0.8
13. 212.23.53.98                                                    0.0%    49   29.6  29.8  29.6  30.5   0.2
14. 91.216.63.13                                                    0.0%    49   30.2  30.1  29.6  30.5   0.2
15. 91.216.63.241                                                   0.0%    49   29.8  29.7  29.5  30.6   0.2

~~~

### Acceso por nombre de máquina

Ahora, **desde la máquina de origen**, para no estar todo el tiempo haciendo uso de la IP para conectarnos a la máquina, podemos añadir un alias (*dns local*). Para ello, haremos lo siguiente como usuario **root**:

```bash
~|🍺  sudo vi /etc/hosts
```

> Contenido
```bash
...
<ip_de_la_maquina_de_produccion> debian imw produccion
...
```

Ahora, desde la máquina de origen, te podrás referir a la máquina, con los nombres `debian`, `imw` ó `produccion`:

```bash
~|🍺  ping debian
PING hillvalley (192.168.1.118): 56 data bytes
64 bytes from 192.168.1.118: icmp_seq=0 ttl=64 time=0.278 ms
64 bytes from 192.168.1.118: icmp_seq=1 ttl=64 time=0.433 ms
^C
--- hillvalley ping statistics ---
2 packets transmitted, 2 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 0.278/0.356/0.433/0.077 ms
~|🍺
```

Dado que vamos a acceder a nuestra máquina, bien desde el instituto o bien desde casa, pondremos un sufijo a los nombres de máquina en el fichero `/etc/hosts` para identificarlos rápidamente. Un ejemplo podría ser lo siguiente:

```bash
172.18.10.22    debian.ies imw.ies produccion.ies
192.168.1.118   debian.home imw.home produccion.home
```

## Instalación de servicio SSH

```bash
sdelquin@imwprofe:~$ sudo apt-get update
sdelquin@imwprofe:~$ sudo apt-get install openssh-server
```

### Acceso por SSH (sin password)

La primera vez que intentamos entrar a nuestra máquina (en mi caso se llama `hillvalley`) aparece un mensaje de autenticidad. Escribimos `yes` y pondremos nuestra contraseña.

```bash
~|🍋  ssh imw.home
The authenticity of host 'imw.home (192.168.1.119)' can't be established.
ECDSA key fingerprint is SHA256:WXdhgwFlATz5mI6GArf0u6XXRG1+WMFkcZm6jO2gO1M.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'imw.home,192.168.1.119' (ECDSA) to the list of known hosts.
sdelquin@imw.home's password:
Welcome to Ubuntu 16.04.3 LTS (GNU/Linux 4.4.0-93-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage
Last login: Sun Sep 17 16:21:59 2017
sdelquin@imwprofe:~$
```

Al hacer esto, se añadirán los datos del host destino en el fichero `~/.ssh/known_hosts`.

Para no tener que escribir la contraseña de usuario cada vez que nos conectamos a la máquina, podemos hacer uso de la clave pública *RSA*

Lo primero es comprobar si ya disponemos de una clave *RSA* en la máquina de origen. Para eso comprobamos que existan ficheros en el directorio `~.ssh`:

```bash
~|🍋  tree .ssh
.ssh
├── config
├── id_rsa
├── id_rsa.pub
└── known_hosts

0 directories, 4 files
~|🍋
```

En este caso, sí disponemos de las claves *RSA*:
- `id_rsa`: clave privada. **No compartir nunca con nadie**
- `id_rsa.pub`: clave pública.

En el caso de que no tuviéramos la pareja de claves *RSA*, tenemos que generarlas con el comando `ssh-keygen`.

> NOTA: Ejecutar este comando como usuario **normal**.

```bash
~|🍋 ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/sdelquin/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/sdelquin/.ssh/id_rsa.
Your public key has been saved in /home/sdelquin/.ssh/id_rsa.pub.
The key fingerprint is:
b7:5f:51:52:22:46:02:18:19:80:64:85:64:88:12:d9 sdelquin@delorean
The key's randomart image is:
+---[RSA 2048]----+
|oB=+o.o=....+ . .|
|=oE   o    o . o |
|.             . .|
|               o |
|        S .   .  |
|         . .   . |
|          .   .  |
|           . .   |
|            .    |
+-----------------+
~|🍺
```

Ahora debemos copiar (ó añadir) nuestra clave pública `id_rsa.pub` al fichero `authorized_keys` de la máquina (`hillvalley` en mi caso):

```bash
~|🍋 scp .ssh/id_rsa.pub imw.home:~/.ssh/authorized_keys
sdelquin@imw.home's password:
id_rsa.pub                                                                  100%  405     0.4KB/s   00:00
~|🍋  
```

> NOTA1: El directorio `~/.ssh` debe existir en la máquina. Si no es así, el comando anterior nos dará un error. Para crearlo, habría que entrar por SSH a la máquina, y crear el directorio: `mkdir ~/.ssh`

> NOTA2: Si el fichero `~/.ssh/authorized_keys` no está vacío previamente en la máquina, debemos tener cuidado con el comando anterior, ya que lo podemos sobreescribir. Si existiera habría que añadir el contenido de la clave pública `id_rsa.pub` al final del fichero `authorized_keys`.

Una vez hecho esto, cuando accedamos por *ssh* ya no tendremos que volver a teclear nuestra contraseña:

```bash
🍋  ssh imw.home
Welcome to Ubuntu 16.04.3 LTS (GNU/Linux 4.4.0-93-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage
Last login: Sun Sep 17 16:49:26 2017 from 192.168.1.41
sdelquin@imwprofe:~$
```

### Acceso root a ssh

Como norma general, no es recomendable habilitar el acceso por *ssh* como `root`. Es preferible acceder como usuario *"normal"*, y una vez dentro, cambiar a superusuario con el comando `su`.

Sin embargo, sólo para el entorno de clase, y para facilitar al profesor el acceso a las máquinas, se tendrá que habilitar el acceso root por ssh. Para ello, desde la máquina y como usuario *root*:

```bash
sdelquin@imwprofe:~$ vi /etc/ssh/sshd_config
```

> Contenido
```ini
...
PermitRootLogin yes
...
```

```bash
sdelquin@imwprofe:~$ /etc/init.d/ssh restart
[ ok ] Restarting ssh (via systemctl): ssh.service.
sdelquin@imwprofe:~$
```

Ahora, podemos comprobar que el acceso *root* por *ssh* ya debe de funcionar. Así que ejecutamos lo siguiente desde la *máquina de origen*:

```bash
~|🍺  ssh root@hillvalley
root@hillvalley's password:

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Fri Aug 26 19:41:22 2016
sdelquin@imwprofe:~$
```

## Configuración de la zona horaria

~~~console
sdelquin@imw:~$ sudo dpkg-reconfigure tzdata
~~~

`Atlántico > Canarias`

~~~console
Current default time zone: 'Atlantic/Canary'
Local time is now:      Sun Sep 16 10:42:44 WEST 2018.
Universal Time is now:  Sun Sep 16 09:42:44 UTC 2018.

sdelquin@imw:~$
~~~

## Paquetes adicionales

```bash
apt-get install vim
apt-get install ntp
apt-get install unzip
```

## Configuraciones varias

### `ntp.conf`

```bash
root@hillvalley:~# crontab -e
```

> Contenido
```cron
5 * * * * /etc/init.d/ntp restart
```

### `.bashrc`

```bash
vi ~/.bashrc
```

> Contenido
```bash
...
export LS_OPTIONS='--color=auto'
eval "`dircolors`"
alias ls='ls $LS_OPTIONS'
...
export PS1="\[\033[38;5;229m\]\u\[$(tput sgr0)\]\[\033[38;5;15m\]@\[$(tput sgr0)\]\[\033[38;5;214m\]\h\[$(tput sgr0)\]\[\033[38;5;15m\]:\[$(tput sgr0)\]\[\033[48;5;164m\]\w\[$(tput sgr0)\]\[\033[48;5;-1m\]\\$ \[$(tput sgr0)\]"
export PATH=$PATH:.
export EDITOR=vim
```

Puedes configurar un prompt coloreado para *bash* a través de [http://bashrcgenerator.com/](http://bashrcgenerator.com/)

### `.exrc`

```bash
vi ~/.exrc
```

> Contenido
```vim
set ts=4
set sw=4
syntax on
set bg=dark
set ai
set expandtab
set paste
```

## Problemas comunes

* Si tienes problemas con la contraseña de `root` en tu máquina virtual, y no te funciona el que se supone que debe tener. Si crees que tu sistema sufre una *amnesia temporal*, debes hacer lo siguiente. Como usuario normal, ejecuta:

```bash
$> sudo passwd root
```

Ahora escribe tu contraseña de usuario normal, y a continuación tendrás que repetir la NUEVA contraseña de `root`.

## Activación del Swap

Si estuviéramos trabajando con una máquina de producción con poca memoria RAM, en este caso, sólo 512MB, debemos activar el Swap para no tener problemas con los servicios.

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

## Completar repositorios

Es posible que la versión `server` de Ubuntu sólo fije los repositorios básicos. Para ampliarlos habría que hacer lo siguiente:

~~~console
$ sudo vi /etc/apt/sources.list
...
~~~

~~~console
deb http://archive.ubuntu.com/ubuntu bionic main restricted universe multiverse
deb http://archive.ubuntu.com/ubuntu bionic-security main restricted universe multiverse
deb http://archive.ubuntu.com/ubuntu bionic-updates main restricted universe multiverse
~~~
