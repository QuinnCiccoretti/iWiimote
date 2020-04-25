from instructions import startInstructionServer
from controller import startControllerServer

import os
import multiprocessing
import socket

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('10.255.255.255', 1))
    # hostname = socket.gethostname()    
    hostname =  s.getsockname()[0]
    s.close()
    IP = socket.gethostbyname(hostname)
    print("Your IP Address is: " + IP)

    server_details = [(startInstructionServer,IP), (startControllerServer,IP)]
    # Run servers
    servers = []
    for s in server_details: 
        p = multiprocessing.Process(
            target=s[0],
            args=[s[1]]
            )
        servers.append(p)  

    for server in servers:
        server.start()

    for server in servers:
        server.join()
