from ups.ups import INA219

class UpsControl:
    def __init__(self) -> None:
        self.ina219 = INA219(addr=0x43)

    def GetVoltage(self):
        return self.ina219.getBusVoltage_V()
    
    def GetCurrent(self):
        return self.ina219.getCurrent_mA() 

    def GetPercent(self):
        return self.ina219.getPercent(self.GetVoltage())
