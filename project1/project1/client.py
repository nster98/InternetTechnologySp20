# Nathan Glikman
# Project 1
# client.py

import threading
import time
import socket as mysoc

# Set up client sockets for TS and RS
def client():
        try:
                ts_socket = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
                print("DEBUG: Client ts socket created\n")
        except mysoc.error as err:
                print('{} \n'.format("Client ts socket open error", err))
	
        try:
                rs_socket = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
                print("DEBUG: Client rs socket created\n")
        except mysoc.error as err:
                print('{} \n'.format("Client rs socket open error", err))

        # Define port for the server
        # TODO: Change to take user input for both
        port = 50007
        port2 = 50006
        sa_sameas_myaddr = mysoc.gethostbyname(mysoc.gethostname())

        # Connect to server on local machine
        # TODO: Change to connect to any machine
        server_binding = (sa_sameas_myaddr, port)
        server_binding2 = (sa_sameas_myaddr, port2)
        ts_socket.connect(server_binding2)
        rs_socket.connect(server_binding)

        query = "localhost"
        rs_socket.send(query.encode('utf-8'))
        returnQuery = rs_socket.recv(1024).decode('utf-8')
        listData = returnQuery.split(' ')
        if listData[2] == 'A':
                print(returnQuery)
        # TODO: Fix message sending to TS server
        elif listData[2] == 'NS':
                ts_socket.send(query.encode('utf-8'))
                returnQuery = ts_socket.recv(1024).decode('utf-8')
                print(returnQuery)
                
                                        
t1 = threading.Thread(name='client', target=client)
t1.start()
time.sleep(1)

input("Hit ENTER to exit")

exit()


