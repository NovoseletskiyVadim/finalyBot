
def sorry_message(bot, message, my_keyBoard):

    backHome=my_keyBoard[1]

    

    bot.send_message(message.chat.id,"🔺 Вибачте, даний розділ зараз розробляється ", reply_markup=backHome)

    sti=open('sticker/catFlirt.tgs', 'rb')
    bot.send_sticker(message.chat.id,sti)