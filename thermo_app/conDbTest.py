import psycopg2

import readTermMeterList as R

def checkTermMetersInDb(termListFromXml):

    for item in termListFromXml:
        list_name = item.name
        list_typ = item.typ
        list_ip = item.ip_add


        if list_typ == "oboji":
            list_senzor_Id_teplota = item.teplotaId
            list_senzor_Id_vlhkost = item.vlhkostId
        elif list_typ == "teplota":
            list_senzor_Id_teplota = item.teplotaId
            list_senzor_Id_vlhkost = None
        elif list_typ == "vlhkost":
            list_senzor_Id_vlhkost = item.vlhkostId
            list_senzor_Id_teplota = None



        conn = psycopg2.connect("dbname='Teplomer' user='postgres' host='localhost' password='pepega'")
        cursor = conn.cursor()


        #### select Name from DB
        queryX = "SELECT (teplomer_name) FROM teplomer WHERE teplomer_name LIKE %s"

        cursor.execute(queryX, (list_name,))
        sqlRespose = cursor.fetchone()

        ####CHECK IF NAME EXIST IN DB

        if sqlRespose is None:
            print("chybí záznam")
            #potřeba insert
            if list_typ == "oboji":
                insertToDbOboji(list_ip, list_name, list_typ, list_senzor_Id_teplota,list_senzor_Id_vlhkost)

            elif list_typ == "teplota":
                insertToDbTeplomer(list_ip, list_name, list_typ, list_senzor_Id_teplota)
            elif list_typ == "vlhkost":
                insertToDbVlhkost(list_ip, list_name, list_typ, list_senzor_Id_vlhkost)
        else:

            dbName = sqlRespose[0]


            #### select IP from DB
            queryX = "SELECT (teplomer_ip) FROM teplomer WHERE teplomer_name LIKE %s"

            cursor.execute(queryX, (list_name,))
            sqlRespose = cursor.fetchone()


            dbIp = sqlRespose[0]



            #### select Typ from DB
            queryX = "SELECT (teplomer_typ) FROM teplomer WHERE teplomer_name LIKE %s"

            cursor.execute(queryX, (list_name,))
            sqlRespose = cursor.fetchone()

            dbTyp = sqlRespose[0]

            #### select Senzor_teplota from DB
            queryX = "SELECT (senzor_id_teplota) FROM teplomer WHERE teplomer_name LIKE %s"

            cursor.execute(queryX, (list_name,))
            sqlRespose = cursor.fetchone()

            dbSenzorIdTeplota = sqlRespose[0]

            #### select Senzor_vlhkost from DB
            queryX = "SELECT (senzor_id_vlhkost) FROM teplomer WHERE teplomer_name LIKE %s"

            cursor.execute(queryX, (list_name,))
            sqlRespose = cursor.fetchone()

            dbSenzorIdVlhkost = sqlRespose[0]


            conn.close()

            print("/*/*/*/*/*/")
            print("objekt záznam")
            print(list_ip)
            print(list_name)
            print(list_typ)
            print(list_senzor_Id_teplota)
            print(list_senzor_Id_vlhkost)
            print("/*/*/*/*/*/")


            print("/*/*/*/*/*/")
            print("db záznamy")
            print(dbIp)
            print(dbName)
            print(dbTyp)
            print(dbSenzorIdTeplota)
            print(dbSenzorIdVlhkost)

            print("/*/*/*/*/*/")

            dbSenzorIdTeplota = str(dbSenzorIdTeplota)
            dbSenzorIdVlhkost = str(dbSenzorIdVlhkost)

            print("záznam je a checkni jestli sedej veci")

            if list_typ =="oboji":
                if (dbIp == list_ip and dbTyp == list_typ and dbSenzorIdTeplota == list_senzor_Id_teplota and dbSenzorIdVlhkost == list_senzor_Id_vlhkost):
                    print("záznam o teploměru sedí")
                else:
                    print("záznam o teploměru je jiný, ---->>> update")
                    updateZaznamOboji(list_ip, list_name, list_typ, list_senzor_Id_teplota,list_senzor_Id_vlhkost)
            elif list_typ =="teplota":
                if dbIp == list_ip and dbTyp == list_typ and dbSenzorIdTeplota == list_senzor_Id_teplota:
                    print("záznam o teploměru sedí")
                else:
                    print("záznam o teploměru je jiný, ---->>> update")
                    updateZaznamTeplomer(list_ip, list_name, list_typ, list_senzor_Id_teplota)
            elif list_typ == "vlhkost":
                if dbIp == list_ip and dbTyp == list_typ and dbSenzorIdVlhkost == list_senzor_Id_vlhkost:
                    print("záznam o teploměru sedí")
                else:
                    print("záznam o teploměru je jiný, ---->>> update")
                    updateZaznamVlhkost(list_ip, list_name, list_typ, list_senzor_Id_vlhkost)





