"""Role testing files using testinfra."""


def test_svc(host):

    if host.system_info.distribution == 'debian' or host.system_info.distribution == 'ubuntu':
      service = host.service("nfs-kernel-server")

    if host.system_info.distribution == 'rocky' or host.system_info.distribution == 'fedora':
      service = host.service("nfs-server")      

    assert service.is_running
    assert service.is_enabled
