from datetime import datetime

class InfoDrugs :
 

    #costructor

    def __init__(self, id_chat):
        
        self.id_chat=id_chat

        #time

        now=0
        now=datetime.now()

        if now==0:

            raise Exception("==WRONG!!== ДАТА НЕ ПРИСВОИЛАСЬ")
        else:

            currentTimeCreateLog=now.strftime("%d/%m/%y %H:%M")

        #логирование создания

        try:
            myFile=open("logs/logCreateForm.txt","a")

            try:
                
                myFile.write("time : {0} create obj=new form send message id={1}\n".format
                             (
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

            currentTimeCreateLog=now.strftime("%d/%m/%y %H:%M")

        try:
            myFile=open("logs/logCreateForm.txt","a")

            try:
                
                myFile.write("time : {0} delete obj=new form send message id={1}\n".format
                             (
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

    
    #создание обьекта User для проверки 

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

            currentTimeCreateLog=now.strftime("%d/%m/%y %H:%M")

        
        #логирование ВЫЗОВА КОМАНДЫ "старт" и создание обьекта User для проверки 
        try:
            myFile=open("logs/logCheckUser.txt","a")

            try:

                myFile.write("time : {0} create obj=checkNewUser id={1} firstName={2} lastName={3}\n".format
                             (
                                currentTimeCreateLog,
                                self.id_chat,
                                self.firstName,
                                self.lastName,
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

            currentTimeCreateLog=now.strftime("%d/%m/%y %H:%M")

        try:
            myFile=open("logs/logCheckUser.txt","a")

            try:

                 myFile.write("time : {0} FINISHED CHECKING! and delete obj=checkNewUser id={1} firstName={2} lastName={3}\n".format
                              (
                                currentTimeCreateLog,
                                self.id_chat,
                                self.firstName,
                                self.lastName,

                                ))
    
            except Exception as e :

                print(repr(e))
    
            finally:
                myFile.close()

        except Exception as ex:

            print(repr(ex))

    #добавление User в файл   после сверки со словарями 
    def addSaveNewUser( self, checkDickResult):

        checkResult=checkDickResult #True or Folse

        checkId=self.id_chat
        

        #time
        now=0
        now=datetime.now()

        if now==0:

            raise Exception("==WRONG!!== ДАТА НЕ ПРИСВОИЛАСЬ")
        else:

            currentTimeCreateLog=now.strftime("%d/%m/%y %H:%M")


        #логирование создания
        if checkResult :

            try:
                myFile=open("logs/usersBotList.txt","a")

                try:


                        myFile.write("time: {0} id={1} firstName={2} lastName={3}\n".format
                                     (
                                        currentTimeCreateLog,
                                        self.id_chat,
                                        self.firstName,
                                        self.lastName,

                                        ))
                except Exception as e :

                    print(repr(e))
    
                finally:
                    myFile.close()

            except Exception as ex:

                print(repr(ex))

            try:
                dictuonaryFile=open("logs/dictuonary.txt","a")
                
                try:

                    dictuonaryFile.write("{0}={1} {2}\n".format
                            (
                                self.id_chat,
                                self.firstName,
                                self.lastName
                            ))

                except Exception as e:

                    print(repr(e))
            
                finally:
                    dictuonaryFile.close()

            except Exception as ex:

                print(repr(ex))

class logInputCommandStart :

     def __init__(self,id_chat, firstName, lastName):
        
        self.id_chat=id_chat
        self.firstName=firstName
        self.lastName=lastName

     def checkCommandStart(self, checkDictuonary):
        #time
        now=0
        now=datetime.now()

        if now==0:

            raise Exception("==WRONG!!== ДАТА НЕ ПРИСВОИЛАСЬ")

        else:

            currentTimeCreateLog=now.strftime("%d/%m/%y %H:%M")
        

        #dictuonary
        if checkDictuonary:
            
            key=str(self.id_chat)

            if key in checkDictuonary:

                return True
            
            else:

                id=self.id_chat
                firstName=str(self.firstName)
                lastName=str(self.lastName)
                name=firstName+" "+lastName

                #add new item in Dictuonary
                checkDictuonary[id]=name

                #add new item in file
                try:

                    myFile=open("logs/logStartCommand.txt","a")

                    try:

                        myFile.write("{0}={1} {2} \n".format
                                        (
                                        self.id_chat,
                                        self.firstName,
                                        self.lastName,
                                        #currentTimeCreateLog,

                                        ))

    
                    except Exception as e :

                        print(repr(e))
    
                    finally:

                        myFile.close()

                except Exception as ex:

                    print(repr(ex))


                return True

        else:

            linesFromFileCheckUpdate=[]

            try:
                
                fileCheckUpdater=open("logs/logStartCommand.txt","r")

                try:
            
                   for line in fileCheckUpdater:
                        
                        #загружаем данные файла в массив строк
                        linesFromFileCheckUpdate.append(line)

                except Exception as e:
                    print(repr(e))
            
            except Exception as ex:

                print(repr(ex))
            
            finally:

                fileCheckUpdater.close()

            x=0

            #проверяем что достало из файла 
            #если записи есть то наполняем словарь инфой:
            if len(linesFromFileCheckUpdate)>0:

                while x<len(linesFromFileCheckUpdate):

                    #берем отдельную строку и распарсиваем для словаря  
                    indexID=linesFromFileCheckUpdate[x].split("=")
                    checkDictuonary[indexID[0]]=indexID[1]

                    x+=1

                #проверяем пользователя 
                key=str(self.id_chat)

                if key in checkDictuonary:

                    return True
            
                else:


                    id=self.id_chat
                    firstName=str(self.firstName)
                    lastName=str(self.lastName)
                    name=firstName+" "+lastName

                    #add new item in Dictuonary
                    checkDictuonary[id]=name

                    #add new item in file
                    try:

                        myFile=open("logs/logStartCommand.txt","a")

                        try:

                            myFile.write("{0}={1} {2} \n".format
                                            (
                                            self.id_chat,
                                            self.firstName,
                                            self.lastName,
                                            #currentTimeCreateLog,

                                            ))

    
                        except Exception as e :

                            print(repr(e))
    
                        finally:

                            myFile.close()

                    except Exception as ex:

                        print(repr(ex))


                    return True

            else:


                    id=self.id_chat
                    firstName=str(self.firstName)
                    lastName=str(self.lastName)
                    name=firstName+" "+lastName

                    #add new item in Dictuonary
                    checkDictuonary[id]=name

                    #add new item in file
                    try:

                        myFile=open("logs/logStartCommand.txt","a")

                        try:

                            myFile.write("{0}={1} {2}\n".format
                                            (
                                            self.id_chat,
                                            self.firstName,
                                            self.lastName,
                                            #currentTimeCreateLog,

                                            ))

    
                        except Exception as e :

                            print(repr(e))
    
                        finally:

                            myFile.close()

                    except Exception as ex:

                        print(repr(ex))


                    return True

class checkDictuonary :

    def __init__(
                    self,
                    mainDictuonary, 
                    blackDictuonary,    
                    message,            
                    ):

        self.mainDictuonary=mainDictuonary
        self.message=message
        self.blackDictuonary=blackDictuonary
        
    
    
    def checkNewUserDictuonaty(self):

        if self.mainDictuonary:

            key=str(self.message.chat.id)

            if key in self.blackDictuonary:

                return False

            elif key in self.mainDictuonary:

                return False
        
            else:

                id=self.message.chat.id
                firstName=str(self.message.from_user.first_name)
                lastName=str(self.message.from_user.last_name)
                name=firstName+" "+lastName

                #add new user in Dictuonary
                self.mainDictuonary[id]=name

                return True
    

        #если словарь пустой то загружаем ключи и пользовтелей из файла 
        else:

            linesFromFile=[]

            try:
                
                fileBaseSucscribes=open("logs/dictuonary.txt","r")

                try:
            
                   for line in fileBaseSucscribes:
                        
                        #загружаем данные файла в массив строк
                        linesFromFile.append(line)

                except Exception as e:
                    print(repr(e))
            
            except Exception as ex:

                print(repr(ex))
            
            finally:

                fileBaseSucscribes.close()

            i=0

            #проверяем что достало из файла 
            #если записи есть то:
            if len(linesFromFile)>0:

                while i<len(linesFromFile):

                    #берем отдельную строку и распарсиваем для словаря  
                    indexID=linesFromFile[i].split("=")

                    self.mainDictuonary[indexID[0]]=indexID[1]

                    i+=1

                key=str(self.message.chat.id)


                if key in self.blackDictuonary:

                    return False

                elif key in self.mainDictuonary:

                    return False
        
                else:

                    id=self.message.chat.id
                    firstName=str(self.message.from_user.first_name)
                    lastName=str(self.message.from_user.last_name)
                    name=firstName+" "+lastName

                    #add new user in Dictuonary
                    self.mainDictuonary[id]=name

                    return True


                

            #если файл "dictuonary.txt" был изначально пустой делаем сначала запись в словарь и возвращ флаг
            else:

                id=self.message.chat.id
                firstName=str(self.message.from_user.first_name)
                lastName=str(self.message.from_user.last_name)
                name=firstName+" "+lastName

                #add new user in Dictuonary
                self.mainDictuonary[id]=name

                return True
           





    








