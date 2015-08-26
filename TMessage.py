    # {{{ Service Messages
    def authenticate(self, user, key): pass
    def getUserSessions(self, user, token): pass
    def destroySession(self, token): pass
    def validateSession(self, token): pass
    def addUser(self, user, key, token): pass
    def deleteUser(self, user, token): pass
    def listUsers(self, token): pass
    def lockUser(self, user, token): pass
    def unlockUser(self, user, token): pass
    def addGroup(self, group, token): pass
    def deleteGroup(self, group, token): pass
    def listGroups(self, token): pass
    def setWSACL(self, newACL, token): pass
    def getWSACL(self, token): pass
    def serializeWSConfig(self, target, token): pass
    def setWSConfig(self, config, token): pass
    def setWSConfigItem(self, name, value, token): pass
    def shutdown(self, token): pass
    def serviceNotify(self, token): pass
    def createModel(self, token): pass
    def cloneModel(self, modelID, newName, token): pass
    def getModelIDs(self, token): pass
    def importModel(self, filename, token): pass
    def importSerializedModel(self, modelString, token): pass
    def exportModel(self, modelID, filename, token): pass
    def loadModel(self, modelID, token): pass
    def getLoadedModelIDs(self, token): pass
    def unloadModel(self, modelID, force=False, token): pass
    def deleteModel(self, modelID, force=False, token): pass
    # }}}

    # {{{ Model Management Messages
    def unload(self, force=False, token): pass
    def getName(self, token): pass
    def setName(self, name, token): pass
    def getModelCodeVersion(self, token): pass
    def setConfig(self, config, token): pass
    def getConfigItem(self, name, token): pass
    def setConfigItem(self, name, value, token): pass
    def setACL(self, newACL, token): pass
    def getACL(self, token): pass
    def lockSingleUser(self, user, session, force=False, token): pass
    def unlockSingleUser(self, user=Null, session=Null, force=False, token): pass
    def isSingleUser(self, token): pass
    def notify(self, token): pass
    def isDirty(self, token): pass
    def save(self, token): passa
    # }}}

    # {{{ Change Management Messages
    def receiveChange(self, eventTypeID, eventParams, branchID): pass
    def rollbackToChange(self, changeID, token): pass
    def prune(self, changeID, token): pass
    # }}}

    # {{{ Branch Management Messages
    def getAllNamedBranches(self, token): pass
    def getAllBranches(self, token): pass
    def getCurrentLeafForBranch(self, branchID, token): pass
    def getBranchName(self, branchID, token): pass
    def getBranchByName(self, branchName, token): pass
    def setBranchName(self, branchID, name, token): pass
    def undoChangesBefore(self, branchID, changeID, token): pass
    def redoChanges(self, branchID, changeID, token): pass
    def portChange(self, changeID, branchID, token): pass
    def receiveBranch(self, name, attachToChangeID, changeSet, token): pass
    def branchFrom(self, changeID, name = null, token): pass
    def deleteBranch(self, branchID, token): pass
    def deleteUnamedBranches(self, token): pass
    # }}}

    # {{{ Serialization Messages
    def serializeModelLifetime(self, clean=False, token): pass
    def serializeModelAt(self, changeID = None, branchID = None, token): pass
    def serializeBranches(self, token): pass
    def getChangeIDsInBranch(self, branchID, token): pass
    def getChangeIDsAfterXInBranch(self, branchID, changeID, token): pass
    def serializeChange(self, changeID, getResults = False, token): pass
    def serializeChangeResults(self, changeID, token): pass
    def serializeChangesInBranch(self, branchID, getResults = False, token): pass
    def serializeChangesInBranchAfterX(self, branchID, changeID, getResults, token): pass
    def getObjectIDsAt(self, changeID = None, branchID, = None, typeID = None, token): pass
    def serializeObjectLifetime(self, objectID, token): pass
    def serializeObjectAt(self, objectID, changeID = None, branchID = None, token): pass
    def serializeObjectsByTypeAt(self, typeID, changeID = None, branchID = None, token): pass
    def serializeConfig(self, token): pass
    # }}}

    # {{{ Trike Messages
    def createActor(self, newName, newType = None, FavoredUser = None, branchID, token): pass
    def renameActor(self, objectID, newName, branchID, token): pass
    def setActorType(self, objectID, newType, branchID, token): pass
    def unsetActorType(self, objectID, branchID, token): pass
    def makeFavoredUser(self, objectID, branchID, token): pass
    def makeNotFavoredUser(self, objectID, branchID, token): pass
    def unsetFavoredUser(self, objectID, branchID, token): pass
    def deleteActor(self, objectID, branchID, token): pass
    
    def createDataObject(self, newName, isAsset = None, branchID, token): pass
    def renameDataObject(self, objectID, newName, branchID, token): pass
    def makeAsset(self, objectID, branchID, token): pass
    def makeNotAsset(self, objectID, branchID, token): pass
    def unsetAsset(self, objectID, branchID, token): pass
    def deleteDataObject(self, objectID, branchID, token): pass

    def setCreateAllowed(self, actorName, assetName, value, branchID, token): pass
    def unsetCreateAllowed(self, actorName, assetName, branchID, token): pass
    def setCreateRules(self, actorName, assetName, value, branchID, token): pass
    def unsetCreateRules(self, actorName, assetName, branchID, token): pass
    # }}}