def insertToDbOboji(ip_add, name, typ, list_senzor_Id_teplota,list_senzor_Id_vlhkost):
    conn = psycopg2.connect("dbname='Teplomer' user='postgres' host='localhost' password='pepega'")
    cursor = conn.cursor()
    queryX = 'INSERT INTO teplomer(teplomer_ip, teplomer_name, teplomer_typ, senzor_id_teplota, senzor_id_vlhkost) VALUES (%s, %s, %s, %s, %s)'
    val = (ip_add, name, typ, list_senzor_Id_teplota,list_senzor_Id_vlhkost)
    cursor.execute(queryX, val)
    conn.commit()
    conn.close()

def insertToDbTeplomer(ip_add, name, typ, list_senzor_Id_teplota):
    conn = psycopg2.connect("dbname='Teplomer' user='postgres' host='localhost' password='pepega'")
    cursor = conn.cursor()
    queryX = 'INSERT INTO teplomer(teplomer_ip, teplomer_name, teplomer_typ, senzor_id_teplota) VALUES (%s, %s, %s, %s)'
    val = (ip_add, name, typ, list_senzor_Id_teplota)
    cursor.execute(queryX, val)
    conn.commit()
    conn.close()

def insertToDbVlhkost(ip_add, name, typ,list_senzor_Id_vlhkost):
    conn = psycopg2.connect("dbname='Teplomer' user='postgres' host='localhost' password='pepega'")
    cursor = conn.cursor()
    queryX = 'INSERT INTO teplomer(teplomer_ip, teplomer_name, teplomer_typ, senzor_id_vlhkost) VALUES (%s, %s, %s, %s)'
    val = (ip_add, name, typ, list_senzor_Id_vlhkost)
    cursor.execute(queryX, val)
    conn.commit()
    conn.close()



def updateZaznamOboji(ip_add, name, typ, list_senzor_Id_teplota,list_senzor_Id_vlhkost):
    conn = psycopg2.connect("dbname='Teplomer' user='postgres' host='localhost' password='pepega'")
    cursor = conn.cursor()

    #change ip
    queryX = 'UPDATE teplomer SET teplomer_ip = %s WHERE teplomer_name = %s'
    dat = ip_add, name
    cursor.execute(queryX, (dat))
    conn.commit()
    #change typ
    queryX = 'UPDATE teplomer SET teplomer_typ = %s WHERE teplomer_name = %s'
    dat = typ, name
    cursor.execute(queryX, (dat))
    conn.commit()
    #change list_senzor_Id_teplota
    queryX = 'UPDATE teplomer SET senzor_id_teplota = %s WHERE teplomer_name = %s'
    dat = list_senzor_Id_teplota, name
    cursor.execute(queryX, (dat))
    conn.commit()
    #change list_senzor_Id_vlhkost
    queryX = 'UPDATE teplomer SET senzor_id_vlhkost = %s WHERE teplomer_name = %s'
    dat = list_senzor_Id_vlhkost, name
    cursor.execute(queryX, (dat))
    conn.commit()

    conn.close()


def updateZaznamTeplomer(ip_add, name, typ, list_senzor_Id_teplota):
    conn = psycopg2.connect("dbname='Teplomer' user='postgres' host='localhost' password='pepega'")
    cursor = conn.cursor()

    # change ip
    queryX = 'UPDATE teplomer SET teplomer_ip = %s WHERE teplomer_name = %s'
    dat = ip_add, name
    cursor.execute(queryX, (dat))
    conn.commit()
    # change typ
    queryX = 'UPDATE teplomer SET teplomer_typ = %s WHERE teplomer_name = %s'
    dat = typ, name
    cursor.execute(queryX, (dat))
    conn.commit()
    # change list_senzor_Id_teplota
    queryX = 'UPDATE teplomer SET senzor_id_teplota = %s WHERE teplomer_name = %s'
    dat = list_senzor_Id_teplota, name
    cursor.execute(queryX, (dat))
    conn.commit()

    conn.close()


def updateZaznamVlhkost(ip_add, name, typ, list_senzor_Id_vlhkost):
    conn = psycopg2.connect("dbname='Teplomer' user='postgres' host='localhost' password='pepega'")
    cursor = conn.cursor()

    # change ip
    queryX = 'UPDATE teplomer SET teplomer_ip = %s WHERE teplomer_name = %s'
    dat = ip_add, name
    cursor.execute(queryX, (dat))
    conn.commit()
    # change typ
    queryX = 'UPDATE teplomer SET teplomer_typ = %s WHERE teplomer_name = %s'
    dat = typ, name
    cursor.execute(queryX, (dat))
    conn.commit()
    # change list_senzor_Id_vlhkost
    queryX = 'UPDATE teplomer SET senzor_id_vlhkost = %s WHERE teplomer_name = %s'
    dat = list_senzor_Id_vlhkost, name
    cursor.execute(queryX, (dat))
    conn.commit()

    conn.close()

