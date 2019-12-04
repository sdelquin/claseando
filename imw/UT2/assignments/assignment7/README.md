# UT2-A7: Hecho con clase!

La actividad consiste en hacer un programa *Python* para gestionar nuestras máquinas virtuales.

En el programa habrá que diseñar una clase `VirtualMachine` con las siguientes características:

+ Atributos
    * `name` (nombre de la máquina)
    * `ram` (expresado en *Gb*)
    * `cpu` (expresado en *Ghz*)
    * `hdd` (expresado en *Gb*)
    * `os` (sistema operativo)
    * `status`
        - 0: Stopped
        - 1: Running
        - 2: Suspended
    * `proc` es una lista de diccionarios, donde cada diccionario tendrá los siguientes campos:
        - `pid`: identificador del proceso.
        - `ram`: cantidad de memoria RAM que usa del proceso.
        - `cpu`: cantidad de CPU que usa el proceso.
        - `hdd`: cantidad de HDD que usa el proceso.

+ Métodos
    * Constructor. `def __init__(self, name, ram=1, cpu=1.3, hdd=100, os='debian'):`
        - Guardar los parámetros como atributos del objeto.
        - Fijar el estado a parado.
        - Inicializar la lista de procesos a vacío.
    * Parar la máquina. `def stop(self):`
        - Debe cambiar el estado de la máquina.
        - Inicializar la lista de procesos a vacío.
    * Arrancar la máquina. `def start(self):`
        - Debe cambiar el estado de la máquina.
    * Suspender la máquina. `def suspend(self):`
        - Debe cambiar el estado de la máquina.
    * Reinicar la máquina. `def reboot(self):`
        - Llamada al método de parar la máquina.
        - Llamada al método de arrancar la máquina.
    * Lanzar un proceso. `def run(self, pid, ram, cpu, hdd)`
        - Mostrar mensaje para indicar que se está ejecutando el proceso con el `pid` pasado por argumentos.
        - Insertar un nuevo diccionario en la lista `proc` con los datos del nuevo proceso.
    * Porcentaje de uso de RAM. `def ram_usage(self):`
        - Recorrer la lista de procesos, y sumar la RAM usada.
        - Regla de 3 para sacar el porcentaje sobre la RAM total de la máquina.
        - Debe tener `return`.
    * Porcentaje de uso de CPU. `def cpu_usage(self):`
        - Recorrer la lista de procesos, y sumar la CPU usada.
        - Regla de 3 para sacar el porcentaje sobre la CPU total de la máquina.
        - Debe tener `return`.
    * Porcentaje de uso de HDD. `def hdd_usage(self):`
        - Recorrer la lista de procesos, y sumar la HDD usada.
        - Regla de 3 para sacar el porcentaje sobre la HDD total de la máquina.
        - Debe tener `return`.
    * Representación. `def __str__(self):`
        - Debe tener la forma:  
        `debian <name> [running|stopped|suspended]`  
        `5% RAM used | 10% CPU used | 25% HDD used`

## Probando nuestra clase

### Minas Tirith

1. Crear la máquina virtual "Minas Tirith". Imprimir máquina.
2. Arrancar la máquina. Imprimir máquina.
3. Lanzar procesos 1, 4 y 7. Imprimir máquina.
4. Reiniciar la máquina. Imprimir máquina.

### Rohan

1. Crear la máquina virtual "Rohan". Imprimir máquina.
2. Arrancar la máquina. Imprimir máquina.
3. Lanzar procesos 2, 5 y 8. Imprimir máquina.
4. Reiniciar la máquina. Imprimir máquina.

### Rivendel

1. Crear la máquina virtual "Rivendel". Imprimir máquina.
2. Arrancar la máquina. Imprimir máquina.
3. Lanzar procesos 3, 6 y 9. Imprimir máquina.
4. Reiniciar la máquina. Imprimir máquina.

#### Características de las máquinas virtuales

![](img/info_maq_virtuales.png)

#### Características de los procesos

![](img/info_procesos.png)

## Salida deseada

~~~console
$ python main.py


ubuntu <Minas Tirith> [Stopped]
0.00% RAM used | 0.00% CPU used | 0.00% HDD used


ubuntu <Minas Tirith> [Running]
0.00% RAM used | 0.00% CPU used | 0.00% HDD used

Ejecutando proceso con PID 1...
Ejecutando proceso con PID 4...
Ejecutando proceso con PID 7...

ubuntu <Minas Tirith> [Running]
76.25% RAM used | 100.00% CPU used | 97.37% HDD used


ubuntu <Minas Tirith> [Running]
0.00% RAM used | 0.00% CPU used | 0.00% HDD used


debian <Rohan> [Stopped]
0.00% RAM used | 0.00% CPU used | 0.00% HDD used


debian <Rohan> [Running]
0.00% RAM used | 0.00% CPU used | 0.00% HDD used

Ejecutando proceso con PID 2...
Ejecutando proceso con PID 5...
Ejecutando proceso con PID 8...

debian <Rohan> [Running]
86.67% RAM used | 68.42% CPU used | 62.00% HDD used


debian <Rohan> [Running]
0.00% RAM used | 0.00% CPU used | 0.00% HDD used


opensuse <Rivendel> [Stopped]
0.00% RAM used | 0.00% CPU used | 0.00% HDD used


opensuse <Rivendel> [Running]
0.00% RAM used | 0.00% CPU used | 0.00% HDD used

Ejecutando proceso con PID 3...
Ejecutando proceso con PID 6...
Ejecutando proceso con PID 9...

opensuse <Rivendel> [Running]
23.12% RAM used | 76.67% CPU used | 10.20% HDD used


opensuse <Rivendel> [Running]
0.00% RAM used | 0.00% CPU used | 0.00% HDD used

~~~

## Información a entregar

Se deberá entregar la *url* al commit en el repositorio privado *GitHub* de la asignatura *IMW*, apuntando a la carpeta que contiene los ficheros de código Python. La *url* debe tener la siguiente estructura:

```
https://github.com/<usuario>/imw/blob/<id del commit>/<ut>/<actividad>/
```

> ⚠️ Al subir la *url*, es importante crear un enlace. Es decir, poner un `href` a la *url* anterior, y no pegar el texto tal cual.
