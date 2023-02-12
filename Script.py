from instabot import Bot
import csv
import requests
import os
import shutil

#delete if exist the directory /home/rouxmi/Documents/Baroudeur/Script-BaroupasseD/config

def deleteFolder():
    if os.path.exists('/home/rouxmi/Documents/Baroudeur/Script-BaroupasseD/config'):
        shutil.rmtree('/home/rouxmi/Documents/Baroudeur/Script-BaroupasseD/config')
        print("Le dossier config a été supprimé")
    else:
        print("Le dossier config n'existe pas")

deleteFolder()



bot = Bot()

#read the file Documents/codebaroudeur.txt to get the username and the password
with open('/home/rouxmi/Documents/Baroudeur/Script-BaroupasseD/codebaroudeur.txt', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)
    for row in your_list:
        username=row[0]
        password=row[1]
        #login with the username and the password   
        bot.login(username=username, password=password)

with open('/home/rouxmi/Documents/Baroudeur/Script-BaroupasseD/BarouPasseD.csv', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)
    for row in your_list[1:]:
        #get the date of the message row[0] and read the file date.txt to know if the message has already been sent
        #if the message has already been sent, skip the message
        date = row[0]
        with open('/home/rouxmi/Documents/Baroudeur/Script-BaroupasseD/date.txt', 'r') as f:
            if date in f.read():
                continue
        #if the message has not been sent, send it and add the date to the file date.txt
        with open('/home/rouxmi/Documents/Baroudeur/Script-BaroupasseD/date.txt', 'a') as f:
            f.write(date+"\n")
            #get the destinataire and check if the account exists
        destinataire=row[3].replace("@","")
        response = requests.get("https://instagram.com/" + destinataire + "/")
        if response.status_code != 404 :
            #ask friend the destinataire
            bot.follow(destinataire)
            message=row[4]
            #bot.send_message(message, [destinataire])
            message="❤️❤️ BarouPasse-D ❤️❤️\n"+ message
            if row[5] != "Oui stp":
                #add some heart at the start of the message 
                message+="\nDe la part de "+row[6]
            #print the destinataire and the message
            bot.send_message(message, [destinataire])     
            print("Message envoyé à "+destinataire)   
        
        
        
        
        
   