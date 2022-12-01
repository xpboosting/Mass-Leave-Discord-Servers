import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
token = "bottoken"

whitelist = [
    # discord guild ids you don't want to leave
    123,
    123
]


@client.event
async def on_ready():
    for guild in client.guilds:
        try:
            if guild.id not in whitelist:
                server = client.get_guild(guild.id)
                await server.leave()
        except Exception as e:
            print(e)


client.run(token)
