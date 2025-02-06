# How to write ansible module

Module != Plugin!
Module runs on remote host, plugin is executed on ansible host

## When should we write our own module?
- When module with similar functions does not exist
- If This module is in development, and PR is not created yet (maybe release would be after 100500 yrs)
- If your task cannot/should not be done by plugin
- If your task should not be done by role
- If your task should not be done by few modules

## Useful links:
https://docs.ansible.com/ansible/latest/dev_guide/developing_modules_general.html
https://medium.com/@deepeshjaiswal6734/how-to-create-custom-ansible-module-a-step-by-step-guide-56860ec671e9

## How doest module interact with ansible?
 - he recieves data in JSON format
 - he gives an output also in JSON 

## How to create a module:
0. prepare environment (vierualenv with certain specific packages)
1. clone ansible repo
2. Add your file "mymodule.py" to folder "library", or _"lib/ansible/modules/"_
3. Write module using a template in docs.ansible.com tutorial

## Key Features:
  - Our script "mymodule.py" uses class ansible.module_utils.basic.AnsibleModule
  - Works with arguments (dict), returns some json output to ansible
  - Uses own libs and functions to execute some actions, for example - boto3 to manipulate AWS, or ClickHouse client to create/delete users

### Notes
Useful module 
contextlib , method suppress - suppress certain errors, instead of try-except;

