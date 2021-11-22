
import telebot
from telebot import types

#add keyboard

def myKeyBoard():

    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("🔴 Залишити побажання")
    item2=types.KeyboardButton("🔴 Повідомити про правопорушення" )

    markup=markup.add(item1,item2)

    service = telebot.types.ReplyKeyboardMarkup(True, True)
    markup_back=service.row('🔴 Повернутися у головне меню')

    remove=types.ReplyKeyboardRemove()

    all_buttons=[markup,markup_back,remove]

    return all_buttons
