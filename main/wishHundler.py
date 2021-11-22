

def wishConditions(bot, message):

    @bot.message_hundler(content_types=["text","document","photo","audio"])
    def content_type_message(message):
        if message.content_type=="text":
            print("вы отправили текст")
        elif message.content_type=="document":
            print("вы отправили документ")
        elif message.content_type=="audio":
            print("вы отправили аудио")
        elif message.content_type=="photo":
            ptint("вы отправили фото")
        else:
            print("вы можете отправить только текст, документ, аудио или фото ")   



            import wishHundler
            