#FIXME Service changes?
#FIXME redo model serialization API
#FIXME Notifiers
#FIXME ACLs
#FIXME locks
#FIXME isDirty
#FIXME SingleUserMode
#Represents a single Trike model
class TModel(object):
    def __init__(self):
        self.objects = TObjectSet(self)
        self.changes = TChangeSet(self)
        self.branches = TBranchSet(self)
        self._ID = GUID()
        self.config = TConfig(model)

        self._dirty = False #Have we changed since load or writeout
        self._busy = False #Lock for serialization

        pass

    # {{{ model management
    #FIXME locks
    def load(self, target):
        pass #returns the most recent ChangeID

    #FIXME locks
    #FIXME isDirty
    #FIXME ACLModelAdmin
    #FIXME SingleUser
    def unload(self, force=False): #WEBMETHOD
        #shuts down model, removes objects from memory
        self.changes.unload()
        self.branches.unload()
        self.objects.unload()
        pass

    #FIXME ACLModelRead
    def getName(self): #WEBMETHOD
        pass

    #FIXME ACLModelAdmin
    #FIXME isDirty
    #FIXME SingleUser
    def setName(self, name): #WEBMETHOD
        pass

    #FIXME ACLModelRead
    def getModelCodeVersion(self): #WEBMETHOD
        pass #what Trike version is this data for?

    #FIXME ACLModelAdmin
    #FIXME isDirty
    #FIXME SingleUser
    def setConfig(self, config): #WEBMETHOD
        pass

    #FIXME ACLModelRead
    def getConfigItem(self, name): #WEBMETHOD
        pass

    #FIXME ACLModelAdmin
    #FIXME isDirty
    #FIXME SingleUser
    def setConfigItem(self, name, value): #WEBMETHOD
        pass

    #FIXME ACLModelAdmin
    #FIXME isDirty
    #FIXME SingleUser
    def setACL(self, newACL): #WEBMETHOD
        pass

    #FIXME ACLModelRead
    def getACL(self): #WEBMETHOD
        pass

    #FIXME ACLModelAdmin
    #FIXME SinglUser
    def lockSingleUser(self, user, session, force=False): #WEBMETHOD
        pass

    #FIXME ACLModelAdmin
    #FIXME SingleUser
    def unlockSingleUser(self, user=Null, session=Null, force=False): #WEBMETHOD
        pass

    #FIXME ACLModelRead
    def isSingleUser(self): #WEBMETHOD
        pass

    #FIXME ACLModelRead
    def notify(self): #WEBMETHOD
        pass #returns when anything changes in the model, for UI coordination

    #FIXME ACLModelRead
    def isDirty(self): #WEBMETHOD
        pass #have we changed since we were loaded

    def makeDirty(self):
        pass

    #FIXME ACLModelWrite
    def save(self): #WEBMETHOD
        pass #Save ourselves to disk

    def isBusy(self):
        pass #lock used for serialization

    def getBusy(self): #Acquire lock
        pass

    def relax(self): #Drop lock
        pass

    def getModelAPIDoc(self): #WEBMETHOD
        #Returns documentation about the API
        pass

    def getTrikeDoc(self): #WEBMETHOD
        #Returns documentation about Trike
        pass

    def getTypeConstants(self): #WEBMETHOD
        #Returns the GUIDs used for messages, events, TObject types, and TObject handlers
        pass
    # }}}

    # {{{ change management
    #FIXME locks
    #FIXME ACLModelWrite
    #FIXME SingleUser
    def receiveChange(self, isCreation = False, targetID = None, targetKey = None,
                      targetTypeID = None, eventTypeID, eventParams, branchID): #WEBMETHOD
        self.changes.enqueue(isCreation, targetID, targetKey, targetTypeID,
                             eventTypeID, eventParams, branchID)
        pass

    #FIXME locks
    #FIXME ACLModelWrite
    #FIXME SingleUser
    def rollbackToChange(self, changeID): #WEBMETHOD
        """This hard-deletes all changes below this one from all branches.
        Most of the time you want undo."""
        self.changes.rollbackTo(changeID)
        pass

    #FIXME locks
    #FIXME ACLModelWrite
    #FIXME SingleUser
    def prune(self, changeID): #WEBMETHOD
        self.changes.prune(changeID)
        pass
    # }}}

    # {{{ branch management
    #FIXME ACLModelRead
    def getAllNamedBranches(self): #WEBMETHOD
        """Returns name, ID pairs for all named branches."""
        self.branches.getNamed()
        pass

    #FIXME ACLModelRead
    def getAllBranches(self): #WEBMETHOD
        """Returns all branch IDs."""
        self.branches.getAllIDs()
        pass

    #FIXME ACLModelRead
    def getCurrentLeafForBranch(self, branchID): #WEBMETHOD
        self.branches.get(branchID).getLeaf()
        pass

    #FIXME ACLModelRead
    def getBranchName(self, branchID): #WEBMETHOD
        self.branches.getName(self.branches.get(branchID))
        pass

    #FIXME ACLModelRead
    def getBranchByName(self, branchName): #WEBMETHOD
        """Returns the ID of a branch by name."""
        self.branches.getByName(branchName).getID()
        pass

    #FIXME locks
    #FIXME ACLModelWrite
    #FIXME SingleUser
    def setBranchName(self, branchID, name): #WEBMETHOD
        self.branches.get(branchID).setName(name)
        pass

    #FIXME locks
    #FIXME ACLModelWrite
    #FIXME SingleUser
    def undoChangesBefore(self, branchID, changeID): #WEBMETHOD
        """Returns the ID of the new undoBranch and the new leaf ID of the main branch."""
        self.branches.get(branchID).undoBefore(changeID)
        pass

    #FIXME locks
    #FIXME ACLModelWrite
    #FIXME SingleUser
    def redoChanges(self, branchID, changeID): #WEBMETHOD
        self.branches.get(branchID).redo(changeID)
        pass

    #FIXME locks
    #FIXME ACLModelWrite
    #FIXME SingleUser
    def portChange(self, changeID, branchID): #WEBMETHOD
        self.branches.port(changeID, branchID)
        pass

    #FIXME locks
    #FIXME ACLModelWrite
    #FIXME SingleUser
    def receiveBranch(self, name, attachToChangeID, changeSet): #WEBMETHOD
        self.branches.receive(name, attachToChangeID, changeSet)
        pass

    #FIXME locks
    #FIXME ACLModelWrite
    #FIXME SingleUser
    def branchFrom(self, changeID, name = null): #WEBMETHOD
        self.branchFrom(changeID, name)
        pass

    #FIXME locks
    #FIXME ACLModelWrite
    #FIXME SingleUser
    def deleteBranch(self, branchID): #WEBMETHOD
        self.branches.get(branchID).delete()
        pass

    #FIXME locks
    #FIXME ACLModelWrite
    #FIXME SingleUser
    def deleteUnamedBranches(self): #WEBMETHOD
        self.branches.deleteUnamed()
        pass
    # }}}

    # {{{ model serialization
    #FIXME ACLModelRead
    #FIXME ACLModelWrite
    #FIXME locks
    #FIXME serialization
    def serializeModelLifetime(self, clean=False): #WEBMETHOD
        """Serialize out everything about this model, including all state,
        changes, change results, branches, and configuration.  If clean is
        set, assume we're flushing ourselves to disk, require ACLModelWrite
        and clear isDirty."""
        pass

    #FIXME ACLModelRead
    #FIXME locks
    #FIXME serialization
    def serializeModelAt(self, changeID = None, branchID = None): #WEBMETHOD
        """Serialize the state of the model at either a specific change or at
        the leaf of a specific branch.  At least one of these two must be
        specified.  Does not include configuration or any history."""
        pass

    #FIXME ACLModelRead
    def serializeBranches(self): #WEBMETHOD
        """Serialize the root and leaf IDs and names of all branches."""
        self.branches.serialize()
        pass

    #FIXME ACLModelRead
    #FIXME serialization
    def getChangeIDsInBranch(self, branchID): #WEBMETHOD
        """Return all of the changeIDs in the given branch in order, from root
        to leaf."""
        pass

    #FIXME ACLModelRead
    #FIXME serialization
    def getChangeIDsAfterXInBranch(self, branchID, changeID): #WEBMETHOD
        """Return a list of all changeIDs more recent than the given one in a
        given branch.  We walk up the branch from the leaf, on the assumption
        that this will nornmally be used to find changes near the leaf."""
        pass

    #FIXME ACLModelRead
    def serializeChange(self, changeID, getResults = False): #WEBMETHOD
        """Serialize a change in the same form it is submitted to a model.  If
        results are asked for, serialize the results of the change as well."""
        changes.get(changeID).serialize(getResults)
        pass

    #FIXME ACLModelRead
    def serializeChangeResults(self, changeID): #WEBMETHOD
        """Serialize just the results of a change."""
        self.changes.get(changeID).getResults()
        pass

    #FIXME ACLModelRead
    #FIXME serialization
    def serializeChangesInBranch(self, branchID, getResults = False): #WEBMETHOD
        """Serialize all changes in a branch from root to leaf, optionally
        including their results."""
        pass

    #FIXME ACLModelRead
    #FIXME serialization
    def serializeChangesInBranchAfterX(self, branchID, changeID, getResults): #WEBMETHOD
        """Serialize all changes in a branch after the specified change,
        optionally including their results."""
        pass

    #FIXME ACLModelRead
    #FIXME locks
    def getObjectIDsAt(self, changeID = None, branchID, = None, typeID = None): #WEBMETHOD
        """Return all objectIDs at a given change or at the leaf of a given
        branch (at least one must be specified).  Optionally, restrict the set
        to objects of the specified type."""
        if changeID is not None:
            self.changes.get(changeID).getRelevantObjectIDs(typeID)
        else:
            if branchID is not None:
                self.changes.get(self.branches.get(branchID).getLeafID()).getRelevantObjectIDs(typeID)
            else:
                raise pass
        pass

    #FIXME ACLModelRead
    def serializeObjectLifetime(self, objectID): #WEBMETHOD
        """Serialize the entire lifetime of the given object."""
        self.objects.get(objectID).serialize()
        pass

    #FIXME ACLModelRead
    def serializeObjectAt(self, objectID, changeID = None, branchID = None): #WEBMETHOD
        """Serialize the specified object at either the given change or at the
        leaf of the given branch."""
        if changeID is not None:
            self.objects.get(objectID).serialize(changeID)
        else:
            if branchID is not None:
                self.objects.get(objectID).serialize(self.branches.get(branchID).getLeafID().getID())
            else:
                raise pass
        pass

    #FIXME ACLModelRead
    #FIXME locks
    #FIXME Exceptions
    def serializeObjectsByTypeAt(self, typeID, changeID = None, branchID = None): #WEBMETHOD
        """Serialize all objects of a given type at either a specific change
        or at the leaf of the specified branch.  If objects of all types are
        desired, use SerializeModelAt() instead."""
        if changeID is not None:
            objects.serialize(changeID, typeID)
        else:
            if branchID is not None:
                objects.serialize(branches.get(branchID).getLeaf.getID(), typeID)
            else:
                raise pass
        pass

    #FIXME ACLModelRead
    def serializeConfig(self): #WEBMETHOD
        """Serialize the current configuration of the model."""
        config.serialize()
        pass
    # }}}

