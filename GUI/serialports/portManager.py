from serialports.port import Port
import serial.tools.list_ports


class PortManager():
    def __init__(self, IGuiController):
        self.port = Port()
        self.IGuiController = IGuiController
        self.IGuiController.bindCommand('refreshPortList', self.refreshPortList)
        self.IGuiController.bindCommand('setSelectedPort', self.setSelectedPort)
        self.IGuiController.createVariable('portList')
        self.IGuiController.bindCommand('togglePort', self.togglePort)

    def setSelectedPort(self, selectedPort):
        self.port.port = selectedPort   # sets the port to try to open, e.g. "COM1"
                                        # weirdly the pyserial "port" object uses a member "port"
                                        # to refer to this name, resulting in the strange port.port

    def refreshPortList(self):
        portInfoList = serial.tools.list_ports.comports()
        portList = []
        for portInfo in portInfoList:
            portList.append(portInfo[0])
            self.IGuiController.set('portList', portList)

    def togglePort(self):
        if not self.port.is_open:
            settings = { "Baudrate":self.IGuiController.get("Baudrate"),
                         "Byte Size":self.IGuiController.get("Byte Size"),
                         "Parity":self.IGuiController.get("Parity"),
                         "Stop Bits":self.IGuiController.get("Stop Bits"),
                         "Timeout":self.IGuiController.get("Timeout")}
            self.port.applySettings(settings)
            result = self.port.tryOpen()
            if result is True:
                self.IGuiController.runCommand("disablePortConfig")
        else:
            result = self.port.tryClose()
            if result is True:
                self.IGuiController.runCommand("enablePortConfig")
