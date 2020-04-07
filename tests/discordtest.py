import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged on as", self.user)

    async def notify(ctx, member: discord.Member, *, content):
        channel = await member.create_dm()
        await channel.send(content)


client = MyClient()
client.run("Njk2OTcwMzE5NDAzMTU1NTI3.Xowf6g.Aqt7JDPXQ4uvUiFYDViVj_R8Vjw")


client.notify(self.author, "Arun8560", "hi")
