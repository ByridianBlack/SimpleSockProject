from email.mime import message
import socket
import sys





try:
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[C]: Client socket created")
except socket.error as err:
    print('socket open error: {} \n'.format(err))
    exit()
        
# Define the port on which you want to connect to the server
port = 50007
localhost_addr = socket.gethostbyname(socket.gethostname())

# connect to the server on local machine
server_binding = (localhost_addr, port)
cs.connect(server_binding)


with open("in-proj.txt", 'r') as NFILE:
    for lines in NFILE.readlines():
        cs.send(str(lines).encode("utf-8"))
        recieved_data = cs.recv(200).decode("utf-8")
        print(recieved_data, end='')

count = 0
while True:
    message_input = ""
    if count == 0:
        message_input = str(input("\nMessage: "))
    else:
        message_input = str(input("Message: "))
    try:
        cs.send(message_input.encode("utf-8"))
        recieved_data = cs.recv(200).decode("utf-8")
        print(recieved_data)
    except Exception as e:
        break
    count+=1
# Receive data from the server
data_from_server=cs.recv(100)
print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))

# close the client socket
cs.close()
exit()