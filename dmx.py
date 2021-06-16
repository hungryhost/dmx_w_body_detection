from DMXEnttecPro import Controller

# dmx = Controller('COM4')  # Typical of Windows
dmx = Controller('/dev/ttyUSB0')  # Typical of Linux

# dmx.set_channel(1, 255)
# dmx.set_channel(2, 0)
dmx.set_channel(3, 0)
# dmx.set_channel(4, 0)
# dmx.set_channel(5, 0)
# dmx.set_channel(6, 0)
# dmx.set_channel(7, 226)
# dmx.set_channel(8, 255)
# dmx.get_channel(1)  # Sets DMX channel 1 to max 255

dmx.submit()  # Sends the update to the controller
