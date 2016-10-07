from serialports.port import Port
import serial.tools.list_ports


class PortManager():
    port = Port()
    portList = []
    IGuiController = None

    def __init__(self, IGuiController):
        self.IGuiController = IGuiController
        self.IGuiController.bindCommand('refreshPortList', self.refreshPortList)
        self.IGuiController.bindCommand('setSelectedPort', self.setSelectedPort)
        self.IGuiController.createVariable('portList', self.portList)
        self.IGuiController.bindCommand('togglePort', self.togglePort)

    def setSelectedPort(self, selectedPort):
        self.port.port = selectedPort

    def refreshPortList(self):
        portInfoList = serial.tools.list_ports.comports()
        self.portList = []
        for portInfo in portInfoList:
            self.portList.append(portInfo[0])
            self.IGuiController.set('portList', self.portList)

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
