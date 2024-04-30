## Atomicity and Deadlock Issues in Existing Code

While testing the werewolves code, we identified an interesting issue with parallel communication. If two or more users send messages at the same time during chatting (discussion) between townspeople, it becomes more than likely that not all the messages are delivered.

Using the script `parallel_conversation.sh` we are trying to identify whether werewolves can handle multiple texts being sent simultaneously. As it is evident from the following image, each box clearly misses a text from a player.

![parallel conversation impeded](https://github.com/BiprarshiD/AOS-backup/assets/46216520/a630c5fd-bff7-475b-b9d9-5a7e8fec6fe1)


## Goals for this Project
1. Solve the atomicity and deadlock issues as described above.
2. Use POSIX_IPC Message Queues to implement the communication layer in the Werewolves game. Instead of named pipes, our code uses Message Passing using POSIX IPC Message Queues to communicate between players and the moderator.


The game has been tested and verified with 4 players. [ player0, player1, player2, player ]


## SETUP POSIX IPC Message Queues in Kernel

To setup posix_ipc we have to do the following setup:

STEP1:  run sudo bash install.sh after extracting the tarball [ image below ]


![step1](https://github.com/BiprarshiD/AOS-backup/assets/46216520/04116fc4-f615-431c-b3b5-60050a1bf7ea)


STEP2 : Run the setup.py scripts as the root user [ image below]

![step2](https://github.com/BiprarshiD/AOS-backup/assets/46216520/cc2bc066-7f9b-45f7-8ac8-b2f591becb81)

As shown in the image above, run the following commands as root user.
The following commands have to be run as the root user to SETUP the kernel with POSIX Message queues
Run the following from the werewolves directory(main)
```bash
sudo su
python3 setup.py
```


## DIRECTORY STRUCTURE

The file layout is as follows:

moderator user directory contains:

```
server.py
communication_server.py
```
![moderatordir](https://github.com/BiprarshiD/AOS-backup/assets/46216520/3dfd353c-ffd5-488a-ab19-053c8a8b924f)


player0 user directory contains:
```
client.py
communicationclient.py
```

player1 user directory contains:
```
client.py
communicationclient1.py
```

player2 user directory contains:
```
client.py
communicationclient2.py
```

player3 user directory contains:
```
client.py
communicationclient3.py
```
![playersdir](https://github.com/BiprarshiD/AOS-backup/assets/46216520/e8a542db-c821-4e53-8a60-a862af1602c6)



The communication script will be different across players and the moderator. No change has been made to the client.py and server.py. The communication between
players and the moderator to do voting, chatting and connection are made through POSIC IPC Message Queues using Message Passing.


## Scripts to run from moderator and players

PLAY THE GAME!

Scripts to run from moderator:
`python3 server.py`

Scripts to run from players:
`python3 client.py`

## GAMEPLAY SCREENSHOTS

![gameplayscreenshot1](https://github.com/BiprarshiD/AOS-backup/assets/46216520/826edbf6-beda-4bb3-812e-68119cc4868e)


![gameplayscreenshot2](https://github.com/BiprarshiD/AOS-backup/assets/46216520/c0284d8e-90f5-4327-9f6c-b48f9a145d43)


![gameplayscreenshot3](https://github.com/BiprarshiD/AOS-backup/assets/46216520/e794633f-1ba5-492e-9455-a463734c7576)


## Python2 to Python3 Porting

Ported the Code from python2 to python3
Used Python3 to run werewolves. Converted all python2 statements to python3 like print ---> print(), exception ---> exception() and raw_input()--->input()
Also, in Python2, dict.keys() is not subscriptable. so changed those statements in server.py and client.py to list(dict.keys()). This change made the keys arrays of the dictionary into a list.
