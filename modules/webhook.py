from discord_webhook import DiscordWebhook, DiscordEmbed
import base64
import os
def create_webhook(serverPayload):
    webhook_url = serverPayload['webhook_url']
    ip = serverPayload['ip_str']
    server_description = serverPayload['description']
    players = serverPayload['players']
    version = serverPayload['version']
    whitelist = serverPayload['whitelist']
    online = serverPayload['online']
    last_pinged = serverPayload['last_pinged']
    favicon = serverPayload['favicon']

    default_favicon = "https://media.minecraftforum.net/attachments/300/619/636977108000120237.png"

    # convert favicon base64 to image, and save it to a file called "temp.png"
    if favicon is not None:
        favicon = favicon.split(",")
        favicon = favicon[1]
        favicon = base64.b64decode(favicon)
        with open("temp.png", "wb") as file:
            file.write(favicon)
        favicon = "temp.png"

    # seperate the date and time
    last_pinged = last_pinged.split("T")
    last_pinged_date, last_pinged_time = last_pinged[0], last_pinged[1]
    # remove the milliseconds from the time
    last_pinged_time = last_pinged_time.split(".")[0]

    country_name = serverPayload['country_name']

    webhook = DiscordWebhook(url=webhook_url, username="ServerBuster")

    embed = DiscordEmbed(title=f'IP | {ip}', description=f'Description | {server_description}', color="355E3B")
    embed.set_author(name="Server Buster", url='https://github.com/TaylorDawson911/Minecraft-Server-Finder', icon_url="https://avatars.githubusercontent.com/u/98752045?s=48&v=4")
    embed.set_footer(text=f'Last Pinged | {last_pinged_date} at {last_pinged_time}')

    embed.add_embed_field(name="Players Online", value=online)
    embed.add_embed_field(name="Max Players", value=players)
    embed.add_embed_field(name="Version", value=version)
    embed.add_embed_field(name="Country", value=country_name)

    if favicon is not None:
        with open("temp.png", "rb") as file:
            webhook.add_file(file.read(), filename="temp.png")

            embed.set_thumbnail(url=f"attachment://temp.png")
    else:
        embed.set_thumbnail(url=default_favicon)

    # re

    webhook.add_embed(embed)
    response = webhook.execute()

    # delete temp.png
    if favicon is not None:
        os.remove("temp.png")
        

    return response
