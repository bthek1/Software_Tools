# Proxmox Storage

Proxmox VE supports multiple storage types, each designed for specific use cases such as **VM disks, backups, ISO images, and templates**. Here’s a detailed comparison of all the storage types supported in Proxmox:

Author

Benedict Thekkel

## **1. Overview of Storage Types**

| Storage Type | Description | Common Use Case | Pros | Cons |
|----|----|----|----|----|
| **Directory (`dir`)** | Local filesystem directory | ISOs, backups, templates | Easy setup, local access | No redundancy, limited scalability |
| **LVM (`lvm`)** | Logical Volume Manager | VM disks | High performance, snapshots | No thin provisioning |
| **LVM-Thin (`lvmthin`)** | Thin-provisioned LVM | VM disks, snapshots | Efficient space usage, snapshots | Complex management |
| **ZFS (`zfspool`)** | Advanced filesystem and volume manager | VM disks, snapshots | Snapshots, compression, RAID | High RAM usage |
| **Ceph (`rbd`)** | Distributed block storage | High availability | Scalability, redundancy | Complex setup, network dependency |
| **NFS (`nfs`)** | Network file system | Shared storage, backups | Centralized storage, scalable | Network dependency |
| **CIFS/SMB (`cifs`)** | Windows share | Backups, ISOs | Easy integration with NAS | Slower network performance |
| **iSCSI (`iscsi`)** | Network block storage | VM disks | High performance SAN | Complex setup, network dependency |
| **GlusterFS (`glusterfs`)** | Distributed file system | High availability | Scalability, redundancy | Performance overhead |

------------------------------------------------------------------------

## **2. Directory Storage (`dir`)**

### **Description:**

- Uses a **local directory** on the Proxmox host.
- Can store **ISOs, backups, LXC templates**, and **VM images**.

### **Common Use Case:**

- Local storage for **ISOs, backups, and VM templates**.

### **Pros:**

- **Easy to set up** and manage.
- **Fast** since it’s local storage.
- Supports **multiple content types** (e.g., ISO, backup, images).

### **Cons:**

- **No redundancy**. If the local disk fails, data is lost.
- **Not scalable**. Limited by local disk capacity.

### **Example Configuration:**

``` ini
dir: local
    path /var/lib/vz
    content iso,backup,vztmpl
    maxfiles 5
```

------------------------------------------------------------------------

## **3. LVM (`lvm`)**

### **Description:**

- Uses **Logical Volume Manager** for **block storage**.
- No thin provisioning; each LV is fully allocated.

### **Common Use Case:**

- **VM disks** that require high performance and stability.

### **Pros:**

- **High performance** for VM disks.
- Supports **snapshots**.
- **Easy to expand** by adding physical volumes.

### **Cons:**

- **No thin provisioning**. Allocates the entire disk space upfront.
- **No native redundancy**.

### **Example Configuration:**

``` ini
lvm: vmdata
    vgname vg_data
    content images
```

------------------------------------------------------------------------

## **4. LVM-Thin (`lvmthin`)**

### **Description:**

- **Thin-provisioned LVM** that allocates space **on demand**.
- Efficient **snapshots** using Copy-on-Write (CoW).

### **Common Use Case:**

- **VM disks** with **snapshots** and **dynamic space usage**.

### **Pros:**

- **Efficient space usage**. Only allocates space as needed.
- **Fast snapshots** with minimal overhead.

### **Cons:**

- **Complex management**. Requires monitoring to avoid over-provisioning.
- No built-in redundancy.

### **Example Configuration:**

``` ini
lvmthin: thin_data
    vgname vg_data
    thinpool thinpool
    content images
```

------------------------------------------------------------------------

## **5. ZFS (`zfspool`)**

### **Description:**

- **Advanced filesystem** and **volume manager**.
- Features **snapshots, compression, checksums, and RAID-like redundancy**.

### **Common Use Case:**

- **High availability**, **data integrity**, and **VM storage** with **snapshots**.

### **Pros:**

