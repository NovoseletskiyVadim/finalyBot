from datetime import datetime



class InfoDrugs :
 

    #costructor

    def __init__(self, id_chat):
        
        self.id_chat=id_chat
        print("обьект {0} создан".format(self.id_chat))

        #time

        now=0
        now=datetime.now()

        if now==0:

            raise Exception("==WRONG!!== ДАТА НЕ ПРИСВОИЛАСЬ")
        else:

            currentTimeCreateLog=now.strftime("%d/%m/%y %I:%M")
            #print("current_time==",currentTimeCreateLog )

        #логирование создания

        try:
            myFile=open("logs/logCreateForm.txt","a")

            try:
                print("time : {0} create obj=new form send message id={1} ".format(
                                                                                    currentTimeCreateLog,
                                                                                    self.id_chat,
                                                                                    ))

                myFile.write("\ntime : {0} create obj=new form send message id={1} ".format(
                                                                                        currentTimeCreateLog,
                                                                                        self.id_chat,
                                                                                        ))

    
            except Exception as e :

                print(repr(e))
    
            finally:
                myFile.close()

        except Exception as ex:

            print(repr(ex))

    def __del__(self):

        now=0
        now=datetime.now()

        if now==0:

            raise Exception("==WRONG!!== ДАТА НЕ ПРИСВОИЛАСЬ")
        else:

            currentTimeCreateLog=now.strftime("%d/%m/%y %I:%M")
            print("current_time==",currentTimeCreateLog )

        try:
            myFile=open("logs/logCreateForm.txt","a")

            try:
                print("time : {0} delete obj=new form send message id={1} ".format(
                                                                                    currentTimeCreateLog,
                                                                                    self.id_chat,
                                                                                    ))

                myFile.write("\ntime : {0} delete obj=new form send message id={1} ".format(
                                                                                        currentTimeCreateLog,
                                                                                        self.id_chat,
                                                                                        ))

    
            except Exception as e :

                print(repr(e))
    
            finally:
                myFile.close()

        except Exception as ex:

            print(repr(ex))

    blockName=0

    startWork=0
    
    textDrugs=0

    photoDrugs=0

    gpsAboutDrugs=0

    latitude=0

    longitude=0


class checkNewUser :

    

    def __init__(self,id_chat, firstName, lastName):
        
        self.id_chat=id_chat
        self.firstName=firstName
        self.lastName=lastName

        #time

        now=0
        now=datetime.now()

        if now==0:

            raise Exception("==WRONG!!== ДАТА НЕ ПРИСВОИЛАСЬ")
        else:

            currentTimeCreateLog=now.strftime("%d/%m/%y %I:%M")
            #print("current_time==",currentTimeCreateLog )

        
        #логирование создания

        try:
            myFile=open("logs/logStartCommand.txt","a")

            try:

                myFile.write("\ntime : {0} create obj=checkNewUser id={1} first_name={2} last_name={3}".format(
                                                                                                              currentTimeCreateLog,
                                                                                                              self.id_chat,
                                                                                                              self.firstName,
                                                                                                              self.lastName))

    
            except Exception as e :

                print(repr(e))
    
            finally:
                myFile.close()

        except Exception as ex:

            print(repr(ex))


    def __del__(self):

        #time

        now=0
        now=datetime.now()

        if now==0:

            raise Exception("==WRONG!!== ДАТА НЕ ПРИСВОИЛАСЬ")
        else:

            currentTimeCreateLog=now.strftime("%d/%m/%y %I:%M")
            #print("current_time==",currentTimeCreateLog )


        try:
            myFile=open("logs/logStartCommand.txt","a")

            try:

                 myFile.write("\ntime : {0} FINISHED CHECKING! and delete obj=checkNewUser id={1} first_name={2} last_name={3}".format(
                                                                                                                                      currentTimeCreateLog,
                                                                                                                                      self.id_chat,
                                                                                                                                      self.firstName,
                                                                                                                                      self.lastName))
    
            except Exception as e :

                print(repr(e))
    
            finally:
                myFile.close()

        except Exception as ex:

            print(repr(ex))







