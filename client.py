import socket
import sys
import time

# Define the port on which you want to connect to the server
port = 11557



try:
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[C]: Client socket created")
except socket.error as err:
    print('[C]: socket open error: {} \n'.format(err))
    exit()
        
localhost_addr = socket.gethostbyname(socket.gethostname())

# connect to the server on local machine
server_binding = (localhost_addr, port)
cs.connect(server_binding)

# Receive data from the server
data_from_server=cs.recv(200)
print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))

with open("in-proj.txt", 'r') as NFILE:
    for lines in NFILE.readlines():
    
        # Handle the case where last line in file is not terminated by \n
        if ((len(lines) > 0) and (lines[-1] != '\n')):
            lines += '\n'
            
        print('[C]: Sending   line: {}'.format(lines), end='')
        try:
            cs.send(str(lines).encode("utf-8"))
            received_data = cs.recv(200).decode("utf-8")
            print('[C]: Receiving line: {}'.format(received_data), end='')
        except Exception as err:
            print('[C]: Encountered Error: {}'.format(err))
        
        # print a line between each sending/receiving pair
        print()

'''
count = 0
while True:
    message_input = ""
    if count == 0:
        message_input = str(input("\nSend Message: "))
    else:
        message_input = str(input("Send Message: "))
    
    try:
        cs.send(message_input.encode("utf-8"))
        recieved_data = cs.recv(200).decode("utf-8")
        print(recieved_data)
    except Exception as err:
        print(err)
        break
    count+=1
'''
time.sleep(26)
# close the client socket
cs.close()
exit()