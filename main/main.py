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

    startCommand.start(bot, my_keyBoard, InfoClass)




    stopDrugsMessageHandler.drugsMessageHundler(bot, my_keyBoard, InfoClass)

   

if __name__=='__main__':
    main()
    bot.infinity_polling()



