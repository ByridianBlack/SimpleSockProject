import socket
import time




try:
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[S]: Server socket created")
except socket.error as err:
    print('socket open error: {}\n'.format(err))
    exit()

server_binding = ('', 50007)
ss.bind(server_binding)
ss.listen(1)
host = socket.gethostname()
print("[S]: Server host name is {}".format(host))
localhost_ip = (socket.gethostbyname(host))
print("[S]: Server IP address is {}".format(localhost_ip))
csockid, addr = ss.accept()
print ("[S]: Got a connection request from a client at {}".format(addr))

# send a intro message to the client.
msg = "Welcome to CS 352!"
csockid.send(msg.encode('utf-8'))
csockid.settimeout(25)

data_buffer = ""
buffer_iter = 0
line_buffer = ""

output = open("out-proj.txt", 'w');
while True:
    try:
        data_buffer += csockid.recv(512).decode("utf-8")
        
        while buffer_iter < (len(data_buffer) - 1):
            atChar = data_buffer[buffer_iter]
            if atChar == '\n':
                output.write(line_buffer.reverse())
                line_buffer = ""
            else:
                line_buffer += atChar
            
            buffer_iter += 1
    
    except:
        break

# Close the server socket
ss.close()
exit()     

'''
while True:
    try:
        data_temp = csockid.recv(200).decode("utf-8")
        with open("out-proj.txt", 'a') as NFILE:
            NFILE.writelines(str(data_temp)[::-1])
        csockid.send((str(data_temp)[::-1]).encode("utf-8"))
    except socket.timeout:
        break

'''