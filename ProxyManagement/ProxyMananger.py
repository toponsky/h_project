import ProxyThread
class ProxyManager:

    def __init__(self, proxies):
      self.index = 0
      self.proxyList = proxies
      self.proxy = None

    def _getIndex(self):
      temp = self.index
      self.index = self.index + 1
      if self.index == len(self.proxyList):
        self.index = 0
      return temp

    def startNextProxy():
      if self.proxy not None:
        self.proxy.stop()

      self.proxy = ProxyThread.ProxyThread(self.proxyList(self._getIndex()))

    def stop():
      if self.proxy not None:
        self.proxy.stop()  
      
