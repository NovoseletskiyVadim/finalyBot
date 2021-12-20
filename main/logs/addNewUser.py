from classes import classes
checkUser=classes.checkNewUser

#check_status==True or False

def addUser(message,check_status):


    user=checkUser(message.chat.id,message.from_user )

    user.addSaveNewUser(check_status)

def checkUserUpdate(bot, message, dictuonaryStartCommand):

    
    if dictuonaryStartCommand:

        #проверяем пользователя 
        key=str(message.chat.id)

        if key in dictuonaryStartCommand:

            return True
            
        else:

            bot.send_message(message.chat.id,"🟡 Увага ❗️❗️❗️ \n\n🔺 Ми зробили певні оновлення у функціях.\nℹ️ Для продовження роботи відправте повідомлення :\n /start  ")

            return False

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
                dictuonaryStartCommand[indexID[0]]=indexID[1]

                x+=1

            #проверяем пользователя 
            key=str(message.chat.id)

            if key in dictuonaryStartCommand:

                return True
            
            else:

                bot.send_message(message.chat.id,"🟡 Увага ❗️❗️❗️ \n\n🔺 Ми зробили певні оновлення у функціях.\nℹ️ Для продовження роботи відправте повідомлення :\n //start  ")

                return False
                

        else:


                    id=str(message.chat.id)
                    firstName=str(message.from_user.first_name)
                    lastName=str(message.from_user.last_name)
                    name=firstName+" "+lastName

                    #add new item in Dictuonary
                    dictuonaryStartCommand[id]=name

                    #add new item in file
                    try:

                        myFile=open("logs/logStartCommand.txt","a")

                        try:

                            myFile.write("{0}={1} {2}\n".format
                                            (
                                            id,
                                            firstName,
                                            lastName,
                                            #currentTimeCreateLog,

                                            ))

    
                        except Exception as e :

                            print(repr(e))
    
                        finally:

                            myFile.close()

                    except Exception as ex:

                        print(repr(ex))


                    return True


