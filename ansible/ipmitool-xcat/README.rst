Build ipmitool-xcat
=========

ipmitool-xcat is a playbook to build packages for various platforms.


Usage
======

Edit ``./ansible/conserver-xcat/inventory/host`` to add hosts where the
packages are built. If you use sshpass to connect to the hosts, make sure hosts
key are added in the `known_hosts` file.

For SLES, development related RPMs are shipped with the SDK ISO.  Ensure that 
the `zypper` repo files are confgiured to point to an SDK repo, or the build for
SLES will not work. 

Example
-------

Run the ipmitool-xcat playbook to build packages::

  cd ansible/ipmitool-xcat
  ansible-playbook -i inventory/host ipmitool-xcat.yml

`ipmitool-xcat` packages will be placed in `/tmp/build` directory on the localhost.

xCAT site
=========

- `xCAT-core <https://github.com/xcat2/xcat-core/>`__ xCAT is a toolkit for
  the deployment and administration of clusters.
- `xCAT-doc <http://xcat-docs.readthedocs.io/en/latest/>`__  Extreme
  Cloud/Cluster Administration Toolkit Document
