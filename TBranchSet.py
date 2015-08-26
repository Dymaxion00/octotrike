#FIXME exceptions
#FIXME receiveBranch
#FIXME serialization
#The set of branches in a model
class TBranchSet(object):
    def __init__(self, model):
        self.model = model
        self._branches = {} #branchID->branch
        self._names = {} #name->branchID
        pass

    def register(self, branchID, branch):
        pass

    #FIXME raise exception if branch not found
    def unregister(self, branchID):
        pass

    #FIXME raise exception if branch not found
    def get(self, branchID):
        pass

    def registerName(self, name, branchID):
        pass

    #FIXME raise exception if name not found
    def unregisterName(self, name):
        pass

    #FIXME raise exception if name not found
    def getByName(self, name):
        pass #returns the branch

    def getAllNamed(self):
        pass #returns name, ID pairs for all named branches

    def getAllIDs(self):
        pass #gets all branchIDs

    def branchFrom(self, changeID, name = None):
        root = self.model.changes.get(changeID) #Call this first to make sure the change exists
        newBranch = TBranch(self.mode, changeID, name)
        root.addBranch(newBranch.getID())
        if name is not None:
            self.registerName(name, newBranch.getID())
        return newBranch.getID()
        pass

    #FIXME exceptions
    def port(self, changeID, branchID):
        if self.model.changes.get(changeID).isInBranch(branchID): raise pass
        self.model.changes.enqueue(self.model.changes.get(changeID).
                                   clone(_branches[branchID].getLeaf()))
        pass

    #FIXME event resolution and creation, change dispatch, etc.
    #FIXME exceptions
    def receive(self, name, attachToChangeID, changeSet):
        """Lands an entire branch of changes in order, branching from the
        attachToChangeID.  If an error occurs at any point, the entire branch
        is rolled back and deleted.  Received branches cannot have synthetic
        roots, and the attachment point must exist.  This is required to
        ensure that object IDs are generally coherent."""
        newID = self.branchFrom(attachToChangeID, name)
        try:
            for change in changeSet:
                if change.isSynthetic: raise pass
                self.model.changes.enqueue(change, newID) #FIXME here
        except:
            self.model.changes.rollbackTo(attachToChangeID)
            raise pass
        pass

    #FIXME serialization
    def serialize(self):
        for branch in self._branches.values():
            branch.serialize()

    def deleteUnamed(self):
        unnamed = []
        for branchID in self._branches.keys:
            if branchID not in self._names.values:
                unnamed.add(branchID)
        
        for branchID in unnamed:
            self._branches[branchID].delete()
        pass

    def unload(self):
        for branch in self._branches:
            branch.delete()
        pass
