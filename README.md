# ansible-role-hashicorp-vault

HashiCorp Vault - A tool for managing secrets"

This role will install Hashicorp Vault via official package on your favorite RHEL / Debian OS.

## Role Variables
Please see https://github.com/OldCrowEW/ansible-role-hashicorp-vault/blob/main/defaults/main.yml 

## Dependencies
ansible-galaxy install oldcrowew.hashicorp_repo

## Example Playbook

    - hosts: servers
      roles:
         - { role: ansible-role-hashicorp-vault }

## License

BSD

## Author Information

John Favorite
