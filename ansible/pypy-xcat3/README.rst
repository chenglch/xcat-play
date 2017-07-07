

pypy-xcat3 playbook
==============

pypy-xcat3 playbook is ansible playbooks to setup xcat3 and run xcat3 with
pypy. It also leverage golang-xcat3client to make the client request much
faster.

Use Cases
=========

Supported operating systems:

* Ubuntu 16.04, 14.04
* Redhat/CentOS >= 7.0

Supported arch:

* ppc64le (experimental, seems not stable when operate large number of nodes)
* x86_64 (pypy takes only half of time than CPython)

Run xcat3 playbook
==================

Download playbook
::

  git clone https://github.com/chenglch/xcat-play.git

Modify the inventory variable in ``xcat-play/ansible/pypy-xcat3/inventory/host`` and
``xcat-play/ansible/pypy-xcat3/inventory/group_vars/all`` to match your environment.

Run the playbook

::

  cd xcat-play/ansible/pypy-xcat3
  ansible-playbook -i inventory/host install-xcat3.yml

Use xcat3 ::

  source /etc/profile.d/xcat3.sh
  xcat3 network-create c920 subnet=11.0.0.0 netmask=255.0.0.0 gateway=11.0.0.101 nameservers=11.0.0.101
  xcat3 service list

Troubleshot
===========

  ps -ef | grep xcat3

::

    root      1882 32367  0 06:25 ?        00:00:00 dhcpd -f -q -4 -pf /var/run/xcat3/dhcpd.pid -cf /etc/xcat3/dhcpd.conf -d -lf /var/lib/xcat3/dhcpd.leases
    root     17125  1582  0 06:51 pts/0    00:00:00 grep --color=auto xcat3
    root     28441     1  1 06:09 ?        00:00:47 pypy /usr/lib64/pypy-5.0.1/bin/xcat3-api --config-file /etc/xcat3/xcat3.conf
    root     28634 28441  0 06:09 ?        00:00:01 pypy /usr/lib64/pypy-5.0.1/bin/xcat3-api --config-file /etc/xcat3/xcat3.conf
    root     28635 28441  0 06:09 ?        00:00:01 pypy /usr/lib64/pypy-5.0.1/bin/xcat3-api --config-file /etc/xcat3/xcat3.conf
    root     30859     1  1 06:09 ?        00:00:46 pypy /usr/lib64/pypy-5.0.1/bin/xcat3-conductor --config-file /etc/xcat3/xcat3.conf
    root     30939 30859  0 06:09 ?        00:00:03 pypy /usr/lib64/pypy-5.0.1/bin/xcat3-conductor --config-file /etc/xcat3/xcat3.conf
    root     30940 30859  0 06:09 ?        00:00:18 pypy /usr/lib64/pypy-5.0.1/bin/xcat3-conductor --config-file /etc/xcat3/xcat3.conf
    root     32367     1  0 06:10 ?        00:00:05 pypy /usr/lib64/pypy-5.0.1/bin/xcat3-network --config-file /etc/xcat3/xcat3.conf

If some of the service is not started, please check the log files in /var/log/xcat3


Reference
=========

- `xcat3 <https://github.com/chenglch/xcat3/>`__ a prototype
  written in python to manage the Bare Metal servers.
- `golang-xcat3client <https://github.com/chenglch/golang-xcat3client/>`__
  xcat3 command line client written in golang.