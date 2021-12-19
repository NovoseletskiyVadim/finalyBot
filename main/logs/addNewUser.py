from classes import classes
checkUser=classes.checkNewUser

#check_status==True or False

#словарь для checkUserUpdate
checkUpdateDictuonart={}

def addUser(message,check_status):


    user=checkUser(message.chat.id,message.from_user )

    user.addSaveNewUser(check_status)


def checkUserUpdate():

    #обращение и считиывние slogStartCommand
    #считывание данных  в словарь если словарь пуст 
    #проверка команды старт .. если она есть в файле то не писать старт в файл= в startCommand

    #TODO:сделать проверку словаря 

    #если словарь пуст загрузить его из файла
    
    
    #если команла старт есть в словаре то разрешать чат.если нет то требрвать ввода команлы старт 

    #при вводе писать старт и в словарь и в фвйл

    #словарь перенести в main

    if checkUserUpdate:

        print("dictionary exists")

    else:

        print("dictionary does not exist")


