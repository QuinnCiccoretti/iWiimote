from instructions import startInstructionServer
from controller import startControllerServer

import os
import multiprocessing

if __name__ == '__main__':
    server_details = [startInstructionServer, startControllerServer]

    # Run servers
    servers = []
    for s in server_details: 
        p = multiprocessing.Process(
            target=s
            )
        servers.append(p)  

    for server in servers:
        server.start()

    for server in servers:
        server.join()
