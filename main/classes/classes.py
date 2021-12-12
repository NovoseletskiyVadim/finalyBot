from datetime import datetime
import saveSubscribers


class InfoDrugs :
 

    #costructor

    def __init__(self, id_chat):
        
        self.id_chat=id_chat
        #print("обьект {0} создан".format(self.id_chat))

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
                #print("time : {0} create obj=new form send message id={1} ".format(
                #                                                                    currentTimeCreateLog,
                #                                                                    self.id_chat,
                #                                                                    ))

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
            #print("current_time==",currentTimeCreateLog )

        try:
            myFile=open("logs/logCreateForm.txt","a")

            try:
                #print("time : {0} delete obj=new form send message id={1} ".format(
                #                                                                    currentTimeCreateLog,
                #                                                                    self.id_chat,
                #                                                                    ))

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

                myFile.write("\ntime : {0} create obj=checkNewUser id={1} firstName={2} lastName={3}".format(
                                                                                                              currentTimeCreateLog,
                                                                                                              self.id_chat,
                                                                                                              self.firstName,
                                                                                                              self.lastName
                                                                                                                            ))

    
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

                 myFile.write("\ntime : {0} FINISHED CHECKING! and delete obj=checkNewUser id={1} firstName={2} lastName={3}".format(
                                                                                                                                      currentTimeCreateLog,
                                                                                                                                      self.id_chat,
                                                                                                                                      self.firstName,
                                                                                                                                      self.lastName
                                                                                                                                                        ))
    
            except Exception as e :

                print(repr(e))
    
            finally:
                myFile.close()

        except Exception as ex:

            print(repr(ex))


    def addSaveNewUser( self, checkDickResult):

        checkResult=checkDickResult #True or Folse

        checkId=self.id_chat
        

        #time
        now=0
        now=datetime.now()

        if now==0:

            raise Exception("==WRONG!!== ДАТА НЕ ПРИСВОИЛАСЬ")
        else:

            currentTimeCreateLog=now.strftime("%d/%m/%y %I:%M")


        #логирование создания
        if checkResult :

            try:
                myFile=open("logs/usersBotList.txt","a")

                try:


                        myFile.write("\ntime: {0} id={1} firstName={2} lastName={3}".format(
                                                                                                                  currentTimeCreateLog,
                                                                                                                  self.id_chat,
                                                                                                                  self.firstName,
                                                                                                                  self.lastName
                                                                                                                                    ))

                except Exception as e :

                    print(repr(e))
    
                finally:
                    myFile.close()

            except Exception as ex:

                print(repr(ex))


class logInputCommandStart :

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

                myFile.write("\ntime : {0} user_command:/start id={1} first_name={2} last_name={3}".format(
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

        print("was command START")

class checkDictuonary :

    def __init__(self, mainDictuonary, blackDictuonary, message, checkDictuonaty):

        self.mainDictuonary=mainDictuonary
        self.message=message
        self.blackDictuonary=blackDictuonary
        self.checkDictuonaty=checkDictuonaty

        
    
    
    def checkNewUserDictuonaty(self):

        # TODO: сделать провверку есть ли в словаре какая то запись
        # если нету то загрузить  из файла всех пользователей и проверить
        # нового пользователя по всем параметрам

        if self.mainDictuonary:

            key=self.message.chat.id

            if key in self.blackDictuonary:

                return False

            elif key in self.mainDictuonary:


            
                return False
        
            else:

                id=self.message.chat.id
                firstName=str(self.message.from_user.first_name)
                lastName=str(self.message.from_user.last_name)
                name=firstName+lastName

                #add new user in file
                self.mainDictuonary[id]=name
                return True
    
        else:

            self.checkDictuonaty.check_subscribes()
           





    








