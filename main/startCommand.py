from classes import classes

logCommandStart=classes.logInputCommandStart

def start(bot, my_keyBoard, array, users):

    #обработчик команды "старт"
    @bot.message_handler(commands=['start'])
    def welcome(message):



        sti=open('sticker/helloBot.tgs', 'rb')
        bot.send_sticker(message.chat.id,sti)


        #add user in dictuonary

        id=str(message.chat.id)
        first_name=str(message.from_user.first_name)
        last_name=str(message.from_user.last_name)

        # counting command "start"
        count_command=logCommandStart(id, first_name, last_name)

        #newUser=addNewUser(id, first_name, last_name)



        # временная проверка состояния словаря
        #print("====Check dictuonary====")

        #for key in users:
        #    print(key," - ",users[key])

        
        m=0
        if len(array)!=0:
            
            # обработка команлы старт, на тот случай если пользователь ее запустит после того как 
            # форма для отправки сообщения уже сформирована и добавлена в массив
            # удалит ее из временного  массива форм


            while m<len(array):

                if array[m].id_chat==message.chat.id:
                    array.remove(array[m])
                    break
                m+=1
  
        bot.send_message(
            message.chat.id,
            "Добро пожаловать,"+
            " {0.first_name}!\nЯ - <b>\"{1.first_name}\"</b>,".format(message.from_user, bot.get_me())+
            " бот созданный чтобы помогать бороться с наркотиками. \n Жду информацию!",
            parse_mode='html',
            reply_markup=my_keyBoard[0]
           )
        print("команда старт")

