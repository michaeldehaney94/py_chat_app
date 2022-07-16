import socket
from tkinter import *


def send(listbox, entry):
    message = entry.get()
    listbox.insert('end', 'Server: ' + message)
    entry.delete(0, END)
    client.send(bytes(message, "utf-8"))


def receive(listbox):
    message_from_client = client.recv(50)
    listbox.insert('end', 'Client: ' + message_from_client.decode('utf-8'))


# ============================ GUI LAYOUT ===================================
root = Tk()
root.title('LinkMe(Server)')

entry = Entry()
entry.pack(side=BOTTOM)

listbox = Listbox(root)
listbox.pack()

button = Button(root, text='Send', command=lambda: send(listbox, entry))
button.pack(side=BOTTOM)

rbutton = Button(root, text='Receive', command=lambda: receive(listbox))
rbutton.pack(side=BOTTOM)

# root.mainloop()
# ======================================================================


# s = socket
# INET = IPv4
# TCP socket type = SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get the ip / host name of machine
HOST_NAME = socket.gethostname()
PORT = 3001

# binding hostname and port together to create endpoint to send/receive data
s.bind((HOST_NAME, PORT))

# listen for connection
s.listen(4)

# accept client connection
client, address = s.accept()

root.mainloop()
