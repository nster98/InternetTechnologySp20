# Nathan Glikman
# Project 1
# ts.py

import socket as mysoc

# Set up DNS Table

fd = open("PROJ1-DNSTS.txt", "r")

num_lines = sum(1 for line in open('PROJ1-DNSTS.txt'))
dnsTable = [dict(hostname = "", ip = "", flag = "") for x in range(num_lines)]

# TODO: Possible error with the \n being written into the dictionary

for i in range(num_lines):
	string = fd.readline()
	data = string.split(' ')
	dnsTable[i] = dict(hostname = data[0], ip = data[1], flag = data[2])

print(dnsTable)

# Set up server socket

try:
	ts = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
	print("TS server created successfully")
except mysoc.error as err:
	print('{} \n'.format("Error creating TS socket", err))

# Bind RS server to port 69696 and enable listening
server_binding = ('', 50007)
ts.bind(server_binding)
ts.listen(1)

# Wait for client to connect
clientid, addr = ts.accept()