- **Built-in redundancy** with RAID-Z or mirrors.
- **Snapshots and rollback** without performance impact.
- **Compression** reduces storage space.

### **Cons:**

- **High RAM usage**. Minimum 8 GB RAM recommended.
- **Complex management** compared to LVM.

### **Example Configuration:**

``` ini
zfspool: zdata
    pool zdata
    content images,rootdir
    sparse 1
```

------------------------------------------------------------------------

## **6. Ceph (`rbd`)**

### **Description:**

- **Distributed block storage** system.
- Offers **high availability, scalability, and redundancy**.

### **Common Use Case:**

- **Highly available VM disks** across multiple Proxmox nodes.

### **Pros:**

- **Scalable and redundant** across nodes.
- **No single point of failure**.
- **Dynamic growth** by adding more nodes.

### **Cons:**

- **Complex setup and maintenance**.
- Requires **high network bandwidth and low latency**.

### **Example Configuration:**

``` ini
rbd: ceph_pool
    pool rbd
    content images,rootdir
    krbd 1
```

------------------------------------------------------------------------

## **7. NFS (`nfs`)**

### **Description:**

- **Network File System** for shared storage.
- Accessible by **multiple Proxmox nodes**.

### **Common Use Case:**

- Centralized storage for **ISOs, backups, and templates**.

### **Pros:**

- **Easy to set up** and manage.
- **Centralized storage** for multiple nodes.
- **Scalable** by expanding the NFS server.

### **Cons:**

- **Network dependency**. Performance affected by network speed.
- **No built-in redundancy**.

### **Example Configuration:**

``` ini
nfs: nfs_data
    server 192.168.2.100
    export /mnt/nfs
    path /mnt/pve/nfs_data
    content images,iso,backup
```

------------------------------------------------------------------------

## **8. CIFS/SMB (`cifs`)**

### **Description:**

- **Windows network share** for storage.
- Used for **backups, ISOs, and templates**.

### **Common Use Case:**

- Backing up to a **NAS or Windows file server**.

### **Pros:**

- **Easy integration** with Windows and NAS systems.
- Good for **backups and non-critical storage**.

### **Cons:**

- **Slower network performance** compared to NFS.
- **Network dependency**.

### **Example Configuration:**

``` ini
cifs: smb_data
    path /mnt/pve/smb_data
    server 192.168.2.100
    share backups
    content images,iso,backup
```

------------------------------------------------------------------------

## **9. iSCSI (`iscsi`)**

### **Description:**

- **Network block storage** protocol.
- Uses **external SAN** for VM disks.

### **Common Use Case:**

- **High-performance VM disks** with external SAN.

### **Pros:**

- **High performance** and **low latency**.
- **Centralized storage** with SAN features.

### **Cons:**

- **Complex configuration and management**.
- **Network dependency**.

### **Example Configuration:**

``` ini
iscsi: iscsi_data
    portal 192.168.2.100
    target iqn.2024-02.com.example:target1
    content images
```

------------------------------------------------------------------------

## **10. GlusterFS (`glusterfs`)**

### **Description:**

- **Distributed file system** for scalability.
- Ideal for **high availability and redundancy**.

### **Common Use Case:**

- **Shared VM storage** across multiple nodes.

### **Pros:**

- **Scalable and redundant** across nodes.
- **Easy to expand** by adding nodes.

### **Cons:**

- **Performance overhead**.
- **Complex management and troubleshooting**.

### **Example Configuration:**

``` ini
glusterfs: gluster_data
    server 192.168.2.200
    volume gv0
    path /mnt/pve/gluster_data
    content images,rootdir
```

------------------------------------------------------------------------

## **Conclusion**

Each storage type in Proxmox has its own strengths and use cases. Choose based on: - **Performance needs** (LVM, iSCSI) - **Redundancy and scalability** (Ceph, ZFS, GlusterFS) - **Centralized storage** (NFS, CIFS)

If you need help with **choosing the right storage type, configuration, or troubleshooting**, let me know! 🚀

------------------------------------------------------------------------

Back to top
