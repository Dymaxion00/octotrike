#FIXME serialization
#Holds state for an object at a specific changeID
class TState(object):
    def __init__(self, model = None, previousStateID = None, initialState = None, prototype = False):
        self.model = model
        self._ID = GUID()
        self._key = ""
        self._objectDelinked = False
        self._store = {} #Key, Value

        if initialState is not None:
        
            if previousStateID is not None:
                previousState = self.model.objects.getState(previousStateID)
                for name in previousState.getNames():
                    self.setValue(name, previousStategetValue(name))
        else:
            for name in initialState.keys():
                self._store[name] = initialState[name]

        if not prototype:
            self.model.objects.registerState(self._ID, self)
        pass

    def getID(self):
        pass

    def getKey(self):
        pass
    def setKey(self):
        pass

    def objectIsDelinked(self):
        return self._objectDelinked
    def objectDelinked(self):
        self._objectDelinked = True
        self.clearStates()

    def getNames(self):
        pass
    def isSet(self, name):
        pass
    def getValue(self, name):
        pass
    def setValue(self, name):
        pass
    def dropValue(self, name):
        pass
    def clearStates(self):
        self._store = {}

    #FIXME serialization
    def serialize(self):
        pass
    
