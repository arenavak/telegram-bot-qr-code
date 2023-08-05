
import qrcode
from telegram import Update
from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters
import telegram
import os
global TOKEN
global chanel_id

#global profile_chat_id
#profile_chat_id=[]
chanel_id="Chanel_id"
TOKEN="token"
updater=Updater(TOKEN)


def send_message(chat_id,text):
    bot=telegram.Bot(token=TOKEN)
    bot.send_message(chat_id=chat_id,text=text)

def start(update :Update , context : CallbackContext):
    chat_id=update.effective_chat.id
    """try:
        profile_chat_id.remove(chat_id)
    except:
        pass"""
    start_text="Hello welcome to QrCode_maker bot  lets start making qr codes by sending a link or a text to me ."
    send_message(chat_id,start_text)



"""def profile(update :Update , context : CallbackContext):
    chat_id=update.effective_chat.id
    profile_chat_id.append(chat_id)
    index=profile_chat_id.index()
    profile_chat_id[index][0]=0"""


#def profile1 (link,chat_id,first_name,last_name,username):
    #send_message(chat_id,"not working now")



def not_text_message(update :Update , context : CallbackContext):
    chat_id=update.effective_chat.id
    send_message(chat_id,"please send me a text or a link .")




def QrCodeAndSend(link,chat_id,first_name,last_name,username):
    BOT=telegram.Bot(token=TOKEN)
    try :
        img=qrcode.make(link)
        img.save(f"{chat_id}.jpg")
        BOT.send_photo(chat_id=chat_id,photo=open(f"{chat_id}.jpg",'rb'))
        os.remove(f"{chat_id}.jpg")

    except  :
        send_message(chat_id,"something goes wrong")




def main(update :Update , context : CallbackContext):
		
    
    chat_id=update.effective_chat.id
    username=update.effective_chat.username
    first_name=update.effective_chat.first_name
    last_name=update.effective_chat.last_name
    link=update.message.text
    BOT=telegram.Bot(token=TOKEN)
    member=BOT.get_chat_member(chat_id=chanel_id,user_id=chat_id,)
    print(username,chat_id,first_name,last_name,link,member.status)
    if  member.status!="member" and member.status!="creator":
        joining_text="for supporting us you must join https://t.me/moodyGroupchanel channel , please join this chanel and press /start"
        BOT.send_message(chat_id=chat_id,text=joining_text)
    else:
        """if profile_chat_id.count(chat_id)==1:
            pass
        elif profile_chat_id.count(chat_id)>1:
            pass
        else:"""
        QrCodeAndSend(link,chat_id,first_name,last_name,username)
        logs=f"Name :{first_name}{last_name}\nUsername:@{username}\nChat_id: {chat_id}\nText :{link}\nStatus: {member.status}"
        BOT.send_message(chat_id="137734386",text=logs)



updater.dispatcher.add_handler(CommandHandler("start", start))
#updater.dispatcher.add_handler(CommandHandler("profile",profile))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, main))
updater.dispatcher.add_handler(MessageHandler(~Filters.text,not_text_message))




updater.start_polling()
updater.idle()
