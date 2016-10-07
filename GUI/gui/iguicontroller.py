from abc import ABCMeta, abstractmethod


class IGuiController(metaclass=ABCMeta):
    commands = {}
    variables = {}

    @abstractmethod
    def runCommand(self, name, *args):
        pass

    @abstractmethod
    def bindCommand(self, name, command):
        pass

    @abstractmethod
    def createVariable(self, name, variable):
        pass

    @abstractmethod
    def set(self, name, variable):
        pass

    @abstractmethod
    def get(self, name):
        pass