# Shell Commands

Here’s a **complete, forward-thinking guide to Linux shell commands** — structured so you can understand *what they do, how they work together, and how to master them for engineering and automation*.

Author

Benedict Thekkel

## 🧭 1. What Is the Linux Shell?

A **shell** is the command interpreter between you and the operating system. Common shells include:

| Shell | Description | Command to start |
|----|----|----|
| **bash** | Default on most distros, scripting-friendly | `bash` |
| **zsh** | Extended Bash with better completion & themes (used in macOS) | `zsh` |
| **fish** | User-friendly, smart autosuggestions | `fish` |
| **sh** | POSIX shell, minimal and portable | `sh` |

**Pro tip:** Use `echo $SHELL` to see which shell you’re using.

------------------------------------------------------------------------

## ⚙️ 2. Shell Command Basics

| Command | Description | Example |
|----|----|----|
| `pwd` | Print working directory | `pwd` |
| `ls` | List files | `ls -la` |
| `cd` | Change directory | `cd /var/www` |
| `mkdir` | Create a directory | `mkdir logs` |
| `rmdir` / `rm -r` | Remove directory / recursively | `rm -rf old_dir` |
| `cp` | Copy files or directories | `cp file1.txt backup/` |
| `mv` | Move or rename files | `mv main.py src/` |
| `cat` | Show file content | `cat /etc/passwd` |
| `less` / `more` | View long files | `less large.log` |
| `touch` | Create empty file or update timestamp | `touch app.log` |

------------------------------------------------------------------------

## 🧩 3. File and Text Manipulation

| Command | Use                          | Example                        |     |
|---------|------------------------------|--------------------------------|-----|
| `grep`  | Search for text patterns     | `grep "error" app.log`         |     |
| `find`  | Search for files             | `find . -name "*.py"`          |     |
| `awk`   | Field-based text processing  | `awk '{print $1,$3}' data.txt` |     |
| `sed`   | Stream editor (find/replace) | `sed 's/foo/bar/g' file.txt`   |     |
| `cut`   | Extract columns              | `cut -d',' -f2 users.csv`      |     |
| `sort`  | Sort lines                   | `sort data.txt`                |     |
| `uniq`  | Remove duplicates            | `sort data.txt | uniq`         |     |
| `wc`    | Word/line/byte count         | `wc -l access.log`             |     |
| `diff`  | Compare files                | `diff file1.txt file2.txt`     |     |

------------------------------------------------------------------------

## 🔁 4. Redirection and Pipes

| Operator | Meaning | Example |  |  |
|----|----|----|----|----|
| `>` | Redirect output (overwrite) | `ls > files.txt` |  |  |
| `>>` | Append output | `echo "done" >> log.txt` |  |  |
| `<` | Take input from file | `sort < data.txt` |  |  |
| `|` | Pipe output into another command | `cat log.txt | grep error` |  |  |
| `2>` | Redirect errors | `python script.py 2> errors.txt` |  |  |
| `&>` | Redirect both stdout and stderr | `./run.sh &> output.log` |  |  |

------------------------------------------------------------------------

## 🧮 5. Permissions and Ownership

| Command | Purpose                     | Example                    |
|---------|-----------------------------|----------------------------|
| `chmod` | Change permissions          | `chmod 755 script.sh`      |
| `chown` | Change owner                | `chown ben:staff project/` |
| `umask` | Set default permission mask | `umask 022`                |
| `sudo`  | Run as superuser            | `sudo apt update`          |

> 💡 `chmod +x file.sh` makes a file executable.

------------------------------------------------------------------------

## 🧠 6. Process & System Management

| Command | Description | Example |  |
|----|----|----|----|
| `ps` | Show running processes | `ps aux | grep nginx` |  |
| `top` / `htop` | Interactive process viewer | `htop` |  |
| `kill` | Stop a process by PID | `kill -9 1024` |  |
| `jobs` / `fg` / `bg` | Manage background tasks | `sleep 60 &` |  |
| `df -h` | Disk usage by filesystem | `df -h` |  |
| `du -sh` | Directory size | `du -sh ~/Downloads` |  |
| `free -h` | Memory usage | `free -h` |  |
| `uptime` | System load | `uptime` |  |
| `whoami` | Current user | `whoami` |  |
| `uname -a` | Kernel info | `uname -a` |  |
| `lscpu`, `lsusb`, `lspci` | Hardware info | `lscpu` |  |

------------------------------------------------------------------------

## 🌐 7. Networking Commands

| Command | Function | Example |
|----|----|----|
| `ping` | Test connection | `ping google.com` |
| `curl` | Fetch URLs | `curl https://example.com` |
| `wget` | Download files | `wget https://example.com/file.zip` |
| `ifconfig` / `ip addr` | Network interfaces | `ip addr show eth0` |
| `netstat` / `ss` | Show open ports | `ss -tuln` |
| `scp` | Copy over SSH | `scp file.txt user@host:/path` |
| `ssh` | Remote shell | `ssh user@192.168.1.10` |
| `traceroute` | Trace network hops | `traceroute 8.8.8.8` |
| `nslookup` / `dig` | DNS lookup | `dig recoverymetrics.com` |

