
def text_processing(bot, message, my_keyBoard, array):

    if len(array)!=0:
        y=0

        while y<len(array):

            if array[y].id_chat==message.chat.id and array[y].blockName=="🔴 інформація про правопорушення" and array[y].startWork=="розпочати роботу" and array[y].textDrugs==0 :

                my_keyBoard[-1]
                            
                keyBoardPhoto=my_keyBoard[2]

                if len(message.text)>15:

                    array[y].textDrugs=message.text

                    bot.send_message(message.chat.id, "✅ Ваше текстове повідомлення  збережено\n\n🔺 📷 наступний крок: ФОТО \n\nℹ️ Ви можете за бажанням додати до вашого повідомлення 📷 фото,та відправити його звичайним способом, або ⏩ пропустити цей крок",reply_markup=keyBoardPhoto)
                else:

                    my_keyBoard[-1]
                            
                    keyBoardHome=my_keyBoard[1]

                    bot.send_message(message.chat.id,"🟡 Увага ❗️❗️❗️ \n\n⛔️ Помилка. Спочатку Ви маєте обов'язково 🖨⌨️ написати та відправити коротке текстове повідомлення(🔸 мінімальний об'єм тексту від 1️⃣5️⃣ символів)",reply_markup=keyBoardHome )
                                    
                    sti=open('sticker/attention.tgs', 'rb')
                    bot.send_sticker(message.chat.id,sti)

            elif array[y].id_chat==message.chat.id and array[y].blockName=="🔴 інформація про правопорушення" and array[y].startWork==0:

                sti=open('sticker/catDontKnow.tgs', 'rb')
                bot.send_sticker(message.chat.id,sti)
                
                bot.send_message(message.chat.id, ' Я не знаю що відповісти😢 \n Виберіть та натисніть\n\n👉 ❌ все відмінити та повернутися в головне меню\n\nабо\n\n👉 ❇️ розпочати роботу')
                             
            elif array[y].id_chat==message.chat.id and array[y].photoDrugs!=0 and array[y].gpsAboutDrugs==0:

                            
                keyBoardEND=my_keyBoard[-2]

                bot.send_message(message.chat.id,"🟡 Увага ❗️❗️❗️ \n\n⛔️ Помилка.\n\n✅ Текст повідомлення та 📷 фото Вами вже збережено ❗️\n\n🔺 🌐 Наступний крок: 📡 GPS \n\nℹ️ Ви можете за бажанням додати до вашого повідомлення 📡 GPS координати місця повязаного з наркотиками чи ⏩ пропустити цей крок \n")    
                bot.send_message(message.chat.id, "🟡 Увага ❗️❗️❗️ Дана можливість доступа тільки користувачам мобільних телефонів та планшетів. \n",reply_markup=keyBoardEND)

                sti=open('sticker/attention.tgs', 'rb')
                bot.send_sticker(message.chat.id,sti)

                
            elif array[y].id_chat==message.chat.id and array[y].blockName=="🔴 інформація про правопорушення" and array[y].textDrugs!=0:

                my_keyBoard[-1]
                            
                keyBoardPhoto=my_keyBoard[2]

                bot.send_message(message.chat.id,"🟡 Увага ❗️❗️❗️ \n\n⛔️ Помилка.\n\n✅ Текст повідомлення Вами вже збережено ❗️\n\n🔺 📷 наступний крок: ФОТО \n\nℹ️ Ви можеге за бажанням додати до вашого повідомлення 📷 фото,та відправити його звичайним способом, або ⏩ пропустити цей крок ",reply_markup=keyBoardPhoto )    

                sti=open('sticker/attention.tgs', 'rb')
                bot.send_sticker(message.chat.id,sti)

           

            y+=1

    else:

        sti=open('sticker/catDontKnow.tgs', 'rb')
        bot.send_sticker(message.chat.id,sti)

        bot.send_message(message.chat.id, ' Я не знаю що відповісти😢 \n Виберіть та натисніть\n\n👉 📖 інструкція із користування\n\nабо\n\n👉 🔴 повідомити про правопорушення')

