
class FileIO():
    def __init__(self, IGuiController, IDataSource):
        self.IGuiController = IGuiController
        self.IDataSource = IDataSource
        self.IGuiController.bindCommand('openfile', self.dataFromFile)

    def dataFromFile(self, filename):
        if filename is not '':
            file = open(filename, 'rb')
            data = file.read()
            self.IDataSource.fromString(data)
