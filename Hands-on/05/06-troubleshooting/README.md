# Ansible Troubleshooting

Ansible is a versatile tool for automation, but troubleshooting issues can sometimes be challenging. This guide provides a detailed approach to troubleshooting common Ansible problems.

### 1. **Understanding Ansible Errors**

**Common Error Types:**
- **Syntax Errors:** Errors in YAML syntax or incorrect module usage.
- **Connection Errors:** Issues related to SSH or network connectivity.
- **Module Errors:** Problems related to module execution, such as missing dependencies or incorrect parameters.

**Error Messages:**
- Carefully read error messages as they often provide clues about what went wrong.
- Use the `-vvv` option to increase verbosity and get more detailed output.

### 2. **Check Syntax and Formatting**

**YAML Syntax:**
- Ensure correct indentation (use spaces, not tabs).
- Verify that all lists and dictionaries are properly formatted.

**Commands:**
To check syntax errors in your playbooks:
```
ansible-playbook playbook.yml --syntax-check
```

### 3. **Verify Inventory Configuration**

**Inventory File:**
- Check the correctness of the inventory file (paths, hostnames, IP addresses).
- Ensure that all hosts are correctly defined.

**Commands:**
To verify inventory:
```
ansible-inventory --list -i inventory/
```

### 4. **Validate Connectivity**

**SSH Issues:**
- Verify that SSH keys are correctly configured and have the right permissions.
- Ensure the SSH agent is running if using an SSH key.

**Commands:**
To test SSH connectivity:
```
ansible all -m ping -i inventory/
```

**Common Issues:**
- Check network firewalls and security groups.
- Ensure that the target hosts are reachable and responding to SSH.

### 5. **Debugging Playbooks**

**Verbose Mode:**
- Use `-v`, `-vv`, or `-vvv` to increase verbosity and get more information about what’s happening.

**Commands:**
To run a playbook with detailed output:
```
ansible-playbook playbook.yml -vvv
```

**Debug Statements:**
- Use the `debug` module to print variable values and understand their content.

**Example:**
```yaml
- name: Debug message
  debug:
    msg: "The value of variable is {{ my_variable }}"
```

### 6. **Check Module and Role Dependencies**

**Dependencies:**
- Ensure all required dependencies are installed.
- Verify that roles and modules are correctly defined and available.

**Commands:**
To check for missing modules:
```
ansible-galaxy list
```

### 7. **Inspect Ansible Configuration**

**Configuration File:**
- Check `ansible.cfg` for misconfigurations.
- Ensure the configuration file is in the correct location or specified correctly.

**Commands:**
To display the current configuration:
```
ansible-config dump
```

### 8. **Handling Failed Tasks**

**Task Failures:**
- Investigate the task that failed and review the module documentation for proper usage.
- Use the `failed_when` and `changed_when` parameters to manage task success and failure conditions.

**Commands:**
To retry failed tasks:
```
ansible-playbook playbook.yml --start-at-task="task_name"
```

### 9. **Troubleshooting Common Issues**

**Permission Denied:**
- Verify file and directory permissions on both the control machine and target hosts.

**Commands:**
To check permissions:
```
ls -l /path/to/file
```

**Module Not Found:**
- Ensure the module is installed and accessible.

**Commands:**
To reinstall a module:
```
ansible-galaxy install <role_name>
```

**Variable Issues:**
- Check for typos and ensure variables are defined in the correct scope (e.g., `group_vars`, `host_vars`, or playbook).

**Commands:**
To print all variables:
```
ansible-playbook playbook.yml -e '@vars.yml' -vvv
```

### 10. **Review Logs and History**

**Log Files:**
- Review Ansible log files for additional details on errors.

**Commands:**
To view Ansible logs (if logging is enabled):
```
cat /var/log/ansible.log
```

**Command History:**
- Check command history for previously executed commands and their outputs.

**Commands:**
To view command history:
```
history
```

### 11. **Seek Help and Resources**

**Documentation:**
- Refer to the official Ansible documentation for guidance on modules and usage.

**Community:**
- Use forums, mailing lists, or communities like Stack Overflow for additional support.

**Official Documentation:**
- Ansible Documentation: https://docs.ansible.com/

**Community Forums:**
- Ansible Community: https://www.ansible.com/community

