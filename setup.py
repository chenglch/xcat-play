import os
import sys
from setuptools import setup
from glob import glob

data_files = []
share_dir = '%s/local/share/xcatplay' % sys.prefix


def traverse(directory):
    if not directory or not os.path.isdir(directory):
        return
    files = [f for f in glob('%s/*' % directory) if os.path.isfile(f)]
    dirs = [d for d in glob('%s/*' % directory) if os.path.isdir(d)]
    for d in dirs:
        traverse("%s" %(d))
    if files:
        data_files.append(('%s/%s' % (share_dir, directory), files))

traverse('ansible')

setup(
    name='xcatplay',
    version='0.1',
    author='chenglch',
    author_email='chenglch@cn.ibm.com',
    url='https://github.com/xcat2/',
    description='xcat playbook',
    packages=['xcatplay', ],
    install_requires=[
        'setuptools>=11.3',
        'Jinja2>=2.8',
        'six>=1.9.0',
        'PyYAML>=3.10.0',
        'ansible>=1.9',
    ],

    #license="GPLv3",
    data_files = data_files,
)
