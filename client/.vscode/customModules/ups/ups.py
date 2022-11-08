from machine import I2C
from micropython import const

# Config Register (R/W)
_REG_CONFIG                 = const(0x00)
_REG_BUSVOLTAGE             = const(0x02)
_REG_CURRENT                = const(0x04)
_REG_CALIBRATION            = const(0x05)

_RANGE_32V                  = const(0x01)
_DIV_8_320MV                = const(0x03)      # shunt prog. gain set to /8, 320 mV range
_ADCRES_12BIT_32S           = const(0x0D)      # 12bit,  32 samples, 17.02ms
_SANDBVOLT_CONTINUOUS       = const(0x07)      # shunt and bus voltage continuous
_CAL_VALUE                  = const(4096)
 
class INA219:
    def __init__(self, i2c_bus=1, addr=0x40):
        self.i2c = I2C(i2c_bus)
        self.addr = addr
        self.set_calibration_32V_2A()
        
    def read(self,address):
        data = self.i2c.readfrom_mem(self.addr, address, 2)
        return ((data[0] << 8 ) + data[1])

    def write(self,address,data):
        temp = [0,0]
        temp[1] = data & 0xFF
        temp[0] =(data & 0xFF00) >> 8
        self.i2c.writeto_mem(self.addr,address,bytes(temp))

    def set_calibration_32V_2A(self):
        self.write(_REG_CALIBRATION,_CAL_VALUE)
        self.config = _RANGE_32V << 13 | \
                      _DIV_8_320MV << 11 | \
                      _ADCRES_12BIT_32S << 7 | \
                      _ADCRES_12BIT_32S << 3 | \
                      _SANDBVOLT_CONTINUOUS
        self.write(_REG_CONFIG,self.config)
        
    def getBusVoltage_V(self):
        return (self.read(_REG_BUSVOLTAGE) >> 1) * 0.001
        
    def getCurrent_mA(self):
        value = self.read(_REG_CURRENT)
        if value > 32767:
            value -= 65535
        return value
    
    def getPercent(self,bus_voltage):
        P = (bus_voltage -3)*0.002
        if(P<0):P=0
        elif(P>100):P=100
        return P
    