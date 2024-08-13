# Simple custom dynamic script creation
 - Review and Modify the script as required:
   - https://raw.githubusercontent.com/atingupta2005/Python-Programming-with-Ansible/main/Hands-on/03/simple-dynamic-inventory.py
 - 
 - Download the script
   - wget https://raw.githubusercontent.com/atingupta2005/Python-Programming-with-Ansible/main/Hands-on/03/simple-dynamic-inventory.py
 - Modify the script (If Required)
 - Make it executable
   - sudo chmod a+x simple-dynamic-inventory.py
 
 - Use the script:
   - ansible -i simple-dynamic-inventory.py all --list-hosts
   - ansible -i simple-dynamic-inventory.py all -m ping
   - ansible -i simple-dynamic-inventory.py db -m ping
