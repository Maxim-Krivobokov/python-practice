# Example from slurm repo

# Signal module allows to work with Linux signals, like SIGTERM, SIGKILL
import signal
import subprocess


def main():
    # subprocess.check_call(["ls", "-l", "-a"])
    # # subprocess.check_call(["ls", "lll"]) # Will fail the script

    # ec = subprocess.call(["ls", "-l", "-a"], stdout=subprocess.DEVNULL) # Call process without checking the result, only saving exit code.
    # # stdout to devnull will just mute the output
    # print(ec) # exit code 0
    # ec = subprocess.call(["ls", "lll"], stdout=subprocess.DEVNULL)
    # print(ec) # exit code 2

    # output = subprocess.check_output(["ls", "-l", "-a"])
    # print(output.decode())


    # # Give an input to the subprocess
    # # Input must be encoded, to convert string to the bytes object
    # output = subprocess.check_output(["sed", "-e", "s/only golang/python/"],
    #                                   input="You can write k8s operator using only golang".encode())
    # print(output.decode())


    process = subprocess.Popen(["bash", "echo_server.sh"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # Poll returns status of a process. None if process is still running. 
    print(process.poll())
    # process.terminate() # terminate process
    # process.kill()      # kill process
    # process.send_signal(signal.Signals.SIGINT) # Send exact signal to process
    stdout, _ = process.communicate(input=b"one\ntwo\nthree\nfour")  # Transfer stdin to the process. Echo-server will return 4 strings. 
    print(stdout.decode()) # Print stdout
    try:
        print(process.decode())
    except AttributeError as e:
        print('Popen object issue')
        print(e)
    print(process.returncode)

    # If process would not finish in 3 sec, we will have subprocess.TimeoutException
    process.wait(timeout=3)


if __name__ == '__main__':
    main()
