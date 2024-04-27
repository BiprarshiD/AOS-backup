import posix_ipc
import os
import getpass
import subprocess
import sys

def setup_mqueue_directory():
    if not os.path.isdir("/dev/mqueue"):
        os.makedirs("/dev/mqueue")
        subprocess.run(["sudo", "mount", "-t", "mqueue", "none", "/dev/mqueue"], check=True)

setup_mqueue_directory()

def create_mq(name, permissions):
    try:
        mq = posix_ipc.MessageQueue(name, posix_ipc.O_CREAT, mode=permissions)

    except Exception as e:
        print(f"{e}", file=sys.stderr)


current_user = getpass.getuser()
if current_user == "moderator":
    for i in range(4):
        create_mq(f"/message_queue_server_p{i}", 0o777)
else:
    create_mq(f"/message_queue_{current_user}", 0o664)

print("Message queues created successfully.")