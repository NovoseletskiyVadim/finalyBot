

def putWish(bot,message, keyBoard ):

    backHome=keyBoard[1]

    bot.send_message(message.chat.id,"🔺 Розділ де ви можете залишити ваші побажання \n"+
                                 " щодо зручності користування \n "+
                                 "та функціоналу боту", reply_markup=backHome)
    bot.send_message(message.chat.id,
                                "🔺 Напишіть та відправте повідомлення звич способом," )
    bot.send_message("-255849345", message.text)

   
    
    


    
