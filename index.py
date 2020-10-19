import discord
from discord.ext import commands
from discord.utils import get
import datetime
import random
import time
import threading

bot = commands.Bot(command_prefix='s!')

dancelinks = "https://data.whicdn.com/images/133670307/original.gif", "https://media1.tenor.com/images/61cf901b1c520204c5c185d4a4244b78/tenor.gif?itemid=13410605", "https://media1.tenor.com/images/b862cc1f052223f8991bd03bdde32420/tenor.gif?itemid=8253143", "https://cdn.discordapp.com/attachments/737633809121411102/741098317123027045/image0-1.gif", "https://cdn.discordapp.com/attachments/753107627000725510/753276279050076200/image0.gif", "https://cdn.discordapp.com/attachments/753107627000725510/753276198557188177/image0.gif", "https://cdn.discordapp.com/attachments/753107627000725510/753276360381825147/image0.gif", "https://cdn.discordapp.com/attachments/753107627000725510/753276075190124574/image0.gif", "https://cdn.discordapp.com/attachments/753107627000725510/753276038888423740/image0.gif", "https://cdn.discordapp.com/attachments/753107627000725510/753276004620828812/image0.gif", "https://cdn.discordapp.com/attachments/753107627000725510/753274397535764641/image0.gif", "https://media1.tenor.com/images/56350dfdcd3a5fa4fd66e9e87f9574bb/tenor.gif?itemid=4718162", "https://cdn.discordapp.com/attachments/755143951794569266/755154904846303333/image1.gif", "https://cdn.discordapp.com/attachments/438768001395982336/458139280209084426/aas.gif", "https://media1.tenor.com/images/81c0b8d3c0617d2902319b7f67e6ce01/tenor.gif?itemid=7560551", "https://media1.tenor.com/images/b05879f6223aa370f2623e70e3c8b2d1/tenor.gif", "https://media.tenor.com/images/a9420b2ac2bc78f5e13ce96703a609a4/tenor.gif", "https://i.pinimg.com/originals/42/d5/aa/42d5aafc733879e5d3bed9303075a0c7.gif", "https://cdn.discordapp.com/attachments/753107627000725510/755545369663897670/konosuba_op.gif", "https://cdn.discordapp.com/attachments/753107627000725510/753262470864568422/image0.gif"

whatlinks = "https://media.discordapp.net/attachments/588569619019857957/737063303880245268/tenor.gif", "https://cdn.discordapp.com/attachments/753107627000725510/753264914226741388/image0.jpg", "https://cdn.discordapp.com/attachments/755143720890007643/755148484771840030/image0.gif", "https://cdn.discordapp.com/attachments/755143720890007643/755148485493260328/image1.gif", "https://media.tenor.com/images/8f48e33e51a52e0edc5fc4a3665cf459/tenor.gif", "https://media1.tenor.com/images/bab858e36ca9203b7575a0656a925874/tenor.gif?itemid=15052547", "https://media1.tenor.com/images/85bc5b32ce4bee0ec93fa40c6a73db52/tenor.gif?itemid=10137967", "https://media1.tenor.com/images/62ee8055964c3a26ff339df816232452/tenor.gif?itemid=14764293", "https://media.tenor.com/images/9e3cba81b337f247f6462d3c968f7185/tenor.gif", "https://media1.tenor.com/images/895fc6fe1dd915ded9cb85dd45a8ab0a/tenor.gif?itemid=14126080", "https://media1.tenor.com/images/2ba945abd8db5c6da04944e154f17640/tenor.gif?itemid=13458008"

huglinks = "https://cdn.discordapp.com/attachments/755143773645963376/755146378568532118/image0.gif", "https://cdn.discordapp.com/attachments/755143773645963376/755146378979704852/image1.gif", "https://cdn.discordapp.com/attachments/755143773645963376/755146379416043541/image2.gif", "https://media.discordapp.net/attachments/755143773645963376/755146434470215841/image0.gif", "https://cdn.discordapp.com/attachments/755143773645963376/755146434889646220/image1.gif", "https://cdn.discordapp.com/attachments/755143773645963376/755146435791683632/image2.gif", "https://cdn.discordapp.com/attachments/755143773645963376/755146690247524403/image0.gif", "https://media.tenor.com/images/a756a73934fb6252bb9acf174d019c73/tenor.gif", "https://media.tenor.com/images/1f35c2fb63c60f791658cb92278b5f31/tenor.gif", "https://cdn.discordapp.com/attachments/755143773645963376/755146278345638010/image0.gif"

