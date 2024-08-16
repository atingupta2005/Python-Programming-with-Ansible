# Ansible Performance Tips
## 1. **Optimize Inventory**

**Tip**: Use a dynamic inventory script or service instead of a static inventory file if you are managing a large number of hosts. This reduces the time spent reading and parsing static files.

**Example**:
Configure a dynamic inventory with AWS:
```ini
[aws]
plugin: aws_ec2
regions:
  - us-east-1
```

## 2. **Minimize SSH Connections**

**Tip**: Use `pipelining` to reduce the number of SSH connections.

**Example**:
In your `ansible.cfg`, enable pipelining:
```ini
[pipelining]
pipelining = True
```

## 3. **Avoid Unnecessary Fact Gathering**

**Tip**: Disable fact gathering if you do not need it for your playbook.

**Example**:
Disable fact gathering in your playbook:
```yaml
- hosts: all
  gather_facts: no
  tasks:
    - name: Run a command
      command: uptime
```

## 4. **Use Async and Polling**

**Tip**: For long-running tasks, use `async` and `poll` to prevent blocking.

**Example**:
Run a task asynchronously:
```yaml
- name: Run a long task
  command: /usr/bin/long_running_command
  async: 600
  poll: 10
```

## 5. **Leverage Delegation**

**Tip**: Use `delegate_to` to offload tasks to a specific host, reducing load on the managed hosts.

**Example**:
Delegate a task to localhost:
```yaml
- name: Run a command on localhost
  command: /usr/bin/some_command
  delegate_to: localhost
```

## 6. **Use the `serial` Keyword**

**Tip**: Deploy changes in batches using `serial` to manage load and avoid overwhelming the infrastructure.

**Example**:
Apply changes to a batch of hosts:
```yaml
- hosts: webservers
  serial: 3
  tasks:
    - name: Install a package
      yum:
        name: httpd
        state: present
```

## 7. **Avoid Using `shell` Module When Possible**

**Tip**: Prefer the `command` module over `shell` for simple commands to avoid additional shell processing overhead.

**Example**:
Use `command` instead of `shell`:
```yaml
- name: List files in /tmp
  command: ls /tmp
```

## 8. **Use `changed_when` and `failed_when`**

**Tip**: Optimize task success and failure conditions to avoid unnecessary task executions.

**Example**:
Control task failure condition:
```yaml
- name: Check if file exists
  stat:
    path: /tmp/some_file
  register: file_stat
  failed_when: "'No such file' in file_stat.msg"
```

## 9. **Minimize Use of Loops**

**Tip**: Avoid excessive looping. Use `with_items` judiciously and consider batch operations when possible.

**Example**:
Batch operations for package installation:
```yaml
- name: Install multiple packages
  yum:
    name: "{{ item }}"
    state: present
  with_items:
    - httpd
    - git
    - vim
```

## 10. **Use Connection Plugins**

**Tip**: Use `ssh` connection plugins with proper settings to improve connection efficiency.

**Example**:
Configure connection plugin settings in `ansible.cfg`:
```ini
[ssh_connection]
ssh_args = -o ControlMaster=auto -o ControlPersist=60s
```

## 11. **Optimize Playbook Structure**

**Tip**: Structure your playbooks efficiently with fewer roles and tasks per playbook to reduce processing time.

**Example**:
Consolidate roles:
```yaml
- hosts: webservers
  roles:
    - common
    - web
    - security
```

## 12. **Use `include_tasks` Instead of `import_tasks`**

**Tip**: Use `include_tasks` to conditionally include tasks at runtime, reducing the initial load.

**Example**:
Include tasks conditionally:
```yaml
- name: Include tasks based on condition
  include_tasks: "tasks/{{ item }}.yml"
  with_items:
    - install
    - configure
```

## 13. **Reduce Ansible Playbook Verbosity**

**Tip**: Minimize verbosity level unless debugging. Excessive verbosity can slow down execution.

**Example**:
Run playbook with reduced verbosity:
```bash
ansible-playbook playbook.yml -v
```

## 14. **Leverage Ansible Caching**

**Tip**: Use fact caching to store and reuse facts, reducing the need to gather them each time.

**Example**:
Enable fact caching in `ansible.cfg`:
```ini
[defaults]
fact_caching = jsonfile
fact_caching_timeout = 86400
fact_caching_connection = /tmp/facts
```

## 15. **Use Tags to Run Specific Tasks**

**Tip**: Use tags to run specific parts of the playbook, avoiding unnecessary execution of tasks.

**Example**:
Run tagged tasks:
```yaml
- hosts: all
  tasks:
    - name: Install package
      yum:
        name: httpd
        state: present
      tags:
        - install
```
```bash
ansible-playbook playbook.yml --tags "install"
```

## 16. **Use Proper Inventory Groups**

**Tip**: Organize hosts into appropriate inventory groups to optimize targeting and reduce complexity.

