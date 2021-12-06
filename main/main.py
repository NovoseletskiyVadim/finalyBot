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

#массив кнопок бота

my_keyBoard=keyBoard.myKeyBoard()

# временный массив для хранения не отправленных форм
# когда пользователь начал оформлять свое сообщение оператору 

InfoClass=[]



SubscribesList=dict()


def main():

    startCommand.start(bot, my_keyBoard, InfoClass, SubscribesList)




    stopDrugsMessageHandler.drugsMessageHundler(bot, my_keyBoard, InfoClass)

   

if __name__=='__main__':
    main()
    bot.infinity_polling()



