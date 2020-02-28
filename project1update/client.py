# Nathan Glikman
# Stephen Scott
# Project 1
# client.py

import threading
import time
import socket as mysoc
import os
import sys

# Set up client sockets for TS and RS
def client():
		if len(sys.argv) != 3:
			print("ERROR: PLEASE INPUT 2 PORTS")

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
			

		port = int(sys.argv[1])
		port2 = int(sys.argv[2])
		sa_sameas_myaddr = mysoc.gethostbyname(mysoc.gethostname())

        # Connect to server on local machine
        # TODO: Change to connect to any machine
		server_binding = (sa_sameas_myaddr, port)
		server_binding2 = (sa_sameas_myaddr, port2)
		ts_socket.connect(server_binding2)
		rs_socket.connect(server_binding)

		inputFile = open(os.path.join(sys.path[0],"PROJI-HNS.txt"),"r")
		if inputFile.mode == 'r':
				inputList = [i.rstrip() for i in inputFile]
				inputString = '_'.join([str(j) for j in inputList])
				query = inputString
				rs_socket.send(query.encode('utf-8'))
				returnQuery = rs_socket.recv(1024).decode('utf-8')
				listData = returnQuery.split('_')
 				outputList = ["NONE"]*len(listData)
				tsList = []
				for i in range(0, len(listData)):
						tempList = listData[i].split(' ')
						if tempList[2] == 'A':
								outputList[i] = listData[i]
						else:
								tsList.append(str(i)+' '+listData[i])
				if len(tsList)>0:
						tsString = '_'.join([str(j) for j in tsList])
						ts_socket.send(tsString.encode('utf-8'))
						returnQuery2 = ts_socket.recv(1024).decode('utf-8')
						returnList = returnQuery2.split('_')
						for i in range(0, len(returnList)):
								tempList = returnList[i].split(' ')
								if tempList[3] == 'Error':
									tempList[3] = 'Error:HOST NOT FOUND'
								outputList[int(tempList[0])] = (tempList[1]+' '+tempList[2]+' '+tempList[3])

				print(outputList)
                
                                        
t1 = threading.Thread(name='client', target=client)
t1.start()
time.sleep(1)

input("Hit ENTER to exit")

exit()


