#!/bin/bash

read -s -p "Enter Password: " PASSWORD
echo ""

# Attempt to kill the existing tmux session named "GameSession" if it exists
tmux kill-session -t GameSession 2>/dev/null

# Start a new tmux session
tmux new-session -d -s GameSession

# Change to the /home directory
tmux send-keys -t GameSession "cd /home" C-m

# List of player directories
players=("player0" "player1" "player2" "player3")

# First player setup in the first window
tmux send-keys -t GameSession "cd ${players[0]}" C-m
tmux send-keys -t GameSession "clear" C-m
tmux send-keys -t GameSession "sudo su - ${players[0]}" C-m
tmux send-keys -t GameSession "$PASSWORD" C-m
sleep 3
tmux send-keys -t GameSession "export PS1='\[\e[0;31m\]\u@\h:\w\$ \[\e[m\]'" C-m  # Red prompt
tmux send-keys -t GameSession "python2 client.py" C-m

# Delay to ensure commands have time to be processed before splitting
sleep 1

# Setup other players in split panes
colors=('\[\e[0;32m\]' '\[\e[0;36m\]' '\[\e[0;33m\]')  # Green, Blue, Yellow
index=0
for i in "${players[@]:1}"; do
    tmux split-window -h
    tmux send-keys "cd /home/$i" C-m
    tmux send-keys "clear" C-m
    tmux send-keys "sudo su - $i" C-m
    tmux send-keys "$PASSWORD" C-m
    sleep 3
    tmux send-keys "export PS1='${colors[$index]}\u@\h:\w\$ \[\e[m\]'" C-m  # Apply different colors
    tmux send-keys "python2 client.py" C-m
    tmux select-layout even-horizontal
    index=$((index + 1))
done

# Normalize pane sizes
tmux select-layout tiled

# Attach to the session
tmux attach -t GameSession
