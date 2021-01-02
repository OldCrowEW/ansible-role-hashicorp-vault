import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_vault_install(host):
    vault_install = host.package("vault")

    assert vault_install.is_installed


def test_vault_config(host):
    vault_config = host.file("/etc/vault.d/vault.hcl")

    assert vault_config.exists
    assert vault_config.is_file
    assert vault_config.user == "vault"
    assert vault_config.group == "vault"
    assert vault_config.mode == 0o644


def test_vault_systemd_config(host):
    vault_systemd_config = host.file("/usr/lib/systemd/system/vault.service")

    assert vault_systemd_config.exists
    assert vault_systemd_config.is_file
    assert vault_systemd_config.user == "root"
    assert vault_systemd_config.group == "root"
    assert vault_systemd_config.mode == 0o644


def test_vault_service(host):
    vault_service = host.service("vault")

    assert vault_service.is_running
    assert vault_service.is_enabled
