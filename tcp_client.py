import socket

address = ("192.168.0.102", 6666)
max_size = 1000

print("starting the cleint\n")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)

while True:
    sms = input("--> ")
    client.sendall(bytes(sms, encoding="utf-8"))
    if sms == "exit":
        break
    else:
        continue

client.close()
