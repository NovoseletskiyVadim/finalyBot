

import config
import telebot


bot=telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):

    sti=open('sticker/AnimatedSticker1.tgs', 'rb')
    bot.send_sticker(message.chat.id,sti)

    bot.send_message(
        message.chat.id,
        "Добро пожаловать,"+
        " {0.first_name}!\nЯ - <b>\"{1.first_name}\"</b>,".format(message.from_user, bot.get_me())+
        " бот созданный чтобы быть подопытным кроликом.",
        parse_mode='html',
       )








@bot.message_handler(content_types=["text"])
def repeat_allMessages(message):

    print("message.chat.id=",message.chat.id)

    bot.send_message(config.Chanel_2, message.text)


if __name__=='__main__':
    bot.infinity_polling()
