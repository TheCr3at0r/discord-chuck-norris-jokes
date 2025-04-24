import discord
from discord.ext import commands
import requests

YOUR_API_TOKEN = ""

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")


@bot.command()
async def next(ctx):
    response = requests.get("https://api.chucknorris.io/jokes/random")
    response_json = response.json()
    joke = response_json["value"]
    await ctx.send(joke)


bot.run(YOUR_API_TOKEN)
