import config

def photo_processing(bot, message, my_keyBoard, array):
    #message,
    h=0

    while h<len(array):
                    
        if array[h].id_chat==message.chat.id and array[h].blockName=="🔴 інформація про правопорушення" and array[h].textDrugs!=0:
                        
            my_keyBoard[-1]
                            
            keyBoardGPS=my_keyBoard[-2]

            photo_id = message.photo[-1]
                        
    
            file_info = bot.get_file(photo_id.file_id)

            array[h].photoDrugs="http://api.telegram.org/file/bot{0}/{1}".format(config.TOKEN, file_info.file_path)

            bot.send_message(message.chat.id, " ✅ фото додано до вашого повідомлення \n\n🔺 🌐 Наступний крок:📡 GPS \n\nℹ️ Ви можете за бажанням додати до вашого повідомлення 📡 GPS координати місця повязаного з наркотиками чи ⏩ пропустити цей крок \n",reply_markup=keyBoardGPS)

            break
                    
        #else

        h+=1


def skip_photo(bot, message, my_keyBoard, array):
    
    my_keyBoard[-1]
                            
    keyBoardEND=my_keyBoard[-2]

    s=0

    while s<len(array):
                    
        if array[s].id_chat==message.chat.id and array[s].blockName=="🔴 інформація про правопорушення" and array[s].textDrugs!=0:
                                
            array[s].photoDrugs="додавання фото пропущено"

            bot.send_message(message.chat.id, "❌ додавання фото пропущено\n\n🔺 🌐 Наступний крок: 📡 GPS \n\nℹ️ Ви можете за бажанням додати до вашого повідомлення 📡 GPS координати місця повязаного з наркотиками чи ⏩ пропустити цей крок \n" )
            bot.send_message(message.chat.id, "🟡 Увага ❗️❗️❗️ Дана можливість доступа тільки користувачам мобільних телефонів та планшетів. \n",reply_markup=keyBoardEND)


            break

        s+=1

