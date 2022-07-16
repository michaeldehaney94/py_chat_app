import socket
from tkinter import *


def send(listbox, entry):
    message = entry.get()
    listbox.insert('end', 'Client: ' + message)
    entry.delete(0, END)
    s.send(bytes(message, 'utf-8'))
    receive(listbox)


def receive(listbox):
    # receive encoded message from server
    # bufsize(buffer size) tells you how many chunks of data is received at a time
    message = s.recv(50)
    listbox.insert('end', 'Server: ' + message.decode('utf-8'))


# ============================ GUI LAYOUT ===================================
root = Tk()
root.title('LinkMe(Client)')

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

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST_NAME = socket.gethostname()
PORT = 3001

# connect client to server through socket
s.connect((HOST_NAME, PORT))

root.mainloop()