slaplinks = "https://media1.tenor.com/images/53f7a45f41b45f46c9a6c4dc154e58c5/tenor.gif?itemid=16268549", "https://media1.tenor.com/images/9ea4fb41d066737c0e3f2d626c13f230/tenor.gif?itemid=7355956", "https://media1.tenor.com/images/89309d227081132425e5931fbbd7f59b/tenor.gif?itemid=4880762", "https://media1.tenor.com/images/b27c5b128b434cc66f8cf32483d6b359/tenor.gif?itemid=17759867", "https://cdn.discordapp.com/attachments/756330629423038504/756421335491805214/image0.gif", "https://cdn.discordapp.com/attachments/756330629423038504/756354289022009344/image0.gif", "https://i.imgur.com/fm49srQ.gif", "https://cdn.lowgif.com/full/f5f1951fe46a4a4f-.gif", "https://i.pinimg.com/originals/1c/8f/0f/1c8f0f43c75c11bf504b25340ddd912d.gif", "https://media1.tenor.com/images/53f7a45f41b45f46c9a6c4dc154e58c5/tenor.gif"

nomlinks = "https://cdn.discordapp.com/attachments/611010500695818256/755275308722028625/image0.gif", "https://media1.tenor.com/images/5aaf1a7f1b7fc56c5f8ee50425efeefd/tenor.gif?itemid=17362621", "https://media1.tenor.com/images/5c21ba92ce99620bc9bea7ca7b1eac73/tenor.gif?itemid=7684098"

mimirlinks = "https://media1.tenor.com/images/a7e8e8f9fd0a8784012d8f14b09da4a8/tenor.gif", "https://media1.tenor.com/images/7175fe4b5e789b94b41a793e2fd4db3d/tenor.gif", "https://media1.tenor.com/images/bc308ef7ed3753ae73f1ff047e14c554/tenor.gif", "https://media.tenor.com/images/3ca01c7206f084d042304b9c4d3c80c0/tenor.gif", "https://media.tenor.com/images/794854414166b6664c6217c6e3342b9d/tenor.gif", "https://media1.tenor.com/images/1cdece239ec7d0fb33d2976d623f5e77/tenor.gif", "https://media1.tenor.com/images/62299afcedd465b631f9baa9786bd83b/tenor.gif", "https://media.tenor.com/images/47ac1ed8c5d5e71e8737ad173f2f8696/tenor.gif"

smilelinks = "https://cdn.discordapp.com/attachments/765371198505877504/767498790097518652/marcksmile-d.gif", "https://media3.giphy.com/media/ree8xCap5nHi/200.gif", "https://31.media.tumblr.com/tumblr_m8wm9nCUGf1rrftqho1_500.gif", "https://media1.tenor.com/images/fa2f0d664c45cbba388619fa650fe013/tenor.gif", "https://media2.giphy.com/media/ellxlkgbPTiM0/giphy.gif", "https://i.gifer.com/3YTP.gif", "https://media1.tenor.com/images/e90d41b53b010dbecf1e25d795ba8987/tenor.gif", "https://thumbs.gfycat.com/MagnificentWillingLabradorretriever-small.gif", "https://thumbs.gfycat.com/InsistentUnnaturalEmu-size_restricted.gif", "https://media1.tenor.com/images/08a2590d9a95501396f0e761953c5e57/tenor.gif", 'https://i.gifer.com/AfZ2.gif'

ppt = "piedra", "papel", "tijeras"

bola = "La verdad lo dudo", "No vuelvas a preguntarme eso", "Me parece algo poco probable", "¿De verdad quieres saberlo?", "... cambiemos de tema", "jajajajaja... ha que no era un chiste", "supongo que en un futuro proximo", "claro, pero no te confies", "Deberia ser un hecho", "¿Perdona? no estaba atendiendo", "... si tu lo dices...", "¡definitivamente!", "la esperanza es lo unico que muere... no?", "Decirlo esta en contra de mi programacion", "Lastima, no estoy obligada a contestarte eso"

