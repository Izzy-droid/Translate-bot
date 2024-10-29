import discord
import translators as ts
import os
import audioop


intents = discord.Intents.default()
client  = discord.Client(intents=intents)
intents.message_content = True

@client.event 
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

#when bot gets a message
async def send_message(channel, msg):
  await channel.send(msg)
  
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('/hello'):
    await message.channel.send('Hello, I am a translator bot. I can translate text to any language. Just type /translate from, to. To translate any previous message.')

  if message.content.startswith('/feedback'):
    await message.channel.send('Please provide your feedback via. @mentioning me and typing your feedback.')
    
  if message.content.startswith('/translate spn, eng'):
    #history
    messages= [msg async for msg in message.channel.history(limit=2)]
    message_before_command= messages[1]
    text_to_translate = message_before_command.content
    
    #detect language
    #detected_lang= ts.detect(text_to_translate)
    translated= ts.translate_text(text_to_translate,from_language='es', to_language='en', translators='google')
    #send back translated text
    await message.channel.send(translated)  
  if message.content.startswith('/translate eng, spn'):
    #history
    messages= [msg async for msg in message.channel.history(limit=2)]
    message_before_command= messages[1]
    text_to_translate = message_before_command.content
    #detect language
    
    translated= ts.translate_text(text_to_translate,from_language='en', to_language='es', translators='google')
    #send back translated text
    await message.channel.send(translated) 

#find how to detect text to translate
 
client.run('')