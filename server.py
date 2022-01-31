import socket
import time

port = 11557


try:
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[S]: Server socket created")
except socket.error as err:
    print('[S]: socket open error: {}\n'.format(err))
    exit()

server_binding = ('', port)
ss.bind(server_binding)
ss.listen(1)
host = socket.gethostname()
print("[S]: Server host name is {}".format(host))
localhost_ip = (socket.gethostbyname(host))
print("[S]: Server IP address is {}".format(localhost_ip))

try:
    output = open("out-proj.txt", 'w')
except OSError as err:
    print('[S]: Could not open file: {}\n'.format(err))
    exit()
else:
    print ("[S]: Successfully opened out-proj.txt")

csockid, addr = ss.accept()
print ("[S]: Got a connection request from a client at {}".format(addr))

# send a intro message to the client.
msg = "Welcome to CS 352!"
csockid.send(msg.encode('utf-8'))
csockid.settimeout(5)

data_buffer = ""
buffer_iter = 0
line_buffer = ""

while True:
    try:
        received = csockid.recv(512).decode("utf-8")
        if (received == ""):
            break
        
        data_buffer += received
        
        while buffer_iter < len(data_buffer):
            atChar = data_buffer[buffer_iter]
            if atChar == '\n':
                # reverse the string
                reverse = line_buffer[::-1] + '\n'
                output.write(reverse)
                csockid.send(reverse.encode("utf-8"))
                line_buffer = ""
            else:
                line_buffer += atChar
            
            buffer_iter += 1
    
    except Exception as err:
        print("[S]: Encountered Error: {}\n".format(err))
        break

# close resources
output.close()
ss.close()
exit()