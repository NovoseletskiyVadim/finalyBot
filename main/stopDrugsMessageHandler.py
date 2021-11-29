import wish
import mainMenu
import config
import checkField

from classes import InfoDrugs


def drugsMessageHundler(bot, my_keyBoard, array):



    @bot.message_handler(content_types=["text", "photo", "audio", "document","location" ])
    def handle_text(message):
        
        
       
        if message.chat.type == "private":
            print("message.chat.type==private")
           

            if message.content_type=="text":
                
                     
           
                if message.text=="🔴 інструкція із користування":
                
                  my_keyBoard[-1]

                  wish.putWish(bot,message,my_keyBoard)

                elif message.text== "🔴 інформація про правопорушення":
                    
                    i=0

                    print("состояние масства=", len(array))

                    if len(array)==0:
                            
                        info_drugs=InfoDrugs(message.chat.id)
                            
                        info_drugs.blockName="🔴 інформація про правопорушення"

                        array.append(info_drugs)

                        print("запись доьавлена в массив")
                    else:

                        while i< len(array): 
                        
                            if array[i].id_chat==message.chat.id:

                                array.remove(array[i])

                                info_drugs=InfoDrugs(message.chat.id)
                            
                                info_drugs.blockName="🔴 інформація про правопорушення"

                                array.append(info_drugs)

                                print("запись доьавлена в массив")

                                break
                            i+=1

              
                    my_keyBoard[-1]

                    textButton=my_keyBoard[4]

                    print("блок инфо про правопорушення")

                    bot.send_message(message.chat.id,
                                    "🔺 Ви перейшли в розділ де ви можете залишити інформацію про правопорушення \n\n "+
                                    "Увага‼️  Щоб Ваше повідомлення було відправлено на обробку воно має складатися із 3 частин \n\n"+
                                    "🔴 1.Текст (обовязкова частина повідомлення) \n\n"+
                                    "🔶 2.Фото місця або скиншот з телефону (цей крок можна пропустити) \n\n"+
                                    "🔶 3.GPS координати (цей крок можна пропустити) \n\n"+
                                    "Увага‼️ лише після цього сформоване повідомлення відправиться оператору на обробку \n\n"+
                                    "\n\n ",
                                    reply_markup=textButton)

                elif message.text=="🔴 відмінити та повернутися в головне меню":

                    mainMenu.menu(bot,my_keyBoard,message)

                elif message.text=="🔴 перейти до повідомлення" :

                    print("блок перейти до повідомлення+++ ")

                    j=0

                    while j<len(array):

                        if array[j].id_chat==message.chat.id and array[j].blockName=="🔴 інформація про правопорушення":

                            my_keyBoard[-1]
                            
                            keyBoardPhoto=my_keyBoard[2]

                            bot.send_message(message.chat.id, "🔺 Напишіть спочатку текстове повідомлення та відправте його звичним в телеграмі способом",reply_markup=keyBoardPhoto)

                            break
                        j+=1
            
                elif message.text=="🔴 перейти до фото":

                    w=0

                    while w<len(array):

                        if array[w].id_chat==message.chat.id and array[w].blockName=="🔴 інформація про правопорушення" and array[w].blockName!=0:

                                my_keyBoard[-1]
                            
                                keyBoardPhoto=my_keyBoard[2]

                                bot.send_message(message.chat.id,"🔺 Ви можеге за бажанням додати до вашого повідомлення фото, або пропустити цей крок",reply_markup=keyBoardPhoto)

                                break
                        w+=1

                elif message.text=="🔴 пропустити відправку GPS":
                    print("команда пропустити выдправку GPS")

                elif message.text=="🔴 перейти до GPS" or message.text=="🔴 пропустити відправку фото":
                    print("команда перейти до GPS")

                    my_keyBoard[-1]
                            
                    keyBoardEND=my_keyBoard[5]

                    s=0

                    while s<len(array):
                    
                        if array[s].id_chat==message.chat.id and array[s].blockName=="🔴 інформація про правопорушення" and array[s].textAboutDrugs!=0:
                                
                            
                            if array[s].photoDrugs==0:

                                array[s].photoDrugs="🔴 додавання фото пропущено"

                            bot.send_message(message.chat.id, "🔺 Ви можеге за бажанням додати до вашого повідомлення GPS координати місця повязаного з наркотиками або пропустити цей крок \n" )
                            bot.send_message(message.chat.id, "Увага ❗️❗️❗️ Дана можливість доступа тільки користувачам мобільних телефонів та планшетів. \n Якщо ви відправляете повідомлення з компьюьер",reply_markup=keyBoardEND)

                            print("GPS=",keyBoardEND)                            

                            break


                
               


            elif message.content_type=="photo":



                h=0

                while h<len(array):

                    #print("id_chat={0} \n blockName={1} \n textAboutDrugs={2}".format(array[h].id_chat,array[h].blockName,array[h].textAboutDrugs ))
                    
                    if array[h].id_chat==message.chat.id and array[h].blockName=="🔴 інформація про правопорушення" and array[h].textDrugs!=0:

                        #print("блок обработки фото: жльавление фото  ") 
                        
                        my_keyBoard[-1]
                            
                        keyBoardGPS=my_keyBoard[3]

                        document_id = message.photo[-1]
                        print("document_id=", document_id)
                        
    
                        file_info = bot.get_file(document_id.file_id)

                        print ("file info=", file_info)

                        array[h].photoDrugs="http://api.telegram.org/file/bot{0}/{1}".format(config.TOKEN, file_info.file_path)

                        bot.send_message(message.chat.id, " ✅ фото додано до вашого повідомлення",reply_markup=keyBoardGPS)

                        break
                    h+=1

            
            elif message.content_type=="location":

                try:

                    q=0

                    while q<len(array):
                    
                        if array[q].id_chat==message.chat.id and array[q].blockName=="🔴 інформація про правопорушення" and array[q].textAboutDrugs!=0 and array[q].photoDrugs!=0 and array[q].gpsAboutDrugs==0:

                            array[q].longitude=message.location.longitude

                            array[q].latitude=message.location.latitude

                            array[q].gpsAboutDrugs="https://www.google.com/maps?q=loc:{0},{1}".format(array[q].latitude, array[q].longitude)

                            photoField, GPSfield=checkField.check_value(array[q])

                            bot.send_message(config.Chanel_2, "Назва : {0}\n\n {1}\n {2}\n\n {3}\n {4}".format(array[q].blockName, photoField, array[q].photoDrugs, GPSfield, array[q].gpsAboutDrugs)) 
                            
                            break

                        q+=1
                except Exception as e:
                    print(repr(e))

                finally:

                    mainMenu.menu(bot,my_keyBoard,message)




                        #print("location=",array[q].gpsAboutDrugs)

                        # широта (latitude) 49
                        # долгота (longitude)32


            else:
               bot.send_message(message.chat.id, '2 Я не знаю що відповісти😢 \n Виберіть та натисніть  будь ласка клавішу ')
            