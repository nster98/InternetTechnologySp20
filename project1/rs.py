# Nathan Glikman
# Project 1
# rs.py

import socket as mysoc

# Set up server socket

try:
	rs = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
	print("RS server created successfully")
except mysoc.error as err:
	print('{} \n'.format("Error creating RS socket", err))

# Bind RS server to port 69696 and enable listening
server_binding = ('', 69696)
rs.bind(server_binding)
rs.listen(1)

# Wait for client to connect
clientid, addr = rs.accept()
