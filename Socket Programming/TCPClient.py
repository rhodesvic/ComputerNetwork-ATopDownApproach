from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input("Input lowcase sentence: ")
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print("From Server: ", modifiedSentence.decode())
clientSocket.close()
