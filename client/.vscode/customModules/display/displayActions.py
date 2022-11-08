import framebuf
from fonts.writer import ThreeColorWriter
from display.dummyDevice import DummyDevice
from waveshare.epaper5in87b import EPaperDisplay5in87b
import gc
import utime

class DisplayActions:
    def __init__(self) -> None:
        self.delay(100)
        print("Initialize DisplayActions")
        self.epd = EPaperDisplay5in87b()
        self.epd.Clear(0xFF, 0x00)
        gc.collect()
        self.delay(10)

    def writeLineBlack(self, text, x, y, font = None):
        self.delay(10)
        if font == None:
            self.epd.imageblack.text(text, x, y)
        else:
            self.dummy = DummyDevice(self.epd.width, font.height(), framebuf.MONO_HMSB)
            self.wri = ThreeColorWriter(self.dummy, font, False)
            self.wri.writeTextBlack(text)
            self.epd.blitBlack(self.dummy, x, y)
            
        self.epd.displayBlack()
        gc.collect()
        self.delay(10)

    def writeLineRed(self, text, x, y, font = None):
        self.delay(10)
        if font == None:
            self.epd.imagered.text(text, x, y)
        else:
            self.dummy = DummyDevice(self.epd.width, font.height(), framebuf.MONO_HMSB)
            self.wri = ThreeColorWriter(self.dummy, font, False)
            self.wri.writeTextRed(text)
            self.epd.blitRed(self.dummy, x, y)
            
        self.epd.displayRed()
        gc.collect()
        self.delay(10)

    def drawLineBlack(self, x, y, length):
        self.delay(10)
        self.epd.imageblack.hline(x, y, length, 0x00)
        self.epd.displayBlack()
        gc.collect()
        self.delay(10)

    def drawLineRed(self, x, y, length):
        self.delay(10)
        self.epd.imagered.hline(x, y, length, 0xff)
        self.epd.displayRed()
        gc.collect()
        self.delay(10)

    def sleep(self):
        self.delay(10)
        print("sleep")
        self.epd.sleep()

    def delay(self, delayTime):
        utime.sleep_ms(delayTime)
