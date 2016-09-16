import serial.tools.list_ports


class PortManager():
    portList = []
    selectedPort = None
    IGuiController = None

    def __init__(self, IGuiController):
        self.IGuiController = IGuiController
        self.IGuiController.assignCommand('refreshPortList', self.refreshPortList)
        self.IGuiController.assignVariable('portList', self.portList)
        ### Doesnt work

    def refreshPortList(self):
        print('refreshPortList()')
        portInfoList = serial.tools.list_ports.comports()
        self.portList = []
        for portInfo in portInfoList:
            self.portList.append(portInfo[0])

