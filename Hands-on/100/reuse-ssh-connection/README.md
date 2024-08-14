# Setting Up SSH Connection Multiplexing for Ansible

## Step-by-Step Instructions

### 1. Install Ansible

Ensure Ansible is installed on your Ubuntu 22.04 controller:

```bash
sudo apt update
sudo apt install ansible
```

### 2. Configure SSH Connection Multiplexing in Ansible

1. **Locate the Ansible Configuration File**:

   The `ansible.cfg` file can be in several places:
   - In your project directory.
   - In your home directory as `.ansible.cfg`.
   - In `/etc/ansible/ansible.cfg` (system-wide configuration).

2. **Edit the Configuration File**:

   Open or create the `ansible.cfg` file using a text editor:

   ```bash
   nano ansible.cfg
   ```

   Add the following configuration under the `[ssh_connection]` section to enable SSH multiplexing:

   ```ini
   [ssh_connection]
   ssh_args = -o ControlMaster=auto -o ControlPersist=60s
   ```

   Save and close the file (Ctrl+X, then Y, then Enter in Nano).

### 3. Create a Multi-Task Playbook for Testing

Create a YAML file named `multi_task_playbook.yml` with multiple tasks to test SSH multiplexing:

```yaml
# multi_task_playbook.yml
- name: Test SSH Multiplexing with Multiple Tasks
  hosts: all
  tasks:
    - name: Check Disk Space
      command: df -h

    - name: Check Memory Usage
      command: free -m

    - name: Check Uptime
      command: uptime
```

### 4. Run the Playbook with Verbose Output

Execute the playbook with verbose output to observe detailed information about the SSH connections:

```bash
ansible-playbook -i inventory multi_task_playbook.yml -vvvv
```

In the output, look for messages indicating the use of the same SSH connection for multiple tasks.

### 5. Check SSH Processes

After running the playbook, verify the SSH processes to confirm multiplexing:

```bash
ps aux | grep ssh
```

Look for a master SSH connection process with `ControlMaster` in its command line.

### 6. Examine ControlPath Files

Check the control socket files in the default path for managing connections:

```bash
ls -l /home/user/.ansible/cp/
```

Presence of control socket files indicates SSH multiplexing is in use.

### 7. Adjust and Test Configuration

Experiment with different `ControlPersist` values or other SSH options as needed. For example:

```ini
[ssh_connection]
ssh_args = -o ControlMaster=auto -o ControlPersist=120s
```

Run your playbook again to see how the changes affect connection behavior.

By following these steps, you should be able to set up and verify SSH connection multiplexing for your Ansible playbooks effectively.
