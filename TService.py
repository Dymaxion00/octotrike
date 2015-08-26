#FIXME need classes for users, sessions, keys, groups, ACLs
#FIXME make this an actual WS
#FIXME figure out our threading model
#Root class for the Trike web service
class TService(object):
    #Root class for a trike web service; manages creation of models
    def authenticate(self, user, key): #WEBMETHOD
        pass #returns session token

    def getUserSessions(self, user): #WEBMETHOD
        pass

    def destroySession(self, session): #WEBMETHOD
        pass

    def validateSession(self, session):
        pass

    def addUser(self, user, key): #WEBMETHOD
        pass

    def deleteUser(self, user): #WEBMETHOD
        pass

    def listUsers(self): #WEBMETHOD
        pass

    def lockUser(self, user): #WEBMETHOD
        pass

    def unlockUser(self, user): #WEBMETHOD
        pass

    def addGroup(self, group): #WEBMETHOD
        pass

    def deleteGroup(self, group): #WEBMETHOD
        pass

    def listGroups(self): #WEBMETHOD
        pass
    
    def setWSACL(self, newACL): #WEBMETHOD
        pass

    def getWSACL(self): #WEBMETHOD
        pass

    def serializeWSConfig(self, target): #WEBMETHOD
        pass

    def setWSConfig(self, config): #WEBMETHOD
        pass

    def setWSConfigItem(self, name, value): #WEBMETHOD
        pass

    def startup(self):
        pass

    def shutdown(self): #WEBMETHOD
        pass

    def serviceNotify(self): #WEBMETHOD
        pass #returns when anything changes at the WS level, for UI coordination

    def createModel(self): #WEBMETHOD
        pass

    def cloneModel(self, modelID, newName): #WEBMETHOD
        pass

    def getModelIDs(self): #WEBMETHOD
        pass

    def importModel(self, filename):
        pass

    def importSerializedModel(self, modelString):
        pass

    def exportModel(self, modelID, filename):
        pass

    def loadModel(self, modelID): #WEBMETHOD
        pass #loads model from model store

    def getLoadedModelIDs(self): #WEBMETHOD
        pass #what's currently loaded

    def unloadModel(self, modelID, force=False): #WEBMETHOD
        #unloads model; leaves in store; force to override unflushed changes
        pass

    def deleteModel(self, modelID, force=False): #WEBMETHOD
        #unloads model and removes it from store
        pass

    def getServiceAPIDoc(self): #WEBMETHOD
        #Returns documentation about the API
        pass
