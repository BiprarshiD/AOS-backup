import subprocess

def run_command(command):
    """
    Run a command as a subprocess and handle the output and errors.
    """
    try:
        print(f"Executing: {command}")
        result = subprocess.run(command, check=True, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Output:\n", result.stdout)
        if result.stderr:
            print("Errors:\n", result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing: {command}\nError: {e}")

def main():
    # Install posix_ipc module
    run_command('pip3 install posix_ipc')

    # Make directory /dev/mqueue
    run_command('mkdir /dev/mqueue')

    # Mount mqueue
    run_command('mount -t mqueue none /dev/mqueue')

    # Execute Python script to create queues
    run_command('python3 create_queues.py')

    # List contents of /dev/mqueue
    run_command('ls /dev/mqueue')

    # Change directory to /dev/mqueue and change permissions
    # These two steps are combined as changing the directory is not persistent across subprocess calls
    run_command('cd /dev/mqueue && chmod 777 message_queue*')

if __name__ == "__main__":
    main()
