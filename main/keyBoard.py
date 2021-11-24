
import telebot
from telebot import types

#add keyboard

def myKeyBoard():

    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("🔴 інструкція із користування")
    item2=types.KeyboardButton("🔴 інформація про правопорушення" )

    markup=markup.add(item1,item2)

    service = telebot.types.ReplyKeyboardMarkup(True, True)
    markup_back=service.row('🔴 повернутися в головне меню')

    markupPhoto=telebot.types.ReplyKeyboardMarkup(True, True)
    buttonsPhoto=markupPhoto.row('🔴 повернутися в головне меню')
    buttonsPhoto=markupPhoto.row('🔴 пропустити')
    buttonsPhoto=markupPhoto.row('🔴 перейти до фото')


    


    remove=types.ReplyKeyboardRemove()

    all_buttons=[markup,markup_back,buttonsPhoto,remove]

    return all_buttons
