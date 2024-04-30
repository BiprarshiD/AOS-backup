import subprocess
import os

def update_import_line(file_path, old_line, new_line):
    """
    Update the specified line in a Python file.
    """
    # Read the original contents
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Modify the line
    with open(file_path, 'w') as file:
        for line in lines:
            if line.strip() == old_line:
                file.write(new_line + '\n')
            else:
                file.write(line)


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

    file_path = os.path.join('/home/player1/', 'client.py')
    old_import_line = 'import communicationclient as c'
    new_import_line = 'import communicationclient1 as c'
    update_import_line(file_path, old_import_line, new_import_line)

    file_path = os.path.join('/home/player2/', 'client.py')
    old_import_line = 'import communicationclient as c'
    new_import_line = 'import communicationclient2 as c'
    update_import_line(file_path, old_import_line, new_import_line)

    file_path = os.path.join('/home/player3/', 'client.py')
    old_import_line = 'import communicationclient as c'
    new_import_line = 'import communicationclient3 as c'
    update_import_line(file_path, old_import_line, new_import_line)

    run_command('cp communicationclient.py /home/player0/')
    run_command('cp communicationclient1.py /home/player1/')
    run_command('cp communicationclient2.py /home/player2/')
    run_command('cp communicationclient3.py /home/player3/')



if __name__ == "__main__":
    main()
