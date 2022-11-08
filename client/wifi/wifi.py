import time
import network
from config import wifiConfig


class Wifi:
  def __init__(self) -> None:
    self.wlan = network.WLAN(network.STA_IF)
    self.wlan.active(True)
    self.wlan.connect(wifiConfig.SSID, wifiConfig.PASSWORD)
    self.__connect__()

  def __connect__(self):
    max_wait = 20
    while max_wait > 0:
      if self.wlan.status() < 0 or self.wlan.status() >= 3:
        break
      max_wait -= 1
      print('waiting for connection...')
      time.sleep(1)
    if self.wlan.status() != 3:
      print(self.wlan.status())
      raise RuntimeError('network connection failed')
    else:
      print('connected')
      status = self.wlan.ifconfig()
      print('ip = ' + status[0])
  