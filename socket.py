# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 11:44:58 2020

@author: alok1
"""
'''
#Create server
import socket

s = socket.socket()     #need to pass ip add and n/w type; default ip4 and tcp
print('Socket created')

s.bind (('192.168.1.100',9999))               #pass ip add and port number and port number range from 0 to 65535, dont use in ths bcoz busy
s.listen(3)
print('waiting for connections')

while True:
   c, addr = s.accept( )         #it will give client socket and address
   name = c.recv(1024).decode()
   print("Connected with ", addr,name)
   c.send(bytes('Welcome to alok1'),'utf-8')
'''
#Client created which communicates to DC4Server.java

import sys
import socket
#IP=input("Enter the IP Address: ") #Host name or IP address any of the one ok.
#Port=input(print("Enter the port number: "))

c = socket.socket()
c.connect((sys.argv[2],sys.argv[1]))       #here at the localhost we need to mention the ip address of the server, ipconfig in command prompt to know ip address
name = input("Enter your name: ")
c.send(bytes(name,'utf-8'))     #send data to server
print(c.recv(1024).decode())      #send in buffer and decode so print in string format


#During connection, we can see IP adress and port number of server