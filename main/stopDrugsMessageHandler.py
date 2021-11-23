import wish
import mainMenu
import config


def drugsMessageHundler(bot, my_keyBoard):



    @bot.message_handler(content_types=["text", "photo", "audio", "document" ])
    def handle_text(message):
        status=0
        if message.chat.type == "private":
            print("message.chat.type =",message.chat.type )
            #print("message=",message.__str__())
            
            myBlock=[]

            if message.content_type=="text":
                
                     
           
                if message.text=="🔴 інструкція із користування":
                
                  my_keyBoard[-1]

                  wish.putWish(bot,message,my_keyBoard)

                elif message.text== "🔴 інформація про правопорушення":
                    
                    myBlock.append("🔴 інформація про правопорушення")
                    myBlock.append(message.chat.id)
                    message.text='none'
                    my_keyBoard[-1]

                    backHome=my_keyBoard[1]

                    bot.send_message(message.chat.id,
                                    "🔺 Розділ де ви можете залишити інформацію про правопорушення\n\n\n\n\n Напишіть та відправте тектове повідомдення звичним способом",
                                    reply_markup=backHome)
                    if message.text!='none':
                       
                        myBlock.append(message.text) 
                        bot.send_message(config.Chanel_2, "назва: {0} \n id= {1} \n текст повідомдення : {2}".format(myBlock[0],myBlock[1],myBlock[2]))
                    
                elif message.text=="🔴 повернутися в головне меню":
 
                    mainMenu.menu(bot,my_keyBoard,message)

                else:
                   if message.text!='none':
                       
                        myBlock.append(message.text) 
                        bot.send_message(config.Chanel_2, "назва: {0} \n id= {1} \n текст повідомдення : {2}".format(myBlock[0],myBlock[1],myBlock[2]))

            
            else:
                bot.send_message(message.chat.id, '2 Я не знаю що відповісти😢 \n Виберіть та натисніть  будь ласка клавішу ')

            
 