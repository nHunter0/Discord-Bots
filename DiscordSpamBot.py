import discord

client = discord.Client()
keywords = ["!releaseSpamBot"] #discord command
@client.event
async def on_message(message):
    for i in range(len(keywords)):
        if keywords[i] in message.content:
            for j in range(10): #amount of time message will be spamed by bot 
                await message.channel.send("spamMessage") #message that will be spamed by bot
                
client.run('DISCORD_TOKEN')
