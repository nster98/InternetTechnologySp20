# Nathan Glikman
# Project 1
# rs.py

import socket as mysoc

# Set up DNS Table

fd = open("PROJ1-DNSRS.txt", "r")

num_lines = sum(1 for line in open('PROJ1-DNSRS.txt'))
dnsTable = [dict(hostname = "", ip = "", flag = "") for x in range(num_lines)]

# TODO: Possible error with the \n being written into the dictionary

for i in range(num_lines):
	string = fd.readline()
	data = string.split(' ')
	dnsTable[i] = dict(hostname = data[0], ip = data[1], flag = data[2])

# print(dnsTable)

# Set up server socket

try:
	rs = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
	print("RS server created successfully")
except mysoc.error as err:
	print('{} \n'.format("Error creating RS socket", err))

# Bind RS server to port 69696 and enable listening
server_binding = ('', 50006)
rs.bind(server_binding)
rs.listen(1)

# Wait for client to connect
clientid, addr = rs.accept()

while True:

	clientQuery = rs.recv(1024).decode('utf-8')
	
	# Check against table to see what we got
	# TODO: Make sure its sending correctly when there is an error and cant find any server, or just the TS server 
	for i in range(num_lines):
		if clientQuery == dnsTable[i]["hostname"]:
			returnString = dnsTable[i]["hostname"] + " " + dnsTable[i]["ip"] + " " + dnsTable[i]["flag"]
		
	rs.send(returnString.encode('utf-8'))
