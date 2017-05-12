xcat-play
=========

xcat-play is a set of Ansible playbooks that automates the task of deploying
operation system onto a set of known hardware using xcat. It provides modular
utility for one-off operating system deployment with as few operational
requirements as reasonably possible.

Function Support
================

* Setup xCAT management node and import osimage with distribution iso that
  supported by xcat.
* Enroll a know pool of nodes( both virtual and bare metal are support) into
  xCAT.
* Deployment of an operating system to a known pool of hardware as
  a batch operation.

Supported operating systems:

* Ubuntu 16.04


Usage
======

Edit ``./ansible/xcat2/inventory/inventory.yml.example`` to match your
environment. The ``inventory.yml.example`` file defines the target nodes where
the playbook is running on and it also defines the properties owns by the nodes
or group, such as the mac address of a node or the osimage will be deployed.
For most cases, mangement node is localhost, and the other nodes are
compute nodes.

Example
-------

Setup xCAT: ::

  cd ansible/xcat2
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
