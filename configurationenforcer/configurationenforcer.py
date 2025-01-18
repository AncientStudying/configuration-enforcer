class ConfigurationEnforcer(object):
    isInitialized = False
    def __init__(self):
        ConfigurationEnforcer.isInitialized = True
        print("Howdy World from the Configuration Enforcer!")



