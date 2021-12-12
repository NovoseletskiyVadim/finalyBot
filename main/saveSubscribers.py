
#добавление пользователей по ключу(id chat == user) в словарь из файла 

# пока нет базы сохранят информацию в файл 


def check_subscribes():

    linesFromFile=[]

    try:

        fileBaseSucscribes=open("logs/usersBotList.txt","r")

        try:
            
            for line in fileBaseSucscribes:

                linesFromFile.append(line)
                print(line, end="")


            
            #print("вывод массива строк массив=",len(linesFromFile))

            i=0

            #загрузка пользователей в словарь

            while i<len(linesFromFile):

                indexID=linesFromFile[i]

                j=0
                userField=0
                userFields=[]

                while j<len(indexID):
                    
                    if indexID[j]=="=":
                        
                        j+=1
                        indexID[j+1]
                        while type(indexID[j])==class 'int':














                    

                


                #print(linesFromFile[i])

                i+=1

                
        except Exception as e :

            print(repr(e))

    except Exception as ex:

        print(repr(ex))
        

        
            






