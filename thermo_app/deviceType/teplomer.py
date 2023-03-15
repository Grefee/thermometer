import datetime as d
import requests
import xml.etree.ElementTree as ET
import io



class Teplomer:
    def __init__(self, typ, name, ip_add,teplotaId):
        self.ip_add = ip_add
        self.teplotaId = teplotaId
        self.name = name

        self.value = None
        self.typ = typ
        self.id = None

    def teplomerData(self):
        self.ip_add
        self.name
        return (self.ip_add,self.name)

    def teplomerName(self):
        self
    def setTeplomerId(self,id):
        self.id = id

    def getData(self):
        page = requests.get("http://" + self.ip_add + "/xml/?mode=sensor&type=list&id=01")
        xmlPage = page.content.decode("utf-8")
        f = io.StringIO(xmlPage)
        tree = ET.parse(f)
        root = tree.getroot()

        for child in root:
            if (child.tag == "name"):
                term_name = child.text
            if (child.tag == "current"):
                term_value = child.text

        timeStamp = str(d.datetime.now())
        print("-----")

        print("nazev :" + term_name)
        print("teplota :" + term_value)

        print("cas :" + timeStamp)

        return (self.ip_add, term_value, timeStamp)
    def setValueTeplota(self,value):
        self.value = value


