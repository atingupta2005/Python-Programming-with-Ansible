#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import requests

def run_module():
    module_args = dict(
        url=dict(type='str', required=True),
        method=dict(type='str', required=True, choices=['GET', 'POST']),
        headers=dict(type='dict', required=False, default={}),
        data=dict(type='dict', required=False, default={})
    )

    result = dict(
        changed=False,
        original_message='',
        message='',
        response=dict()
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    url = module.params['url']
    method = module.params['method']
    headers = module.params['headers']
    data = module.params['data']

    try:
        if method == 'GET':
            response = requests.get(url, headers=headers)
        elif method == 'POST':
            response = requests.post(url, headers=headers, json=data)

        result['response'] = response.json()
        result['message'] = f"Request completed with status code {response.status_code}"
        if response.status_code >= 400:
            module.fail_json(msg=f"Request failed with status code {response.status_code}", **result)

    except requests.RequestException as e:
        module.fail_json(msg=f"Request failed: {str(e)}", **result)

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()