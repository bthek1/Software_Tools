# Service Journalctl

Here’s a comprehensive and structured guide to **`journalctl`**, the powerful logging tool for `systemd`-based Linux systems.

Author

Benedict Thekkel

# 🧠 What is `journalctl`?

`journalctl` is a command-line utility to **query and view logs** collected by the **systemd journal** — including logs from:

- System services (`systemd` units)
- Kernel messages
- Boot logs
- Custom apps using `stdout`/`stderr`

It replaces older tools like `dmesg`, `/var/log/syslog`, and `/var/log/messages`.

------------------------------------------------------------------------

## 📦 Prerequisites

- Works only on `systemd` systems (Ubuntu ≥ 16.04, Debian ≥ 8, CentOS ≥ 7, Arch, etc.)
- Run as `root` to access full logs (especially system logs)

------------------------------------------------------------------------

# 🧰 Core Usage

### View All Logs

``` bash
journalctl
```

### Follow Logs (like `tail -f`)

``` bash
journalctl -f
```

### Show Boot Logs

``` bash
journalctl -b                    # Current boot
journalctl -b -1                 # Previous boot
journalctl --list-boots          # List all boots with index
```

### View Service Logs

``` bash
journalctl -u nginx              # Specific service
journalctl -u nginx -f          # Follow service logs
journalctl -u nginx --since today
```

### Logs by Executable or Process

``` bash
journalctl _PID=1234
journalctl _COMM=python3
journalctl _EXE=/usr/sbin/nginx
```

------------------------------------------------------------------------

# ⏱️ Time Filters

``` bash
journalctl --since "1 hour ago"
journalctl --since "2024-07-01 12:00" --until "2024-07-01 14:00"
journalctl --since yesterday
journalctl --since today
```

------------------------------------------------------------------------

# 🔍 Filtering Logs

### By Priority

``` bash
journalctl -p err             # Errors and worse
journalctl -p warning
journalctl -p info
journalctl -p 0..3            # Emergency to error
```

| Priority | Code    | Description             |
|----------|---------|-------------------------|
| 0        | emerg   | System is unusable      |
| 1        | alert   | Immediate action needed |
| 2        | crit    | Critical conditions     |
| 3        | err     | Error conditions        |
| 4        | warning | Warning conditions      |
| 5        | notice  | Normal but significant  |
| 6        | info    | Informational           |
| 7        | debug   | Debug-level messages    |

------------------------------------------------------------------------

### By Boot, User, or Message

``` bash
journalctl -b -1             # Previous boot
journalctl _UID=1000         # Specific user
journalctl MESSAGE_ID=...    # Structured log ID
```

------------------------------------------------------------------------

# 🪵 Log Persistence

By default, logs may be ephemeral (`/run/log/journal`). To persist logs:

``` bash
sudo mkdir -p /var/log/journal
sudo systemd-tmpfiles --create --prefix /var/log/journal
sudo systemctl restart systemd-journald
```

------------------------------------------------------------------------

# 📤 Output Formats

### Default (verbose):

``` bash
journalctl
```

### Short/Concise:

``` bash
journalctl -o short           # default
journalctl -o short-iso       # ISO timestamps
journalctl -o json-pretty     # JSON logs
journalctl -o cat             # Just the message text
```

------------------------------------------------------------------------

# 📁 Log Location

| Location                     | Description                    |
|------------------------------|--------------------------------|
| `/run/log/journal/`          | Volatile logs (lost on reboot) |
| `/var/log/journal/`          | Persistent logs                |
| `/etc/systemd/journald.conf` | Journal config                 |

To make logs persistent, ensure `Storage=persistent` is set in:

``` bash
sudo nano /etc/systemd/journald.conf
```

------------------------------------------------------------------------

# 🧹 Maintenance

### Rotate and Vacuum Old Logs

``` bash
journalctl --disk-usage                  # Show journal size
sudo journalctl --vacuum-size=500M      # Keep only 500MB logs
sudo journalctl --vacuum-time=7d        # Keep logs from last 7 days
```

### Remove All Logs

``` bash
sudo journalctl --rotate
sudo journalctl --vacuum-time=1s
```

------------------------------------------------------------------------

# 🔐 Permissions

Regular users can only read their own logs unless added to the `systemd-journal` group:

``` bash
sudo usermod -aG systemd-journal <your-user>
```

------------------------------------------------------------------------

# 🧪 Example Use Cases

### View Celery Worker Logs

``` bash
journalctl -u rm-queue -f
```

### See Logs from 2 Days Ago

``` bash
journalctl --since "2 days ago"
```

### View Kernel Logs

``` bash
journalctl -k
```

------------------------------------------------------------------------

# 📊 Summary Cheat Sheet

| Action                   | Command                            |
|--------------------------|------------------------------------|
| View all logs            | `journalctl`                       |
| Follow logs live         | `journalctl -f`                    |
| Filter by unit           | `journalctl -u nginx`              |
| Show logs from last boot | `journalctl -b`                    |
| Show logs by time        | `journalctl --since "2024-01-01"`  |
| Filter by priority       | `journalctl -p err`                |
| Output JSON              | `journalctl -o json-pretty`        |
| Vacuum old logs          | `sudo journalctl --vacuum-time=7d` |

Back to top
