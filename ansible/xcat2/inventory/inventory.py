#!/usr/bin/env python

import os
import six
import sys
import yaml
import json
import logging
import traceback

MODULE_NAME = os.path.splitext(os.path.basename(__file__))[0]
if not os.path.exists( os.path.join('/var/log/xcatplay', MODULE_NAME)):
    os.makedirs(os.path.join('/var/log/xcatplay', MODULE_NAME))

logging.basicConfig(
    filename = '/var/log/xcatplay/%s.log' % MODULE_NAME)
LOG = logging.getLogger(MODULE_NAME)

ENV_XCAT_SOURCE = 'ENV_XCAT_SOURCE'


def _prepare_inventory():
    hostvars = dict()
    groups = dict()
    groups.update({'management': {'hosts': []}})
    groups.update({'compute': {'hosts': []}})
    return (groups, hostvars)


def _process_node_data(data_source, groups, hostvars):
    """Process data through as pre-formatted data"""
    with open(data_source, 'rb') as file_object:
        try:
            file_data = yaml.load(file_object)
        except Exception as e:
            LOG.debug("Attempting to parse YAML: %s" % e)
            raise Exception("Failed to parse YAML")

        for name in file_data:
            host = file_data[name]
            if name == 'localhost':
                host['name'] = name
                hostvars.update({name: host})
            elif name == 'management':
                if ('provision_address' not in host or not host[
                    'provision_address']):
                    LOG.debug(
                        "The provision_address %s is not defined." % name)
                    raise Exception("Miising provision_address on host" % name)
                host['name'] = name
                hostvars.update({name: host})
                groups['management']['hosts'].append(host['name'])
            else:
                if ('def_attrs' not in host or not host['def_attrs']):
                    LOG.debug(
                        "The attrs of host %s is not defined." % name)
                    raise Exception("Miising attrs on host" % name)
                host['nodename'] = name
                hostvars.update({name: host})
                groups['compute']['hosts'].append(host['nodename'])
        return (groups, hostvars)


def main():
    """Generate a list of hosts."""
    (groups, hostvars) = _prepare_inventory()
    if ENV_XCAT_SOURCE not in os.environ:
        LOG.error('Please define a %s environment variable with a comma '
                  'separated list of data sources' % ENV_XCAT_SOURCE)
        sys.exit(1)

    try:
        data_source = os.environ[ENV_XCAT_SOURCE]
        if os.path.isfile(data_source):
            try:
                (groups, hostvars) = _process_node_data(
                    data_source,
                    groups,
                    hostvars)
            except Exception as e:
                LOG.error("File does not appear to be YAML - %s" % e)
                sys.exit(1)
        else:
            LOG.error('%s does not define a file' % ENV_XCAT_SOURCE)
            sys.exit(1)

    except Exception as error:
        LOG.error('Failed processing: %s' % error)
        sys.exit(1)

    inventory = {'_meta': {'hostvars': hostvars}}
    inventory.update(groups)
    print(json.dumps(inventory, indent=2))


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(traceback.format_exc())
        sys.exit(1)