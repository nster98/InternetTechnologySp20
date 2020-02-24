# Nathan Glikman
# Project 1
# ts.py

import socket as mysoc

# Set up server socket

try:
	ts = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
	print("TS server created successfully")
except mysoc.error as err:
	print('{} \n'.format("Error creating TS socket", err))

# Bind RS server to port 69696 and enable listening
server_binding = ('', 69696)
ts.bind(server_binding)
ts.listen(1)

# Wait for client to connect
clientid, addr = ts.accept()
