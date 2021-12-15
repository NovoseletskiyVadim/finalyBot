import config
import wish
import sorry
from menu import mainMenu
from menu import keyBoard
from handlers import checkField
from handlers import locationHandler
from handlers import photoHandler
from handlers import textHandler
from handlers import formHandler
from handlers import createTextMessageButtonHandler

#from classes import InfoDrugs

# обработчик всего входящего контента 

 
def drugsMessageHundler(bot, my_keyBoard, array):



    @bot.message_handler(content_types=["text", "photo", "audio", "document","location" ])
    def handle_text(message):
        
        
       
        if message.chat.type == "private":
            #print("message.chat.type==private")
           

            if message.content_type=="text":

                if message.text=="📖 інструкція із користування":
                
                  my_keyBoard[-1]

                  wish.putWish(bot,message,my_keyBoard)

                elif message.text== "🔴 повідомити про правопорушення":
                    
                    #create form of message
                    formHandler.create_form(bot, message, my_keyBoard, array)

                elif message.text=="❌ все відмінити та повернутися в головне меню":

                    #button handling"отменить "
                    mainMenu.menu(bot,my_keyBoard,message, array)

                elif message.text=="❇️ розпочати роботу" :

                    #button handling "начать работу"
                    createTextMessageButtonHandler.message_text(bot, message, my_keyBoard, array)
                     
                elif message.text=="⏩ пропустити відправку GPS":

                    #обработка "пропустить отправку GPS"
                    locationHandler.skipGPS(bot, message, my_keyBoard, array)

                elif message.text=="⏩ пропустити відправку фото":

                    #обработка (прпустить отправку фото)
                    photoHandler.skip_photo(bot, message, my_keyBoard, array)


                else:

                    #обработка отправки тестового соопщения 
                    textHandler.text_processing(bot, message, my_keyBoard, array)
                                   


            elif message.content_type=="photo":

                #обработка отправки фото 
                photoHandler.photo_processing(bot, message, my_keyBoard, array)

                

            
            elif message.content_type=="location":
                
                #Обработка отправки GPS
                locationHandler.gps_processing(bot, message, my_keyBoard, array)
               



                        

            
            