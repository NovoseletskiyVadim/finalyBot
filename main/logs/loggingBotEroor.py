from datetime import datetime


def add_infoException_inFile(errorException, moduleName):

    now=datetime.now()

    currentTimeCreateLog=now.strftime("%d/%m/%y %I:%M")

    data=str(errorException)

    try:
        myFile=open("logs/logException.txt","a")

        try:

            myFile.write(currentTimeCreateLog+" module_name : " + moduleName + "describes : " + data)
    
        except Exception as e :

            print(repr(e))
    
        finally:
            myFile.close()

    except Exception as ex:

        print(repr(ex))



