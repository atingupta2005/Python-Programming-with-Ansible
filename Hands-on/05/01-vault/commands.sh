# Create a file called vault.yml to store database credentials:

# Add the following content:

db_user: "admin"
db_password: "secure_password"


# Use the following command to run the playbook, prompting for the vault password:
ansible-playbook deploy_web_server.yml --ask-vault-pass


# Or use a vault password file for automation:
ansible-playbook deploy_web_server.yml --vault-password-file ~/.vault_pass.txt
