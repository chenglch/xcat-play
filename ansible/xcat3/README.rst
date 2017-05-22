

xcat3 playbook
==============

xcat3 playbook is ansible playbooks to setup xcat3 services on target hosts.

Use Cases
=========

Supported operating systems:

* Ubuntu 16.04
* Ubuntu 14.04
* Redhat/Centos >= 7.0

Run xcat3 playbook
==================

Download playbook
::

  git clone https://github.com/chenglch/xcat-play.git

Modify the inventory variable in ``xcat-play/ansible/xcat3/inventory/host`` and
``xcat-play/ansible/xcat3/inventory/group_vars/all`` to match your environment.

Run the playbook

::

  cd xcat-play/ansible/xcat3
  ansible-playbook -i inventory/host install-xcat3.yml

Use xcat3 ::

  source /etc/profile.d/xcat3.sh
  xcat3 network-create c920 subnet=11.0.0.0 netmask=255.0.0.0 gateway=11.0.0.101 nameservers=11.0.0.101
  xcat3 service-list

Troubleshot
===========

  ps -ef | grep xcat3

::

    root     20002     1  0 22:23 ?        00:00:05 /usr/bin/python /usr/local/bin/xcat3-api --config-file /etc/xcat3/xcat3.conf
    root     20019 20002  0 22:23 ?        00:00:00 /usr/bin/python /usr/local/bin/xcat3-api --config-file /etc/xcat3/xcat3.conf
    root     20072 20002  0 22:23 ?        00:00:00 /usr/bin/python /usr/local/bin/xcat3-api --config-file /etc/xcat3/xcat3.conf
    root     24571     1  1 22:30 ?        00:00:01 /usr/bin/python /usr/local/bin/xcat3-conductor --config-file /etc/xcat3/xcat3.conf
    root     24588 24571  1 22:30 ?        00:00:03 /usr/bin/python /usr/local/bin/xcat3-conductor --config-file /etc/xcat3/xcat3.conf
    root     24648 24571  1 22:30 ?        00:00:03 /usr/bin/python /usr/local/bin/xcat3-conductor --config-file /etc/xcat3/xcat3.conf
    root     26068     1  2 22:30 ?        00:00:03 /usr/bin/python /usr/local/bin/xcat3-network --config-file /etc/xcat3/xcat3.conf

If some of the service is not started, please check the log files in /var/log/xcat3


Reference
=========

- `xcat3 <https://github.com/chenglch/xcat3/>`__ a prototype
  written in python to manage the Bare Metal servers.
- `xcat3-client <https://github.com/chenglch/python-xcat3client/>`__  python
  command line client for xcat3 prototype.
