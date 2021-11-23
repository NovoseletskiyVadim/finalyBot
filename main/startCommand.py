

def start(bot, my_keyBoard):

    #обработчик команды "старт"
    @bot.message_handler(commands=['start'])
    def welcome(message):


        print("message from start",message)

        sti=open('sticker/AnimatedSticker1.tgs', 'rb')
        bot.send_sticker(message.chat.id,sti)

  
        bot.send_message(
            message.chat.id,
            "Добро пожаловать,"+
            " {0.first_name}!\nЯ - <b>\"{1.first_name}\"</b>,".format(message.from_user, bot.get_me())+
            " бот созданный чтобы помогать бороться с наркотиками. \n Жду информацию!",
            parse_mode='html',
            reply_markup=my_keyBoard[0]
           )

