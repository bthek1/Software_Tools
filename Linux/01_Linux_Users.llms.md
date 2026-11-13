# Linux Users, Groups and Permissions

Linux User, Groups and Permissions

Author

Benedict Thekkel

## Types of Users in Linux

### Root User (Superuser):

- The root user has unrestricted access to the entire system.
- Root can execute any command, access any file, and modify any configuration.
- Typically used for system administration tasks.
- Home directory is usually /root.
- Commands are run as root using sudo or by switching to the root user with su.

### Regular Users:

- Regular users have limited access to the system.
- Each user has a home directory under /home/username.
- Regular users can only access files and resources they own or have permission to access.
- Used for day-to-day tasks and activities.

### System Users:

- System users are non-login accounts used by system services and daemons (e.g., www-data for web servers, mysql for databases).
- Typically, these users don’t have a home directory or an interactive shell.
- Created to run specific services securely, without giving them unnecessary privileges.

## User Management

### Creating a User:

- Users are created using the useradd or adduser command.
- useradd is the low-level command, while adduser is a more user-friendly script that provides additional features.
- Example:

``` sh
sudo useradd -m username
sudo passwd username
```

- `-m` creates a home directory for the user.

### Deleting a User:

- Users can be deleted using the userdel command.
- userdel -r will delete the user’s home directory as well.
- Example:

``` sh
sudo userdel -r username
```

### Modifying a User:

- The usermod command allows you to modify user details, such as changing the username, home directory, or adding the user to a group.
- Example:

``` sh
sudo usermod -d /new/home username
sudo usermod -aG groupname username
```

### Changing User Passwords:

- The passwd command is used to change a user’s password.
- Users can change their own password using passwd, or an administrator can change another user’s password using sudo passwd username.
- Example:

``` sh
sudo passwd username
```

## User and Group Files

- /etc/passwd:
  - This file contains basic information about all user accounts, including the username, UID (User ID), GID (Group ID), home directory, and shell.
  - Each line represents a user, with fields separated by colons.
- /etc/shadow:
  - This file stores secure password information, including the hashed passwords and password expiration data.
  - It is only readable by the root user for security purposes.
- etc/group:
  - This file lists all groups on the system and the users belonging to each group.
  - Similar to /etc/passwd, each line represents a group, with fields separated by colons.

## User IDs and Group IDs

- UID (User ID):
  - A unique number assigned to each user.
  - The root user typically has a UID of 0.
  - Regular users usually have UIDs starting from 1000 (depending on the distribution).
- GID (Group ID):
  - A unique number assigned to each group.
  - The root group typically has a GID of 0.
  - Like UIDs, system and service accounts usually have lower GIDs, while regular user groups start from 1000.

## Groups in Linux

- Primary and Secondary Groups:
  - Each user belongs to a primary group, which is usually created with the same name as the user.
  - Users can also belong to secondary groups, which grant additional permissions.

### Managing Groups:

- Creating a Group:

``` sh
sudo groupadd groupname
```

- Adding a User to a Group

``` sh
sudo usermod -aG groupname username
```

- Deleting a Group

``` sh
sudo groupdel groupname
```

### Listing Groups

> To see the groups a user belongs to, use the `groups` command

``` sh
groups username
```

## File Permissions

### Understanding File Permissions:

- Each file and directory has permissions set for three categories: owner, group, and others
- Permissions are represented as r (read), w (write), and x (execute).
- Example:

``` sh
-rwxr-xr--
```

- In this example:
  - `rwx` is the permission for the owner (read, write, execute).
  - `r-x` is the permission for the group (read, execute).
  - `r--` is the permission for others (read only).

### Changing File Permissions:

- Use the chmod command to change permissions.
- Numeric representation:
  - 4: read (r)
  - 2: write (w)
  - 1: execute (x)

  ``` sh
  chmod 755 filename
  ```

### Changing File Ownership:

- The chown command is used to change the owner or group of a file.
- Example:

``` sh
sudo chown username:groupname filename
```

## Switching Users

### su (Substitute User):

- The `su` command allows you to switch to another user account.
- Example:

``` sh
su - username
su -        # Switches to the root user
```

- The `-` option ensures that the environment is set up as if the user had logged in directly

### sudo (Superuser Do):

- The `sudo` command allows a permitted user to execute a command as the superuser or another user, as specified in the `/etc/sudoers` file.
- Example:

``` sh
sudo command
sudo -u username command
```

### Sudoers File:

- The `/etc/sudoers` file controls which users have sudo privileges.
- Use the `visudo` command to edit the sudoers file safely.

## User Environment

- Home Directory:
  - A user’s personal space for storing files and configurations.
  - Located at `/home/username` for regular users and `/root` for the root user.
- Shell:
  - The command-line interface that users interact with, typically `bash`, `sh`, or `zsh`.
  - The default shell is specified in the `/etc/passwd` file.
- Environment Variables:
  - Variables that control the behavior of the user’s environment (e.g., `PATH`, `HOME`, `USER`).
  - Can be configured in files like `.bashrc`, `.bash_profile`, `.profile`, etc.

## User Session Management

- `who` Command: Displays who is currently logged into the system.
- `w` Command: Shows who is logged in and what they are doing.
- `last` Command: Displays the last login history of users.
- `kill` Command: Use the kill command to terminate a user’s session or specific processes.

## Security Considerations

- Password Policies:
  - Enforce strong passwords using tools like `pam_pwquality`.
  - Set password expiration and aging policies to ensure regular password changes.
- Restricting Root Access:
  - Disable root login over SSH by setting `PermitRootLogin no` in `/etc/ssh/sshd_config`.
  - Use `sudo` instead of direct root access for better security.
- Monitoring and Auditing:
  - Monitor user activities by examining logs in `/var/log/` (e.g., `auth.log`, `secure`).
  - Use tools like `auditd` to track system events and user actions.

``` python
!
```

Back to top
