import discord
from discord.ext import commands
import json
import os
from webscrapping.scrapper import tracker
from webscrapping.dict import global_data_dict

client = commands.Bot(command_prefix='?')


@client.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    client.global_info = tracker()
    client.global_dict = global_data_dict(client.global_info)




@client.command(name='covid')
async def covid(ctx, message):
    message = message.capitalize()
    
    countries = ["USA", "INDIA","BRAZIL","FRANCE","GERMANY","UK","RUSSIA","S. KOREA", "ITALY", "TURKEY", "SPAIN", "VIETNAM","ARGENTINA","JAPAN","NETHERLANDS","IRAN","AUSTRALIA","COLOMBIA", "INDONESIA","POLAND","MEXICO","UKRAINE","MALAYSIA","THAILAND","AUSTRIA","BELGIUM","ISRAEL","PORTUGAL","SOUTH AFRICA","CZECHIA","CANADA","PHILLPPINES","SWITZERLAND","CHILE","PERU","GREECE","DENMARK","ROMANIA","SWEDEN","N. KOREA","IRAQ","SERBIA","BANGLADESH","HUNGARY","SLOVAKIA","JORDAN","GEORGIA","IRELAND","PAKISTAN","NORWAY","KAZAKHSTAN","SINGAPORE","TAIWAN","HONG KONG","MOROCCO","BULGARIA","CROATIA","CUBA","LEBANON","NEW ZEALAND","FINLAND","LITHUANIA","TUNISIA","SLOVENIA","BELARUS","NEPAL","BOLIVIA","UNITED ARAB EMIRATES","UAE","URUGUAY","COSTA RICA","ECUADOR","GUATEMALA","LATVIA","PANAMA","AZERBAIJAN","SAUDI ARABIA","SRI LANKA","PARAGUAY","KUWAIT","MYANMAR","PALESTINE","DOMINICAN REPUBLIC","BAHRAIN","ESTONIA","VENEZUELA","MOLDLOVA","EGYPT","LIBYA","CYRPUS","ETHIOPIA","MONGOLIA","HONDURAS","ARMENIA","REUNION","OMAN","BOSNIA AND HERZOGOVINA","QATAR","KENYA","ZAMBIA","NORTH MACEDONIA","BOTSWANA","ALBANIA","ALGERIA","NIGERIA","ZIMBABWE","LUXEMBOURG","UZBEKISTAN","MONTENEGRO","MOZAMBIQUE","CHINA","LAOS","KYRGYZSTAN","ICELAND","AFGHANISTAN","MALDIVES","UGANDA","EL SALVADOR","GHANA","NAMIBIA","TRINIDAD AND TOBAGO","MARTINIQUE","BRUNEI","GUADELOUPE","CAMBODIA","JAMAICA","RWANDA","CAMEROON","ANGOLA","MALTA","DEMOCRATIC REPUBLIC OF THE CONGO","DRC","SENEGAL","MALAWI","FRENCH GUINEA","IVORY COAST","SURINAME","BARBADOS","CHANNEL ISLANDS","FRENCH POLYNESIA","ESWATINI","FIJI","MADAGASCAR","GUYANA","SUDAN","NEWCALEDONIA","BHUTAN","MAURITANIA","BELIZE","CABO VERDE","SYRIA","GABON","PAPUA NEWGUINEA","SEYCHELLES","CURACAO","ANDORRA","BURUNDI","MAUITIUS","MAYOTTE","TOGO","GUINEA","ARUBA","TANZANIA","FAEROE ISLANDS","FARO ISLANDS","BAHAMAS","LESOTHO","MALI","HAITI","ISLE OF MAN","BENIN","SOMALIA","SAINT LUCIA","CAYMAN ISLANDS","CONGO","TIMOR-LESTE","BURKINA FASO","NICARAGUA","GILBRALTAR","SOLOMON ISLANDS","SOUTH SUDAN","LIECHTENSTEIN","TAJIKISTAN","GRENADA","SAN MARINO","EQUATORIAL GUINEA","DJIBOUTI","CAR","CENTRAL AFRICAN REPUBLIC","BERMUDA","DOMINICA","SAMOA","MONACO","GAMBIA","GREENLAND","YEMEN","TONGA","SAINT MARTIN","SAINT MAARTEN","CARRIBEAN NETHERLANDS","ERITREA","NIGER","VANUATA","GUINEA-BISSAU","COMOROS","ANTIGUA AND BARDBUDA","SIERRA LEONE","LIBERIA","CHAD","ST. VINCENT GRENADINES","BRITISH VIRGIN ISLANDS","TURKS AND CAICOS","SAO TOME AND PRINCIPE","SAINT KITTS AND NEVIS","COOK ISLANDS","PALAU","ST. BARTH","ANGUILLA","KIRIBATI","SAINT PIERRE MIQUELON","FALKLAND ISLANDS","MONTSERRAT","DIAMOND PRINCESS","WALLIS AND FUTUNA","MACAO",'VATICAN CITY',"MARSHALL ISLANDS","WESTERN SAHARA","MS ZAANDAM","NIUE","NAURU","MICRONESIA","SAINT HELENA"]
    if message.upper() not in countries:
        await ctx.message.channel.send('Make sure you enter in a valid country and it is spelt correctly.')

    info_list = ['Total Cases', 'New Cases', 'Total Deaths', 'Total Recovered', 'New Recovered', 'Active Cases', 'Serious Critical', 'Total Cases/ 1M population', 'Deaths/ 1M population', 'Total Tests', 'Tests / 1M population', 'Population' ]
    
    global_data = discord.Embed(title=message, color=0xe74c3c) 
    for x in info_list:
        current = client.global_dict[message][x]
        if current == '':
            current = 'N/A'
        global_data.add_field(name=f'{x}:', value=current, inline=False)
    global_data.set_footer(text='Source: [https://www.worldometers.info/coronavirus/]')
    await ctx.message.channel.send(embed=global_data)

@client.command(name="top")
async def top(ctx):

    top = discord.Embed(title="Most Cases of Covid", color=0xe74c3c)
    i = 0
    for x in client.global_dict:       
        i += 1
        top.add_field(name=i, value=x, inline=False)
        if i == 5:
            break
    top.set_footer(text='View least cases of Covid use ?bottom')
    await ctx.message.channel.send(embed=top)        

@client.command(name='bottom')  
async def bottom(ctx):  
    en = []
    lst = []
    i = 0
    
    for j in client.global_dict:
        lst.append(j)
    
    lst.reverse()
    for o in lst:
        i += 1
        en.append(o)
        if i == 6:
            break
    
    en.remove(en[0])

    i = 0
    bottom = discord.Embed(title="Least Cases of Covid", color=0xe74c3c)

    for x in en:       
        i += 1
        bottom.add_field(name=i, value=x, inline=False)
        if i == 5:
            break
    bottom.set_footer(text='View most cases of Covid use ?top')
    await ctx.message.channel.send(embed=bottom)        


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f'Invalid command.')

@covid.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'Make sure you enter a country.')

json_path = os.path.abspath('config.json')
with open(json_path) as config_file:
    token = json.load(config_file)
    
client.run(token['token'])

