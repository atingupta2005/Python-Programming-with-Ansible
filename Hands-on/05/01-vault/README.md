# Ansible Vault
- Allows to encrypt and decrypt files
- Helps to securely store sensitive data, such as passwords, API keys, and other secrets, that you need for Ansible playbooks

## Here are some key aspects of Ansible Vault:

1. **Encryption**: You can encrypt entire files or individual variables within your Ansible playbooks, ensuring that sensitive information is kept secure.

2. **Decryption**: When running playbooks, Ansible Vault will automatically decrypt the necessary files if you provide the correct password or key.

3. **Password Management**: You can use a password file or prompt for a password to encrypt and decrypt vault files. The password should be kept secure.

4. **Integration**: Ansible Vault integrates seamlessly with other Ansible features, allowing encrypted data to be used directly in playbooks and roles.

5. **Command Line Interface**: Ansible Vault provides a command-line interface for creating, editing, and encrypting files. Commands include `ansible-vault create`, `ansible-vault encrypt`, `ansible-vault decrypt`, and more.

Here’s a basic example of how to use Ansible Vault:

- **Encrypt a file**: `ansible-vault encrypt secrets.yml`
- **Decrypt a file**: `ansible-vault decrypt secrets.yml`
- **Edit an encrypted file**: `ansible-vault edit secrets.yml`
- **Run a playbook with encrypted variables**: `ansible-playbook playbook.yml --ask-vault-pass`

By using Ansible Vault, you ensure that sensitive information remains protected while still allowing automation and configuration management to proceed securely.


# Example: Installing and Configuring Nginx with an API Key Using Ansible Vault

## Scenario

You need to install the `nginx` web server and configure it with an API key that is used for a third-party service integration. This API key must be securely managed using Ansible Vault.

## 1. Encrypting the API Key

### Step 1: Create an Encrypted File

Create a file named `nginx_secrets.yml` to store your API key. Encrypt this file using Ansible Vault:

```sh
ansible-vault create nginx_secrets.yml
```

- You will be prompted to enter a password for encrypting the file. Once inside the editor, add your API key:
```
# nginx_secrets.yml
api_key: "your_secret_api_key_here"
```


- Save and close the editor. The nginx_secrets.yml file is now encrypted.

## 2. Creating a Playbook
### Step 2: Create a Playbook
- Create a playbook file named setup_nginx.yml. This playbook will install nginx, configure it using the API key, and then start the service.

```
- name: Install and Configure Nginx with API Key
  hosts: webservers
  vars_files:
    - nginx_secrets.yml
  tasks:
    - name: Ensure Nginx is installed
      apt:
        name: nginx
        state: present

    - name: Configure Nginx with API key
      template:
        src: nginx_config.j2
        dest: /etc/nginx/nginx.conf
      vars:
        api_key: "{{ api_key }}"

    - name: Start Nginx service
      service:
        name: nginx
        state: started
```

## Step 3: Create a Template
- Create a Jinja2 template named nginx_config.j2 to be used by the template module. This file will be rendered with the sensitive data.
```
# nginx_config.j2
user www-data;
worker_processes auto;
pid /run/nginx.pid;

events {
    worker_connections 1024;
}

http {
    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    # Configure third-party service using the API key
    set $api_key "{{ api_key }}";

    server {
        listen 80;
        server_name localhost;

        location / {
            root /var/www/html;
            index index.html index.htm;
        }
    }
}
```

## 3. Running the Playbook
- To run the playbook and decrypt the nginx_secrets.yml file, provide the Vault password:
### Option 1: Prompt for Password
```
ansible-playbook setup_nginx.yml --ask-vault-pass
```

### Option 2: Use a Password File
- Create a file named vault_password.txt and store your Vault password in it. Make sure this file is secure:
ansible-playbook setup_nginx.yml --vault-password-file vault_password.txt


## 4. Updating Encrypted Data
- If you need to update the API key, use:
```
ansible-vault edit nginx_secrets.yml
```

- This will open the file in your default editor, allowing you to make changes securely.

## 5. Decrypting Data
- To decrypt the file and view it in plaintext:
```
ansible-vault decrypt nginx_secrets.yml
```

- Be cautious with decrypted files as they are not encrypted until you re-encrypt them.

## Summary
 - Encrypt Data: Use ansible-vault create to create and encrypt a file containing sensitive data like API keys.
- Use in Playbooks: Include the encrypted file in your playbook using vars_files and reference the variables.
- Run Playbooks: Provide the Vault password using --ask-vault-pass or --vault-password-file.
- Update Data: Use ansible-vault edit to modify the encrypted file.
- Decrypt Data: Use ansible-vault decrypt to view or edit encrypted files in plaintext.

This example demonstrates how to securely manage and use sensitive API keys during the installation and configuration of a software package with Ansible.