# Ansible Role: NFS

[![CI](https://github.com/j1ngk3/ansible-role-nfs/workflows/CI/badge.svg?event=push)](https://github.com/j1ngk3/ansible-role-nfs/actions?query=workflow%3ACI)

Install NFS server/client.

## Requirements

None.

## Role Variables

The variables that can be passed to this role and a brief description about them are as follows.

```yaml
# NFS install mode: server or client
nfs_mode: server

# Line to add to the /etc/exports file
nfs_exports:
  - path: "/home"
    export: "vnode*.localdomain(fsid=0,rw,async,no_root_squash,no_subtree_check,insecure)"

# Line to add to the /etc/fstab file
nfs_client_imports:
  - local: "/home"
    remote: "/home"
    server_host: "{{hostvars['server']['ansible_default_ipv4']}}"
```

NFS client imports can also define the following variables:
  * `state`: see: http://docs.ansible.com/ansible/mount_module.html for more information.
  * `opts`: see https://wiki.debian.org/fr/fstab for more information.
  * `dump`: see https://wiki.debian.org/fr/fstab for more information.
  * `passno`: see https://wiki.debian.org/fr/fstab for more information.

## Dependencies

None.

## Example Playbook

This an example of how to install and configure a NFS server and client:
```yaml
    - hosts: server
      roles:
      - { role: 'j1ngk3.nfs', nfs_mode: 'server', nfs_exports: [{path: "/home", export: "vnode*.localdomain(fsid=0,rw,async,no_root_squash,no_subtree_check,insecure)"}] }

    - hosts: client
      roles:
      - { role: 'j1ngk3.nfs', nfs_mode: 'client', nfs_client_imports: [{ local: "/home", remote: "/home", server_host: "{{hostvars['server']['ansible_default_ipv4']}}" }] }
```

## License


Apache Licence v2 [1]

[1] http://www.apache.org/licenses/LICENSE-2.0
