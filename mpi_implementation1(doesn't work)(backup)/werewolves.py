from mpi4py import MPI
import server as s
import client as c
from threading import Thread



def play():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    clientThread = Thread(target=c.listen,args=[])
    clientThread.daemon = True
    serverThread = Thread(target=s.main,args=[])
    serverThread.daemon = True
    if(rank==0):
        print('Hello from ' + str(rank))
        serverThread.start()
    elif(rank==1):
        print('Hello from '  + str(rank))
        clientThread.start()
    while(serverThread.is_alive()==True or clientThread.is_alive()==True):
        pass    
        


if __name__ == "__main__":
    play()
