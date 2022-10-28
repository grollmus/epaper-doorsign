import time
import network
ssid = 'WLAN-G'
password = 'Xsimatic2015!'
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

def main():
  max_wait = 20
  while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
      break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)
  if wlan.status() != 3:
    print(wlan.status())
    raise RuntimeError('network connection failed')
  else:
    print('connected')
    status = wlan.ifconfig()
    print('ip = ' + status[0])

if __name__ == "__main__":
  main()
  