#FIXME exceptions
#FIXME serialization
#The set of objects in a model
class TObjectSet(object):
    """This class holds the set of objects in a model, the type of those
    objects, and their states at different changeIDs.  It is responsible for
    looking objects up by key or ID, resolving the targets of events, and
    dispatching events to the relevant objects."""

    def __init__(self, model):
        self.model = model
        self._objects = {} #objectID->object for every object in the system
        self._types = {} #typeID->[objectID] for every object in the system??
        self._states = {} #stateID->state for every state in the system
        pass

    #NB: We manage neither locking nor model dirtyness

    def register(self, typeID, objectID, object):
        pass

    #FIXME exceptions
    def get(self, objectID):
        pass

    def getByKey(self, typeID, changeID, key):
        for objectID in self._types[typeID]:
            if key == self._objects[objectID].getKey(changeID):
                return objectiD
        return None
        pass

    def resolveEvent(self, event):
        if event.getTargetKey() is not None:
            targetID = self.getByKey(event.getTargetTypeID(),
                                     event.getChangeID(), event.getTargetKey())
            event.resolve(targetID)
        pass

    #Event handlers for objects that don't exist yet (object creation)
    #are applied here.
    def eventDispatch(self, event): #Events should be resolved before dispatching
        #Synthetic events must be broken up before dispatching
        if event.isSynthetic(): raise pass 

        changeID = event.getChangeID()
        if event.isCreation():
            TObject.TypeIDs[event.getTargetTypeID()](model, changeID, event)

        if event.getTarget() is None:
            if event.getTargetTypeID() is None:
                for object in self._objects.values():
                    if object.isAliveAtChange(changeID):
                        object.receiveEvent(event)
            else:
                for objectID in self._types[event.getTargetTypeID()]:
                    if self._objects[objectID].isAliveAtChange(changeID):
                        self._objects[objectID].receiveEvent(event)
        else:
            self._objects[event.getTarget()].receiveEvent(event)
        self.model.changes.get(changeID).memorializeEvent(event)


    def filterObjectIDsByType(self, objectIDSet, typeID):
        results = []
        for objectID in objectIDSet:
            if objectID in self._types[typeID]:
                results.add(objectID)
        return results

    def unregister(self, typeID, objectID):
        #Used when deleting an object
        pass

    def registerState(self, stateID, state):
        pass

    #FIXME exceptions
    def getState(self, stateID):
        pass

    #FIXME serialization
    def serialize(changeID = None, typeID = None):
        if changeID is not None:
            for objectID in self.model.changes.get(changeID).getRelevantObjectIDs():
                if typeID is not None:
                    if objectID in self._types[typeID]:
                        self._objects[objectID].serialize(changeID)
                else:
                    self._objects[objectID].serialize(changeID)
        else:
            if typeID is not None:
                for object in self._types[typeID]:
                    self._objects[objectID].serialize()
        else:
            for object in self._objects.values():
                object.serialize()
        pass

    def unregisterState(self, stateID):
        #Used when deleting a state
        pass

    def unload(self):
        for object in self._objects:
            object.delete()
        for state in self._states:
            state.delete()
        pass
    
