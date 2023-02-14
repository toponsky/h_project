import threading
import subprocess

class ProxyManager(threading.Thread):
    def __init__(self):
        self.stdout = subprocess.PIPE
        self.stdin = subprocess.PIPE
        self.stderr = subprocess.stdout
        threading.Thread.__init__(self)

    def run(self):
        p = subprocess.Popen('sudo openvpn --config /home/pi/Downloads/ch.hideservers.net.ovpn'.split(),
                             shell=False,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)

        self.stdout, self.stderr = p.communicate()