import os
import discord as dc
from keep_alive import keep_alive
import time

client = dc.Client()
my_secret = os.environ['TOKEN']



@client.event
async def on_ready():
    print("Yo, I'm currently logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('??cringe'):
        await message.channel.send('Hmm... Sounds like Eli.')

    if message.content.startswith('??1min'):
      await message.channel.send("Pinging in one minute...")
      time.sleep(60)
      await message.channel.send("One minute timer is up " + message.author.mention)

    if message.content.startswith('??ping'):
      await message.channel.send(message.author.mention)

    if message.content.startswith("hi amin bot"):
      await message.channel.send("Whats good homie")
    

keep_alive()
client.run(my_secret)
