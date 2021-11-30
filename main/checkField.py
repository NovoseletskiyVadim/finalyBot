

def check_value(objForm):

    infoAboutText="🟢 текст повідомлення:"
    infoAboutPhoto="🟢 фото місця :"
    infoAboutGPS="🟢 GPS координати місця :"

    if objForm.photoDrugs=="🔴 додавання фото пропущено":
        
        infoAboutPhoto="🔴 фото місця :"

    elif objForm.gpsAboutDrugs=="🔴 пропустити відправку GPS":

        infoAboutGPS="🔴 GPS координати місця : "

    return infoAboutText, infoAboutPhoto , infoAboutGPS


