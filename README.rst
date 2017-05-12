Pre-install steps
=================

Setup ansible environment on ansible host.
For Ubuntu 14.04 or higher
::

  apt-get update && apt-get install -y python-dev python-pip libffi-dev libssl-dev git
  pip install ansible

For Redhat 7
::

  yum install python-devel python git python-setuptools gcc openssl-devel
  easy_install pip
  pip install ansible

Playbook
========

Please reference the links below to run the playbook you want:

  .. _xcat3: ansible/xcat3/README.rst
  .. _xcat2: ansible/xcat2/README.rst
  .. _ipmitool-xcat: ansible/ipmitool-xcat/README.rst
  - xcat3: `xcat3`_
  - xcat2(setup, and basic node provision): `xcat2`_
  - ipmitool-xcat: `ipmitool-xcat`_