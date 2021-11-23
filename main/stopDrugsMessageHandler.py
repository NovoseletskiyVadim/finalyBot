import wish


def drugsMessageHundler(bot, my_keyBoard):



    @bot.message_handler(content_types=["text", "photo", "audio", "document" ])
    def handle_text(message):

        if message.chat.type == "private":
            print("message.chat.type =",message.chat.type )
            #print("message=",message.__str__())
            
            if message.content_type=="text":
            
           
                if message.text=="🔴 інструкція із користування":
                
                  my_keyBoard[-1]

                  wish.putWish(bot,message,my_keyBoard)

                elif message.text== "🔴 інформація про правопорушення":

                    my_keyBoard[-1]

                    backHome=my_keyBoard[1]
                    bot.send_message(message.chat.id,
                                    "🔺 Розділ де ви можете залишити інформацію про правопорушення\n",
                                    reply_markup=backHome)
                
                elif message.text=="/start":

                   

                    bot.send_message(message.chat.id, message.text)

                else:
                    bot.send_message(message.chat.id, 'Я не знаю що відповісти😢 \n Виберіть та натисніть  будь ласка клавішу ')
            
            else:
                bot.send_message(message.chat.id, 'Я не знаю що відповісти😢 \n Виберіть та натисніть  будь ласка клавішу ')

            
 