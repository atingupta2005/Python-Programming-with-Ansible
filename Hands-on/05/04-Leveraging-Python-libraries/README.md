# Leveraging Python Libraries within Ansible

Using Python libraries within Ansible custom modules can significantly enhance the functionality and flexibility of your playbooks. In this example, we'll demonstrate how to use the `requests` library to interact with a REST API from within an Ansible custom module.

## Example: Custom Ansible Module Using `requests` Library

### 0. Install Python Virtual Environment if required

### 1. Install Required Python Library

First, ensure that the `requests` library is available in your environment. You can install it using pip:

```sh
pip install requests
```

### 2. Create the Custom Ansible Module

Create a custom Ansible module that uses the requests library to perform HTTP requests. Save the following script as api_fetcher.py:
```
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
```

### 3. Explanation
 - Parameters:
   - url: The URL of the API endpoint.
   - method: The HTTP method to use (GET or POST).
   - headers: Optional headers to include in the request.
   - data: Optional data to send with the request (used with POST).
 - Functionality:
   - Performs HTTP requests using the requests library.
   - Handles both GET and POST methods.
   - Provides the response in JSON format.
   - Handles exceptions and reports errors.

### 4. Create the Ansible Playbook
Use the custom module in an Ansible playbook to fetch and post data from/to a public API. Save the following playbook as api_playbook.yml:

```
- name: Fetch data from API using custom module
  hosts: localhost
  tasks:
    - name: Fetch JSON data from example API
      api_fetcher:
        url: "https://jsonplaceholder.typicode.com/posts/1"
        method: GET
      register: result_get

    - name: Show GET request result
      debug:
        msg: "GET Request Response: {{ result_get.response }}"

    - name: Post data to example API
      api_fetcher:
        url: "https://jsonplaceholder.typicode.com/posts"
        method: POST
        headers:
          Content-Type: "application/json"
        data:
          title: "foo"
          body: "bar"
          userId: 1
      register: result_post

    - name: Show POST request result
      debug:
        msg: "POST Request Response: {{ result_post.response }}"
```

## 5. Summary
In this example:

 - We created a custom Ansible module (api_fetcher.py) that uses the requests library to interact with REST APIs.
 - The module supports both GET and POST methods and can handle headers and data.
 - The Ansible playbook demonstrates how to use this module to fetch and post data from/to a public API.

This approach allows you to harness the power of Python libraries to extend Ansible's capabilities and interact with external systems in a more flexible and powerful way.