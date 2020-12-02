import jpysocket
host = "127.0.0.1"
port = 8080
s=jpysocket.jpysocket() #Create Socket
s.connect((host,port)) #Connect to socket
while True:
    in_data =  s.recv(1024)
    in_data = jpysocket.jpydecode(in_data)
    print("From Server :",in_data)
    out_data = input()
    out_data =  jpysocket.jpyencode(out_data)
    s.sendall(out_data)
    if out_data=='bye':
     break
    in_data =  s.recv(1024)
    in_data = jpysocket.jpydecode(in_data)
    print("From Server :",in_data)
s.close()

#import jpysocket
#host='localhost' #Host Name
#port=8080    #Port Number
#
#s=jpysocket.jpysocket() #Create Socket
#s.connect((host,port)) #Connect to socket
#while True:
#    print("Socket Is Connected....")
#    msgrecv=s.recv(1024) #Recieve msg
#    msgrecv=jpysocket.jpydecode(msgrecv) #Decript msg
#    print("From Server: ",msgrecv)
#    msgsend=jpysocket.jpyencode(input()) #Encript The Msg
#    s.send(msgsend) #Send Msg
#     if msgsend=='bye':
#        break
#  s.close()