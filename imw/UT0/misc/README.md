# Misc

## Paquetes adicionales

```console
apt-get install vim
apt-get install ntp
apt-get install unzip
```

## Configuraciones varias

### `ntp.conf`

```console
root@hillvalley:~# crontab -e
```

> Contenido
```cron
5 * * * * /etc/init.d/ntp restart
```

### `.bashrc`

```console
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

```console
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
```

## Problemas comunes

* Si tienes problemas con la contraseña de `root` en tu máquina virtual, y no te funciona el que se supone que debe tener. Si crees que tu sistema sufre una *amnesia temporal*, debes hacer lo siguiente. Como usuario normal, ejecuta:

```console
$> sudo passwd root
```

Ahora escribe tu contraseña de usuario normal, y a continuación tendrás que repetir la NUEVA contraseña de `root`.
