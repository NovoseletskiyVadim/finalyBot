from datetime import datetime


def add_info_inFile(errorException):

    now=datetime.now()

    currentTimeCreateLog=now.strftime("%d/%m/%y %I:%M")

    data=str(errorException)

    try:
        myFile=open("/logs/logException.txt","a")

        try:

            myFile.write(currentTimeCreateLog+" : " +data)
    
        except Exception as e :

            print(repr(e))
    
        finally:
            myFile.close()

    except Exception as ex:

        print(repr(e))



