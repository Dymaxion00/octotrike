#FIXME lock management
#FIXME change processing
#FIXME exceptions
#The set of changes in a model
class TChangeSet(object):
    def __init__(self, model):
        self.model = model
        self._changes = {} #changeID->change for every change in the system
        self._changeQueue = [] #changes received that we haven't processed


    #FIXME: change processing
    def enqueue(self, isCreation = False, targetID = None, targetKey = None,
                targetTypeID = None, eventTypeID, eventParams, branchID):
        """Create an event from the material passed in, wrap a change around
        it so we can manage its execution, and add it to the queue."""
        changeID = GUID()
        event = apply(TEvent.TypeIDs[eventTypeID], (changeID, isCreation, targetKey,
                                                    targetTypeID, eventParams))
        change = TChange(changeID, event, self.model,
                         self.model.branches.get(branchID).getLeafID(), [branchID])
        self._changesQueue.append(change)
        # Here we should trigger change processing sanely
        pass

    #FIXME Lock management
    def process(self, changeID, branchID):
        self.model.getBusy()
        #See TOBject for how queueing can work FIXME
        self.model.makeDirty()
        self._changes[changeID].apply()
        self.model.relax()
        pass
    
    #FIXME throw exception on not found
    def get(self, changeID):
        pass

    def register(self, changeID, change):
        self._changes[changeID] = change
        pass

    #FIXME exception handling if the change is already gone
    def unregister(self, changeID):
        self._changes.delete(changeID)
        pass

    def rollbackTo(self, changeID):
        """This hard-deletes changes from all branches.  Most of the time we want undo."""
        for branchID in self._changes[changeID].getBranches():
            self.model.branches.get(branchID).setLeaf(changeID)
        for child in self._changes[changeID].getChildren():
            self._changes[child].delete()
        pass
    
    def prune(self, changeID):
        newRoots = []
        newRoots.add(changeID)

        #If the tree branches above us, we'll need to create several synthetic roots
        for change in self._changes[changeID].getAncestorsOtherChildren():
            newRoots.add(change)

        for change in newRoots:
            self._changes[change].synthesizeRoot()
            
        for change in newRoots:
            self._changes[change].getParent().prune()
            
        #Tell every branch to reset it's root, because they've probably all changed
        for branchID in self.model.branches.getAllIDs():
            self.model.branches.get(branchID).resetRoot()

        #NB: This will often fragment the tree.  This is fine, because the system
        #operates fine across a forest.  This operation is not normally needed, but
        #is provided for situations where the model has grown very large over time.
        #Also, note that pruning can prevent branches from other versions of the model
        #being imported, as the changeIDs they attach to may be gone.
        pass

    def findOnlyInDown(self, rootChangeID, branchIDSet = None):
        if branchIDSet is None:
            branchIDSet = []
        self._changes[rootChangeID].findOnlyInDown(branchIDSet)
        #Finds changes from a given root only in the set of branches specified
        #If null, finds changes not in any branch
        pass

    def findFirstOnlyInDown(self, rootChangeID, branchIDSet = None):
        if branchIDSet is None:
            branchIDSet = []
        self._changes[rootChangeID].findFirstOnlyInDown(branchIDSet)
        #Finds the first change from a given root only in the set of branches specified.
        #If null, finds the first change not in any branch
        pass

    def findOnlyInUp(self, leafChangeID, branchIDSet = None):
        if branchIDSet is None:
            branchIDSet = []
        self._changes[leafChangeID].findOnlyInUp(branchIDSet)
        #Finds changes from a given leaf only in the set of branches specified
        #If null, finds changes not in any branch
        pass

    def unload(self):
        for change in self._changes:
            del change
        pass
    
