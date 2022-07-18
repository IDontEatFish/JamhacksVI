import discord
from discord.ext import commands
from webscrapping.dict import sorted_countries


class Country(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.countries_embed = [' ']
        self.countries = self.client.countries_sorted
    
        max_counter = 18
        tab = 1
        i = 0
        current_embed = discord.Embed(title=f"Countries tab: {tab}", color=0x1ABC9C)
        for x in self.countries:
            
            if len(self.countries) < max_counter:
            
                current_embed = discord.Embed(title=f"Countries tab: {tab}", color=0x1ABC9C)
                counter = i 
                for j in self.countries[i:]:
                    counter += 1
                    current_embed.add_field(name=f'{counter + 1}:', value=j, inline=True)
                    
                self.countries_embed.append(current_embed)
                break

            else:
                current_embed.add_field(name=f'{i + 1}:', value=x, inline=True)
                i += 1
                


                if i == max_counter:
                    max_counter += 18
                    tab += 1
                    self.countries_embed.append(current_embed)
                    current_embed = discord.Embed(title=f"Countries tab: {tab}", color=0x1ABC9C)
                

    @commands.command()
    async def countries(self, ctx, message):
        print(message)
        try: 

            message = int(message)
            
                
            await ctx.send(embed=self.countries_embed[message])
        except:
            await ctx.send("If you want to see the avaible countries do ?countries [index]!")


    @countries.error
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Make sure you enter an index!')


    @commands.command()
    async def search(self, ctx, message):
        message = message.capitalize()
        if message in self.countries:
            
            counter = 1
            current = 1
            upcoming = 18 
            embed_index = 0
            country_index = self.countries.index(message)
            for _ in range(len(self.countries_embed) - 1):
                if country_index in range(current, upcoming):
                    embed_index = counter
                else:
                    current += 18
                    upcoming += 18 
                    counter += 1
            await ctx.send(embed=self.countries_embed[embed_index])
        else:
            await ctx.send("Make sure you entered the proper country and make sure the spelling is correct!")
                
    @search.error
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Make sure you enter a country!')   



def setup(client):
    client.add_cog(Country(client))
