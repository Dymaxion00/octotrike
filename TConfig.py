#FIXME serialization
#Configuration class for TModels and TServices
class TConfig(object):
    def __init__(self, model):
        self._store = {}
        self.model = model
        pass

    def getNames(self):
        pass

    def isSet(self, name):
        pass

    def getValue(self, name):
        pass

    def setValue(self, name, value):
        pass

    def dropValue(self, name):
        pass

    #FIXME Serialization
    def serialize(self):
        pass