kisslinks = "https://media1.tenor.com/images/78095c007974aceb72b91aeb7ee54a71/tenor.gif", "https://media1.tenor.com/images/b088ccf8075a4113efcbc5bc31fa46c2/tenor.gif"

lkisslinks = "https://media1.tenor.com/images/503bb007a3c84b569153dcfaaf9df46a/tenor.gif", "https://i.pinimg.com/originals/d2/ce/64/d2ce648e0cc47de76ce93daff13b93ac.gif", "https://media1.tenor.com/images/3d56f6ef81e5c01241ff17c364b72529/tenor.gif"

temas = "hombre calabaza", "chica de dulce", "Espnjoso", "Leyendas", "Linternas de calabaza", "hombre sombra", "poción", "caras", "helado", "fases"
#Comandos Basicos


@bot.command(pass_context=True)
@commands.cooldown(1, 60*60*24, commands.BucketType.user)
async def daily(ctx):
    user = ctx.message.author 
    await ctx.send(f"pues... todavia no se como recordar cosas de ese estilo {user.name}, pero aqui tienes una galleta 🍪")

@bot.command()
async def inkweek(ctx):
    chosen_theme = random.choice(temas)
    embed = discord.Embed(title=f"El tema de esta semana es... ¡{chosen_theme}!", description="Tienen hasta el siguiente domingo para presentarlo en su respectivo canal. Recuerden evitar el NSFW", timestamp=datetime.datetime.utcnow(), color=discord.Color.purple())
    embed.set_image(url="https://cdn.discordapp.com/attachments/709956040770191382/767627752496037948/1589185344392.png")
    await ctx.send(embed=embed)
    await ctx.message.delete()

@bot.command()
async def piedra(ctx):
    resultado = random.choice(ppt)
    if resultado == "piedra":
        await ctx.send("Piedra! uhm, pues empate")
    elif resultado == "papel":
        await ctx.send("Papel!... Ja! gané :D ")
    elif resultado == "tijeras":
        await ctx.send("Tijeras!... ou ganaste :C")

@bot.command()
async def papel(ctx):
    resultado = random.choice(ppt)
    if resultado == "papel":
        await ctx.send("Papel! uhm, pues empate")
    elif resultado == "piedra":
        await ctx.send("Tijeras!... Ja! gané :D ")
    elif resultado == "tijeras":
        await ctx.send("Piedra!... ou ganaste :C")

@bot.command()
async def tijeras(ctx):
    resultado = random.choice(ppt)
    if resultado == "tijeras":
        await ctx.send("Tijeras! uhm, pues empate")
    elif resultado == "piedra":
        await ctx.send("Piedra! ... Ja! gané :D ")
    elif resultado == "papel":
        await ctx.send("Papel!... ou ganaste :C")

@bot.command()
async def bola8(ctx):
    bola8_dice = random.choice(bola)
    embed = discord.Embed(title="Suki dice que...", description= bola8_dice, color=discord.Color.purple())
    await ctx.send(embed=embed)

@bot.command()
async def donar(ctx):
    await ctx.send(f'¡Jefe alguien a caido! ¿Ahora que hago?')

@bot.command()
async def yo(ctx, *, message):
    await ctx.send(message)
    await ctx.message.delete()

#Reacciones
@bot.command()
async def kiss(ctx, user: discord.Member):
    if user.name == "Suki Nomura":
        await ctx.send("Uhm, creo que lo mejor seria decir, no gracias")
    else:
        chosen_image = random.choice(kisslinks)
        embed = discord.Embed(title=f"{ctx.author.name}Esta besando a {user.name} u///u", color=discord.Color.purple())
        embed.set_image(url=chosen_image)
        await ctx.send(embed=embed)

