import discord
#importação da lib

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
#Nossa conexão com o Discord. Instância da classe Client

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Olá, como vai? ' + str(message.author))

client.run('XXX')
