xcat-play
=========

xcat-play is a set of Ansible playbooks that automates the task of deploying
operation system onto a set of known hardware using xcat. It provides modular
utility for one-off operating system deployment with as few operational
requirements as reasonably possible.

Use Cases
=========

* Setup xCAT management node and import osimage with distribution iso that
  supported by xcat.
* Enroll a know pool of nodes( both virtual and bare metal are support) into
  xCAT.
* Deployment of an operating system to a known pool of hardware as
  a batch operation.

Supported operating systems:

* Ubuntu 14.04

Pre-install steps
=================

::

  apt-get update && apt-get install -y python-dev python-pip libffi-dev libssl-dev git

Installation
============

::

  git clone https://github.com/chenglch/xcat-play.git
  cd xcat-play
  python setup.py install

Use
====

Edit ``./ansible/inventory/inventory.yml.example`` to match your environment.
The ``inventory.yml.example`` file defines the target nodes where the playbook
is running on and it also defines the properties that nodes or groups have,
such as the mac address of a node or which osimage should be deployed. For most
cases, mangement node is localhost, and the other nodes are compute nodes.

Example
-------

Setup xCAT: ::

  cd ansible
  export ENV_XCAT_SOURCE=inventory/inventory.yml.example
  ansible-playbook -i inventory/inventory.py install-xcat.yml

Define nodes ::

  export ENV_XCAT_SOURCE=inventory/inventory.yml.example
  ansible-playbook -i inventory/inventory.py erroll-node.yml

Deploy nodes ::

  export ENV_XCAT_SOURCE=inventory/inventory.yml.example
  ansible-playbook -i inventory/inventory.py deploy-node.yml

xCAT site
=========

- `xCAT-core <https://github.com/xcat2/xcat-core/>`__ xCAT is a toolkit for
  the deployment and administration of clusters.
- `xCAT-doc <http://xcat-docs.readthedocs.io/en/latest/>`__  Extreme
  Cloud/Cluster Administration Toolkit Document
