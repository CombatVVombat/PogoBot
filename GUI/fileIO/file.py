class FileIO():
    def __init__(self, IGuiController, IDataSource):
        self.data = bytearray()
        self.IGuiController = IGuiController
        self.IGuiController.bindCommand('openfile', self.dataFromFile)
        self.dataOutputHandle = IDataSource

    def dataFromFile(self, filename):
        self.data = bytearray()
        if filename is not '':
            try:
                file = open(filename, 'rb')
                self.data = file.read()
            except IOError:
                print("FoleIO::dataFromFile exception IOError occurred.")
        else:
            print("FileIO::dataFromFile no filename provided")
        for x in self.data:
            self.dataOutputHandle.append(x)
        return self.data


