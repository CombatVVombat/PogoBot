from abc import ABCMeta, abstractmethod


class IDataSource():
    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def append(self, value):
        pass

    @abstractmethod
    def fromString(self, string):
        pass

