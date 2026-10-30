import board
import digitalio
import time
import analogio
import displayio
import i2cdisplaybus
import adafruit_displayio_ssd1306
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font

sw1=digitalio.DigitalInOut(board.D2)
sw1.direction=digitalio.Direction.INPUT
sw1.pull=digitalio.Pull.UP

sw2=digitalio.DigitalInOut(board.D3)
sw2.direction=digitalio.Direction.INPUT
sw2.pull=digitalio.Pull.UP

displayio.release_displays()
i2c=board.I2C()
display_bus=i2cdisplaybus.I2CDisplayBus(i2c, device_address=0x3C)
display=adafruit_displayio_ssd1306.SSD1306(
    display_bus,
    width=128,
    height=64
)

pages=[
    displayio.OnDiskBitmap("/menu_cont.bmp"),
    displayio.OnDiskBitmap("/menu_volt.bmp"),
    displayio.OnDiskBitmap("/menu_dig.bmp"),
    displayio.OnDiskBitmap("/cont_no.bmp"),
    displayio.OnDiskBitmap("/cont_yes.bmp"),
    displayio.OnDiskBitmap("/volt.bmp"),
    displayio.OnDiskBitmap("/dig_low.bmp"),
    displayio.OnDiskBitmap("/dig_high.bmp")
]

tile=displayio.TileGrid(pages[0], pixel_shader=pages[0].pixel_shader)
group=displayio.Group()
group.append(tile)

font=bitmap_font.load_font("/font.bdf")

v_text=label.Label(
    font,
    text="",
    color=0xFFFFFF,
    x=40,
    y=28
)
group.append(v_text)

display.root_group=group

current_page=0
def change_page(index):
    global current_page
    if current_page==index:
        return
    current_page=index
    tile.bitmap=pages[index]
    tile.pixel_shader=pages[index].pixel_shader

continuity=digitalio.DigitalInOut(board.D1)
continuity.direction=digitalio.Direction.INPUT

def set_analog():
    in_analog=analogio.AnalogIn(board.A0)
    return in_analog

def set_digital():
    in_digital=digitalio.DigitalInOut(board.D0)
    in_digital.direction=digitalio.Direction.INPUT
    return in_digital

def get_voltage(in_analog):
    total=0
    for i in range(16):
        total+=in_analog.value
        return ((total/16)*4.95)/65535


mode=3 #3=menu, 0=continuity, 1=Analog voltage, 2=Digital input
cursor=0 #Which mode is the cursor pointing to
inpin=0 #What is the current mode of pin A0 (1=Analog, 2=Digital, 0=Neither)
last_update=0
prev1=True
prev2=True

while True:
    now1=sw1.value
    now2=sw2.value

    if prev2 and not now2:
        mode=cursor
        cursor=3
        if inpin==1:
            analog.deinit()
            v_text.text=""
            inpin=0
        elif inpin==2:
            digital.deinit()
            inpin=0

    #-----MENU-----
    if mode==3:
        if cursor==3: cursor=0
        change_page(cursor)
        if prev1 and not now1:
            cursor=(cursor+1)%3

    #-----CONTINUITY-----   
    elif mode==0:
        if continuity.value:
            change_page(4)
        else:
            change_page(3)

    #-----VOLTAGE-----
    elif mode==1:
        if inpin==0:
            analog=set_analog()
            inpin=1

        change_page(5)
        t=time.monotonic()
        if t-last_update>0.2:
            voltage=get_voltage(analog)
            v_text.text=f"{voltage:.2f}"
            last_update=t

    #-----DIGITAL-----
    elif mode==2:
        if inpin==0:
            digital=set_digital()
            inpin=2

        if digital.value:
            change_page(7)
        else:
            change_page(6)

    prev1=now1
    prev2=now2

    time.sleep(0.01)
