import config
from menu import keyBoard
from menu import mainMenu
from handlers import checkField

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

                bot.send_message(config.Chanel_2, "{0}\n\n 🚻 заявник : {1} {2}\n\n {3}\n {4}\n\n {5}\n {6}\n\n {7}\n {8}\n\n message_from_user_id={9}\n\n user_name={10}".format(
                                                                                                    nameBlock,
                                                                                                    message.from_user.first_name,
                                                                                                    message.from_user.last_name,
                                                                                                    textField,
                                                                                                    array[q].textDrugs,
                                                                                                    photoField,
                                                                                                    array[q].photoDrugs,
                                                                                                    GPSfield,
                                                                                                    array[q].gpsAboutDrugs,
                                                                                                    message.from_user.id,
                                                                                                    message.from_user.username))
                sti=open('sticker/mailGood.tgs', 'rb')
                bot.send_sticker(message.chat.id,sti) 
                
                bot.send_message(message.chat.id, "✅ 📥 Повідомлення успішно доставлено🙂")
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

                bot.send_message(config.Chanel_2, "{0}\n\n 🚻 заявник : {1} {2}\n\n {3}\n {4}\n\n {5}\n {6}\n\n {7}\n {8}\n\n message_from_user_id={9}\n\n user_name={10}".format(
                                                                                                    nameBlock,
                                                                                                    message.from_user.first_name,
                                                                                                    message.from_user.last_name,
                                                                                                    textField,
                                                                                                    array[q].textDrugs,
                                                                                                    photoField,
                                                                                                    array[q].photoDrugs,
                                                                                                    GPSfield,
                                                                                                    array[q].gpsAboutDrugs,
                                                                                                    message.from_user.id,
                                                                                                    message.from_user.username))
                sti=open('sticker/mailGood.tgs', 'rb')
                bot.send_sticker(message.chat.id,sti) 
                
                bot.send_message(message.chat.id, "✅ 📥 Повідомлення успішно доставлено🙂")

                break


            q+=1

    except Exception as e:
        print(repr(e))
    finally:
        print("finaly")
        mainMenu.menu(bot,my_keyBoard,message, array)