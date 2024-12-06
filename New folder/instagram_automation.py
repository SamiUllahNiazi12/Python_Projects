from instabot import Bot
bot = Bot()

bot.login(username="jone_python08",password ="Gaurav29@")
# bot.follow("wscubetechindia")  # to follow 

# bot.upload_photo("C:/Users/Pak Sialkoti MoBile/Desktop/mix/ppppp",
                #  caption="I Love Python") # to upload a photo 

# bot.unfollow("wscubetechindia") # to unfollow

# bot.send_message("I love python",["rv_goswami_2","wscubetechindia"]) # To send message

# followers = bot.get_user_followers("jone_python08")
# for follwer in followers:  
    # print(bot.get_user_info(follower))   #about followers

following = bot.get_user_following("jone_python08")
for Following in following:
    print(bot.get_user_info(Following))