from ast import arg
from email import message
import os
import hikari
import lightbulb
import random

cwd = os.getcwd()

os.listdir()
os.chdir("C:/Users/Guy/Documents/GitHub/Guy_Harary/Labs/autonomous-artistic-agent/Bot")

print("Current working directory: {0}".format(cwd))


token_file = open("secret.txt","r").read()

bot = lightbulb.BotApp(token = token_file, prefix="[]")


@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print('Bot Has Started!')

# @bot.listen()
# async def ping(event: hikari.GuildMessageCreateEvent) -> None:
#     if event.is_bot or not event.content:
#         return

#     if event.content.__contains__("clutch"):
#         await event.message.respond("https://tenor.com/view/hungrybox-gif-21713449")

# @bot.command
# @lightbulb.command('ping', 'Says pong!')
# @lightbulb.implements(lightbulb.SlashCommand) 
# async def ping(ctx):
#     await ctx.respond('Pong!')

@bot.command

@lightbulb.command('helping', 'Gives you a list of available commands and features!')
@lightbulb.implements(lightbulb.PrefixCommand) 
async def helping(ctx: lightbulb.Context) -> None:

    await ctx.respond('''```[]helping : Posts the help menu which informs the user of the commands available and their usage.
[]character : Fetches the SSBWiki page for a Melee character (e.g., Fox, Falco, Roy, Donkey_Kong) 
[]player : Fetches the SSBWiki page for a Melee player (e.g., Mango, Hungrybox, Bananas, Zain)
[]combo : Posts a random one of nine combos 
[]combogen : Generates a random combo for you to try!```''')



# #subcommand test
# @bot.command
# @lightbulb.command('group', 'This is a group')
# @lightbulb.implements(lightbulb.SlashCommandGroup) 
# async def my_group(ctx):
#     pass

# @my_group.child
# @lightbulb.command('subcommand', 'This is a subcommand')
# @lightbulb.implements(lightbulb.SlashSubCommand) 
# async def subcommand(ctx):
#     await ctx.respond('Subcommand!')


# #add command
# @bot.command
# @lightbulb.option('num2', 'The second number', type=int)
# @lightbulb.option('num1', 'The first number', type=int)

# @lightbulb.command('add', 'Add two numbers together')
# @lightbulb.implements(lightbulb.SlashCommand)
# async def add(ctx):
#     await ctx.respond(ctx.options.num1 + ctx.options.num2)

# character command
@bot.command
@lightbulb.option('name', 'Character\'s name', type= str)

@lightbulb.command('character', 'Fetches the SSBWiki page for a Melee character')
@lightbulb.implements(lightbulb.PrefixCommand)
async def character(ctx: lightbulb.context)-> None:
    await ctx.respond('https://www.ssbwiki.com/'+ctx.options.name.replace(' ', '_')+'_(SSBM)')

# player command
@bot.command
@lightbulb.option('name', 'Player\'s name', type= str)

@lightbulb.command('player', 'Fetches the SSBWiki page for a Melee player')
@lightbulb.implements(lightbulb.PrefixCommand)
async def player(ctx: lightbulb.context)-> None:
    await ctx.respond('https://www.ssbwiki.com/Smasher:'+ctx.options.name.replace(' ', '_'))

# combo command
@bot.command

@lightbulb.command('combo', 'Posts a random one of nine combos')
@lightbulb.implements(lightbulb.PrefixCommand)
async def combo(ctx: lightbulb.context)-> None:
    x = random.randint(1, 9)
    if x == 1:
        await ctx.respond('https://youtu.be/pD_imYhNoQ4')
    elif x == 2:
        await ctx.respond('https://youtu.be/pD_imYhNoQ4')
    elif x == 3:
        await ctx.respond('https://youtu.be/CfUvm7nEH6M')
    elif x == 4:
        await ctx.respond('https://youtu.be/gzr2cJq8DrU')
    elif x == 5:
        await ctx.respond('https://youtu.be/DeFNe-avyi0')
    elif x == 6:
        await ctx.respond('https://youtu.be/KnRHr7fZnKw')
    elif x == 7:
        await ctx.respond('https://youtu.be/KxQRf_GTl-c')
    elif x == 8:
        await ctx.respond('https://youtu.be/4GXb2Da1Rak')
    elif x == 9:
        await ctx.respond('https://youtu.be/j9UYHdL_fzQ')

# framedata command



# notable players



# random combo generator
@bot.command

@lightbulb.command('combogen', 'Generates a random combo for you to try!')
@lightbulb.implements(lightbulb.PrefixCommand)
async def add(ctx: lightbulb.context)-> None:
    moves = ['JAB', 'F TILT', 'UP TILT', 'DOWN TILT', 'DASH ATTACK', 'FORWARD SMASH', 
        'UP SMASH', 'DOWN SMASH', 'NEUTRAL AIR', 'FORWARD AIR', 'BACK AIR', 'UP AIR', 'DOWN AIR',
        'NEUTRAL B', 'SIDE B', 'UP B', 'DOWN B', 'SHIELDDROP']
    s=' '
    length = random.randint(3,10)
    for i in range(length):
        s+=moves[random.randint(0, len(moves)-1)]
        if i < length - 1:
            s+=(' to ')

    await ctx.respond(s)

bot.run() 