**Example**:
Define inventory groups in `hosts` file:
```ini
[webservers]
web1
web2

[dbservers]
db1
```

## 17. **Optimize `async` Task Configuration**

**Tip**: Configure async tasks properly to avoid excessive waiting times.

**Example**:
Set async task duration:
```yaml
- name: Run long command
  command: /usr/bin/long_command
  async: 3600
  poll: 30
```

## 18. **Use `block` for Error Handling**

**Tip**: Group tasks using `block` for better error handling and performance management.

**Example**:
Handle errors with `block`:
```yaml
- name: Deploy application
  block:
    - name: Install package
      yum:
        name: httpd
        state: present
    - name: Start service
      service:
        name: httpd
        state: started
  rescue:
    - name: Rollback changes
      command: /usr/bin/rollback
```

## 19. **Limit the Number of Forks**

**Tip**: Set a reasonable number of forks in `ansible.cfg` to avoid overwhelming the network and managed nodes.

**Example**:
Configure forks in `ansible.cfg`:
```ini
[defaults]
forks = 10
```

## 20. **Use `when` Statements Wisely**

**Tip**: Use `when` conditions to execute tasks conditionally and avoid unnecessary operations.

**Example**:
Conditional task execution:
```yaml
- name: Install package only if not installed
  yum:
    name: httpd
    state: present
  when: ansible_facts.packages['httpd'] is not defined
```

## 21. **Monitor and Optimize Playbook Execution**

**Tip**: Regularly review and optimize playbook execution to improve performance and efficiency.

**Example**:
Monitor execution times:
```bash
time ansible-playbook playbook.yml
```

## 22. **Optimize Role Execution**

**Tip**: Use roles efficiently by minimizing the number of role inclusions and structuring roles properly.

**Example**:
Organize roles in a directory structure:
```bash
roles/
  common/
    tasks/
    handlers/
  web/
    tasks/
    handlers/
```

## 23. **Avoid Excessive Use of `debug` Module**

**Tip**: Use `debug` module sparingly to avoid excessive output that can slow down execution.

**Example**:
Use `debug` only for necessary information:
```yaml
- name: Debug variable
  debug:
    var: some_variable
```

## 24. **Use Ansible Collections for Reusable Content**

**Tip**: Use Ansible collections to package and reuse automation content efficiently.

**Example**:
Install and use an Ansible collection:
```bash
ansible-galaxy collection install community.general
```
```yaml
- name: Use community.general collection
  hosts: localhost
  tasks:
    - name: Create a directory
      community.general.file:
        path: /tmp/example
        state: directory
```

## 25. **Optimize Ansible Modules Usage**

**Tip**: Prefer modules that are optimized for performance over generic commands.

**Example**:
Use `yum` module instead of `command` for package management:
```yaml
- name: Install nginx
  yum:
    name: nginx
    state: present
```

## 26. **Handle Large Data Efficiently**

**Tip**: Use data streaming or chunking for handling large datasets to avoid memory issues.

**Example**:
Handle large data with streaming:
```yaml
---
- name: Fetch a large file from a URL
  hosts: localhost
  tasks:
    - name: Download a large file
      get_url:
        url: https://example.com/largefile.zip
        dest: /tmp/largefile.zip
        validate_certs: no
      register: download_result

    - name: Display download result
      debug:
        msg: "Downloaded {{ download_result.url }} to {{ download_result.dest }}"
```

## 27. **Optimize Fact Gathering**

**Tip**: Gather only the necessary facts to reduce overhead.

**Example**:
Gather specific facts:
```yaml
---
- name: Optimize Fact Gathering Example
  hosts: all
  gather_facts: yes
  tasks:
    - name: Gather only specific facts
      setup:
        gather_subset:
          - network
          - hardware
          - virtual
      register: facts

    - name: Show gathered network facts
      debug:
        msg: "{{ facts.ansible_facts['network'] }}"

    - name: Show gathered hardware facts
      debug:
        msg: "{{ facts.ansible_facts['hardware'] }}"

    - name: Show gathered virtual facts
      debug:
        msg: "{{ facts.ansible_facts['virtual'] }}"
```

## 28. **Use `copy` Module for Large Files**

**Tip**: Use `copy` module to handle large file transfers efficiently.

**Example**:
Copy a large file:
```yaml
- name: Copy large file
  copy:
    src: /path/to/largefile
    dest: /remote/path/largefile
```

## 29. **Optimize Playbook for Parallelism**

**Tip**: Increase parallelism by optimizing the number of forks and using efficient inventory groups.

**Example**:
Configure inventory and forks for parallelism:
```ini
[defaults]
forks = 20
```

## 30. **Reduce Network Latency**

**Tip**: Optimize network latency by ensuring fast and reliable network connections between the control node and managed nodes.

**Example**:
Check network latency:
```bash
ping -c 4 managed_node
```