------------------------------------------------------------------------

## 📦 8. Package Management

| Distro        | Commands         | Example                   |
|---------------|------------------|---------------------------|
| Debian/Ubuntu | `apt`, `apt-get` | `sudo apt install vim`    |
| Fedora/RHEL   | `dnf`, `yum`     | `sudo dnf update`         |
| Arch          | `pacman`         | `sudo pacman -S neovim`   |
| Alpine        | `apk`            | `apk add curl`            |
| openSUSE      | `zypper`         | `sudo zypper install git` |

------------------------------------------------------------------------

## 🧰 9. System and User Management

| Command               | Purpose         | Example                        |
|-----------------------|-----------------|--------------------------------|
| `adduser`, `useradd`  | Create user     | `sudo adduser ben`             |
| `passwd`              | Change password | `passwd ben`                   |
| `groups`, `usermod`   | Manage groups   | `sudo usermod -aG sudo ben`    |
| `crontab -e`          | Schedule jobs   | `0 3 * * * /usr/bin/backup.sh` |
| `systemctl`           | Manage services | `sudo systemctl restart nginx` |
| `journalctl`          | View logs       | `sudo journalctl -u nginx`     |
| `shutdown` / `reboot` | Power control   | `sudo reboot`                  |

------------------------------------------------------------------------

## 🧑‍💻 10. Scripting and Automation

### Example: `backup.sh`

``` bash
#!/bin/bash
SRC="/var/www"
DEST="/backup/www_$(date +%F).tar.gz"

tar -czf "$DEST" "$SRC"
echo "Backup completed: $DEST"
```

Make it executable:

``` bash
chmod +x backup.sh
```

Schedule it with cron:

``` bash
crontab -e
0 2 * * * /home/ben/backup.sh
```

------------------------------------------------------------------------

## 🧱 11. Environment Variables

| Command      | Description          | Example             |
|--------------|----------------------|---------------------|
| `export`     | Set variable         | `export DEBUG=True` |
| `env`        | List variables       | `env`               |
| `unset`      | Remove variable      | `unset DEBUG`       |
| `.env` files | Common in dev setups | `source .env`       |

------------------------------------------------------------------------

## 🧮 12. Compression and Archiving

| Command           | Type                   | Example                          |
|-------------------|------------------------|----------------------------------|
| `tar`             | Archive multiple files | `tar -czf backup.tar.gz folder/` |
| `zip`, `unzip`    | ZIP format             | `zip -r project.zip .`           |
| `gzip` / `gunzip` | Compress single file   | `gzip bigfile.log`               |
| `xz`, `bz2`       | High-ratio compression | `xz -z data.csv`                 |

------------------------------------------------------------------------

## 🧰 13. Monitoring & Performance Tools

| Command                      | Description               |
|------------------------------|---------------------------|
| `htop` / `atop`              | Real-time process stats   |
| `iotop`                      | Disk I/O usage            |
| `iftop`                      | Network usage per process |
| `vmstat`, `mpstat`, `iostat` | CPU/memory/disk stats     |
| `sar`                        | System Activity Reporter  |

------------------------------------------------------------------------

## 🧠 14. Power Shell Tricks

| Trick                     | Description                            |     |
|---------------------------|----------------------------------------|-----|
| `!!`                      | Re-run last command                    |     |
| `!sudo`                   | Run last command with sudo             |     |
| `!ls`                     | Re-run last command starting with “ls” |     |
| `Ctrl + R`                | Search command history                 |     |
| `history`                 | List command history                   |     |
| `alias ll='ls -la'`       | Create custom shortcuts                |     |
| `df -Th | grep /dev/nvme` | Check specific disk type               |     |

------------------------------------------------------------------------

## 📈 15. Example Workflow (Data Analysis)

``` bash
# Find all CSVs modified today and summarize line counts
find . -name "*.csv" -mtime -1 | while read f; do
  echo "$(wc -l < "$f") lines in $f"
done | sort -nr
```

------------------------------------------------------------------------

## 📊 16. Visual Diagram: Shell Command Flow

    Input -> Shell -> Command -> Kernel -> Hardware
                         |
                         v
                  stdout / stderr -> Terminal / Pipe

------------------------------------------------------------------------

## 🚀 17. Next-Level Mastery

| Area | Description | Tools |
|----|----|----|
| **Scripting** | Learn conditionals, loops, functions | `bash`, `zsh`, `fish` |
| **Regex mastery** | Combine `grep`, `awk`, `sed` |  |
| **Automation** | Combine cron + systemd + scripts |  |
| **Security** | Learn `sudo`, `ufw`, and file perms |  |
| **Networking** | Practice with `ssh`, `scp`, `nmap` |  |
| **Observability** | `dmesg`, `journalctl`, `htop`, `ps`, etc. |  |

------------------------------------------------------------------------

Back to top
