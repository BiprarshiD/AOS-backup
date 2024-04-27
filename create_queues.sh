#!/bin/bash

sudo -u moderator pip install posix_ipc
sudo -u moderator python create_queue.py

for i in {0..3}
do
    sudo -u player$i pip install posix_ipc
    sudo -u player$i python create_queue.py
done

cd /dev/mqueue
chmod 777 message_queue_server_p*