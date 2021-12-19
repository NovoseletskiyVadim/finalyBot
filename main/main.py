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

#словари:

#словарь команлы старт (после глобального апдейта)
checkUpdateDictuonary={}
#словарь всех пользователей
mainDictuonary={}
#TODO inicialisation and addition:
blackDictuonary={}



def main():


    startCommand.start(
                        bot,
                        my_keyBoard,
                        InfoClass,
                        mainDictuonary,
                        blackDictuonary,
                        checkUpdateDictuonary,
                        )




    stopDrugsMessageHandler.drugsMessageHundler(
                                                bot,
                                                my_keyBoard,
                                                InfoClass,
                                                
                                                )

   

if __name__=='__main__':
    main()
    bot.infinity_polling()



