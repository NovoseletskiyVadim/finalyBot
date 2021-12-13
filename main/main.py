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
#done
mainDictuonary={}
#TODO inicialisation and addition:
blackDictuonary={}

errorBot=loggingBotEroor.add_info_inFile 




def main():


    startCommand.start(
                        bot,
                        my_keyBoard,
                        InfoClass,
                        mainDictuonary,
                        blackDictuonary,
                        
                        )




    stopDrugsMessageHandler.drugsMessageHundler(
                                                bot,
                                                my_keyBoard,
                                                InfoClass,
                                                
                                                )

   

if __name__=='__main__':
    main()
    bot.infinity_polling()



