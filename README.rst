Pre-install steps
=================

Setup ansible environment on ansible host.
For Ubuntu 14.04 or higher
::

  apt-get update && apt-get install -y python-dev python-pip libffi-dev libssl-dev git
  pip install ansible

For Redhat 7 / CentOS 7
::

  yum install -y python-devel python git python-setuptools gcc openssl-devel libffi-devel file make
  easy_install pip
  pip install ansible

Playbook
========

Please reference the links below to run the playbook you want:

  .. _xcat3: ansible/xcat3/README.rst
  .. _pypy-xcat3: ansible/pypy-xcat3/README.rst
  .. _xcat2: ansible/xcat2/README.rst
  .. _ipmitool-xcat: ansible/ipmitool-xcat/README.rst
  .. _conserver-xcat: ansible/conserver-xcat/README.rst
  - Setup xcat3 prototype: `xcat3`_
  - xcat3 service(pypy), xcat3 client(golang): `pypy-xcat3`_
  - xcat2(setup, and basic node provision): `xcat2`_
  - Build ipmitool-xcat packages for multiple platforms: `ipmitool-xcat`_
  - Build conserver-xcat packages for multiple platforms: `conserver-xcat`_