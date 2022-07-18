import discord
from discord.ext import commands
from webscrapping.dict import global_data_dict


class Virus(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def covid(self, ctx, message):
        message = message.capitalize()
        countries = self.client.countries_sorted
        
        if message not in countries:
            await ctx.send('Make sure you enter in a valid country and it is spelt correctly.')

        info_list = ['Total Cases', 'New Cases', 'Total Deaths', 'Total Recovered', 'New Recovered', 'Active Cases', 'Serious Critical', 'Total Cases/ 1M population', 'Deaths/ 1M population', 'Total Tests', 'Tests / 1M population', 'Population' ]
        
        global_data = discord.Embed(title=message, color=0xe74c3c) 
        
        for x in info_list:
            current = self.client.global_dict[message][x]
            if current == '':
                current = 'N/A'
            global_data.add_field(name=f'{x}:', value=current, inline=False)
        global_data.set_footer(text='Source: [https://www.worldometers.info/coronavirus/]')

        await ctx.send(embed=global_data)
    
    @covid.error
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Make sure you enter a country.')

def setup(client):
    client.add_cog(Virus(client))
