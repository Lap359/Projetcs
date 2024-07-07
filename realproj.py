def listusers():
    file=open('database.txt','r')
    data=file.readlines()
    print('User Lists')
    for line in data:
        print(line)
    print("------------------")
    file.close()

def useradd():
    file=open('database.txt','a+')
    print("Add new user: Please fillout all information listed below.")
    name=input('User name:')
    age=input('Age of user:')
    classgg=input('Class:')
    hmetwn=input('User home town:')
    infos=name+','+age+','+classgg+','+hmetwn+'\n'
    file.write(infos)
    file.close()
    print("Successfully added!")

def userdel():
    stt=int(input("Number of the deleting user:"))
    file=open('database.txt','r')
    dnhsch=file.readlines()
    file.seek(0)
    count=0
    for line in dnhsch:
        if stt != count:
            file.write(line)
        count+=1
    file.close()
    print('Successfully deleted user!')

def finduser():
    name=input('User name to find:')
    file=open('database.txt','r+')
    dnhsch=file.readlines(0)
    for line in dnhsch:
        dnhsch2=line.split(',')
        if dnhsch2[0]==name:
            print("The found informations are:")
            print(line)
            file.close()
            return
        if dnhsch[0]!=name:
            print('Information not found!')
            print('This my cause by info not on database or the file has been moved to somewhere.')
    file.close()

def credits():
    MainCodes='Lap359/GreesTree'
    ContactEmail='vuhai4135@gmail.com'
    print(MainCodes)
    print(ContactEmail)