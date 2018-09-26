# Máquina de desarrollo

Para trabajar en esta asignatura necesitaremos dos máquinas: **máquina de desarrollo** y **máquina de producción**:

![Machines Diagram](img/machines_diagram.png) 

## Instalación

Usaremos una *máquina virtual* como *máquina de desarrollo*. Esta máquina tendrá sistema operativo Linux 64 bits, con las siguientes características:

- **Distribución**: `Ubuntu 18.04.1 Desktop LTS (Bionic Beaver)`. [Enlace para descargar iso](http://releases.ubuntu.com/18.04/ubuntu-18.04.1-desktop-amd64.iso).
La *.iso* también estará disponible en el servidor *Leela*.
- **Tamaño del disco duro**: 25GB.
- **Memoria**: 2GB.
- **Nombre de la máquina**: `imw<expediente>` (ej. *imw3421*) Así evitamos conflictos del mismo nombre de máquina en la red local.
- **Nombre de usuario**: `alu<expediente>` (ej. *alu3421*)

> **NOTA**:Puede que haya problemas de **"freezing"** con VirtualBox y máquinas virtuales Ubuntu 18.04. Si esto pasa, se recomienda cambiar el *adaptador de red* de la máquina virtual a **NAT**.

> Realizar **instalación mínima** y **desactivar actualizaciones**.

## Configuración de la interfaz de red

Si vamos a trabajar en el instituto y en casa, tendremos que poder acceder a la máquina de desarrollo desde las dos localizaciones.

### Asignar una IP fija

Dado que tenemos redes diferentes en el instituto y en casa, vamos a configurar la interfaz de red en la máquina de desarrollo, para que asuma 2 direcciones de red diferentes, y podamos acceder a ella desde ambas localizaciones.

> NOTA:
> El adaptador de red debe configurarse en modo *bridge* o *puente*.

Lo primero de todo es deshabilitar la configuración por defecto que activa el *DHCP*:

~~~console
sdelquin@imw:~$ sudo vi /etc/netplan/50-cloud-init.yaml
...
~~~

~~~yaml
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
~~~

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
