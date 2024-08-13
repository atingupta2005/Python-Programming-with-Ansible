# Executing Ansible tasks with default and different users on Managed Nodes
   - ansible ip_of_vm -i hostfile_name -m ping
     - It will work using default user
   - ansible ip_of_vm -i hostfile_name -m ping -u user1
     - It will work using user specified