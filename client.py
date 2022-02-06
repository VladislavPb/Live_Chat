import socket
import threading
import datetime

'''Setting fix IP-adress and port. It should be the same as 
on server side:'''
IP_ad = '127.0.0.1'
Port = 5000

name = input('Please enter your name:\n')
print(f'Connecting to server {IP_ad}:{Port}')

'''Initialising client with given IP-adress and port'''
soc = socket.socket()
soc.connect((IP_ad, Port))

'''Client app should be killed using keyboard interrupt:'''
print(f'Hello, {name}! Start messaging. To exit press ctr-C"')

'''Client will have two threads - one for listening for messaging
from server (which receive them from clients) and to send messages
to server (which will re-send them to all currently active clients:'''
def listening():

    while True:
        try:
            message = soc.recv(1024)
            print(message.decode())
        except:
            soc.close()
            break

def sending():

    while True:
        message = input()
        time = str(datetime.datetime.now())[:-7]
        message = time + ' | ' + name + ': ' + message
        soc.send(message.encode())

'''Activating both threads:'''
income_thread = threading.Thread(target=listening)
income_thread.start()

outcome_thread = threading.Thread(target=sending)
outcome_thread.start()