# Ansible Troubleshooting Scenarios and Commands

### 1. Check Ansible Version
```bash
ansible --version
```

### 2. Test Connection to Hosts
```bash
ansible all -m ping
```

### 3. Run a Playbook with Verbose Output
```bash
ansible-playbook playbook.yml -vvv
```

### 4. List Inventory Hosts
```bash
ansible-inventory --list
```

### 5. Check Syntax of Playbooks
```bash
ansible-playbook playbook.yml --syntax-check
```

### 6. Check for Unreachable Hosts
```bash
ansible all -m ping -a "msg='Testing connectivity'"
```

### 7. View Registered Variables
```yaml
- name: Debug all variables
  debug:
    var: hostvars[inventory_hostname]
```

### 8. Inspect Task Results
```yaml
- name: Run a command
  command: /usr/bin/uptime
  register: uptime_result

- name: Display uptime
  debug:
    var: uptime_result
```

### 9. Print Facts from Hosts
```yaml
- name: Gather system facts
  setup:
```

### 10. Check Task Status
```yaml
- name: Check if /etc/hosts file exists
  stat:
    path: /etc/hosts
  register: hosts_stat

- name: Display file status
  debug:
    var: hosts_stat
```

### 11. Test Playbook Execution on a Single Host
```bash
ansible-playbook playbook.yml -l webserver1
```

### 12. Display Ansible Configuration
```bash
ansible-config dump
```

### 13. List Playbook Roles and Tasks
```bash
ansible-playbook playbook.yml --list-tasks
```

### 14. Use `failed_when` and `changed_when` for Debugging
```yaml
- name: Check for a non-existent file
  command: /bin/ls /nonexistentfile
  register: result
  failed_when: "'No such file' in result.stderr"
  changed_when: false
```

### 15. Enable Debug Mode for Specific Tasks
```yaml
- name: List files in /tmp
  command: ls /tmp
  register: tmp_files
  ignore_errors: yes

- name: Show files in /tmp
  debug:
    msg: "{{ tmp_files.stdout }}"
```

### 16. Check File Permissions and Ownership
```yaml
- name: Check permissions of /etc/hosts
  stat:
    path: /etc/hosts
  register: file_stat

- name: Display file permissions
  debug:
    var: file_stat
```

### 17. Inspect Task Execution Time
```yaml
- name: Measure time to list /tmp contents
  command: /usr/bin/time ls /tmp
  register: time_result

- name: Show execution time
  debug:
    msg: "Execution time: {{ time_result.elapsed }}"
```

### 18. Review Ansible Logs
```bash
tail -f /var/log/ansible.log
```

### 19. Check Network Connectivity
```bash
ansible all -m command -a "ping -c 4 8.8.8.8"
```

### 20. Review Ansible Facts
```bash
ansible localhost -m setup
```

### 21. Test Playbook with a Single Task
```bash
ansible-playbook playbook.yml --start-at-task="Install Apache"
```

### 22. Display Host Variables
```bash
ansible localhost -m debug -a "var=hostvars['localhost']"
```

### 23. Check For Correct YAML Syntax
```bash
yamllint playbook.yml
```

### 24. Test SSH Connectivity
```bash
ssh -i /path/to/ssh/key user@hostname
```

### 25. Validate Inventory File Syntax
```bash
ansible-inventory --inventory-file /etc/ansible/hosts --list
```

### 26. Inspect SSH Connection Issues
```bash
ssh -vvv user@hostname
```

### 27. Check for Correct Ansible Permissions
```bash
ls -l /path/to/playbook.yml
```

### 28. Review Ansible Configuration File
```bash
cat /etc/ansible/ansible.cfg
```

### 29. List All Variables for a Host
```bash
ansible localhost -m debug -a "var=hostvars['localhost']"
```

### 30. Check Execution Time for Tasks
```yaml
- name: Measure time to run ls
  command: /usr/bin/time ls /some_directory
```

### 31. Verify Host's Network Configuration
```bash
ansible localhost -m command -a "ip a"
```

### 32. Monitor Disk Usage
```bash
ansible localhost -m command -a "df -h"
```

### 33. Verify Memory Usage
```bash
ansible localhost -m command -a "free -m"
```

### 34. Inspect Running Processes
```bash
ansible localhost -m command -a "ps aux"
```

