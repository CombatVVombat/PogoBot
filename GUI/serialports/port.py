import serial as serial


class Port(serial.Serial):
    def __init__(self, *args, **kwargs):
        serial.Serial.__init__(self, *args, **kwargs)
        self.port = None
        self.baudrate = 9600
        self.bytesize = serial.EIGHTBITS
        self.parity = serial.PARITY_NONE
        self.stopbits = serial.STOPBITS_ONE

    def applySettings(self, d):
        self.baudrate = int(d["Baudrate"])
        byteSizeDict = { 5:serial.FIVEBITS, 6:serial.SIXBITS, 7:serial.SEVENBITS, 8:serial.EIGHTBITS }
        self.bytesize = byteSizeDict[int(d["Byte Size"])]
        parityDict = { "None":serial.PARITY_NONE, "Even":serial.PARITY_EVEN,
                       "Odd":serial.PARITY_ODD, "Mark":serial.PARITY_MARK, "Space":serial.PARITY_SPACE }
        self.parity = parityDict[d["Parity"]]
        stopBitsDict = { "1":serial.STOPBITS_ONE, "2":serial.STOPBITS_TWO }
        self.stopbits = stopBitsDict[d["Stop Bits"]]
        timeoutDict = { "None":None, "Non-Blocking":0, "1 second":1.0, "2 seconds":2.0, "5 seconds":5.0 }
        self.timeout = timeoutDict[d["Timeout"]]

    def tryOpen(self):
        if self.port is None:
            print("Port open failed: Name is 'None'")
            return False

        if self.is_open:
            print("Port open failed: already open")
            return False

        self.open()
        if self.is_open:
            settings = self.get_settings()
            print("Port opened.")
            for key, value in settings.items():
                print("   " + str(key) + ": " + str(value))
            return True

    def tryClose(self):
        self.close()
        print("Port closed.")
        return True

"""def readFromPort():
    bytesRead = 0
    global rawByteStream
    if portOpen.get() == 1:
        while ser.inWaiting() > 0:
            rawByteStream.extend(ser.read())
            bytesRead = bytesRead + 1
    return bytesRead"""
