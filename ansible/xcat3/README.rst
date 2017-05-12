

xcat3 playbook
==============

xcat3 playbook is ansible playbooks to setup xcat3 services on target hosts.

Use Cases
=========

Supported operating systems:

* Ubuntu 16.04

Run xcat3 playbook
==================

Download playbook
::

  git clone https://github.com/chenglch/xcat-play.git

Modify the inventory variable in ``xcat-play/ansible/xcat3/inventory/host`` and
``xcat-play/ansible/xcat3/inventory/group_vars`` to match your environment.

Run the playbook

::

  cd xcat-play/ansible/xcat3
  ansible-playbook -i inventory/host install-xcat3.yml


Reference
=========

- `xcat3 <https://github.com/chenglch/xcat3/>`__ a prototype
  written in python to manage the Bare Metal servers.
- `xcat3-client <https://github.com/chenglch/python-xcat3client/>`__  python
  command line client for xcat3 prototype.
