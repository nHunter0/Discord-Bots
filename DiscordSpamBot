import discord
import re
import random

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as: ', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        RNG = random.randint(1, 4) #1/4 times message will send when send
        
        if  RNG == 1: 

            rere = re.search('(?i)keyWord' , message.content) #regex search for 'keyWord' in sentances 
            if rere:
                await message.channel.send('message') #If 'word' is found "message' will be sent by bot
            
client = MyClient()
client.run('DISCORD_TOKEN')
