import socket


class GameSocket():

    def __init__(self, ip, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        self.s.connect((ip, port))

    def send_action(self, action):
        self.s.send(action)
        reply = self.s.recv(4096)
        return reply

    def close(self):
        self.s.close()

    def __del__(self):
        self.s.close()