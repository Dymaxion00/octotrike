#FIXME exceptions
#FIXME serialization
class TBranch(object):
    def __init__(self, model, leafID, name = None):
        self.model = model
        self._ID = GUID()
        self._leafID = leafID
        self._rootID = None
        self._name = name

        self.model.branches.register(self._ID, self)
        if self._name is not None:
            self.model.branches.registerName(self._name, self._ID)
        self.resetRoot()
        pass

    def getID(self):
        pass

    def getLeafID(self):
        pass

    def setLeaf(self, newLeafID):
        if self.model.changes.get(newLeafID).isDescendant(self._leafID): #If the new leaf is below, extend
            self._leafID = newLeafID
            self.model.changes.get(newLeafID).addBranch(self._ID)
        else:
            if self.model.changes.get(newLeafID).isAncestor(self._leafID): #If the new leaf is above, contract
                for child in self.model.changes.get(newLeafID):
                    child.deleteBranch(self._ID)
                self._leafID = newLeafID
                else: #New leaf is in an entirely different tree
                    self.model.changes.get(self._leafID).deleteBranch(self._ID)
                    self.model.changes.get(newLeafID).addBranch(self._ID)
                    self._leafID = newLeafID
                    self._rootID = self.model.changes.get(newLeafID).getRoot()
        pass

    def getRootID(self):
        pass

    def resetRoot(self):
        """We never explicitly set the root of a branch.  If we've pruned the
        changeset, we tell all branches to find their current root instead,
        which prevents the tree pointers getting out of sync."""
        self._rootID = self.model.changes.get(self._leafID).getRoot()
        pass

    def undoBefore(self, changeID):
        """Creates a new unnamed branch with the same state as our current
        leaf, then sets our leaf to the parent of the change we're undoing."""
        self.model.branches.branchFrom(self._leafID)
        self.setLeaf(self.model.changes.get(changeID).getParent())
        pass

    #FIXME exeptions
    def redo(self, changeID):
        if not self.model.changes.get(self._leafID).isDescendant(changeID):
            raise pass #Fails unless changeID descends from branchID->leafID
        self.setLeaf(changeID)
        pass

    #FIXME serialization
    def serialize(self):
        pass

    def delete(self):
        self.model.changes.get(self._leafID).deleteBranch(self._ID)
        self.model.changes.get(self._rootID).findFirstOnlyInDown(self._ID).delete()
        self.model.branches.unregister(self._ID)
        if self._name is not None:
            self.model.branches.unregisterName(self._name)
        pass

    def deleteBranchOnly(self):
        self.model.changes.get(self._leafID).deleteBranch(self._ID)
        self.model.branches.unregister(self._ID)
        if self._name is not None:
            self.model.branches.unregisterName(self._name)
        pass

    
