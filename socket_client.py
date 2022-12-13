import socket

# Make a phone (i.e. Client socket)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Dial the phone (i.e. Initiate a connection with the server socket)
s.connect(('127.0.0.1', 9000))

# DON'T FORGET: the "\r\n\r\n" puts the blank line after the request line, 
# which indicates the end of the request
# Normally, it will wait for headers then blank line.
cmd = 'GET / HTTP/1.0\r\n\r\n'

# Send the command to the server (request object)
s.send(cmd.encode())

while True:
    # Keep receiving response data
    data = s.recv(512)

    # Till there is no more
    if len(data) < 1:
        break

    # Print the data
    print(data.decode(), end='')

# Hang up the phone (i.e. Close the connection)
s.close()
