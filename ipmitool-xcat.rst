Build ipmitool-xcat
=========

ipmitool-xcat is a playbook to build packages for various platforms.

Use Cases
=========

Supported operating systems:

* Ubuntu 14.04

Pre-install steps
=================

::

  apt-get update && apt-get install -y sshpass python-dev python-pip libffi-dev libssl-dev git

Installation
============

::

  git clone https://github.com/chenglch/xcat-play.git
  cd xcat-play
  python setup.py install

Use
====

Edit ``./ansible/inventory/ipmitool-xcat.host`` to add hosts on witch the
packages are built. If you use sshpass to connect to the hosts, make sure hosts
key are added in the `known_hosts` file.

Copy rpm dependencies which are needed to complie the openssl library into
`ansible/roles/ipmitool-xcat/files` directory.(Only for sles)

Example
-------

Run the ipmitool-xcat playbook to build packages::

  cd ansible
  ansible-playbook -i inventory/ipmitool-xcat.host ipmitool-xcat.yml

`ipmitool-xcat` packages will be placed in `/tmp/build` directory.

xCAT site
=========

- `xCAT-core <https://github.com/xcat2/xcat-core/>`__ xCAT is a toolkit for
  the deployment and administration of clusters.
- `xCAT-doc <http://xcat-docs.readthedocs.io/en/latest/>`__  Extreme
  Cloud/Cluster Administration Toolkit Document
