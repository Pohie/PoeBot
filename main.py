import discord
import random
import os
intents = discord.Intents.default()
intents.members = True
bot = discord.Client(intents=intents)
os.system("echo 'Connected to terminal'")
beanlist = ["https://www.recipetineats.com/wp-content/uploads/2014/05/Homemade-Heinz-Baked-Beans_0-SQ.jpg?w=480&h=270&crop=1","https://cdn11.bigcommerce.com/s-ww1fqjacln/images/stencil/1200x1200/products/1260/24269/vpnq1ejzfeqctexqrtvx__54438.1698780064.jpg?c=1","https://ih1.redbubble.net/image.155141026.5532/st,small,507x507-pad,600x600,f8f8f8.jpg","https://img.wattpad.com/f85a1d43e1808f86023bd59ee25cddd734897afe/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f4f6d456976306a684277667858773d3d2d3730333035373634352e3135383866336531383362343037656437393837393030333736372e6a7067","https://i.pinimg.com/736x/88/56/bb/8856bbb98a91dc25c086aae7ce2a4d5c.jpg","https://i.pinimg.com/originals/4c/8e/d4/4c8ed494bb49d6dbe2821da8239faeef.jpg"]
rand = ["My fish ate my homework", "Want some free candy? :))))", "Can I have your toes?", "**MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM**", "B E A N S .", "Never gonna give you up", "Toe butter", "https://i.ytimg.com/vi/ozDidzHdAIU/maxresdefault.jpg", "I drink mayo", "my mom is a can of beans", "UwU", "I will appear in your bedroom and steal your toes at exactly 3:21am", "duolingo is currently holding my family hostage", "I am currently in your closet", "beans?", "https://youtu.be/6kD0aggjDQM?si=ku-_iPNfcwQCQG8l", "heheh... i'm in danger", "I'm wanted in 27 states", "A is for arson!", "I eat children", "C O N S U M E .", "This bot is sponsored by **RAID SHADOW LEGEN-**", "My cat just barked at the dog", "Imma go eat some water rq", "Imma go drink some pizza rq", "I am not ok!", "Puppies are delicious", "The homework ate my dog.", "ඞ", "Wanna contribute to PoeBot? Join the development server! https://discord.gg/k6Gmv8uXV2", "pogbet iz hving a stornk", "I have your parents buried at -36.73883152343947, -72.3087952151461", "Toes are delicious", "rehehehehehehehhe", "You didn't pass the vibe check. 🔫", "👁👄👁", "😞 ↙️ 🦂 🌘 🍒 ⏫ ⏱ ⛵️ 📱 🍷 😿 ⌚️ 🆖 👮 🌸 🕝 👩 ↩️ 🚌 ✏️ 🏅 🍋 🕢 🛫 🎨 🏦 💋 🌀 🔹 ↪️ 🔰 🏅 ✏️ 🚓 🎱 🛅 🖨 💱 🆔 🌥 🌪 🤘 💟 ♻️ 👄 🕢 🌯 🐟 🉐 ♏️", "👢🍴😋", "Look, mum! I can speak microwave! **MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM**", "WOOOOOOO YEAH BABYYYY", "you better watch out! you better watch out! YOU BETTER WATCH OU! YOU BETTER WATCH OUT! **YOU BETTER WATCH OUT! YOU BETTER WATCH OUT!**", "The watch ate the watch that was watching a watch watch the watch that was eating the watching watchy watch.", "", "https://hypixel.net/attachments/1655134661329-png.3011058/", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQR_PIt77zsyZ2VP2OCfLj9OA4WDQJhDiPmUw&usqp=CAU", "Looks like you need a snickers", "I eat babies", "My burger ate the baby", "balls?", "https://discord.gg/v5jBMeDYMf", "E", "I am one with the darkness", "**C h i c k e n  F i n g e r s .**", "A muffin a minute keeps the docter nearby!", "https://youtu.be/9d8ry1pU-9E?si=hpBf6N0wzM6iynWt", "https://i.redd.it/4a5wlwhdvr031.jpg", "https://i.imgflip.com/4nimac.jpg", "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/hostedimages/1608866262i/30584492.jpg", "Ya like jazz?", "Screw gravity! **Ascends**", "timmy had 2 apples. he ate 2,174 of them. how many apples does timmy have left?", "Yo did you hear that water is wet?", "2 + 2 = 22 https://pbs.twimg.com/media/E0ZsArDWUAUyDyB.png", "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/69666e82-baef-459d-9eca-83e30caa4129/dfvi6mj-d0d3ba8a-545d-4324-b368-6b3ad307ae1d.jpg/v1/fill/w_750,h_920,q_75,strp/buff_kirby_by_bandanawaddledee2138_dfvi6mj-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9OTIwIiwicGF0aCI6IlwvZlwvNjk2NjZlODItYmFlZi00NTlkLTllY2EtODNlMzBjYWE0MTI5XC9kZnZpNm1qLWQwZDNiYThhLTU0NWQtNDMyNC1iMzY4LTZiM2FkMzA3YWUxZC5qcGciLCJ3aWR0aCI6Ijw9NzUwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.YgQDqeuh1ET8U9-BKb81uIH25O0kpT9YMhLWAvjrt0M","https://static.wikia.nocookie.net/belectonic-arts-official/images/7/7a/Costume2.png/revision/latest?cb=20200703233042","https://imgb.ifunny.co/images/9e2d372102be1214076d587dd4b2ce8d15c6e0b6e83a0e977a356a6bfa118251_1.jpg","I'm being updated several times per day, so don't worry about seeing all of my messages, there's more to come! :]","I watch you while you're sleeping :)))))","The road just crossed the chicken","lorax","I inhaled kirby.", "https://preview.redd.it/post-random-cursed-images-of-your-pet-or-of-someone-elses-v0-3w00gq6vaekb1.jpg?width=640&crop=smart&auto=webp&s=e2bc0c14acd0692272e3261f38f3f2e022481be1","https://img-9gag-fun.9cache.com/photo/a5n5LKN_460s.jpg","Free lemonade in the bathroom!", "Back in my day, I had to fight 19 lions, 4 snakes, a wolf, and 109 spiders to get to school.","https://cdn11.bigcommerce.com/s-ww1fqjacln/images/stencil/1200x1200/products/1260/24269/vpnq1ejzfeqctexqrtvx__54438.1698780064.jpg?c=1","stonk"]
serv = ["https://discord.gg/GMe5DjRXQE","https://discord.gg/nhtuhuhAcz","https://discord.gg/bHbbYYWevt","https://discord.gg/3VQycSM8rb","https://discord.gg/TtS68NCZXs"]
jd = ["y","n","n","n","n","n"]
yn = ["y","n"]

@bot.event
async def on_ready():
        os.system('clear')
        print("")
        print("\x1b[1;36m POEBOT LOGS")
        print(" ______________")
        print("")
        print("__________________________________________________________________________________________________")
        print("")
        print("Server count:",len(bot.guilds))
        print("")
        print("Created by Pohie on Dec 14, 2023")
        print("__________________________________________________________________________________________________")
        print("")
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for pings"))

@bot.event
async def on_guild_join(guild):
        dev = bot.get_channel(1194050537071587428)
        await dev.send("Added to a new server!")
        await dev.send("Server name: "+str(guild.name))
        await dev.send("‎ ")
        if guild.system_channel:
                await guild.system_channel.send("Howdy ya'll")
                await guild.system_channel.send("https://cdn11.bigcommerce.com/s-ww1fqjacln/images/stencil/1200x1200/products/1260/24269/vpnq1ejzfeqctexqrtvx__54438.1698780064.jpg?c=1")

@bot.event
async def on_message(message):
        user = bot.get_user(1128398088848027798)
        if message.author.bot:
                return
        link = "https://discordapp.com/channels/"+str(message.guild.id)+"/"+str(message.channel.id)+"/"+str(message.id)
        if message.guild.id == 1185034513823322213:
                if not bot.user.mentioned_in(message):
                        await user.send("Someone chatted in the PoeBot dev server! "+str(link))
        if bot.get_user(1128398088848027798).mentioned_in(message):
                bot.get_user(1128398088848027798).send("You got pinged! "+str(link))
        if bot.user.mentioned_in(message):
                ran = random.choice(rand)
                serv2 = random.choice(serv)
                jd2 = random.choice(jd)
                yn2 = random.choice(yn)
                author = message.author
                server = message.guild
                channel = message.channel
                dev = bot.get_channel(1194050537071587428)
                chan = bot.get_channel(1194056025892986880)
                if message.guild.id == 1186817133976489994:
                        ran = serv2
                if message.channel == 1194056025892986880:
                        await chan.send("Server count:",len(bot.guilds))
                if ran == "lorax":
                        await message.channel.send("The trees can't be harmed if the lorax is armed.")
                        ran = "https://i.pinimg.com/originals/18/e0/b1/18e0b1cc573fb9b44f566daeee4268e7.png"
                if ran == "stonk":
                        await message.channel.send("I'm in "+str(len(bot.guilds))+"!")
                        ran = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.9fyAoFYO6p7sSJKBxCs3TwHaFg%26pid%3DApi&f=1&ipt=f755a078e8fc9da6ba5309869244fd9631aa7aac9f1aad2e4e0f36c3348ee729&ipo=images"
                await message.channel.send(ran)
                print("\x1b[1;36m ")
                print("__________________________________________________________________________________________________")
                print("")
                print("Bot pinged!")
                print("")
                print('Replied with "',ran,'"')
                print("")
                print("Server count:",len(bot.guilds))
                print("")
                print("User:",author)
                print("")
                print("Server:",server)
                print("")
                print("Channel:",channel)
                print("")
                print("Message link:",link)
                print("__________________________________________________________________________________________________")
                print("")
                reply = ('Replied with',str(ran))
                linkto = ('Link to message:',str(link))
                await dev.send("Bot Pinged")
                await dev.send('Replied with '+str(ran))
                await dev.send('Link to message: '+str(link))
                await dev.send("‎ ")
                if jd2 == "y":
                        if yn2 == "y":
                                await message.author.send("Enjoying PoeBot? Join the development server to help add more to PoeBot!")
                                await message.author.send("https://discord.gg/xqp9ZKNnZR")
                        if yn2 == "n":
                                await message.author.send("Add PoeBot to your server: https://discord.com/api/oauth2/authorize?client_id=1185006044338995331&permissions=274879272960&scope=bot")
                
bot.run("Token")
