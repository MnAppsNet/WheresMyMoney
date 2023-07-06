import json, os

class Config:

    class Property:
        Server = 'server'
        Port = 'port'
        Database = 'database'
        Host = 'host'
        Username = 'username'
        Password = 'password'

    def __init__(self):
        self.configs = None
        self.path = os.path.dirname(__file__)
        self._getConfigs()

    def _getConfigs(self):
        if self.configs == None:
            with open(self.path+'/config.json') as fp:
                self.configs = json.load(fp)

    def getServerPort(self):
        if Config.Property.Server in self.configs:
            if Config.Property.Port in self.configs[Config.Property.Server]:
                return self.configs[Config.Property.Server][Config.Property.Port]
        return None

    def getDatabaseHost(self):
        if Config.Property.Database in self.configs:
            if Config.Property.Host in self.configs[Config.Property.Database]:
                return self.configs[Config.Property.Database][Config.Property.Host]
        return None

    def getDatabasePort(self):
        if Config.Property.Database in self.configs:
            if Config.Property.Port in self.configs[Config.Property.Database]:
                return self.configs[Config.Property.Database][Config.Property.Port]
        return None
    
    def getDatabaseUsername(self):
        if Config.Property.Database in self.configs:
            if Config.Property.Username in self.configs[Config.Property.Database]:
                return self.configs[Config.Property.Database][Config.Property.Username]
        return None

    def getDatabasePassword(self):
        if Config.Property.Database in self.configs:
            if Config.Property.Password in self.configs[Config.Property.Database]:
                return self.configs[Config.Property.Database][Config.Property.Password]
        return None