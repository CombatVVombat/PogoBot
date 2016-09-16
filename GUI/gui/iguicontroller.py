from abc import ABCMeta, abstractmethod


class IGuiController(metaclass=ABCMeta):
    commands = {}
    variables = {}

    @abstractmethod
    def runCommand(self, name):
        pass

    @abstractmethod
    def assignCommand(self, name, command):
        pass

    @abstractmethod
    def assignVariable(self, name, variable):
        pass