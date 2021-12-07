
def message_text(bot, message, my_keyBoard, array):
    print("Абонент id №={0} розпочав роботу із інформування".format(message.chat.id))

    j=0

    while j<len(array):

        if array[j].id_chat==message.chat.id and array[j].blockName=="🔴 інформація про правопорушення":

            my_keyBoard[-1]
                            
            keyBoardBack=my_keyBoard[1]

            array[j].startWork="розпочати роботу"

            bot.send_message(message.chat.id, "🔺 Напишіть спочатку 📝 текстове повідомлення та відправте його звичним в телеграмі способом 📤",reply_markup=keyBoardBack)

            break
        j+=1
