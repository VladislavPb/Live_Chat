import socket
import threading


'''Setting fix IP-adress and port:'''
IP_ad = '127.0.0.1'
Port = 5000

'''Initialiasing server with given IP-adress and port'''
soc = socket.socket()
soc.bind((IP_ad, Port))

'''Server will listen to up to 10 connections.
Number can be decreased or increased:'''
soc.listen(10)

'''Initialiasing empty set to store active client hosts:'''
conns = set()

'''Function to handle messages from each active clients to all clients:'''
def connection(client):

    while True:

        '''If all goes smoothly, message will be re-send to all
        clients without decoding&encoding; also decoded message
        will be printed in server console. In the case of error
        client will be disconnected'''

        try:
            message = client.recv(1024)
            for c in conns:
                c.send(message)

            print(message.decode())

        except:
            conns.remove(client)
            client.close()
            break

'''Starting server. Each new connection from client starts
individual thread:'''

while True:
    conn, address = soc.accept()
    conns.add(conn)

    thread = threading.Thread(target=connection, args=(conn,))
    thread.start()
