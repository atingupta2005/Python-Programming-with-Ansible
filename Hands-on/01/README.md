# Installation:
 - sudo apt update
 - git clone https://github.com/atingupta2005/Python-Programming-with-Ansible.git
 - cd Python-Programming-with-Ansible
 - sudo apt -y install software-properties-common
 - sudo apt-add-repository ppa:ansible/ansible
 - sudo apt update
 - sudo apt install ansible

# Install specific Python version
## Install using virtualenv
```
sudo apt-get install python3.8
pip install virtualenv
virtualenv -p /usr/bin/python3.8 my_env
source my_env/bin/activate
deactivate
```

## Install using pyenv
```
pyenv install 3.9.0
pyenv virtualenv 3.9.0 myenv
pyenv activate myenv
pyenv deactivate
```

# ssh-keygen
 - ssh-keygen -f ~/.ssh/demo_id_rsa
 - chmod 0600 ~/.ssh/demo_id_rsa

# Update Hosts:
 - vim hosts

# Update SSH Key File Path:
 - vim hosts

# Validate and obtain information about your Ansible inventory
 - ansible-inventory -i hosts --list

# Deploy Public Key to host
 - ssh-copy-id -i ~/.ssh/demo_id_rsa.pub demouser@52.152.231.15
 - ssh-copy-id -i ~/.ssh/demo_id_rsa.pub demouser@52.150.11.244

# Test the key
 - ssh -i ~/.ssh/demo_id_rsa demouser@52.152.231.15
   - exit
 - ssh -i ~/.ssh/demo_id_rsa demouser@52.150.11.244
   - exit

# Test Ansible is able to conenct to all hosts
 - ansible all -i hosts -m ping

# Running ad hoc commands
- ansible all -i hosts -a uptime
- ansible all -i hosts -a "free -m"
- ansible all -i hosts -a "df -h"

# Running Playbook
- vim first_playbook.yml
- ansible-playbook -i hosts first_playbook.yml

# Confirm content of the file in all hosts
- ansible all -i hosts -a "cat /tmp/testfile.txt"
