#An event passed between objects
#FIXME class method to register event type IDs
#FIXME self.TypeID per type
class TEvent(object):
    self.TypeIDs = {"C6ACD4DAEE9A4030B58088D901CBB37F": TEventSynthetic,
                    "832E5EC291334D2193A9D51D90ADAFEA": TEVentCreateActor,
                    "": TEventActorCreated,
                    "8DBFB5BFDD0B485AA037FFBEABC65CC3": TEventRenameActor,
                    "": TEventActorRenamed,
                    "DA1E0FF394494772835956FEB9EEB694": TEventSetActorType,
                    "8DA1D94500C94441815F71CF8F28CEFE": TEventUnsetActorType,
                    "6E5F1DCE9CA34B519649306973FC3EB6": TEventMakeFavoredUser,
                    "2D3DC63D80564C06AF99D767401984F8": TEventMakeNotFavoredUser,
                    "5710BEFD4F3C426C80DE44AA3E41A84B": TEventUnsetFavoredUser,
                    "D54741C973764E7394596AC3053796CD": TEventDeleteActor,
                    "F3544CC4C3C3441C8873D6601F14D1D8": TEventCreateDataObject,
                    "DBB3A77DDEC64694B22583A9C4246816": TEventRenameDataObject,
                    "0D1B455664ED41A39F46D46F44C2CFDD": TEventMakeAsset,
                    "55F1ED222616479DA953A0E5A4603368": TEventMakeNotAsset,
                    "1F1F9497CA454B01B765C98890FEC3A2": TEventUnsetAsset,
                    "1000C7F55AB049969011AB1107D086F5": TEventDeleteDataObject,
                    "0A104426A2A64F118E297CDFACD4DB01": TEventSetCreateAllowed,
                    "1AC690A271834656AC4D460BBA5CDB7D": TEventUnsetCreateAllowed,
                    "A08F75611E9247009B9E5DEED1F6B5FA": TEventSetCreateRules,
                    "6BA0180D2E5F439DB649EEA2569515D5": TEventUnsetCreateRules}
    #FIXME eventTypeID shouldn't be necessary when calling with subclass
    def __init__(self, changeID, isCreation = False, targetID = None,
                 targetKey = None, targetTypeID = None, eventTypeID, eventParams)
        self._changeID = changeID
        self._isCreation = isCreation
        self._targetID = targetID
        self._targetKey = targetKey
        self._targetTypeID = targetTypeID
        self._type = eventTypeID
        self._params = eventParams
        self.isSynthetic = False
        pass

    def getChangeID(self):
        #which external change ID we're associated with
        pass
    def isCreation(self):
        pass
    def getTypeID(self):
        pass
    def getTargetID(self):
        pass
    def getTargetKey(self):
        pass
    def getTargetTypeID(self):
        pass
    def getParams(self):
        pass
    def resolve(self, targetID):
        self._targetID = targetID
        self._targetKey = None
        pass
    
    def clone(self, changeID):
        return self.TypeIDs[self._type](changeID, self._target, self._targetType,
                                        self._type, self._params)
        pass


class TEventSynthetic(TEvent):
    def __init__(self, changeID):
        super.__init__(changeID, "C6ACD4DAEE9A4030B58088D901CBB37F", {})
        self._events = []
        self.isSynthentic = True
    
    def addSynthetic(self, event):
        self._events.append(event)

    def getEvents(self):
        return self._events

    def clone(self, changeID):
        ev = self.TypeIDs[self._type](changeID)
        for event in self._events:
            ev.addSynthetic(event.clone())
        return ev


class TEVentCreateActor(TEvent): pass #newName, newType = None, favoredUser = None
class TEventRenameActor(TEvent): pass #newName
class TEventSetActorType(TEvent): pass #newType
class TEventUnsetActorType(TEvent): pass
class TEventMakeFavoredUser(TEvent): pass
class TEventMakeNotFavoredUser(TEvent): pass
class TEventUnsetFavoredUser(TEvent): pass
class TEventDeleteActor(TEvent): pass
class TEventCreateDataObject(TEvent): pass #newName, isAsset = None
class TEventRenameDataObject(TEvent): pass #newName
class TEventMakeAsset(TEvent): pass
class TEventMakeNotAsset(TEvent): pass
class TEventUnsetAsset(TEvent): pass
class TEventDeleteDataObject(TEvent): pass
class TEventSetCreateAllowed(TEvent): pass #actorName, assetName, value
class TEventUnsetCreateAllowed(TEvent): pass #actorName, assetName
class TEventSetCreateRules(TEvent): pass #actorName, assetName, value
class TEventUnsetCreateRules(TEvent): pass #actorName, assetName
