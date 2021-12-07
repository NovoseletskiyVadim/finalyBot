import telebot
import config
import startCommand

from menu import keyBoard
from handlers import stopDrugsMessageHandler
from logs import loggingBotEroor

bot=telebot.TeleBot(config.TOKEN)

#массив кнопок бота

my_keyBoard=keyBoard.myKeyBoard()


# временный массив для хранения не отправленных форм
# когда пользователь начал оформлять свое сообщение оператору 

InfoClass=[]

errorBot=loggingBotEroor.add_info_inFile 


#создание словаря для хранения значений сат id== userName

SubscribesList=dict()



def main():

    startCommand.start(bot, my_keyBoard, InfoClass, SubscribesList, errorBot )




    stopDrugsMessageHandler.drugsMessageHundler(bot, my_keyBoard, InfoClass)

   

if __name__=='__main__':
    main()
    bot.infinity_polling()



