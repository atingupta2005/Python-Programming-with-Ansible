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