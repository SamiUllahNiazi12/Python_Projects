from skpy import Skype
import os.path
slogin = Skype("prajapatgaurav08@gmail.com","prajapat29@")

contact = slogin.contacts["live:.cid.2405d0ce58c715aa"]

with open("C:/Users/Pak Sialkoti MoBile/Pictures/image","rb") as f:
    contact.chat.sendFile(f,"image",image = True)    # To send image


group = slogin.chats.create(["live:.cid.2405d0ce58c715aa",
                             "live:.cid.2405d0ce58c715bb",
                             "live:.cid.2405d0ce58c715cc"]) # To create Group


contact = slogin.contacts["live:.cid.2405d0ce58c715aa"]
contact.chat.sendMsg(" Welcome to Wscube Tech. ") # to send meassage

for i in contact :
    print(i)