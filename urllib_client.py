import urllib.request

r = urllib.request.urlopen("http://localhost:9000")
for line in r:
    print(line.decode().strip())
