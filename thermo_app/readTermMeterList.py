import xml.etree.ElementTree as ET
import io
import teplomer as T

import vlhkomer as V
import oboji as O


global termListFromXml
termListFromXml = []

global termName
termName = []

global numberOfTermListFromXml
numberOfTermListFromXml = 0


def readTermMeter():
    with io.open("xmlConfig.xml", "r", encoding="utf-8") as xmlPage:
        f = ET.parse(xmlPage)
        root = f.getroot()




        for child in root:
            i = 0
            if child.attrib.get("typ") == "teplota":
                typVar = "teplota"
                for var in child:
                    if var.tag == "name":
                        name = var.text
                    if var.tag == "ip":
                        ip_add = var.text
                    if var.tag == "id":
                        teplotaId = var.text

                        #print("name :" + name + "  ip is: " + ip_add + "  id is :" + teplotaId)
                        # inicializace objektu
                        objName = "teplomer" + str(i)
                        objName = T.Teplomer(typVar, name, ip_add, teplotaId)
                        termListFromXml.append(objName)
                        termName.append(name)


            if child.attrib.get("typ") == "oboji":
                typVar = "oboji"
                for var in child:
                    if var.tag == "name":
                        name = var.text
                    if var.tag == "ip":
                        ip_add = var.text
                    if var.tag == "idT":
                        teplotaId = var.text
                    if var.tag == "idV":
                        vlhkostId = var.text
                        objName = "teplomer" + str(i)
                        objName = O.Oboji(typVar, ip_add, name, teplotaId, vlhkostId)
                        termListFromXml.append(objName)
                        termName.append(name)



            if child.attrib.get("typ") == "vlhkost":
                typVar = "vlhkost"
                for var in child:
                    if var.tag == "name":
                        name = var.text
                    if var.tag == "ip":
                        ip_add = var.text
                    if var.tag == "id":
                        vlhkostId = var.text

                        # inicializace objektu
                        objName = "teplomer" + str(i)
                        objName = V.Vlhkomer(typVar, name, ip_add, vlhkostId)
                        termListFromXml.append(objName)
                        termName.append(name)

            i = i + 1




