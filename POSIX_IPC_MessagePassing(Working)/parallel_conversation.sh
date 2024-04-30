#!/bin/bash

# Run this during the discussion session

# Name of the tmux session
SESSION="GameSession"

# Pane indices for the players
PANE_PLAYER0=0  
PANE_PLAYER1=1
PANE_PLAYER2=2
PANE_PLAYER3=3

# Messages to send
MESSAGE_PLAYER0="This is player 0"
MESSAGE_PLAYER1="This is player 1"
MESSAGE_PLAYER2="This is player 2"
MESSAGE_PLAYER3="This is player 3"

# Send message to Player 0
tmux send-keys -t $SESSION:0.$PANE_PLAYER0 "$MESSAGE_PLAYER0" C-m &

# Send message to Player 1
tmux send-keys -t $SESSION:0.$PANE_PLAYER1 "$MESSAGE_PLAYER1" C-m &

# Send message to Player 2
tmux send-keys -t $SESSION:0.$PANE_PLAYER2 "$MESSAGE_PLAYER2" C-m &

# Send message to Player 3
tmux send-keys -t $SESSION:0.$PANE_PLAYER3 "$MESSAGE_PLAYER3" C-m &

wait

echo "Messages sent simultaneously."