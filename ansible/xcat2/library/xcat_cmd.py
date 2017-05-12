#!/usr/bin/python

import datetime
import six
import subprocess
import traceback

READONLY_CMDS = ['lsdef', 'tabdump']


class XCATPlayException(Exception):
    """Base xcat play Exception

    To correctly use this class, inherit from it and define
    a '_msg_fmt' property. That message will get printf'd
    with the keyword arguments provided to the constructor.

    If you need to access the message from an exception you should use
    six.text_type(exc)

    """
    _msg_fmt = "An unknown exception occurred."

    def __init__(self, message=None, **kwargs):
        self.kwargs = kwargs

        if not message:
            # Check if class is using deprecated 'message' attribute.
            if (hasattr(self, 'message') and self.message):
                self._msg_fmt = self.message

            try:
                message = self._msg_fmt % kwargs

            except Exception as e:
                message = self._msg_fmt

        super(XCATPlayException, self).__init__(message)

    def __str__(self):
        """Encode to utf-8 then wsme api can consume it as well."""
        if not six.PY3:
            return unicode(self.args[0]).encode('utf-8')

        return self.args[0]

    def __unicode__(self):
        """Return a unicode representation of the exception message."""
        return unicode(self.args[0])


def _execute_command(cmd, **kwargs):
    if not kwargs.get('stdin'):
        kwargs['stdin'] = subprocess.PIPE
    if not kwargs.get('stdout'):
        kwargs['stdout'] = subprocess.PIPE
    if not kwargs.get('stderr'):
        kwargs['stderr'] = subprocess.PIPE
    try:
        pobj = subprocess.Popen(cmd, **kwargs)
        (out, err) = pobj.communicate()
        rc = pobj.returncode
        return (rc, out, err)
    except subprocess.CalledProcessError:
        if kwargs['shell']:
            raise XCATPlayException(cmd=cmd)
        else:
            raise XCATPlayException(cmd=' '.join(cmd))


class XCATWorker(object):
    def __init__(self, module):
        self.module = module
        self.params = module.params
        self.rc = None
        self.changed = True

    def _parse_command_options(self, map):
        if map is None:
            return ''
        options = []
        for k, v in six.iteritems(map):
            options.append(k)
            options.append(v)
        return ' '.join(options)

    def _parse_command_args(self, args):
        return ' '.join(args) if args is not None else ''

    def _exec_xcat_cmd(self):
        result = dict()
        cmd = [self.params['command'],
               self._parse_command_args(self.params['args']),
               self._parse_command_options(self.params['options']),
               ]
        cmd = ' '.join(cmd)
        startd = datetime.datetime.now()
        env = self.params['environment']
        xcat_env_path = env.get('xcat_env_path')
        cmd = "bash -c \'source %(env)s && %(cmd)s \'" % {'env': xcat_env_path,
                                                          'cmd': cmd}
        try:
            (rc, out, err) = _execute_command(cmd, shell=True)
        except Exception:
            result['err'] = traceback.format_exc()
            self.rc = -1
            return dict(failed=True, changed=self.changed, rc=self.rc, cmd=cmd,
                        msg="Command error: {}".format(result))

        endd = datetime.datetime.now()
        delta = endd - startd
        result['out'] = out
        self.rc = int(rc)
        # command success
        if self.rc is not 0:
            result['err'] = err
            return dict(failed=True, changed=self.changed, rc=self.rc,
                        startd=str(startd), endd=str(endd),
                        delta=str(delta),
                        msg="Command error: {}".format(result),
                        cmd=cmd, out=out, err=err)
        else:
            return dict(changed=self.changed, rc=self.rc, startd=str(startd),
                        endd=str(endd), delta=str(delta),
                        msg="Command success: {}".format(result),
                        cmd=cmd, out=out, err=err)

    def exec_xcat_cmd(self):
        if self.params['command'] in READONLY_CMDS:
            self.changed = False
        result = self._exec_xcat_cmd()
        if self.rc != 0:
            self.module.fail_json(**result)
            return
        if self.params['format_obj']:
            self._format_object_result(result)
        self.module.exit_json(**result)

    def _format_object_result(self, result):
        """Process object output from xcat command

            Object name: kvmhost
                groups=all
                ip=10.5.101.1
                postbootscripts=otherpkgs
                postscripts=syslog,remoteshell,syncfiles
            Object name: testnode1
                arch=x86_64
                currchain=boot
                currstate=boot
                groups=all
                initrd=xcat/osimage/ubuntu16.04.1-x86_64-install-compute/initrd.img
        """
        out = result['out']
        lines = out.split('\n')
        obj = None
        xcat_objs = []
        xcat_attrs = dict()
        for line in lines:
            line = line.strip()
            if line.startswith('Object name:'):
                if obj is not None:
                    xcat_objs.append(xcat_attrs)
                temp = line.split(':')
                if len(temp) > 1:
                    obj = line.split(':')[1].strip()
                    xcat_attrs['name'] = obj
                continue
            elif obj is not None:
                temp = line.split('=')
                if len(temp) > 1:
                    key = line.split('=')[0].strip()
                    val = line.split('=')[1].strip()
                    xcat_attrs[key] = val
        if obj is not None:
            xcat_objs.append(xcat_attrs)
        result['xcat_objs'] = xcat_objs


def generate_module():
    argument_spec = dict(
        command=dict(requried=True, type='str'),
        options=dict(required=False, type='dict'),
        args=dict(required=False, type='list'),
        format_obj=dict(required=False, type='str'),
        stdin=dict(required=False, type='str'),
        stdout=dict(required=False, type='str'),
        environment=dict(required=False, type='dict'),
    )
    module = AnsibleModule(
        argument_spec=argument_spec,
        bypass_checks=True
    )
    env = module.params.pop('environment', dict())
    new_args = module.params.pop('common_options', dict())
    new_args['environment'] = {'xcat_env_path': '/etc/profile.d/xcat.sh'}
    if env:
        new_args['environment'].update(env)

    for key, value in module.params.items():
        if key in new_args and value is None:
            continue
        new_args[key] = value

    module.params = new_args
    return module


def main():
    module = generate_module()

    try:
        XCATWorker(module).exec_xcat_cmd()
        # if ret is not None:
        #     xcat_worker.print_json_data(ret)
    except Exception:
        module.exit_json(failed=True, changed=True,
                         msg=repr(traceback.format_exc()))


# import module snippets
from ansible.module_utils.basic import *  # noqa

if __name__ == '__main__':
    main()
