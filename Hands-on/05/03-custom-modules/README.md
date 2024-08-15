# Custom Ansible Module for File Management

This document outlines the process of creating a custom Ansible module in Python that manages files on remote servers. The module allows you to create, modify, update permissions, and delete files as needed.

## Objective

Create a custom module that can:
1. Create a file if it doesn't exist.
2. Ensure the file has the correct permissions.
3. Update the file's content.
4. Delete the file if specified.

## Module Name: `file_manager.py`

### Step 1: Create the Custom Module

1. **Create the Module File**

   Create a file named `file_manager.py` in your custom modules directory (e.g., `~/ansible/custom_modules/`).

2. **Write the Module Code**

   Here’s a Python script for the custom module:

   ```python
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


### Explanation:

- Parameters: path, state, content, and mode.
- State Options: present to ensure the file exists, absent to delete the file.
- Permissions: Uses oct to set file permissions.
- Check Mode: Supports Ansible’s check mode for dry runs.

## Step 2: Configure Ansible to Use the Custom Module
- Update ansible.cfg

- Make sure your ansible.cfg file includes the path to your custom modules:

```
[defaults]
library = ~/ansible/custom_modules
```

## Step 3: Write a Playbook to Test the Module
- Create a Playbook
- Create a playbook named test_file_manager.yml to use your custom module:

```
---
- name: Test File Manager Module
  hosts: all
  tasks:
    - name: Ensure file is present with specific content
      file_manager:
        path: /tmp/test_file.txt
        state: present
        content: "Hello, Ansible!"
        mode: '0644'

    - name: Ensure file is absent
      file_manager:
        path: /tmp/test_file_to_delete.txt
        state: absent
```

## Step 4: Run the Playbook
- Execute the playbook with the ansible-playbook command:

```
ansible-playbook test_file_manager.yml
```
