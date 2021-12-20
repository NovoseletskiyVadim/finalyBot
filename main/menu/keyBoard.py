
import telebot
from telebot import types

#add keyboard

def myKeyBoard():

    #[0]
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("📖 користувачам боту")
    item2=types.KeyboardButton("🔴 повідомити про правопорушення" )
    markup=markup.add(item1,item2)
    
    #[1]
    service = telebot.types.ReplyKeyboardMarkup(True, True)
    markup_back=service.row('❌ все відмінити та повернутися в головне меню')

    #[2]
    markupPhoto=telebot.types.ReplyKeyboardMarkup(True, True)
    buttonsPhoto=markupPhoto.row('❌ все відмінити та повернутися в головне меню')
    buttonsPhoto=markupPhoto.row('⏩ пропустити відправку фото')

    #[3]
    markupGPS=types.ReplyKeyboardMarkup(True, True)
    buttonsGPS=markupGPS.row('❌ все відмінити та повернутися в головне меню')
    buttonsGPS=markupGPS.row('⏩ пропустити відправку GPS')

    #[4]
    markupStart = telebot.types.ReplyKeyboardMarkup(True, True)
    buttonStart = markupStart.row("/start" )

    #[5 /-3]
    markupText=telebot.types.ReplyKeyboardMarkup(True, True)
    buttonsText=markupText.row('❌ все відмінити та повернутися в головне меню')
    buttonsText=markupText.row('❇️ розпочати роботу')

    #[6 /-2]
    markupEND=types.ReplyKeyboardMarkup(resize_keyboard=False)
    item4=types.KeyboardButton("❌ все відмінити та повернутися в головне меню")
    item5=types.KeyboardButton("⏩ пропустити відправку GPS")
    item6=types.KeyboardButton("✅ відправити GPS", request_location=True)

    markup_end=markupEND.add(item4,item5,item6)



    

    #[7 /-1]
    remove=types.ReplyKeyboardRemove()

    all_buttons=[markup,markup_back,buttonsPhoto,buttonsGPS,buttonStart,markupText,markup_end, remove]

    return all_buttons
