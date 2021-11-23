

def menu(bot, my_keyBoard, message):

   

        my_keyBoard[-1]
        
        reply=bot.send_message(
            message.chat.id,
            "Ви в головному меню \n"+
            "виберіть будь ласка в меню наступний крок: \n"
            "👉 🔴 інструкція із користування \n"
            "👉 🔴 інформація про правопорушення \n",
            parse_mode='html',
            reply_markup=my_keyBoard[0]
           )
        return reply
