import config
from menu import keyBoard
from menu import mainMenu
from handlers import checkField
from datetime import datetime


# широта (latitude) 49
# долгота (longitude)32



def gps_processing(bot, message, my_keyBoard, array):
    try:

        q=0

        while q<len(array):
                    
            if array[q].id_chat==message.chat.id and array[q].blockName=="🔴 інформація про правопорушення" and array[q].textDrugs!=0 and array[q].photoDrugs!=0 and array[q].gpsAboutDrugs==0:

                sti=open('sticker/mailGood.tgs', 'rb')
                bot.send_sticker(config.Chanel_2,sti)
                
                
                array[q].longitude=message.location.longitude

                array[q].latitude=message.location.latitude

                array[q].gpsAboutDrugs="https://www.google.com/maps?q=loc:{0},{1}".format(array[q].latitude, array[q].longitude)

                nameBlock, textField, photoField, GPSfield=checkField.check_value(array[q])

                timeMessage=datetime.now()

                currentTimeMessage=timeMessage.strftime("%d/%m/%y %I:%M")

                bot.send_message(config.Chanel_2, "{0}\n\n📅🕑={1}\n\n🔑={2}\n\n {3}\n {4}\n\n {5}\n {6}\n\n {7}\n {8}\n\n ".format
                              (
                                nameBlock,#{0}
                                currentTimeMessage,#{1}
                                message.from_user.id,#{2}
                                textField,#{3}
                                array[q].textDrugs,#{4}
                                photoField,#{5}
                                array[q].photoDrugs,#{6}
                                GPSfield,#{7}
                                array[q].gpsAboutDrugs,#{8}
                                                                                                    
                                ))
                sti=open('sticker/mailGood.tgs', 'rb')
                bot.send_sticker(message.chat.id,sti) 
                
                bot.send_message(message.chat.id, "✅ 📥 Повідомлення успішно доставлено🙂")
                
                
                now=0
                now=datetime.now()
                currentTimeCreateLog=now.strftime("%d/%m/%y %I:%M")

                try:
                    myFile=open("logs/logCreateForm.txt","a")

                    try:
                        

                        myFile.write("\ntime : {0} send_successful obj=new form send message id={1} ".format
                                    (
                                    currentTimeCreateLog,
                                    message.chat.id,
                                    ))

    
                    except Exception as e :

                        print(repr(e))
    
                    finally:
                        myFile.close()

                except Exception as ex:

                    print(repr(ex))
                
                
                break

            q+=1

    except Exception as e:
       print(repr(e))

    finally:

      mainMenu.menu(bot,my_keyBoard,message, array)


def skipGPS(bot, message, my_keyBoard, array):
      
    try:
    
         
        q=0

        while q<len(array):
                    
            if array[q].id_chat==message.chat.id and array[q].blockName=="🔴 інформація про правопорушення" and array[q].textDrugs!=0 and array[q].photoDrugs!=0 and array[q].gpsAboutDrugs==0:
                
                array[q].gpsAboutDrugs="додавання GPS пропущено"

                nameBlock, textField, photoField, GPSfield=checkField.check_value(array[q])

                timeMessage=datetime.now()

                currentTimeMessage=timeMessage.strftime("%d/%m/%y %I:%M")

                bot.send_message(config.Chanel_2, "{0}\n\n 📅🕑={1}\n\n 🔑={2}\n\n {3}\n {4}\n\n {5}\n {6}\n\n {7}\n {8}\n\n".format
                                 (
                                    nameBlock,#{0}
                                    currentTimeMessage,#{1}
                                    message.from_user.id,#{2}
                                    textField,#{3}
                                    array[q].textDrugs,#{4}
                                    photoField,#{5}
                                    array[q].photoDrugs,#{6}
                                    GPSfield,#{7}
                                    array[q].gpsAboutDrugs,#{8}
                                    
                                    ))

                sti=open('sticker/mailGood.tgs', 'rb')
                bot.send_sticker(message.chat.id,sti) 
                
                bot.send_message(message.chat.id, "✅ 📥 Повідомлення успішно доставлено🙂")

                now=0
                now=datetime.now()
                currentTimeCreateLog=now.strftime("%d/%m/%y %I:%M")

                try:
                    myFile=open("logs/logCreateForm.txt","a")

                    try:
                       

                        myFile.write("time : {0} send_successful obj=new form send message id={1}\n".format
                                     (
                                        currentTimeCreateLog,
                                        message.chat.id,
                                      ))

    
                    except Exception as e :

                        print(repr(e))
    
                    finally:

                        myFile.close()

                except Exception as ex:

                    print(repr(ex))

                break


            q+=1

    except Exception as e:
        print(repr(e))
    finally:
        mainMenu.menu(bot,my_keyBoard,message, array)