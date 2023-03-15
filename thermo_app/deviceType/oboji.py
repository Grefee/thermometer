import datetime as d
import requests
import xml.etree.ElementTree as ET
import io



class Oboji:
    def __init__(self,typ, ip_add, name,teplotaId ,vlhkostId):
        self.ip_add = ip_add
        self.name = name
        self.typ = typ

        self.teplotaId = teplotaId
        self.vlhkostId = vlhkostId

        self.teplotaValue = None
        self.vlhkostValue = None

        self.id = None

    def setObojiId(self,id):
        self.id = id

    def setValueOboji(self,teplotaValue,vlhkostValue):
        self.teplotaValue = teplotaValue
        self.vlhkostValue = vlhkostValue


