# Linux Computer

New Ubuntu Computer

Author

Benedict Thekkel

## Install Git

``` sh
sudo apt install git
```

## Install Code

``` sh
sudo snap install code --classic
```

## Install stow

``` sh
sudp apt install stow
```

## Install tmux

``` sh
sudo apt install tmux
```

## [Set up ssh with Github](https://bthek1.github.io/Web_development/github.html)

## Install curl

``` sh
sudo apt install curl
```

## Battery limit Change

### Installation

``` sh
sudo apt-get update
sudo apt-get install tlp tlp-rdw
```

### Enable

``` sh
sudo systemctl enable tlp
```

### Check

``` sh

sudo systemctl status tlp

sudo tlp-stat -b
```

### Configure

> edit `/etc/tlp.conf`

``` sh
START_CHARGE_THRESH_BAT0=75
STOP_CHARGE_THRESH_BAT0=80
```

## Temporary Full Charge

``` sh
sudo tlp fullcharge
```

Back to top
