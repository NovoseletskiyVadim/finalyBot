from classes import classes

InfoDrugs=classes.InfoDrugs

def create_form(bot, message, my_keyBoard, array):
    i=0

    if len(array)==0:
                            
        info_drugs=InfoDrugs(message.chat.id)
                            
        info_drugs.blockName="🔴 інформація про правопорушення"

        array.append(info_drugs)

        print("Створено саму  першу форму=) \n Та добавлено заголовок повідомлення ")
    else:

        

        info_drugs=InfoDrugs(message.chat.id)
                            
        info_drugs.blockName="🔴 інформація про правопорушення"

        array.append(info_drugs)

        print("Добавлено заголовок нового повідомлення")

        


              
    my_keyBoard[-1]

    textButton=my_keyBoard[4]

    bot.send_message(message.chat.id,
                    "🔺 Ви перейшли в розділ де ви можете залишити інформацію про правопорушення \n\n "+
                    "🟡 Увага‼️  Щоб Ваше повідомлення було відправлено оператору на обробку воно має складатися із 3️⃣ х частин: \n\n"+
                    "🔴 1️⃣ Текст (обовязкова частина повідомлення) \n\n"+
                    "🔹 2️⃣ Фото місця або скиншот з телефону (цей крок можна пропустити) \n\n"+
                    "🔹 3️⃣ GPS координати (цей крок можна пропустити) \n\n"+
                    "\n\n ",
                    reply_markup=textButton)