import paramiko

key = paramiko.RSAKey.from_private_key_file("C:\\Users\\m_krivobokov\\.ssh\\id_rsa", password="Gazprom09")

def main():
    with paramiko.SSHClient() as ssh_client:
        ssh_client.load_system_host_keys()
        # ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.set_missing_host_key_policy(paramiko.WarningPolicy())
        # Connect with login-password
        #ssh_client.connect(hostname="localhost", port=2222, username="service_user", password="q1w2e3")
        # Connect with a SSH key
        ssh_client.connect(hostname="localhost", port=2222, username="service_user", pkey=key)
        # Execute commands on remote host
        stdin, stdout, stderr = ssh_client.exec_command("task_generator 0")
        stdin.write("Hello world!\n")
        stdin.flush() # That will work with scripts that waits for an input
        print(stdout.read().decode("utf-8"))   # read all data; may case hang if exec is interactive script and wait for input OR must wait Ctrl-C
        print(stderr.read())
        # print(stdout.read(18).decode("utf-8")) # read 18 bytes, and thats it. Will hang if stdout has < 18 bytes
        #print(stdout.readline())   # read just one line
        #print(stdout.readlines())  # read all lines, and puts them into array
        # ssh_client.invoke_shell()



def use_sftp():
    with paramiko.SSHClient() as ssh_client:
        ssh_client.load_system_host_keys()
        ssh_client.connect(hostname="localhost", port=2222, username="service_user", pkey=key)
        # SCP from remote host to local folder
        with ssh_client.open_sftp() as sftp_client:
            sftp_client.get(remotepath="/usr/bin/task_generator", localpath="./remote_task_generator")

        # SCP from local to remote, with try-except
        with ssh_client.open_sftp() as sftp_client:
            try:
                sftp_client.put(remotepath="/root/docker.yml", localpath="./docker-compose.yml") # May cause an error
            except PermissionError:
                print('Permission Error: Using reserve filepath')
                sftp_client.put(remotepath="/tmp/docker.yml", localpath="./docker-compose.yml")


def work_with_remote():
    with paramiko.SSHClient() as ssh_client:
        ssh_client.load_system_host_keys()
        ssh_client.connect(hostname="localhost", port=2222, username="service_user", pkey=key)
        # Read remote file and write to stdout
        with ssh_client.open_sftp() as sftp_client:
            with sftp_client.open("/tmp/docker.yml", "r") as yaml_file:
                # print(yaml_file.read().decode("utf-8")) # Too long output
                print("file was read")

            # Rename file
            #sftp_client.rename(oldpath="/tmp/docker.yml", newpath="/tmp/docker-compose-new.yml")

            # truncate file to decrease its size
            #sftp_client.truncate(path="/tmp/docker.yml", size=40)

            # roaming in remote's filesystem
            print(sftp_client.getcwd())
            sftp_client.chdir("/tmp")
            print(sftp_client.getcwd())

            # Changing file permissions and owner
            sftp_client.chmod("docker.yml", 0o0755)
            sftp_client.chown('docker.yml', 0, 0)





if __name__ == '__main__':
    #main()
    use_sftp()
    work_with_remote()