
class InfoDrugs :

    #costructor

    def __init__(self, id_chat):
        
        self.id_chat=id_chat
        print("обьект {0} создан".format(self.id_chat))

    def __del__(self):

        print("обьект {0} удален из памяти".format(self.id_chat))

   
    textAboutDrugs=0

    photoAboutDrugs=0

    gpsAboutDrugs=0

    blockName=0


    def get_idChat(self):
        print("metod get id chat")
        return self.id_chat



