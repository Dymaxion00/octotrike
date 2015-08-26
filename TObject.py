#FIXME class method to register TypeIDs
#FIXME objects that skip changeIDs
#FIXME Synthesize object at change; make sure we're initialized first
#FIXME event processing
#FIXME serialization
#An object in a Trike model
class TObject(object):
    self.TypeIDs = {"A2FA65E6E5724BC5B80EF4962B758EDF": TrikeActor,
                    "8C376D6B0C3B4CC780371D7077AC5616": TrikeDataObject,
                    "BF8D00BEC957405CA926043E340FBD08": TrikeActionSet}

    def __init__(self, model, typeID, changeID):
        self._ID = GUID()
        self.model = model
        self._typeID = typeID
        self._stateIDs = {} #changeID->stateID mapping for all changes
        self._stateIDs[changeID] = TState(model, None, self.TypeIDs[typeID].initialState)
        model.registerObject(self.typeID, self.id, self)

        self._eventQueue = []
        self._working = False

        self._wChangeID = None
        self._wState = None
        pass

    def getID(self):
        pass
    
    def getKey(self, changeID):
        self.model.objects.getState(self._stateIDs[changeID]).getKey()
        pass

    #FIXME exceptions
    def _setKey(self, newKey):
        if not self._working: raise pass
        if self.model.objects.getByKey(self._typeID, self._wChangeID, newKey) is not None:
            self._wState.setKey(newKey)

    def getTypeID(self):
        pass

    def initForChange(self, changeID):
        # First event we've received for this change
        if changeID() not in self.stateIDs:
            self._stateIDs[changeID] = TState(model,
                                              self.states[model.changes.get(changeID).getParent()]).getID()
            
        

    #FIXME: objects that get no events for more than one change
    def receiveEvent(self, event):
        self.initForChange(event.getChangeID())
        self.eventQueue.append(event)

        if not self.working:
            self._working = True
            self._wChangeID = event.getChangeID()
            self._wState = model.objects.getState(self._stateIDs[self._wChangeID])
            self._processEvent()
        else:
            return
        pass

    #FIXME event processing
    def _processEvent(self):
        ev = self._eventQueue.pop()
        #Event handlers for objects that already exist are called here.
        apply(self.TypeIDs[self._typeID].handlers[ev.getTypeID], ev.getParams())

        #handle event, sending new events to other objects as needed
        #push every state change event into the response buffer so the UI
        #knows what happened


        #check if we've got events in the queue (received while we were working)
        #if so, call ourself again with the first event in the queue
        #otherwise, we're all done:
        self._working = False
        self._wChangeID = None
        self._wState = None
        pass

    def _sendEvent(self, eventTypeID, targetTypeID, targetKey, params):
        #We don't send any events during synthetic change creation
        if model.changes.get(self._wChangeID).isSynthetic():
            return
        event = TEvent.TypeIDs[eventTypeID](self._wChange,
                                            targetKey = targetKey,
                                            targetTypeID = targetTypeID,
                                            params)
        self.model.objects.resolveEvent(event)
        self.model.objects.dispatchEvent(event)
        pass

    def isAliveAtChange(self, changeID):
        self.initForChange(changeID)
        return not model.objects.getState(self._states[changeID]).objectIsDelinked()
    
    def _delink(self):
        """Called by processEvent() in cases where the this object should be
        deleted as a result of messages received in this change, to let us
        notify the relevant objects."""
        self._wState.objectDelinked()
        model.changes.get(self._wChangeID).receiveDelinkedObject(self._ID)
        pass

    #FIXME Synthesize object at change; make sure we're initialized first
    # This must be implemented by our subclasses
    def synethesize(self, changeID):
        """Return a creationEvent with the current state embedded in it."""
        self.initForChange
        raise NotImplemented

    #FIXME serialization
    def serialize(self, changeID = None):
        #Serialize ID, typeID
        if changeID is None:
            for state in states:
                pass #Serialize state
        else:
            pass #Serialize states[changeID] unless we don't exist for
                 #this state, then return <delinked>
        pass

    def delete(self):
        """We're being deleted for good, likely as part of a prune or unload."""
        model.objects.unregister(self._typeID, self._ID)
        for stateID in self._stateIDs:
            model.objects.unregisterState(stateID)
        pass

