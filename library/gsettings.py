#!/usr/bin/python

import subprocess

from ansible.module_utils.basic import *


def set_value(schema, key, value):
    return subprocess.check_output([
        'gsettings', 'set', schema, key, value
    ]).strip()


def get_value(schema, key):
    return subprocess.check_output([
        'gsettings', 'get', schema, key
    ]).strip()[1:-1]


def main():
    module = AnsibleModule(
        argument_spec={
            'state': {'choices': ['present'], 'default': 'present'},
            'schema': {'required': True},
            'key': {'required': True},
            'value': {'required': True},
        },
        supports_check_mode=True,
    )

    schema = module.params['schema']
    key = module.params['key']
    value = module.params['value']

    value = value.strip()
    value = value.replace('\n', '')

    try:
        old_value = get_value(schema, key)
        changed = old_value != value

        if changed and not module.check_mode:
            set_value(schema, key, value)
    except subprocess.CalledProcessError as e:
        module.fail_json(msg=e.output)
    else:
        module.exit_json(
            changed=changed,
            key=key,
            value=value,
            old_value=old_value,
        )

if __name__ == '__main__':
    main()
