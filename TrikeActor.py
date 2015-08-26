#FIXME synthesize
#FIXME deletion
#FIXME class method to register TypeIDs with TObject
#FIXME flesh out the miniTrikemodel
#FIXME split this into separate files
#A Trike Actor
class TrikeActor(TObject):

    self.TypeID = #FIXME
    #FIXME class method to register TypeIDs with TObject
    #Which function should TObject.processEvent() call for events
    self.handlers = {"832E5EC291334D2193A9D51D90ADAFEA": self.__dict__[create], #TEVentCreateActor
                     "8DBFB5BFDD0B485AA037FFBEABC65CC3": self.__dict__[rename], #TEventRenameActor
                     "DA1E0FF394494772835956FEB9EEB694": self.__dict__[setType], #TEventSetActorType
                     "8DA1D94500C94441815F71CF8F28CEFE": self.__dict__[unsetType], #TEventUnsetActorType
                     "6E5F1DCE9CA34B519649306973FC3EB6": self.__dict__[makeFavoredUser], #TEventMakeFavoredUser
                     "2D3DC63D80564C06AF99D767401984F8": self.__dict__[makeNotFavoredUser], #TEventMakeNotFavoredUser
                     "5710BEFD4F3C426C80DE44AA3E41A84B": self.__dict__[unsetFavoredUser], #TEventUnsetFavoredUser
                     "D54741C973764E7394596AC3053796CD": self.__dict__[delete]} #TEventDeleteActor

        self.addListener(TEventCreateDataObject, self.__dict__[handleNewDataObject])


    self.initialState = TState(prototype = True)
    self.initialState.setValue("name", "")
    self.initialState.setValue("type", None)
    self.initialState.setValue("isFavoredUser", None)
    #self.description = ""
    #self.isAuthenticated = None        #self.isAttacker = None
    #self.usesSystem = None        #self.usedBySystem = None
    #self.isShared = None        #self.hasSharedResources = None

    self.Types = ["Component Process", "Execution Environment", "External Interactor"]

    def __init__(self, model, creationEvent):
        super.__init__(self, TOType.TrikeActor, creationEvent.getChangeID())
        self.receiveEvent(creationEvent)
        pass

    def create(self, params): #name, type, isFavoredUser
        self._wState.setValue("name", params["name"])
        self._wState.setValue("type", params["type"])
        self._wState.setValue("isFavoredUser", params["isFavoredUser"])

        self._sendEvent(TEventActorCreated.TypeID, TrikeDataObject.TypeID, {"name": params["name"]})

 
    def rename(self, params):
        self._wState.setValue("name", params["name"])
        self._setKey()
        pass

    def _setKey(self):
        super._setKey(self._wState.getValue("name"))
        pass

    def setType(self, params): #type
        pass

    def unsetType(self, params):
        pass

    def makeFavoredUser(self, params):
        pass

    def makeNotFavoredUser(self, params):
        pass

    def unsetFavoredUser(self, params):
        pass

    #FIXME deletion
    def delete(self, params):
        super._delink()
        pass

    #FIXME synthesize
    def synthesize(self, changeID):
        pass

    
class TrikeDataObject(TObject):
    self.Types = ["Data", "Software", "Hardware Data Container", "Software Data Container"]

    def __init__(self, creationEvent):
        super.__init__(self, TOType.TrikeDataObject, creationEvent.getChangeID())

        self.name = ""
        #self.description = ""
        self.isAsset = None
        #self.isShared = None        #self.isTransient = None
        pass

    def rename(self, newName):
        pass

    def makeAsset(self):
        pass

    def makeNotAsset(self):
        pass

    def unsetAsset(self):
        pass


class TrikeActionSet(TObject):
    self.ActionValues = ["Unknown", "N/A", "Always", "Sometimes", "Never"]

    def __init__(self, creationEvent):
        super.__init__(self, TOType.TrikeAction, creationEvent.getChangeID())

        self.Actor = None
        self.Asset = None
        
        self.isCreateAllowed = self.ActionValues[0]
        #self.isReadAllowed = self.ActionValues[0]        #self.isUpdateAllowed = self.ActionValues[0]
        #self.isDeleteAllowed = self.ActionValues[0]        #self.iseXecuteAllowed = self.ActionValues[0]
        #self.isconFigureAllowed = self.ActionValues[0]
        self.createRules = None
        #self.readRules = ""        #self.updateRules = ""
        #self.deleteRules = ""        #self.executeRules = ""
        #self.configureRules = ""
        pass

    def setCreateAllowed(self, value):
        pass

    def unsetCreateAllowed(self, value):
        pass

    def setCreateRules(self, rules):
        pass

    def unsetCreateRules(self, rules):
        pass
    
