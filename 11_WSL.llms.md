# WSL

Details on setting up WSL

Author

Benedict Thekkel

## Change Settings in `Turn Windows features on or off`

Turn on: - Virtual Machine Platform - Windows Hypervisor Platform - Windows Subsystem for Linux

## Download WSL - Windows Subsystem for Linux

- goto powershell

``` sh
wsl --install
```

If there is error with wsl

    Invoke-WebRequest -UseBasicParsing "https://raw.githubusercontent.com/microsoft/WSL/master/triage/install-latest-wsl.ps1" -OutFile install-latest-wsl.ps1
    Set-ExecutionPolicy Bypass -Scope Process -Force
    .\install-latest-wsl.ps1

- o see a list of available Linux distributions available for download through the online store

``` sh
wsl -l -o
```

- to download a Linux distribution

``` sh
wsl --install -d <Distribution Name>
```

- to remove a distribution

``` sh
wsl --unregister <Distribution Name>
```

## WSL Config Files

### .wslconfig

> .wslconfig to configure global settings across all installed distributions running on WSL 2.

``` powershell
 # Settings apply across all Linux distros running on WSL 2
[wsl2]

# Limits VM memory to use no more than 4 GB, this can be set as whole numbers using GB or MB
memory=30GB 
swap=32GB

# Sets the VM to use two virtual processors
processors=12


networkingMode = mirrored
# dnsProxy = false
firewall = false


[experimental]
autoMemoryReclaim = dropcache
```

### wsl.conf

> wsl.conf to configure local settings per-distribution for each Linux distribution running on WSL 1 or WSL 2.

> Location: /etc/wsl.conf

> The wsl.conf file supports four sections: `automount`, `network`, `interop`, and `user`.

``` python
!cat /etc/wsl.conf
```

    [boot]
    systemd=true

    [network]
    # hostname = DemoHost
    generateHosts = true
    generateResolvConf = true

    # [user]
    # default = DemoUser

### Settings for port forwarding into virtual network

> rule: allow all traffic from port 8888 to pass through

    netsh interface portproxy add v4tov4 listenport=8888 listenaddress=0.0.0.0 connectport=8888 connectaddress=172.22.253.143

> delete rule:

    netsh interface portproxy delete v4tov4 listenport=8888 listenaddress=0.0.0.0

> view rules:

    netsh interface portproxy show all

    sudo apt install firefox

## WSL to Windows port forwarding

> In powershell as administrator

``` sh
netsh interface portproxy add v4tov4 listenport=80 listenaddress=0.0.0.0 connectport=80 connectaddress=$($(wsl hostname -I).Trim());
```

``` sh
New-NetFirewallRule -DisplayName "WSL2 Port Bridge" -Direction Inbound -Action Allow -Protocol TCP -LocalPort 80
```

Back to top
