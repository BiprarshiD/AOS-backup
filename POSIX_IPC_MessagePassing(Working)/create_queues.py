import posix_ipc

mq_name0 = "/message_queue_server_p0"
mq0 = posix_ipc.MessageQueue(mq_name0, posix_ipc.O_CREAT, mode=0o666)

mq_name1 = "/message_queue_server_p1"
mq1 = posix_ipc.MessageQueue(mq_name1, posix_ipc.O_CREAT, mode=0o666)

mq_name2 = "/message_queue_server_p2"
mq2 = posix_ipc.MessageQueue(mq_name2, posix_ipc.O_CREAT, mode=0o666)

mq_name3 = "/message_queue_server_p3"
mq3 = posix_ipc.MessageQueue(mq_name3, posix_ipc.O_CREAT, mode=0o666)

mq_name = "/message_queue_player0"
mq = posix_ipc.MessageQueue(mq_name, posix_ipc.O_CREAT,mode=0o666)


mq_name = "/message_queue_player1"
mq = posix_ipc.MessageQueue(mq_name, posix_ipc.O_CREAT,mode=0o666)

mq_name = "/message_queue_player2"
mq = posix_ipc.MessageQueue(mq_name, posix_ipc.O_CREAT,mode=0o666)


mq_name = "/message_queue_player3"
mq = posix_ipc.MessageQueue(mq_name, posix_ipc.O_CREAT,mode=0o666)
