import datetime as d
import requests
import xml.etree.ElementTree as ET
import io



class Vlhkomer:
    def __init__(self, typ, name, ip_add, vlhkostId):
        self.ip_add = ip_add
        self.vlhkostId = vlhkostId
        self.name = name
        self.value
        self.typ = typ
        self.id = None
    def setVlhkomerId(self,id):
        self.id = id