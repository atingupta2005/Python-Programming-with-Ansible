#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import os
import stat

def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        state=dict(type='str', choices=['present', 'absent'], default='present'),
        content=dict(type='str', required=False, default=''),
        mode=dict(type='str', required=False, default='0644')
    )

    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    path = module.params['path']
    state = module.params['state']
    content = module.params['content']
    mode = module.params['mode']

    if state == 'present':
        if not os.path.isfile(path):
            if not module.check_mode:
                with open(path, 'w') as f:
                    f.write(content)
                os.chmod(path, int(mode, 8))
            result['changed'] = True
            result['message'] = 'File created'
        else:
            # Check if content needs to be updated
            with open(path, 'r') as f:
                existing_content = f.read()
            if existing_content != content:
                if not module.check_mode:
                    with open(path, 'w') as f:
                        f.write(content)
                result['changed'] = True
                result['message'] = 'File content updated'
            else:
                result['message'] = 'File already exists with correct content'
            # Check permissions
            current_permissions = oct(stat.S_IMODE(os.lstat(path).st_mode))
            if current_permissions != mode:
                if not module.check_mode:
                    os.chmod(path, int(mode, 8))
                result['changed'] = True
                result['message'] = 'File permissions updated'
    elif state == 'absent':
        if os.path.isfile(path):
            if not module.check_mode:
                os.remove(path)
            result['changed'] = True
            result['message'] = 'File deleted'
        else:
            result['message'] = 'File does not exist'

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
