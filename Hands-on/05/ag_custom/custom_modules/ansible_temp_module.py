#!/usr/bin/python3

from temperature_converter import *
from ansible.module_utils.basic import AnsibleModule


def run_module():
  module_args = dict(
    farenheit=dict(type='float', required=True)
  )
  
  result = dict(
    changed=False,
    celcius=None
  )
  
  module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)
  farenheit = module.params['farenheit']
  try:
    result['celcius'] = farenheit_to_celcius(farenheit)
  except Exception as e:
    module.fail_json(msg=str(e))
  
  module.exit_json(**result)
    
    
if __name__ == "__main__":
  run_module()
