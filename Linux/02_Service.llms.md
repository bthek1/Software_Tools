# Services in Linux

`systemd` is a system and service manager for Linux that initializes the system, manages services, and controls system resources. It uses *unit files* to define services, targets, timers, and other components — replacing older systems like SysVinit.

Author

Benedict Thekkel

## **Key Concepts**

### **1. Unit Files**

Configuration files that describe system components.

Common unit types:

| Type       | Purpose                                          |
|------------|--------------------------------------------------|
| `.service` | Runs and manages services or daemons             |
| `.target`  | Groups units into boot/run-level states          |
| `.timer`   | Schedules recurring or delayed tasks             |
| `.mount`   | Defines filesystem mount points                  |
| `.socket`  | Manages sockets for on-demand service activation |

------------------------------------------------------------------------

### **2. Unit File Locations**

| Scope         | Path                       | Description               |
|---------------|----------------------------|---------------------------|
| System-wide   | `/etc/systemd/system/`     | Administrator overrides   |
| Default       | `/usr/lib/systemd/system/` | Package-provided defaults |
| User-specific | `~/.config/systemd/user/`  | Per-user services         |

------------------------------------------------------------------------

### **3. Service States**

| State      | Meaning              |
|------------|----------------------|
| `active`   | Running normally     |
| `inactive` | Stopped              |
| `failed`   | Encountered an error |

------------------------------------------------------------------------

## **Creating a Service**

### **Example: `my-service.service`**

``` ini
[Unit]
Description=My Custom Service
After=network.target

[Service]
Type=simple
ExecStart=/path/to/app --arg1 --arg2
WorkingDirectory=/path/to/working/directory
User=myuser
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

------------------------------------------------------------------------

### **Key Sections**

**`[Unit]`**

- Defines metadata and dependencies.

- Example:

  ``` ini
  After=network.target
  Requires=network-online.target
  ```

**`[Service]`**

- Describes how the service behaves.

- Common directives:

  | Directive    | Description                                               |
  |--------------|-----------------------------------------------------------|
  | `Type`       | How service starts (`simple`, `forking`, `oneshot`, etc.) |
  | `ExecStart`  | Command to start the service                              |
  | `User`       | User under which the service runs                         |
  | `Restart`    | Restart policy (`always`, `on-failure`, etc.)             |
  | `RestartSec` | Delay before restart                                      |

**`[Install]`**

- Defines how the service integrates into the boot process. Example:

  ``` ini
  WantedBy=multi-user.target
  ```

------------------------------------------------------------------------

## **Enable and Start a Service**

``` bash
sudo cp my-service.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable my-service.service
sudo systemctl start my-service.service
sudo systemctl status my-service.service
```

------------------------------------------------------------------------

## **Managing Services**

| Action         | Command                             |
|----------------|-------------------------------------|
| Start          | `sudo systemctl start my-service`   |
| Stop           | `sudo systemctl stop my-service`    |
| Restart        | `sudo systemctl restart my-service` |
| Enable at boot | `sudo systemctl enable my-service`  |
| Disable        | `sudo systemctl disable my-service` |
| View status    | `sudo systemctl status my-service`  |
| View logs      | `journalctl -u my-service`          |
| Tail logs      | `journalctl -u my-service -f`       |

------------------------------------------------------------------------

## **Advanced Topics**

### **1. Environment Variables**

``` ini
Environment=MY_VAR=value
EnvironmentFile=/etc/my-service.env
```

------------------------------------------------------------------------

### **2. Dependency Management**

``` ini
[Unit]
Requires=network.target
After=network.target
```

- `Requires` → Hard dependency
- `Wants` → Soft dependency
- `Before` / `After` → Order control

------------------------------------------------------------------------

### **3. Timer Units**

``` ini
[Unit]
Description=Run My Service Daily

[Timer]
OnCalendar=daily
Persistent=true