@bot.command()
async def kisu(ctx, user: discord.Member):
    chosen_image = random.choice(lkisslinks)
    embed = discord.Embed(title=f"{ctx.author.name} Le dio un besito a {user.name} uwu", color=discord.Color.purple())
    embed.set_image(url=chosen_image)
    await ctx.send(embed=embed)

@bot.command()
async def dance(ctx):
    chosen_image = random.choice(dancelinks)
    user = ctx.message.author
    embed = discord.Embed(title=f"{user.name} Esta siguiendo el ritmo", color=discord.Color.purple())
    embed.set_image(url=chosen_image)
    await ctx.send(embed=embed)

@bot.command()
async def smile(ctx):
    chosen_image = random.choice(smilelinks)
    user = ctx.message.author
    if chosen_image == "https://cdn.discordapp.com/attachments/765371198505877504/767498790097518652/marcksmile-d.gif":
        embed = discord.Embed(title=f"{user.name} esta sonriendo ^w^", description="Creado por @nintenella", color=discord.Color.purple())
        embed.set_image(url=chosen_image)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title=f"{user.name} esta sonriendo ^w^", color=discord.Color.purple())
        embed.set_image(url=chosen_image)
        await ctx.send(embed=embed)
@bot.command()
async def slap(ctx, user: discord.Member):
    chosen_image = random.choice(slaplinks)
    embed = discord.Embed(title=f"{ctx.author.name}! No golpees a {user.name}", color=discord.Color.purple())
    embed.set_image(url=chosen_image)
    await ctx.send(embed=embed)

@bot.command()
async def what(ctx):
    chosen_image = random.choice(whatlinks)
    
    embed = discord.Embed(title="what a_a", color=discord.Color.purple())
    embed.set_image(url=chosen_image)
    await ctx.send(embed=embed)

@bot.command()
async def hug(ctx, user: discord.Member):
    chosen_image = random.choice(huglinks)
    embed = discord.Embed(title=f"{ctx.author.name} le dio un abacho a {user.name}", color=discord.Color.purple())
    embed.set_image(url=chosen_image)
    await ctx.send(embed=embed)

@bot.command()
async def nom(ctx):
    chosen_image = random.choice(nomlinks)
    
    embed = discord.Embed(title="ñam ñam", color=discord.Color.purple())
    embed.set_image(url=chosen_image)
    await ctx.send(embed=embed)

@bot.command()
async def mimir(ctx):
    chosen_image = random.choice(mimirlinks)
    
    embed = discord.Embed(title=f"{ctx.author.name} se fue a mimir", color=discord.Color.purple())
    embed.set_image(url=chosen_image)
    await ctx.send(embed=embed)

@bot.command()
async def miku_dance(ctx):
    embed = discord.Embed(colour=discord.Colour.from_rgb(0, 229, 229), title="A Bailar")
    embed.set_image(url='https://data.whicdn.com/images/133670307/original.gif')
    await ctx.send(embed=embed)

@bot.command()
async def chika_dance(ctx):
    embed = discord.Embed(colour=discord.Colour.from_rgb(255, 200, 220), title="A Bailar")
    embed.set_image(url='https://media1.tenor.com/images/61cf901b1c520204c5c185d4a4244b78/tenor.gif?itemid=13410605')
    await ctx.send(embed=embed)

@bot.command()
async def miku_what(ctx):
    embed = discord.Embed(colour=discord.Colour.from_rgb(0, 229, 229), title="what a_a")
    embed.set_image(url='https://media.discordapp.net/attachments/588569619019857957/737063303880245268/tenor.gif')
    await ctx.send(embed=embed)

@bot.command()
async def suki_smile(ctx):
    user = ctx.message.author
    embed = discord.Embed(colour=discord.Colour.purple(), title=f"{user.name} esta sonriendo ^w^", description=f"Creado por @nintenella")
    embed.set_image(url="https://cdn.discordapp.com/attachments/765371198505877504/767498790097518652/marcksmile-d.gif")
    await ctx.send(embed=embed)


@bot.command()
async def ping(ctx):
    await ctx.send(f'¡PONG! digo... Mi ping es {bot.latency}')

#Colores

