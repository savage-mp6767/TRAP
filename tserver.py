##        ##
## TRAP   ##
## SERVER ##

import socket
import pickle

class TServer_ClientInst:
    def __init__(self, ip, connection):
        self.con = connection
        self.client_addr = ip

class TServer:
    def __init__(self, host, port, maxClients):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.connection.bind((host,port))
        self.connection.listen(maxClients)
        self.maxClients = maxClients
        self.clients = []
        self.conCommands = []
        print 'Initialized TRAP server on ' + str(host + ":" + port) + '(' + str(len(self.clients)) + '/' + str(maxClients) + ')'

    def mainloop(self):
        con, ip = self.connection.accept()
        print str(ip) + ' connected. (' + str(ip) + ') (' + str(len(self.clients)) + '/' + str(len(self.maxClients)) + ')'
        
serv = TServer('localhost',1234,5)
serv.mainloop()