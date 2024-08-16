### Ansible Console

**Ansible Console** is an interactive tool that allows you to run ad-hoc Ansible commands and explore your Ansible environment interactively. It's especially useful for debugging and running quick commands without writing playbooks.

#### **Getting Started**

To use `ansible-console`, you need to have Ansible installed on your system. If Ansible is not already installed, you can install it using pip:

```bash
pip install ansible
```

#### **Launching Ansible Console**

To start the Ansible console, use the following command:

```bash
ansible-console
```

This will open an interactive console where you can enter Ansible commands and interact with your inventory.

#### **Basic Commands and Usage**

Once inside the console, you can use various commands to interact with your Ansible environment. Here are some basic commands:

1. **Run Ad-Hoc Commands**

   You can run ad-hoc commands using the `run` command followed by the module name and arguments. For example, to check the uptime of your hosts, you can use:

   ```bash
   ansible-console> run shell uptime
   ```

2. **Access Variables**

   You can access variables from your inventory or playbooks using the `vars` command. For example:

   ```bash
   ansible-console> vars
   ```

3. **Check Inventory**

   To list the hosts and groups in your inventory, use:

   ```bash
   ansible-console> inventory
   ```

4. **Run Playbooks**

   You can run playbooks directly from the console using the `playbook` command:

   ```bash
   ansible-console> playbook playbook.yml
   ```

5. **View Host Facts**

   To view facts about a particular host, use:

   ```bash
   ansible-console> facts [hostname]
   ```

6. **Use Modules**

   You can use Ansible modules interactively. For example, to check disk space on a host, you can use:

   ```bash
   ansible-console> run command df -h
   ```

7. **Exit Console**

   To exit the Ansible console, simply type `exit` or press `Ctrl+D`.

#### **Example Usage**

Here’s an example session using `ansible-console`:

```bash
$ ansible-console
ansible-console> run ping
ansible-console> inventory
ansible-console> vars
ansible-console> facts [hostname]
ansible-console> playbook playbook.yml
ansible-console> exit
```

