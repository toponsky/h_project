import threading
import subprocess
import signal

class ProxyThread(threading.Thread):
    def __init__(self, proxy):
        self.stdout = subprocess.PIPE
        self.stdin = subprocess.PIPE
        self.proxy = proxy
        self.p = None
        threading.Thread.__init__(self)
        self._stop = threading.Event()
    
    def run(self):
        print('Start Proxy: {0}'.format(self.proxy))
        command = 'sudo openvpn --config /home/pi/Downloads/{0}.hideservers.net.ovpn'.format(self.proxy).split()
        self.p = subprocess.Popen(command,
                             shell=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
	
    def stop(self):
        print('Stop Proxy: {0}'.format(self.proxy))
        if self.p is not None:
            self.p.kill()
