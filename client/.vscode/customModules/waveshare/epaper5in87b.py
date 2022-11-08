from machine import Pin, SPI
import framebuf
import utime
from waveshare.epaperCommands import *

_RST_PIN        = const(12)
_DC_PIN         = const(8)
_CS_PIN         = const(9)
_BUSY_PIN       = const(13)
_SPI_BAUD       = const(4000_000)

_HEIGHT         = const(480)
_WIDTH          = const(648)

_BUFFER_SIZE    = const(38880) # Height * Width / 8

BUSY = const(0)  # 0=busy, 1=idle

class EPaperDisplay5in87b():
    def __init__(self):
        self.width = _WIDTH
        self.height = _HEIGHT

        self.reset_pin = Pin(_RST_PIN, Pin.OUT)
        self.busy_pin = Pin(_BUSY_PIN, Pin.IN, Pin.PULL_UP)
        self.cs_pin = Pin(_CS_PIN, Pin.OUT)
        self.dc_pin = Pin(_DC_PIN, Pin.OUT)
        
        self.spi = SPI(1)
        self.spi.init(baudrate=_SPI_BAUD)
        
        self.buffer_black = bytearray(_BUFFER_SIZE)
        self.buffer_red = bytearray(_BUFFER_SIZE)
        self.imageblack = framebuf.FrameBuffer(self.buffer_black, _WIDTH, _HEIGHT, framebuf.MONO_HLSB)
        self.imagered = framebuf.FrameBuffer(self.buffer_red, _WIDTH, _HEIGHT, framebuf.MONO_HLSB)
        
        self.init()

    def digital_write(self, pin, value):
        pin.value(value)

    def digital_read(self, pin):
        return pin.value()

    def spi_writebyte(self, data):
        self.spi.write(bytearray(data))

    def module_exit(self):
        self.digital_write(self.reset_pin, 0)

    def delay_ms(self, delaytime):
        utime.sleep_ms(delaytime)

    # Hardware reset
    def reset(self):
        self.digital_write(self.reset_pin, 1)
        self.delay_ms(50) 
        self.digital_write(self.reset_pin, 0)
        self.delay_ms(2)
        self.digital_write(self.reset_pin, 1)
        self.delay_ms(10)   

    def send_command(self, command):
        self.digital_write(self.dc_pin, 0)
        self.digital_write(self.cs_pin, 0)
        self.spi_writebyte([command])
        self.digital_write(self.cs_pin, 1)

    def send_data(self, data):
        self.digital_write(self.dc_pin, 1)
        self.digital_write(self.cs_pin, 0)
        self.spi_writebyte([data])
        self.digital_write(self.cs_pin, 1)
        
    def send_data2(self, data):
        self.digital_write(self.dc_pin, 1)
        self.digital_write(self.cs_pin, 0)
        self.spi_writebyte(data)
        self.digital_write(self.cs_pin, 1)

    def ReadBusy(self):
        print("e-Paper busy")
        while(self.digital_read(self.busy_pin) == BUSY):      #  1: idle, 0: busy
            self.delay_ms(100)
        print("e-Paper busy release")  

    def TurnOnDisplay(self):
        self.send_command(DISPLAY_REFRESH) 
        self.delay_ms(10)
        self.ReadBusy()
        
    def init(self):
        # EPD hardware init start     
        self.reset()
        
        self.send_command(POWER_SETTINGS)
        self.send_data (0x07)
        self.send_data (0x07)       #VGH=20V,VGL=-20V
        self.send_data (0x3f)       #VDH=15V
        self.send_data (0x3f)       #VDL=-15V

        self.send_command(POWER_ON)
        self.delay_ms(50)  
        self.ReadBusy()   #waiting for the electronic paper IC to release the idle signal

        self.send_command(PANEL_SETTINGS)
        self.send_data(0x0F)        #KW-3f   KWR-2F    BWROTP 0f   BWOTP 1f

        self.send_command(RESOLUTION_SETTINGS)
        self.send_data (0x02)       #source 648
        self.send_data (0x88)
        self.send_data (0x01)       #gate 480
        self.send_data (0xe0)

        self.send_command(DUAL_SPI)
        self.send_data(0x00)

        self.send_command(VCOM_DATA_INTERVAL_SETTINGS)
        self.send_data(0x11)
        self.send_data(0x07)

        self.send_command(TCON_SETTINGS)
        self.send_data(0x22)
        # EPD hardware init end
        return 0

    def display(self, imageBlack, imageRed):
        if (imageBlack == None or imageRed == None):
            return    
        self.send_command(DISPLAY_BLACK_DATA)
        self.send_data2(imageBlack)
        self.delay_ms(50)
        self.send_command(DISPLAY_RED_DATA)
        self.send_data2(imageRed)
        self.TurnOnDisplay()

    def displayBlack(self):
        self.delay_ms(50)
        self.send_command(DISPLAY_BLACK_DATA)
        self.send_data2(self.buffer_black)
        self.delay_ms(50)
        self.TurnOnDisplay()

    def displayRed(self):
        self.delay_ms(50)
        self.send_command(DISPLAY_RED_DATA)
        self.send_data2(self.buffer_red)
        self.delay_ms(50)
        self.TurnOnDisplay()

    def show(self):
        self.displayBlack()
        self.delay_ms(50)
        self.displayRed()
        self.delay_ms(50)

    def Clear(self, colorBlack, colorRed):
        self.imageblack.fill(colorBlack)
        self.imagered.fill(colorRed)
        self.display(self.buffer_black, self.buffer_red)
        self.delay_ms(50)

    def sleep(self):
        self.send_command(POWER_OFF)
        self.ReadBusy()
        self.send_command(DEEP_SLEEP)
        self.send_data(0xa5)
        
        self.delay_ms(2000)
        self.module_exit()

    def blitBlack(self, fbuf, x, y):
        self.imageblack.blit(fbuf, x, y)

    def blitRed(self, fbuf, x, y):
        self.imagered.blit(fbuf, x, y, 0x00)