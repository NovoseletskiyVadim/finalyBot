
import telebot
from telebot import types

#add keyboard

def myKeyBoard():

    #[0]
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("🔴 інструкція із користування")
    item2=types.KeyboardButton("🔴 інформація про правопорушення" )
    markup=markup.add(item1,item2)
    
    #[1]
    service = telebot.types.ReplyKeyboardMarkup(True, True)
    markup_back=service.row('🔴 відмінити та повернутися в головне меню')

    #[2]
    markupPhoto=telebot.types.ReplyKeyboardMarkup(True, True)
    buttonsPhoto=markupPhoto.row('🔴 відмінити та повернутися в головне меню')
    buttonsPhoto=markupPhoto.row('🔴 пропустити відправку фото')
    buttonsPhoto=markupPhoto.row('🔴 перейти до фото')

    #[3]
    markupGPS=types.ReplyKeyboardMarkup(True, True)
    buttonsGPS=markupGPS.row('🔴 відмінити та повернутися в головне меню')
    buttonsGPS=markupGPS.row('🔴 пропустити відправку GPS')
    buttonsGPS=markupGPS.row('🔴 перейти до GPS')

    #[4]
    markupText=telebot.types.ReplyKeyboardMarkup(True, True)
    buttonsText=markupText.row('🔴 відмінити та повернутися в головне меню')
    buttonsText=markupText.row('🔴 перейти до повідомлення')

    #[5]
    markupEND=types.ReplyKeyboardMarkup()
    item4=types.KeyboardButton("🔴 я відправляю з компьтера")
    item5=types.KeyboardButton("🔴 відправити GPS", request_location=True)

    markup_end=markupEND.add(item4,item5)



    

    #[-1]
    remove=types.ReplyKeyboardRemove()

    all_buttons=[markup,markup_back,buttonsPhoto,buttonsGPS,markupText,markup_end, remove]

    return all_buttons
