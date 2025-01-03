import socket
from TOKEN import address


max_size = 1000

print("starting the cleint\n")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)


def while_chat():
    while True:
        sms = input("--> ")
        client.sendall(bytes(sms, encoding="utf-8"))
        if sms == "exit":
            break
        else:
            continue
    client.close()