### 35. Debug with `ansible-playbook` Dry Run
```bash
ansible-playbook playbook.yml --check
```

### 36. Test Task Failures
```yaml
- name: Force failure
  command: /bin/false
  ignore_errors: yes
```

### 37. Review Ansible Role Dependencies
```bash
ansible-galaxy role list
```

### 38. Check Environment Variables in Playbook
```yaml
- name: Display environment variables
  command: env
  register: env_result

- name: Show environment variables
  debug:
    msg: "{{ env_result.stdout }}"
```

### 39. Verify Connection with Specific User
```bash
ansible all -m ping -u myuser
```

### 40. Display Host Facts in JSON
```bash
ansible localhost -m setup -a 'filter=ansible_facts' -j
```

### 41. Check Ansible Role Directory Structure
```bash
ls -R roles/
```

### 42. View Registered Variables for a Task
```yaml
- name: List contents of /tmp
  command: ls /tmp
  register: tmp_files

- name: Show contents of /tmp
  debug:
    var: tmp_files
```

### 43. Check Task Errors
```bash
ansible-playbook playbook.yml --check --diff
```

### 44. Verify Inventory Host Variables
```bash
ansible localhost -m debug -a "var=hostvars['localhost']['ansible_facts']"
```

### 45. Review Playbook Execution Results
```bash
ansible-playbook playbook.yml | tee playbook_output.log
```

### 46. Inspect Task Results with `register`
```yaml
- name: Run uptime command
  command: uptime
  register: uptime_result

- name: Display uptime
  debug:
    var: uptime_result
```

### 47. Monitor Ansible Performance
```bash
time ansible-playbook playbook.yml
```

### 48. View Playbook Debug Output
```bash
ansible-playbook playbook.yml -vvvv
```

### 49. Verify Task Output Content
```yaml
- name: Run ls command
  command: ls /some_directory
  register: ls_result

- name: Show ls output
  debug:
    msg: "{{ ls_result.stdout }}"
```

### 50. Ensure Correct Permissions on Playbook Files
```bash
chmod 644 /path/to/playbook.yml
```

### 51. Check for Valid Playbook Syntax
```bash
ansible-playbook playbook.yml --syntax-check
```

### 52. Run Playbook on a Specific Group
```bash
ansible-playbook playbook.yml -l webservers
```

### 53. Debug with `assert` Module
```yaml
- name: Assert a variable value
  assert:
    that:
      - some_variable == 'expected_value'
```

### 54. Verify Host Reachability
```bash
ansible all -m ping -i /etc/ansible/hosts
```

### 55. Check Task Output for Specific Values
```yaml
- name: Check for specific value in output
  command: /bin/ls /some_directory
  register: ls_result

- name: Assert specific value
  assert:
    that:
      - "'important_file.txt' in ls_result.stdout"
```

### 56. Inspect Playbook Variables
```yaml
- name: Print all variables
  debug:
    var: vars
```

### 57. Test with `ansible-playbook` Dry Run
```bash
ansible-playbook playbook.yml --check
```

### 58. Validate Syntax for Ansible Roles
```bash
ansible-galaxy role init role_name
```

### 59. Check for Ansible Vault Issues
```bash
ansible-vault decrypt /path/to/encrypted_file
```

### 60. Verify Host Key Checking
```bash
ansible all -m command -a "ssh-keyscan -H example.com"
```

### 61. Test File Deployment
```yaml
- name: Deploy a file
  copy:
    src: /local/path/file.txt
    dest

: /remote/path/file.txt
```

### 62. Verify Command Execution
```yaml
- name: Check for installed package
  command: dpkg -l | grep nginx
  register: package_status

- name: Show package status
  debug:
    var: package_status
```

### 63. Check Playbook Errors
```bash
ansible-playbook playbook.yml --diff
```

### 64. Test Using `ansible-console`
```bash
ansible-console
```

### 65. View All Hosts and Groups
```bash
ansible-inventory --list
```

### 66. Check If a Service is Running
```yaml
- name: Check if apache2 is running
  service:
    name: apache2
    state: started
  register: service_status

- name: Show service status
  debug:
    var: service_status
```

### 67. Validate Ansible Variables
```yaml
- name: Validate variables
  assert:
    that:
      - some_variable is defined
```

