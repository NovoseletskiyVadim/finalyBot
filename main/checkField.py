

def check_value(objForm):

    infoAboutPhoto="🟢 фото місця :"
    infoAboutGPS="🟢 GPS координати місця :"

    if objForm.photoDrugs=="🔴 додавання фото пропущено":
        
        infoAboutPhoto="🔴 фото місця :"

    elif objForm.gpsAboutDrugs=="🔴 пропустити відправку GPS":

        infoAboutGPS="🔴 GPS координати місця : "

    return infoAboutPhoto , infoAboutGPS


