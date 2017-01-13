from datasource.idatasource import IDataSource as IDataSource


class DatasourceList(IDataSource):

    def __init__(self):
        self.data = []

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    def get(self):
        return self.data

    def len(self):
        return len(self.data)

    def append(self, value):
        self.data.append(value)

    def fromString(self, string):
        self.data.clear()
        for c in string:
            self.data.append(c)