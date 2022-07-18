import discord
from discord.ext import commands, tasks
import json
import os
from webscrapping.webscrapper import tracker
from webscrapping.dict import global_data_dict
from webscrapping.dict import sorted_countries


client = commands.Bot(command_prefix='?')


client.global_info = tracker()
client.global_dict = global_data_dict(client.global_info)
client.countries_sorted = sorted_countries(client.global_info)



@tasks.loop(hours=2) # updates every 2 hours 
async def update():
    client.global_info = tracker()
    client.global_dict = global_data_dict(client.global_info)
    client.countries_sorted = sorted_countries(client.global_info)
    print("Update...")

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


    

@client.event
async def on_ready():
    update.start()
    print('------')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
   


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f'Invalid command.')


json_path = os.path.abspath('config.json')
with open(json_path) as config_file:
    token = json.load(config_file)
    
client.run(token['token'])