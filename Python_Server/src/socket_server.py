#import socket, threading
#class ClientThread(threading.Thread):
#    def __init__(self,clientAddress,clientsocket):
#        threading.Thread.__init__(self)
#        self.csocket = clientsocket
#        print ("New connection added: ", clientAddress)
#    def run(self):
#        print ("Connection from : ", clientAddress)
#        self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
#        msg = ''
#        while True:
#            data = self.csocket.recv(1024)
#            msg = data.decode()
#            if msg=='bye':
#              break
#            print ("from client", msg)
#            self.csocket.send(bytes(msg,'UTF-8'))
#        print ("Client at ", clientAddress , " disconnected...")
#LOCALHOST = "127.0.0.1"
#PORT = 1234
#server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#server.bind((LOCALHOST, PORT))
#print("Server started")
#print("Waiting for client request..")
#while True:
#    server.listen(1)
#    clientsock, clientAddress = server.accept()
#    newthread = ClientThread(clientAddress, clientsock)
#    newthread.start()
#



#while True:
#    
#    msgsend=jpysocket.jpyencode("Thank You For Connecting.") #Encript The Msg
#    connection.send(msgsend) #Send Msg
#    while True:
#        msgrecv=connection.recv(1024) #Recieve msg
#        msgrecv=jpysocket.jpydecode(msgrecv) #Decript msg
#        if not msgrecv:
#            break
#        print("From Client: ",msgrecv)
#s.close() #Close connection
#print("Connection Closed.")

import jpysocket

host="localhost" #Host Name
port=12345    #Port Number
s=jpysocket.jpysocket() #Create Socket
s.bind((host,port)) #Bind Port And Host
s.listen(5) #Socket is Listening
test = "Socket Is Listening...."
print(test)


while True:
    connection,address=s.accept() #Accept the Connection
    print("Connected To ",address)
    while 1:
        data = connection.recv(1024)
        if not data:
            break
        print("RECIEVED FROM JAVA SERVER:" , jpysocket.jpydecode(data))
#        msgsend=jpysocket.jpyencode(input()) #Encript The Msg
        connection.send(data) #Send Msg