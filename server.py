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
recieved_data = ""
data_temp = ""


csockid.settimeout(25)
while True:
    try:
        data_temp = csockid.recv(200).decode("utf-8")
        with open("out-proj.txt", 'a') as NFILE:
            NFILE.writelines(str(data_temp)[::-1])
        csockid.send((str(data_temp)[::-1]).encode("utf-8"))
    except socket.timeout:
        break

    



msg = "Welcome to CS 352!"
csockid.send(msg.encode('utf-8'))

    # Close the server socket
ss.close()
exit()