from ProxyManagement import ProxyThread
class ProxyManager:

    def __init__(self, proxies):
      self.index = 0
      self.proxyList = proxies
      self.proxy = None

    def getCurIndex(self):
      temp = self.index
      self.index = self.index + 1
      if self.index == len(self.proxyList):
        self.index = 0
      return temp

    def startNextProxy(self):
      if self.proxy is not None:
        self.proxy.stop()

      self.proxy = ProxyThread.ProxyThread(self.proxyList[self.getCurIndex()])
      self.proxy.start()

    def stop(self):
      self.proxy.stop()  
      
    def getProxyCount():
      return len(self.proxyList)
