import wish


def textMessageHundler(bot, my_keyBoard):


    @bot.message_handler(content_types=["text"])
    def handle_text(message):

        if message.chat.type == "private":
            if message.text=="🔴 Залишити побажання":
                try:
                    my_keyBoard[-1]
                    

                except Exception as e:
                    print(repr(e))

                wish.putWish(bot,message,my_keyBoard)

            elif message.text== "🔴 Повідомити про правопорушення":
                bot.send_message(message.chat.id,
                                "🔺 Розділ де ви можете залишити інформацію про правопорушення\n")

            else:
                bot.send_message(message.chat.id, 'Я не знаю що відповісти😢 \n Виберіть будьласка клавішу та натисніть!')
 