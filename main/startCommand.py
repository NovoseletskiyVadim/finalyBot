

def start(bot, my_keyBoard, array):

    #обработчик команды "старт"
    @bot.message_handler(commands=['start'])
    def welcome(message):



        sti=open('sticker/helloBot.tgs', 'rb')
        bot.send_sticker(message.chat.id,sti)
        
        m=0
        if len(array)!=0:

            while m<len(array):

                if array[m].id_chat==message.chat.id:
                    array.remove(array[m])
                    break
                l+=1
  
        bot.send_message(
            message.chat.id,
            "Добро пожаловать,"+
            " {0.first_name}!\nЯ - <b>\"{1.first_name}\"</b>,".format(message.from_user, bot.get_me())+
            " бот созданный чтобы помогать бороться с наркотиками. \n Жду информацию!",
            parse_mode='html',
            reply_markup=my_keyBoard[0]
           )
        print("команда старт")

