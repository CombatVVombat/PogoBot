from datasource.idatasource import IDataSource as IDataSource


class DatasourceList(IDataSource):
    data = []

    def __init__(self):
        pass

    def get(self):
        return self.data

    def len(self):
        return len(self.data)

    def append(self, value):
        self.data.append(value)

    def fromString(self, string):
        for c in string:
            self.data.append(c)