from classes import classes

checkUser=classes.checkNewUser

#check_status==True or False

def addUser(message,check_status):


    user=checkUser(message.chat.id,message.from_user )

    user.addSaveNewUser(check_status)

    #print("add new user")
