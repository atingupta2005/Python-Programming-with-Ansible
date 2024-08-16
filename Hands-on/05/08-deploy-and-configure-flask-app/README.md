ansible-playbook deploy_flask_app.yml -e "env=development server_name=dev.example.com"
ansible-playbook deploy_flask_app.yml -e "env=staging server_name=staging.example.com"
ansible-playbook deploy_flask_app.yml -e "env=production server_name=prod.example.com"
