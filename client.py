import socket
from struct import *
import binascii
import time
import threading


info =pack('>7sc', b'LTEInfo', b'\x00')
reset =pack('>8sc', b'CPLReset', b'\x00')
reqinfo =pack('>7sc', b'ReqInfo', b'\x00')

print(info)
print(binascii.hexlify(info))
print(reset)
print(binascii.hexlify(reset))
print(reqinfo)
print(binascii.hexlify(reqinfo))

msgFromClient = 'Hello UDP Server'
bytesToSend = str.encode(msgFromClient)
serverAddressPort = ('10.10.10.254', 8901)
bufferSize = 1024

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
#UDPClientSocket.sendto(bytesToSend, serverAddressPort)
UDPClientSocket.sendto(info, serverAddressPort)
#UDPClientSocket.sendto(reset, serverAddressPort)
#UDPClientSocket.sendto(reqinfo, serverAddressPort)

msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = 'Message from Server {}'.format(msgFromServer[0])

print(msg)

