import socket

print('Running on http://localhost:9000')

# Create the server socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind(('localhost', 9000))
    s.listen(5)
    while True:
        # Accept a client socket connection
        client, address = s.accept()

        # Receive data form client socket
        rawdata = client.recv(5000).decode()
        pieces = rawdata.split("\n")

        # Print the received data
        if len(pieces[0]) > 0:
            print(pieces[0])

        # Create the response string
        data = "HTTP/1.1 200 OK\r\n"
        data += "Content-Type: text/html; charset=utf-8\r\n"
        data += "\r\n"
        data += "<html><body>Hello World</body></html>"

        # Send the response to the client socket
        client.sendall(data.encode())

        # Close the connection
        client.shutdown(socket.SHUT_WR)

except KeyboardInterrupt:
    print("\nShutting down...\n")
except Exception as e:
    print("\nError:\n")
    print(e)
