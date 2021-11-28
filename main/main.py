import config
import startCommand
import keyBoard
import stopDrugsMessageHandler
import mainMenu

import telebot
import urllib.request # request нужен для загрузки файлов от пользователя
#from telebot import types
#from classes import InfoDrugs


bot=telebot.TeleBot(config.TOKEN)
my_keyBoard=keyBoard.myKeyBoard()

InfoClass=[]


def main():

    startCommand.start(bot, my_keyBoard)




    stopDrugsMessageHandler.drugsMessageHundler(bot, my_keyBoard, InfoClass)

   

if __name__=='__main__':
    main()
    bot.infinity_polling()



#@bot.message_handler(content_types=["text"])
##@bot.message_handler(content_types=["photo"])

#def repeat_allMessages(message):

#    print("message.chat.id=",message.chat.id)

#    bot.send_message(message.chat.id,"🔺 Розділ де ви можете залишити ваші побажання \n"+
#                            " щодо зручності користування \n "+
#                            "та функціоналу боту", reply_markup=markup)
#    document_id = message.document.file_id
    
#    file_info = bot.get_file(document_id)
#    print(" document_id=",message.document.file_id)

#    bot.send_message(config.Chanel_2, message.text)

    
#@bot.message_handler(content_types=["photo"])
#def handle_docs_audio(message):

#    document_id = message.photo.file_id
    
#    file_info = bot.get_file(document_id)
#    print(" document_id=",message.document.file_id)
#    #urllib.request.urlretrieve(f'http://api.telegram.org/file/bot{config.TOKEN}/{file_info.file_path}', file_info.file_path) 
#    bot.send_message(config.Chanel_2, file_info.file_path)



#    if message.chat.type == "private":
#        if message.text=="🔴 Залишити побажання":

            
#            bot.send_message(message.chat.id,"🔺 Розділ де ви можете залишити ваші побажання \n"+
#                             " щодо зручності користування \n "+
#                             "та функціоналу боту", reply_markup=service)

#            bot.send_message(message.chat.id,
#                            "🔺 Напишіть та відправте повідомлення звич способом," )

#        elif message.text== "🔴 Повідомити про правопорушення":
#            bot.send_message(message.chat.id,
#                            "🔺 Розділ де ви можете залишити інформацію про правопорушення\n")

#        else:
#            bot.send_message(message.chat.id, 'Я не знаю що відповісти😢 \n Виберіть будьласка клавішу та натисніть!')
 


        





    #bot.send_message(config.Chanel_2, message.text)

#@bot.callback_query_handler(func=lambda call: True)
#def callback_reply(call):
#    try:
#        if call.message:
#            if call.data=="wish":
#                bot.send_message(call.message.chat.id, "Ты вибрал оставить пожелание")
#            elif call.data=="drug":
#                bot.send_message(call.message.chat.id, "Ты вибрал сообщить про наркотики")
#            else:
#                bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')   


#    except Exception as e:
#        print(repr(e))




    #@bot.message_handler(commands=['start'])
    #def selfmyself(message):
    #    service = telebot.types.ReplyKeyboardMarkup(True, True)
    #    service.row('Wunderlist')
    #    service.row('Telegraph')
    #    service.row('Погода')
    #    bot.send_message(message.from_user.id, 'Что будем делать?', reply_markup=service)


    #@bot.message_handler(content_types=['text'])
    #def handle_text(message):
    #    if message.text == "Wunderlist":
    #        a = telebot.types.ReplyKeyboardRemove()
    #        bot.send_message(message.from_user.id, 'Что', reply_markup=a)