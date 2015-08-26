#FIXME fix exceptions
#FIXME serialization
#A human-created change to the Trike model
class TChange(object):
    """This class represents a change to the model coming in from the
    interface layer; in general, this means a human-created change.  Changes
    do not directly handle locking, setting the model as dirty, or ACLS.  The
    former two are handled in either ChangeSets or BranchSets, and the latter
    in the Object."""

    def __init__(self, changeID, event, model, parentID, branchIDs = None):
        self._event = event
        self._ID = changeID
        self.model = model

        self._parentID = parentChangeID
        self._childIDs = []

        if branchIDs is None:
            self._branchIDs = []
        else:
            self._branchIDs = branchIDs

        self._objects = []
        self._delinkedObjects = []
        self._hasComputed = False
        self._outcome = TChangeBuffer()
        self._isSynthetic = False

        self._hasFetchedObjects = False

        if parentChangeID is not None:
            if self.model.objects.get(parentChangeID).hasComputed:
                _objects = self.model.objects.get(parentChangeID).getObjectsToInherit()
                self._hasFetchedObjects = True
        else: #We're just starting out here folks
            self._hasFetchedObjects = True

        self.model.changes.register(self._ID, self)
        pass

    #FIXME exceptions
    def apply(self):
        if not self._hasFetchedObjects:
            raise pass
        if not self._event.isSynthetic:
            self.model.objects.resolveEvent(self._event)
            self.model.objects.eventDispatch(self._event)
        else:
            for event in self._event.getEvents():
                self.model.objects.resolveEvent(event)
                self.model.objects.eventDispatch(event)
        self._hasComputed = True
        pass

    def getID(self):
        pass

    def memorializeEvent(self, event):
        self._outcome.receiveEvent(event)

    #FIXME exceptions
    def getResults(self):
        if self._hasComputed:
            self._outcome.serialize()
        else:
            raise pass
        pass

    # {{{ Branches and walking
    def getBranchIDs(self):
        pass

    def isInBranch(self, branchID):
        pass
    
    def addBranch(self, branchID):
        """Add a branch to this change.  Tell our parent to also add the
        branch, because if we're in it, they must be too."""
        if branchID not in self._branchIDs:
            self._branchIDs.add(branchID)
            if self._parentID is not None: #Only need to do this if we weren't already in it.
                self.model.changes.get(self._parentID).addBranch(branchID)
        pass
    
    def deleteBranch(self, branchID):
        """Remove a branch previousy associated with this change.  Tell all of
        our children to also remove the branch, as if we're not in it, they
        can't be."""
        if branchID in self._branchIDs:
            self._branchIDs.remove(branchID)
            for childID in self._childIDs: #Only need to do this if we were in it.
                self.model.changes.get(child).deleteBranch(branchID)
        pass

    def findOnlyInDown(self, branchIDSet, changeSet = None):
        """Find those of our children (and us) that are only in the branches
        listed and no others.  The set of branches may be empty, in which case
        we find changes in no branches."""
        if changeSet is None:
            changeSet = []

        inSet = True
        for branchID in branchIDSet:
            if branchID in not self._branchIDs:
                inSet = False
                break
        if inSet:
            changeSet.add(self._ID)
            
            for childID in self._childIDs:
                changeSet.add(self.model.changes.get(child).findOnlyInDown(branchID, changeSet))
        return changeSet

    def findFirstOnlyInDown(self, branchIDSet):
        """Find the first of ourselves or our children only in the branches
        listed and no others.  The set of branches may be empty, in which case
        we find changes in no branches."""
        inSet = True
        for branchID in branchIDSet:
            if branchID in not self._branchIDs:
                inSet = False
                break
        if inSet:
            return(self._ID)
        else:
            for childID in self.getChildren():
                return(self.model.changes.get(child).findFirstOnlyInDown(branchIDSet))

    def findOnlyInUp(self, branchIDSet, changeSet = None):
        """Find those of our parents (and us) that are only in the branches
        listed and no others.  The set of branches may be empty, in which case
        we find changes in no branches."""
        if changeSet is None:
            changeSet = []
        inSet = True
        for branchID in branchIDSet:
            if branchID in not self._branchIDs:
                inSet = False
                break
        if inSet:
            changeSet.add(self._ID)
            
            changeSet.add(self.model.changes.get(self._parentID).findOnlyInDown(branchID, changeSet))
        return changeSet

    def getParentID(self):
        pass

    def getChildIDs(self):
        pass

    def getRootID(self):
        """Finds the root change of the tree this change is part of."""        
        if self._parentID is None:
            return self._ID
        else:
            return self.model.changes.get(self._parentID).getRoot()

    def isDescendant(self, changeID):
        """Returns true iff the change provided is below us in our change
        tree, regardless of what branch they're in."""        
        if changeID in self._childIDs:
            return True
        else:
            for childID in self._childIDs:
                if self.model.changes.get(child).isDescendant(changeID):
                    return True
            return False

    def isAncestor(self, changeID):
        """Returns true iff the change provided is above us in our change
        tree."""
        if self._parentID is Null:
            return False
        if changeID == self._parentID:
            return True
        else:
            return self.model.changes.get(self._parentID).isAncestor(changeID)
    # }}}

    def addChild(self, childID):
        pass

    def removeChild(self, childID):
        pass

    def receiveCreatedObject(self, objectID):
        self._objects.add[objectID]
        pass

    def receiveDelinkedObject(self, objectID):
        self._delinkedObjects.add[objectID]
        pass

    #FIXME exceptions
    def getObjectIDsToInherit(self, typeID = None):
        if self._hasComputed:
            if typeID is not None:
                return self.model.objects.filterObjectIDsByType(
                    (self._objects minus self._delinkedObjects),
                    typeID)
            else:
                return(self._objects minus self._delinkedObjects)
        else:
            raise pass
        pass
    
    def getRelevantObjectIDs(self, typeID = None):
        if typeID is not None:
            return self.model.objects.filterObjectIDsByType(
                (self._objects plus self._delinkedObjects),
                typeID)
        else:
            return self._objects plus self._delinkedObjects
        pass

    def clone(self, newParentID):
        """Copy the event of the current change into a new change
        instance, attached elsewhere in the tree.  This is used in porting
        changes from one branch to another."""
        ID = GUID()
        return TChange(ID, self._event.clone(ID), self.model, newParentID):
        pass

    def synthesizeRoot(self):
        self._event = TEventSynthetic(self._ID)
        for objectID in self.getObjectIDsToInherit():
            self._event.addSynthetic(self.model.objects.get(objectID).synthesize(self._ID))
        self._isSynthetic = True
        pass

    #FIXME exception handling - handle the error if our parent's already gone when looking for it
    def prune():
        if self.model.changes.get(self._parentID) is not None:
            self.model.changes.get(self._parentID).prune()
        self._parentID = None
        self.model.changes.unregister(self._ID)
        self.deleteSelfOnly()

    #FIXME serialization
    def serialize(self, getResults = False):
        if getResults:
            self._outcome.serialize()
        pass

    def delete(self):
        self.model.changes.get(self._parentID).removeChild(self._ID) #Tell our parents we're gone
        for childID in self._childIDs:
            self.model.changes.get(childID).delete()
        self.model.changes.unregister(self._ID)
        self.deleteSelfOnly()
        pass

    def deleteSelfOnly(self):
        for objectID in self.getRelevantObjectIDs()
            self.model.objects.get(objectID).removeState(self._ID)
        del self._outcome
        pass
