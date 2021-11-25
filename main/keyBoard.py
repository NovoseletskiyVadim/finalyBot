
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
    markup_back=service.row('🔴 повернутися в головне меню')

    #[2]
    markupPhoto=telebot.types.ReplyKeyboardMarkup(True, True)
    buttonsPhoto=markupPhoto.row('🔴 повернутися в головне меню')
    buttonsPhoto=markupPhoto.row('🔴 пропустити відправку фото')
    buttonsPhoto=markupPhoto.row('🔴 перейти до фото')

    #[3]
    markupGPS=telebot.types.ReplyKeyboardMarkup(True, True)
    buttonsGPS=markupGPS.row('🔴 відмінити та повернутися в головне меню')
    buttonsGPS=markupGPS.row('🔴 пропустити відправку GPS')
    buttonsGPS=markupGPS.row('🔴 перейти до GPS')


    

    #[-1]
    remove=types.ReplyKeyboardRemove()

    all_buttons=[markup,markup_back,buttonsPhoto,buttonsGPS,remove]

    return all_buttons
