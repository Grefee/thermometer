import io
import xml.etree.ElementTree as ET
import datetime as d
import psycopg2
import oboji as O
import teplomer as T
import vlhkomer as V
import requests




global dbListTeplomer
dbListTeplomer = []


def getIdOfTeplomer(termListFromXml):


    for meno in termListFromXml:

        docasneMeno = meno.name
        docasneTyp = meno.typ


        if docasneTyp == "oboji":

            conn = psycopg2.connect("dbname='Teplomer' user='postgres' host='localhost' password='pepega'")
            cursor = conn.cursor()

            queryA = "SELECT (teplomer_id) FROM teplomer WHERE teplomer_name LIKE %s"
            dat = docasneMeno

            cursor.execute(queryA, (dat,))
            docasneId = cursor.fetchone()
            for id in docasneId:
                meno.setObojiId(id)

        elif docasneTyp == "teplota":

            conn = psycopg2.connect("dbname='Teplomer' user='postgres' host='localhost' password='pepega'")
            cursor = conn.cursor()

            queryA = "SELECT (teplomer_id) FROM teplomer WHERE teplomer_name LIKE %s"
            dat = docasneMeno

            cursor.execute(queryA, (dat,))
            docasneId = cursor.fetchone()
            for id in docasneId:
                meno.setTeplomerId(id)


        elif docasneTyp == "vlhkost":

            conn = psycopg2.connect("dbname='Teplomer' user='postgres' host='localhost' password='pepega'")
            cursor = conn.cursor()

            queryA = "SELECT (teplomer_id) FROM teplomer WHERE teplomer_name LIKE %s"
            dat = docasneMeno

            cursor.execute(queryA, (dat,))
            docasneId = cursor.fetchone()
            for id in docasneId:
                meno.setVlhkomerId(id)



        print("id is : " + str(meno.id) + " meno is : " + str(meno.name) + " ip is : " + str(meno.ip_add))



def sendDataToDb(objekt):

    ip = str(objekt.ip_add)
    name = objekt.name
    id = objekt.id
    typ = objekt.typ

    if typ == "oboji":

        senzorT = str(objekt.teplotaId)
        senzorV = str(objekt.vlhkostId)

        #TEPLOTA ULOZENI DO DB

        page = requests.get("http://" + ip + "/xml/?mode=sensor&type=list&id=" + senzorT)
        xmlPage = page.content.decode("utf-8")
        f = io.StringIO(xmlPage)
        tree = ET.parse(f)
        root = tree.getroot()

        for child in root:
            if child.tag == "current":
                valueT = child.text
        timeStamp = str(d.datetime.now())
        ezTime = timeStamp[0:16]

        conn = psycopg2.connect("dbname='Teplomer' user='postgres' host='localhost' password='pepega'")
        cursor = conn.cursor()

        queryT = "INSERT INTO teplota (teplota_value, teplomer_id, teplota_cas) VALUES (%s, %s, %s)"
        inputValues = (valueT, id, ezTime)
        cursor.execute(queryT, inputValues)
        conn.commit()



        #VLHKOST ULOZENI DO DB

        page = requests.get("http://" + ip + "/xml/?mode=sensor&type=list&id=" + senzorV)
        xmlPage = page.content.decode("utf-8")
        f = io.StringIO(xmlPage)
        tree = ET.parse(f)
        root = tree.getroot()

        for child in root:
            if child.tag == "current":
                valueV = child.text
        timeStamp = str(d.datetime.now())
        ezTime = timeStamp[0:16]

        conn = psycopg2.connect("dbname='Teplomer' user='postgres' host='localhost' password='pepega'")
        cursor = conn.cursor()

        queryV = "INSERT INTO vlhkost (vlhkost_value, teplomer_id, vlhkost_cas) VALUES (%s, %s, %s)"
        inputValues = (valueV, id, ezTime)
        cursor.execute(queryV, inputValues)
        conn.commit()

        conn.close()

        objekt.setValueOboji(valueT,valueV)
        print(objekt.teplotaValue)
        print(objekt.vlhkostValue)

    elif typ == "teplota":

        senzorT = str(objekt.teplotaId)

        #TEPLOTA ULOZENI DO DB
        try:
            page = requests.get("http://" + ip + "/xml/?mode=sensor&type=list&id=" + senzorT,timeout=3)

            xmlPage = page.content.decode("utf-8")
            f = io.StringIO(xmlPage)
            tree = ET.parse(f)
            root = tree.getroot()

            for child in root:
                if child.tag == "current":
                    value = child.text
            timeStamp = str(d.datetime.now())
            ezTime = timeStamp[0:16]

            conn = psycopg2.connect("dbname='Teplomer' user='postgres' host='localhost' password='pepega'")
            cursor = conn.cursor()

            queryT = "INSERT INTO teplota (teplota_value, teplomer_id, teplota_cas) VALUES (%s, %s, %s)"
            inputValues = (value, id, ezTime)
            cursor.execute(queryT, inputValues)
            conn.commit()
            objekt.setValueTeplota(value)
            print(objekt.value)

        except requests.exceptions.Timeout as error:
            print(error)
            logFile = open("log.txt", "a")
            logFile.write(str(d.datetime.now()) + "  " + str(error) + "\n")
            logFile.close()



    elif typ == "vlhkost":
        senzorV = objekt.vlhkostId











