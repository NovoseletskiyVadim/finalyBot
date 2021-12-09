
#проверка формы перед отправкой в канал


def check_value(objForm):

    infoAboutText="🟢 текст :"
    infoAboutBlock="🔺 📬 інформація про наркотики"
    infoAboutPhoto="🟢 фото місця :"
    infoAboutGPS="🟢 GPS координати місця :"

    if objForm.photoDrugs=="додавання фото пропущено" and objForm.gpsAboutDrugs=="додавання GPS пропущено" :
        
        infoAboutPhoto="🔴 фото місця :"
        infoAboutGPS="🔴 GPS координати місця :"

    elif objForm.photoDrugs=="додавання фото пропущено":

        infoAboutPhoto="🔴 фото місця :"

    elif objForm.gpsAboutDrugs=="додавання GPS пропущено":

        infoAboutGPS="🔴 GPS координати місця : "

        print("infoAboutGPS=",infoAboutGPS)


        

    return infoAboutBlock, infoAboutText, infoAboutPhoto , infoAboutGPS


