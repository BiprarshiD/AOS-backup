## Issue Identified

While testing the werewolves code, we identified an interesting issue with parallel communication. If two or more users send messages at the same time, it becomes more than likely that not all the messages are delivered.

Using the script `parallel_conversation.sh` we are trying to identify whether werewolves can handle multiple texts being sent simulatenously. As it is evident from the following image , each box clearly misses a text from a player.

![parallel conversation impeded](https://github.com/BiprarshiD/AOS-backup/assets/46216520/a630c5fd-bff7-475b-b9d9-5a7e8fec6fe1)


So our goal for using `posix_ipc` is to solve this atomicity and deadlock issues that arises.

The game has been tested and verified with 4 players.

## DIRECTORY STRUCTURE

The file layout is as follows:

moderator user directory contains:

```
server.py
communication_server.py
```

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

The communication script will be different across players and the moderator. No change has been made to the client.py and server.py. The communication between
players and the moderator to do voting, chatting and connection are made through POSIC IPC Message Queues using Message Passing.

## SETUP POSIX IPC Message Queues in Kernel

To setup posix_ipc we have to do the following setup:
```bash
sudo su
./create_queues.sh
```
create_queues.sh file will generate all the necessary message queues

## Scripts to run from moderator and players

Scripts to run from moderator:
`python3 server.py`

Scripts to run from players:
`python3 client.py`

>Note: [change the import header for communicationclient.py in each client.py(`line 27`) file according to the player]

```
Player0: import communicationclient
```
```
Player1 : import communicationclient1
```
```
Player2 : import communicationclient2
```
```
Player3 : import communicationclient3
```

## Python2 to Python3 Porting

Ported the Code from python2 to python3
Used Python3 to run werewolves. Converted all python2 statements to python3 like print ---> print(), exception ---> exception() and raw_input()--->input()
Also, In python2, dict.keys() is not subscriptable. so changed those statements in server.py and client.py to list(dict.keys()). This change made the keys arrays of the dictionary into a list.
