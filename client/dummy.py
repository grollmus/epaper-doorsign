from display.displayActions import DisplayActions
import gc
from utime import ticks_ms, ticks_diff, sleep
import fonts.freesans20
import _thread
from ups.upsControl import UpsControl

print("Starting Application")
print("Initialize DisplayActions")
start_mem = gc.mem_free()
start_t = ticks_ms()
displayAction = DisplayActions()
fin_t = ticks_ms()
fin_mem = gc.mem_free()
print(f'DisplayActions took: {ticks_diff(fin_t, start_t)} ms to finish')
print(f'DisplayActions used around {start_mem - fin_mem} B of memory')
print(f'Free Memory left {fin_mem} B of memory')

print("Registring UPS Service")
def upsThread():
    upsControl = UpsControl()
    while True:
        print(f'Voltage: {upsControl.GetVoltage()} V')
        print(f'Current: {upsControl.GetCurrent()} mA')
        print(f'Percent: {upsControl.GetPercent()} %')
        gc.collect()
        sleep(10)
_thread.start_new_thread(upsThread, ())
gc.collect()
print(f'Free Memory: {gc.mem_free()}')

print("Write Line Black")
start_mem = gc.mem_free()
start_t = ticks_ms()
displayAction.writeLineBlack("Test Text Black", 0, 10, fonts.freesans20)
fin_t = ticks_ms()
fin_mem = gc.mem_free()
print(f'Write Line took: {ticks_diff(fin_t, start_t)} ms to finish')
print(f'Write Line used around {start_mem - fin_mem} B of memory')
print(f'Free Memory left {fin_mem} B of memory')

print("Write Line Red")
start_mem = gc.mem_free()
start_t = ticks_ms()
displayAction.writeLineRed("Test Text Red", 0, 35, fonts.freesans20)
fin_t = ticks_ms()
fin_mem = gc.mem_free()
print(f'Write Line took: {ticks_diff(fin_t, start_t)} ms to finish')
print(f'Write Line used around {start_mem - fin_mem} B of memory')
print(f'Free Memory left {fin_mem} B of memory')

displayAction.epd.Clear(0xFF, 0x00)
displayAction.delay(2000)