[Install]
WantedBy=timers.target
```

------------------------------------------------------------------------

### **4. User Services**

For non-root users:

``` bash
systemctl --user enable my-service
systemctl --user start my-service
```

------------------------------------------------------------------------

### **5. Debugging**

``` bash
sudo systemd-analyze verify /etc/systemd/system/my-service.service
sudo journalctl -xe
sudo -u myuser /path/to/app --arg1 --arg2
```

------------------------------------------------------------------------

## ⚙️ **Resource Management in systemd**

`systemd` provides fine-grained resource control using **cgroups** (control groups). You can set CPU, memory, I/O, and process limits directly in the `[Service]` section.

### **1. CPU Limits**

| Directive | Description |
|----|----|
| `CPUQuota=` | Percentage of CPU allowed (e.g., `CPUQuota=50%` limits to half a core). |
| `CPUShares=` | Relative CPU weight compared to other services (default = 1024). |
| `AllowedCPUs=` | Restrict service to specific cores (e.g., `AllowedCPUs=0,2`). |

Example:

``` ini
[Service]
CPUQuota=75%
CPUShares=512
AllowedCPUs=0-1
```

------------------------------------------------------------------------

### **2. Memory Limits**

| Directive | Description |
|----|----|
| `MemoryMax=` | Hard memory cap. (`MemoryMax=500M`) |
| `MemorySwapMax=` | Max combined RAM + swap usage |
| `MemoryHigh=` | Soft memory threshold — triggers reclaim pressure before the hard limit |

Example:

``` ini
[Service]
MemoryMax=1G
MemoryHigh=800M
MemorySwapMax=0
```

------------------------------------------------------------------------

### **3. I/O (Disk) Limits**

| Directive              | Description                           |
|------------------------|---------------------------------------|
| `IOReadBandwidthMax=`  | Limit read speed per device           |
| `IOWriteBandwidthMax=` | Limit write speed per device          |
| `IOWeight=`            | Relative I/O priority (default = 100) |

Example:

``` ini
[Service]
IOReadBandwidthMax=/dev/sda 10M
IOWriteBandwidthMax=/dev/sda 5M
IOWeight=200
```

------------------------------------------------------------------------

### **4. Process Limits**

| Directive      | Description                         |
|----------------|-------------------------------------|
| `TasksMax=`    | Maximum number of processes/threads |
| `LimitNOFILE=` | Max open file descriptors           |
| `LimitNPROC=`  | Max number of processes             |

Example:

``` ini
[Service]
TasksMax=100
LimitNOFILE=4096
LimitNPROC=200
```

------------------------------------------------------------------------

### **5. Network Limits (Systemd ≥ 250)**

| Directive | Description |
|----|----|
| `IPAddressDeny=` | Block network access |
| `IPAddressAllow=` | Allow specific IPs |
| `RestrictAddressFamilies=` | Restrict socket address families (e.g., only `AF_INET`) |

Example:

``` ini
[Service]
IPAddressDeny=any
IPAddressAllow=10.0.0.0/8
RestrictAddressFamilies=AF_INET AF_INET6
```

------------------------------------------------------------------------

### **6. Security & Isolation**

| Directive | Description |
|----|----|
| `ProtectSystem=` | Makes parts of the filesystem read-only (`full`, `strict`) |
| `ProtectHome=` | Hides or makes `/home` inaccessible |
| `PrivateTmp=` | Gives each service a private `/tmp` |
| `NoNewPrivileges=` | Prevent privilege escalation |
| `CapabilityBoundingSet=` | Restrict Linux capabilities |

Example:

``` ini
[Service]
ProtectSystem=full
ProtectHome=yes
PrivateTmp=yes
NoNewPrivileges=yes
CapabilityBoundingSet=CAP_NET_BIND_SERVICE
```

------------------------------------------------------------------------

### **7. Inspecting Resource Usage**

You can view live resource usage:

``` bash
systemctl status my-service
systemd-cgls               # Show hierarchy
systemd-cgtop              # Live CPU/memory usage
```

------------------------------------------------------------------------

## ✅ **Best Practices**

1.  **Use absolute paths** in all directives.
2.  **Run as non-root** whenever possible.
3.  **Enable restart policies** for reliability.
4.  **Use `systemctl edit`** for overrides instead of editing defaults.
5.  **Apply cgroup limits** (`CPUQuota`, `MemoryMax`, etc.) to ensure system stability.
6.  **Use timers** instead of `cron` for unified management and logging.

------------------------------------------------------------------------

Back to top
