import wish
import mainMenu
import config


def drugsMessageHundler(bot, my_keyBoard):



    @bot.message_handler(content_types=["text", "photo", "audio", "document" ])
    def handle_text(message):
        status=0
       
        if message.chat.type == "private":
            print("message.chat.type==private")
            #print("message.chat.type =",message.chat.type )
            #print("message=",message.__str__())
            myBlock=[]
            

            if message.content_type=="text":
                
                     
           
                if message.text=="🔴 інструкція із користування":
                
                  my_keyBoard[-1]

                  wish.putWish(bot,message,my_keyBoard)

                elif message.text== "🔴 інформація про правопорушення":

                    #myBlock.insert(0, 'none')
                    #myBlock.insert(1, 'none')
                    #myBlock.insert(2, 'none')
                    
                    myBlock.insert(0,"🔴 інформація про правопорушення")
                    myBlock.insert(1, message.chat.id)
                    
                    my_keyBoard[-1]

                    backHome=my_keyBoard[1]

                    bot.send_message(message.chat.id,
                                    "🔺 Ви перейшли в розділ де ви можете залишити інформацію про правопорушення \n\n "+
                                    "Увага‼️  Щоб Ваше повідомлення було відправлено на обробку воно має складатися із 3 частин \n\n"+
                                    "🔴 1.Текст (обовязкова частина повідомлення) \n\n"+
                                    "🔶 2.Фото місця або скиншот з телефону (цей крок можна пропустити) \n\n"+
                                    "🔶 3.GPS координати (цей крок можна пропустити) \n\n"+
                                    "Увага‼️ лише після цього сформоване повідомлення відправиться оператору на обробку \n\n"+
                                    "\n\n ",
                                    reply_markup=backHome)
                    print("перед отправкой текста")
                    i=0
                    while i<len(myBlock):
                        print(myBlock[i])
                        i+=1
                  
                        
                    keyBoardPhoto=my_keyBoard[2]

                    bot.send_message(message.chat.id, "🔺 Напишіть спочатку текстове повідомлення та відправте його звичним в телеграмі способом",reply_markup=keyBoardPhoto)

                        #bot.send_message(config.Chanel_2, "назва: {0} \n id= {1} \n текст повідомдення : {2}".format(myBlock[0],myBlock[1],myBlock[2]))
                    
                elif message.text=="🔴 повернутися в головне меню":
                    
                    print("перед  обнулением")
                    #myBlock.insert(0, 'none')
                    #myBlock.insert(1, 'none')
                    #myBlock.insert(2, 'none')


                    print("размер массива=",len(myBlock))

                    #проверка
                    p=0
                    while p<len(myBlock):
                        print(myBlock[p])
                        p+=1



                    mainMenu.menu(bot,my_keyBoard,message)

                    print("после обнуления")
                    j=0
                    while j<len(myBlock):
                        print(myBlock[j])
                        j+=1

                else:
                   if message.text!='none':
                       
                        bot.send_message(config.Chanel_2, message.text)

                        bot.send_message(config.Chanel_2, "назва: {0} \n id= {1} \n текст повідомдення : {2}".format(myBlock[0],myBlock[1],myBlock[2]))

            
            else:
                bot.send_message(message.chat.id, '2 Я не знаю що відповісти😢 \n Виберіть та натисніть  будь ласка клавішу ')

            
 