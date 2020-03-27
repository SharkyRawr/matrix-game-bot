import json

class Config(object):
    def __init__(self, configpath='config.json'):
        self.configpath = configpath
        self.load()

    def load(self):
        self.cfg = json.load(open(self.configpath))

    def get(self, key, default=None):
        if default is Exception:
            if not key in self.cfg:
                raise Exception("key '{}' not found in config".format(key))
        
        return self.cfg.get(key, default)