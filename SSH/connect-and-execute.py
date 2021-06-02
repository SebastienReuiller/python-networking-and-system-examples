#!/usr/bin/env python
# coding: utf8

import paramiko 

SERVER = ''
PORT = '22'
USER = 'root'
KEY_PATH = '~/.ssh/id_rsa.pub'

ssh_cnx = paramiko.SSHClient()

# ajout automatique aux serveurs connus
ssh_cnx.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_cnx.connect(hostname=SERVER, port=PORT, username=USER, key_filename=KEY_PATH)
    
ssh_stdin, ssh_stdout, ssh_stderr = ssh_cnx.exec_command('ls /tmp')
  
print(f"output : {ssh_stdout.read()}")

error = ssh_stderr.read()
print(f"err : {error} ") 
