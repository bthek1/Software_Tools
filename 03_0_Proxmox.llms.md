# Proxmox

Proxmox Virtual Environment (Proxmox VE) is a powerful, open-source platform for managing virtual machines (VMs) and containers. It integrates enterprise-class features with ease of use, making it an excellent choice for virtualization. Here’s an all-in-one guide to help you understand and get started with Proxmox.

Author

Benedict Thekkel

- Proxmox
  - jupyter docker
  - windows
  - ubuntu
  - pihole
  - home assistant
  - NAS - trueNAS
  - prometheous and grafana
  - blueiris - camera
- gpu hdmi pass through for ubuntu

[Things to do before setup up proxmox](https://www.youtube.com/watch?v=GoZaMgEgrHw)

[Video Tutorials](https://www.youtube.com/watch?v=J29onrRqE_I&list=PLT98CRl2KxKHnlbYhtABg6cF50bYa8Ulo&index=12)

## **What is Proxmox?**

- **Type 1 Hypervisor**: Runs directly on hardware for better performance.
- **Based on Debian**: Uses a Linux kernel with KVM (Kernel-based Virtual Machine) and LXC (Linux Containers) for virtualization.
- **Web-Based Management**: Administer everything through an intuitive web interface.
- **Free & Open Source**: Enterprise features available for free; optional support subscription for updates.

------------------------------------------------------------------------

## **Key Features**

1.  **Virtualization Options**:
    - **KVM**: Full virtualization for running any operating system.
    - **LXC**: Lightweight containers for running Linux-based applications.
2.  **High Availability (HA)**:
    - Create clusters with multiple nodes for redundancy and failover.
3.  **Backup and Restore**:
    - Built-in backup solutions (full and incremental backups).
    - Supports external storage for backups.
4.  **Storage Options**:
    - Local storage, NFS, iSCSI, Ceph, or ZFS file systems.
5.  **Networking**:
    - Virtual networking with VLAN support and bonding.
    - Bridged networking for external connectivity.
6.  **Proxmox VE Cluster**:
    - Manage multiple nodes from a single interface.
7.  **Integrated Web Interface**:
    - Manage VMs, storage, networking, and clusters through a single dashboard.
8.  **Flexible Storage**:
    - Mix and match storage technologies (ZFS, Ceph, local disks, etc.).
9.  **Live Migration**:
    - Move running VMs between nodes without downtime.
10. **Support for Templates and Clones**:
    - Easily deploy new VMs from existing templates.

------------------------------------------------------------------------

## **System Requirements**

- **CPU**: 64-bit processor with virtualization support (Intel VT-x or AMD-V).
- **RAM**: Minimum 2 GB (8 GB or more recommended for multiple VMs).
- **Storage**: SSDs recommended for faster I/O.
- **Network**: At least 1 Gbps for high-performance clusters.

------------------------------------------------------------------------

## **Getting Started**

- agree to end user license

- Target Harddisk: choose /dev/nvme0n1, ext4

- Location and Time Zone selection: Country: Australia, Time Zone: Australia/Brisbane, Keyboard Layout: U.S. English

- Password:

  - bthek1 login: root
  - password: YME (classic)

- Management Network Configuration

  - Managemen Interface: eno1
    - eno1, eno2, etc. (on-board devices)
    - enp10s0, enp3s0, etc. (PCI devices)
    - wlp3s0 (wireless card on PCI), etc.
  - Hostname (FQDN): bthek1.thekkel.com
  - IP: 192.168.2.70/24
  - Gateway: 192.168.2.1
  - DNS: 127.0.0.1

## Storage and Paritioners in Proxmox

``` bash
lsblk -o NAME,FSTYPE,SIZE,MOUNTPOINT,TYPE

NAME               FSTYPE        SIZE MOUNTPOINT TYPE
sda                            111.8G            disk
nvme0n1                        931.5G            disk
├─nvme0n1p1                     1007K            part
├─nvme0n1p2        vfat            1G /boot/efi  part
└─nvme0n1p3        LVM2_member 930.5G            part
  ├─pve-swap       swap            8G [SWAP]     lvm
  ├─pve-root       ext4           96G /          lvm
  ├─pve-data_tmeta               8.1G            lvm
  │ └─pve-data                 794.3G            lvm
  └─pve-data_tdata             794.3G            lvm
    └─pve-data                 794.3G            lvm
```

- /boot/efi is your EFI partition for system boot.
- pve is the Proxmox volume group on the NVMe drive.
- pve-root (ext4) is your main OS partition mounted at /.
- pve-data (thin pool) is for VM/container storage.
- pve-swap is your swap space.
- /dev/sda is unpartitioned/unused in this listing, so it’s effectively free if you want to set it up for additional storage.

## Adding User in Proxmox

#### 1. Create the User Account

1.  **SSH into your Proxmox host** as `root` or log in via console.

2.  **Create a new user** (replace `ben` with the desired username):

    ``` bash
    adduser ben
    ```

    - You’ll be prompted to set a password and (optionally) fill in some personal info.

3.  *(Optional)* **Give the user sudo privileges** (if you want them to be able to run administrative commands):

    - Install `sudo` if it’s not already installed:

      ``` bash
      apt update
      apt install sudo
      ```

    - Add the user to the `sudo` group:

      ``` bash
      usermod -aG sudo ben
      ```

    - Now, user `ben` can run `sudo <command>` when necessary.

------------------------------------------------------------------------

#### 2. Configure SSH Key-Based Authentication (Recommended)

Using SSH keys is more secure than a password-based login. Here are the steps:

1.  **Generate an SSH key pair** (on your local machine **not** on Proxmox) if you don’t already have one:

    ``` bash
    ssh-keygen -t ed25519
    ```

    or

    ``` bash
    ssh-keygen -t rsa -b 4096
    ```

    - Press **Enter** to accept the default file location (e.g., `~/.ssh/id_ed25519` or `~/.ssh/id_rsa`).\
    - Optionally protect the key with a passphrase.

2.  **Copy your public key** to the Proxmox server for user `ben`:

    ``` bash
    ssh-copy-id ben@<Proxmox_IP_Address>
    ```

    - If prompted for a password, provide the one you created for `ben`.
    - This will create the `~ben/.ssh/authorized_keys` file on the server and put your public key there.

    **If `ssh-copy-id` is not available**, do it manually:

    - **On your local machine**, view your public key:

      ``` bash
      cat ~/.ssh/id_ed25519.pub
      ```

    - **On Proxmox** (logged in as root, or via su - ben):

      ``` bash
      su - ben
      mkdir -p ~/.ssh
      chmod 700 ~/.ssh
      nano ~/.ssh/authorized_keys
      ```

      - Paste the public key line into the file.

      - Save and exit.

      - Set proper permissions:

        ``` bash
        chmod 600 ~/.ssh/authorized_keys
        ```

3.  **(Optional) Disable password authentication** for extra security:

    - Edit `/etc/ssh/sshd_config`:

      ``` bash
      nano /etc/ssh/sshd_config
      ```

    - Find (or add) and set:

          PasswordAuthentication no
          ChallengeResponseAuthentication no
          UsePAM yes

    - Make sure key-based auth is on:

          PubkeyAuthentication yes

    - Restart SSH:

      ``` bash
      systemctl restart ssh
      ```

    - **Important**: Only do this **after** confirming key-based login works, or you might lock yourself out if something is misconfigured.

------------------------------------------------------------------------

#### 3. Test the New User’s SSH Login

1.  **From your local machine**, attempt to SSH in:

    ``` bash
    ssh ben@<Proxmox_IP_Address>
    ```

2.  If you used key-based auth, you should not be asked for a password (or only for the passphrase of your SSH key if you set one).\

3.  If you didn’t disable password authentication, you can also login with `ben`’s password.

------------------------------------------------------------------------

#### 4. Verify Sudo (Optional)

If you added `ben` to the `sudo` group, verify you can run administrative commands:

``` bash
sudo apt update
```

- Enter `ben`’s password if prompted (for the sudo prompt).

------------------------------------------------------------------------

##### Summary

1.  **Create user**: `adduser ben`\
2.  **(Optional) Add to sudo**: `usermod -aG sudo ben`\
3.  **Setup SSH**:
    - Generate SSH keys on **local** machine: `ssh-keygen`\
    - Copy the public key to the Proxmox server: `ssh-copy-id ben@<Proxmox_IP>`\
    - *(Optionally)* Disable password auth in `/etc/ssh/sshd_config` for enhanced security.\
4.  **Test**: `ssh ben@<Proxmox_IP>`

## **Using Proxmox**

#### 1. **Creating VMs**

- In the web interface, navigate to **Create VM**.
- Configure resources:
  - CPU, RAM, storage, and network interfaces.
- Install the operating system from an ISO image.

Example Configuration for a Modern VM

    Graphics Card: VirtIO GPU (or PCI Passthrough for gaming).
    SCSI Controller: VirtIO SCSI.
    Machine Type: q35.
    BIOS: OVMF (UEFI).
    QEMU Agent: Enabled.
    TPM: Add TPM 2.0 for Windows 11 or enhanced security needs.

#### 2. **Using Containers (LXC)**

- Navigate to **Create CT** for creating lightweight Linux containers.
- Select the Linux distribution template and configure resources.

#### 3. **Storage Management**

- Add storage under **Datacenter \> Storage**:
  - Local disks, shared storage (NFS/iSCSI), or distributed storage (Ceph, ZFS).

#### 4. **Backup and Restore**

- Set up backup jobs for VMs and containers.
- Backups can be stored locally or on external storage.

#### 5. **Networking**

- Configure virtual bridges under **Datacenter \> Network**.
- Use VLANs for isolated networks or create NAT for external access.

#### 6. **Clustering**

- Add nodes to a cluster for centralized management:
  - Run `pvecm add <IP_ADDRESS>` on new nodes.
- Ensure consistent storage and networking configuration across nodes.

------------------------------------------------------------------------

## Adding GPU

use display: none

    sudo apt install qemu-guest-agent

``` sh
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt update


ubuntu-drivers devices

apt search nvidia-driver

sudo apt install nvidia-driver-560
```

## Cloud init

``` bash
sudo apt install cloud-init
```

## Getting devices

### Getting USB ports

``` sh
lspci | grep -i usb
```

### Getting Audio ports

``` sh
lspci | grep -i audio
```

## **Advanced Features**

#### 1. **Proxmox VE Cluster**

- High availability across nodes.
- Shared storage (Ceph or NFS) is recommended for live migration.

#### 2. **ZFS Integration**

- Proxmox includes ZFS for advanced storage management:
  - Snapshots, compression, and RAID-like redundancy.

#### 3. **Ceph Storage**

- Use Ceph for scalable, distributed storage:
  - Install Ceph packages and create a Ceph cluster.

#### 4. **PCI Passthrough**

- Pass hardware devices directly to a VM for bare-metal performance.
- Requires a CPU with IOMMU support (Intel VT-d/AMD-Vi).

#### 5. **Cloud-Init**

- Automate VM deployment with preconfigured settings (e.g., hostname, networking).

------------------------------------------------------------------------

## **Maintenance**

- **Updates**:
  - Regularly update Proxmox (`apt update && apt upgrade`) for security and feature improvements.
- **Subscriptions**:
  - Optional enterprise subscription for support and access to stable update repositories.
  - Free repositories are available but may include testing features.
- **Logs**:
  - Monitor logs under **Syslog** for troubleshooting.

------------------------------------------------------------------------

## **Best Practices**

1.  **Use ZFS or Ceph** for resilient storage solutions.
2.  **Schedule Regular Backups** of all critical VMs.
3.  **Allocate Resources Wisely**:
    - Ensure sufficient CPU and RAM are allocated to each VM or container.
4.  **Secure Proxmox**:
    - Use strong passwords and enable two-factor authentication (2FA).
    - Restrict web interface access to trusted IPs.
5.  **Networking**:
    - Use VLANs for better isolation and scalability.
6.  **Monitor Performance**:
    - Check CPU, memory, and storage usage under the **Dashboard**.

------------------------------------------------------------------------

## **Common Issues and Troubleshooting**

1.  **VM Won’t Start**:
    - Check if sufficient resources are available.
    - Review logs in `/var/log/pve/tasks`.
2.  **Storage Issues**:
    - Ensure correct permissions for shared storage.
3.  **Cluster Problems**:
    - Use `pvecm status` to check cluster health.
    - Sync time across nodes using `ntpd` or `chrony`.

------------------------------------------------------------------------

Back to top