@bot.command()
async def color(ctx, *, message):
    user = ctx.message.author
    role = message
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Blanco"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Gris"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Negro"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Rojo"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Rojo 2"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Rojo 3"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Rojo 4"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Rojo 5"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Naranja"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Naranja 2"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Naranja 3"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Amarillo"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Amarillo 2"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Amarillo 3"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Verde"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Verde 2"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Verde 3"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Verde 4"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Verde 5"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Celeste"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Celeste 2"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Celeste 3"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Celeste 4"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Turquesa"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Turquesa 2"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Turquesa 3"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Cian"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Cian 2"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Cian 3"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Cian 4"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Azul"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Azul 2"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Azul 3"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Morado"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Morado 2"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Morado 3"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Purpura"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Purpura 2"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Violeta"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Violeta 2"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Violeta 3"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Rosa"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Rosa 2"))
    await user.remove_roles(discord.utils.get(user.guild.roles, name="Rosa 3"))
    if role == "Blanco":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Gris":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Negro":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Rojo":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Rojo 2":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Rojo 3":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Rojo 4":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Rojo 5":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Naranja":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Naranja 2":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Naranja 3":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Amarillo":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Amarillo 2":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Armaillo 3":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Verde":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Verde 2":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Verde 3":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Verde 4":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Verde 5":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Celeste":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Celeste 2":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Celeste 3":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Celeste 4":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Turquesa":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Turquesa 2":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Turquesa 3":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Cian":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Cian 2":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Cian 3":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Cian 4":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Azul":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Azul 2":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Azul 3":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Morado":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Morado 2":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Morado 3":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Purpura":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Purpura 2":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Violeta":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Violeta 2":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Violeta 3":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Rosa":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Rosa 2":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Rosa 3":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    await ctx.send(F"{user.name} ¡Bien! Se te cambio el color a {role}")
    await ctx.message.delete()

@bot.command()
async def hola(ctx):
    await ctx.send(hola)

#Tags

@bot.command()
async def tag(ctx, *, message):
    user = ctx.message.author
    role = message
    if role == "Youtuber":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Streamer":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "MudaFan":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Cinefilo":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Escritor":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Lector":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "VCero":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Wild sider":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Entrenador Pokemon":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Mario Sports":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Minecrafter":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Fontanero":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Robloxian":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Osu Fan":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Smasher":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Calamar":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Rocketo":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Fiestero":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Zeldero":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Vecino":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Us":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "DnD Espectador":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Challenger":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Inkweekers":
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    await ctx.send(F"{user.name} ¡Bien! Se te agrego el rol {role}")
    await ctx.message.delete()

@bot.command()
async def tagR(ctx, *, message):
    user = ctx.message.author
    role = message
    if role == "Youtuber":
        await user.remove_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Streamer":
        await user.remove_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "MudaFan":
        await user.remove_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Cinefilo":
        await user.remove_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Escritor":
        await user.remove_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Lector":
        await user.remove_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "VCero":
        await user.remove_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Wild sider":
        await user.remove_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Entrenador Pokemon":
        await user.remove_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Mario Sports":
        await user.remove_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Minecrafter":
        await user.remove_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Fontanero":
        await user.remove_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Robloxian":
        await user.remove_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Osu Fan":
        await user.remove_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Smasher":
        await user.remove_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Calamar":
        await user.remove_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Rocketo":
        await user.remove_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Fiestero":
        await user.remove_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Zeldero":
        await user.remove_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Vecino":
        await user.remove_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Us":
        await user.remove_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "DnD Espectador":
        await user.remove_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Challenger":
        await user.remove_roles(discord.utils.get(user.guild.roles, name=role))
    elif role == "Inkweekers":
        await user.remove_roles(discord.utils.get(user.guild.roles, name=role))
    await ctx.send(F"{user.name} Se te quito el tag {role}")
    await ctx.message.delete()
#Events
@bot.event
async def on_ready():
    print('Estoy lista')

@bot.event
async def on_member_join(member):
   await member.add_roles(discord.utils.get(member.guild.roles, name="Fluffy Sociedad"))


bot.run('NzUyNzUxODA4NjgxNzM4NDIy.X1cMwA.OjOeeILxiJpGeeRq_cGUY97s9CQ')
