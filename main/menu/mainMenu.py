

def menu(bot, my_keyBoard, message, array):

        my_keyBoard[-1]
        
        l=0

        if len(array)!=0:

            while l<len(array):

                if array[l].id_chat==message.chat.id:
                    array.remove(array[l])
                    break
                l+=1


        sti=open('sticker/helloBot.tgs', 'rb')
        catBot=bot.send_sticker(message.chat.id,sti)


        reply=bot.send_message(
            message.chat.id,
            "Ви знову в головному меню \n"+
            "виберіть будь ласка в меню наступний крок: \n"
            "👉 🔴 інструкція із користування \n"
            "👉 🔴 інформація про правопорушення \n",
            parse_mode='html',
            reply_markup=my_keyBoard[0]
           )
        return reply, catBot
