from classes import classes
InfoDrugs=classes.InfoDrugs

#creating a post form and adding a form header

def create_form(bot, message, my_keyBoard, array):

                            
    info_drugs=InfoDrugs(message.chat.id)
                            
    info_drugs.blockName="🔴 інформація про правопорушення"

    array.append(info_drugs)
        


              
    my_keyBoard[-1]

    textButton=my_keyBoard[-3]

    bot.send_message(message.chat.id,
                    "🔺 Ви перейшли в розділ де ви можете залишити інформацію про правопорушення \n\n "+
                    "🟡 Увага‼️  Щоб Ваше повідомлення було відправлено оператору на обробку воно має складатися із 3️⃣ х частин: \n\n"+
                    "🔴 1️⃣ Текст (обовязкова частина повідомлення) \n\n"+
                    "🔹 2️⃣ Фото місця або скиншот з телефону (цей крок можна пропустити) \n\n"+
                    "🔹 3️⃣ GPS координати (цей крок можна пропустити) \n\n"+
                    "\n\n ",
                    reply_markup=textButton)