# Nathan Glikman
# Project 1
# client.py

import socket as mysoc

# Set up client sockets for TS and RS

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
port = 69696
sa_sameas_myaddr = mysoc.gethostbyname(mysoc.gethostname())

# Connect to server on local machine
# TODO: Change to connect to any machine
server_binding = (sa_sameas_myaddr, port)
ts_socket.connect(server_binding)
rs_socket.connect(server_binding)