### 68. Test Playbook Execution with Specific Tags
```bash
ansible-playbook playbook.yml --tags "install,configure"
```

### 69. Monitor Playbook Execution in Real-Time
```bash
ansible-playbook playbook.yml -f 1
```

### 70. Review Ansible Task Output
```yaml
- name: Show task output
  debug:
    msg: "{{ task_output.stdout }}"
```

### 71. Check for Configuration Errors
```bash
ansible-playbook playbook.yml --check
```

### 72. Inspect Ansible Environment
```bash
ansible all -m command -a "env"
```

### 73. Test with `ansible-playbook` with Limitations
```bash
ansible-playbook playbook.yml -l 'webservers'
```

### 74. Validate Ansible Hosts
```bash
ansible all -m ping -i /path/to/inventory
```

### 75. Review Ansible Playbook Diff
```bash
ansible-playbook playbook.yml --diff
```

### 76. Check for Hostname Issues
```yaml
- name: Verify hostname
  command: hostname
  register: hostname_result

- name: Display hostname
  debug:
    var: hostname_result
```

### 77. Inspect File System Changes
```yaml
- name: Check disk space
  command: df -h
  register: disk_space

- name: Show disk space
  debug:
    var: disk_space
```

### 78. Validate Module Installation
```bash
ansible-galaxy collection list
```

### 79. Test Playbook with `--start-at-task`
```bash
ansible-playbook playbook.yml --start-at-task="Install nginx"
```

### 80. Verify Host Configuration with `setup` Module
```bash
ansible localhost -m setup
```

### 81. Check Service Status with `systemd`
```yaml
- name: Check systemd service status
  systemd:
    name: nginx
    state: started
  register: service_status

- name: Show service status
  debug:
    var: service_status
```

### 82. Validate Ansible Playbook Parameters
```yaml
- name: Validate parameters
  assert:
    that:
      - ansible_ssh_user is defined
      - ansible_ssh_pass is defined
```

### 83. Test Ansible Playbook with `--list-hosts`
```bash
ansible-playbook playbook.yml --list-hosts
```

### 84. Review Ansible Command Output
```yaml
- name: Run command
  command: ls /etc
  register: command_result

- name: Display command output
  debug:
    var: command_result
```

### 85. Check Ansible Role Dependencies
```bash
ansible-galaxy role list
```

### 86. Inspect Host Logs
```bash
ansible localhost -m command -a "tail -n 50 /var/log/syslog"
```

### 87. Validate Inventory Variables
```yaml
- name: Display inventory variables
  debug:
    var: hostvars['localhost']
```

### 88. Test Ansible Playbook with `--extra-vars`
```bash
ansible-playbook playbook.yml --extra-vars "env=prod"
```

### 89. Monitor System Resource Usage
```yaml
- name: Check CPU usage
  command: top -bn1 | grep "Cpu(s)"
  register: cpu_usage

- name: Show CPU usage
  debug:
    var: cpu_usage
```

### 90. Review Ansible Execution Time
```bash
time ansible-playbook playbook.yml
```

### 91. Check SSH Key Permissions
```bash
ls -l ~/.ssh/id_rsa
```

### 92. Inspect File Changes
```yaml
- name: Check file contents
  command: cat /etc/hosts
  register: file_contents

- name: Show file contents
  debug:
    var: file_contents
```

### 93. Validate Ansible Vault File
```bash
ansible-vault view secrets.yml
```

### 94. Review Playbook Variables and Defaults
```yaml
- name: Print default variables
  debug:
    var: vars
```

### 95. Check for Syntax Errors in Roles
```bash
ansible-playbook playbook.yml --syntax-check
```

### 96. Verify Installed Ansible Collections
```bash
ansible-galaxy collection list
```

### 97. Validate Ansible Hosts File
```bash
ansible-inventory --list -i /etc/ansible/hosts
```

### 98. Review Playbook Execution with `--check`
```bash
ansible-playbook playbook.yml --check
```

### 99. Inspect Task Output with Debug
```yaml
- name: Run a command
  command: date
  register: date_result

- name: Show date output
  debug:
    var: date_result
```

### 100. Validate Service State
```yaml
- name: Ensure nginx is running
  service:
    name: nginx
    state: started
  register: service_status

- name: Display service status
  debug:
    var: service_status

