# Ansible Lint

`ansible-lint` is a tool for analyzing Ansible playbooks and roles to ensure they adhere to best practices and guidelines. It comes with a set of predefined rules to catch common issues. Here's a detailed example of how to use `ansible-lint` with predefined rules, including installation, configuration, and execution steps.

### 1. **Install `ansible-lint`**

First, you need to install `ansible-lint`. You can do this using `pip`:

```bash
python3 -m venv venv
source venv/bin/activate
pip install ansible
pip install ansible-lint
```

### 2. **Create a Sample Ansible Playbook**

For demonstration purposes, create a sample Ansible playbook and role. 

#### Example Playbook (`playbook.yml`):

```yaml
- name: Deploy Sample Application
  hosts: all
  become: yes
  vars:
    app_name: "myapp"
    app_port: 8080
  tasks:
    - name: Install Apache
      package:
        name: httpd
        state: present

    - name: Ensure the application directory exists
      file:
        path: "/var/www/{{ app_name }}"
        state: directory

    - name: Deploy application files
      copy:
        src: "{{ app_name }}/"
        dest: "/var/www/{{ app_name }}/"
```

### 3. **Create an `.ansible-lint` Configuration File**

You can customize `ansible-lint` rules by creating a `.ansible-lint` configuration file. This file allows you to specify which rules to enable or disable.

#### Example Configuration File (`.ansible-lint.yml`):

```yaml
# .ansible-lint.yml
rules:
  no_duplicate_tasks:
    enabled: true
  no_tabs:
    enabled: true
  syntax:
    enabled: true
```

Alternatively, you can use `ansible-lint`'s default configuration and specify any additional rules or overrides directly via command-line options.

### 4. **Run `ansible-lint`**

You can run `ansible-lint` on your playbook or role directory to check for issues based on the predefined rules and your configuration.

#### Example Command to Lint a Playbook:

```bash
ansible-lint playbook.yml
```

### Summary

Using `ansible-lint` with predefined rules helps you enforce best practices and maintain quality in your Ansible playbooks and roles. By installing `ansible-lint`, configuring rules via `.ansible-lint` or `.ansible-lint.yml`, and running the tool, you can identify and resolve issues in your Ansible configurations.

