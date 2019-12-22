               
import asyncio 
import sys
import discord
# import sys 
# import os

import asyncio

bot_channel_id = discord.Object(id='643316408511365121')
oot_channel_id_list = ["657955269086674955","655058181583667201","640877280960184332","640877254385336331","569420128794443776"]

sent_new_message = False
answer_scores = {
    "1": 0,
    "2": 0,
    "3": 0,
   
}
answer_scores_last = {
    "1": 0,
    "2": 0,
    "3": 0,

}
# def restart_program():
#     """Restarts the current program.
#     Note: this function does not return. Any cleanup action (like
#     saving data) must be done before calling this function."""
#     python = sys.executable
#     os.execl(python, python, * sys.argv)

nomarkscore = 213
markscore = 113
score = 7000

bot = discord.Client()
selfbot = discord.Client()


   

   

@bot.event
async def on_message(message):
    global sent_new_message
    global answer
    global wrong
    global answer_scores
    global answer_scores_last

    

    if message.server == None:
        return
    if message.content.lower() == "q":
    
       if "590819962671726594" in [role.id for role in message.author.roles]:
           sent_new_message =False
           answer_scores = {
                "1": 0,
                "2": 0,
                "3": 0,
           }
           wrong = " "
           answer = " " 
           


@bot.event
async def on_ready():
    print("LOCO")
    print("Connected to discord.")
    print("User: " + bot.user.name)
    print("ID: " + bot.user.id)
    await bot.send_message(bot_channel_id, "**connected to server.** ")

@selfbot.event
async def on_ready():
    print("Self Bot")
    print("======================")
    print("Connected to discord.")
    print("User: " + selfbot.user.name)
    print("ID: " + selfbot.user.id)


@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="loco Answers!!",type=1))
    await bot.send_message(bot_channel_id, "Connected with server.")

    
@selfbot.event
async def on_message(message):
    global answer_scores
    
    global answer
    global wrong


    

    if message.server == None:
        return

   
    if message.channel.id in oot_channel_id_list:
        content = message.content.lower().replace(' ', '').replace("'", "")
        if content in ["1", "1apg","1c","1cnf","cnf1","1f"]:
            answer_scores["1"] += nomarkscore
        elif content in ["2", "2apg","2c","2cnf","cnf2","2f"]:
            answer_scores["2"] += nomarkscore
        elif content in ["3", "3apg","3c","3cnf","cnf3","3f"]:
            answer_scores["3"] += nomarkscore
        
        

        elif content in ["1?","?1","w1","1w"]:
            answer_scores["1"] += markscore
        elif content in ["2?","?2","w2","2w"]:
            answer_scores["2"] += markscore
        elif content in ["3?","?3","w3","3w"]:
            answer_scores["3"] += markscore
	
	
        elif content in ["/1"]:
            answer_scores["1"] += score
        elif content in ["/2"]:
            answer_scores["2"] += score
        elif content in ["/3"]:
            answer_scores["3"] += score
	
        
        
        elif content in ["not1", "n1"]:
            answer_scores["1"] -= nomarkscore
        elif content in ["not2", "n2"]:
            answer_scores["2"] -= nomarkscore
        elif content in ["not3", "n3"]:
            answer_scores["3"] -= nomarkscore
        
        elif content.startswith("not1?") or content.startswith("n1?"):
            answer_scores["1"] -= markscore
        elif content.startswith("not2?") or content.startswith("n2?"):
            answer_scores["2"] -= markscore
        elif content.startswith("not3?") or content.startswith("n3?"):
            answer_scores["3"] -= markscore
        
            
       
       
        else:
            return

        allanswers = answer_scores.values()
        highest = max(allanswers)
        lowest = min(allanswers)
        answer = list(allanswers).index(highest)+1
        wrong = list(allanswers).index(lowest)+1
        

async def send_embed(client, embed):
    return await client.send_message(bot_channel_id, embed=embed)

async def edit_embed(client, old_embed, new_embed):
    return await client.edit_message(old_embed, embed=new_embed)

async def discord_send():
    global sent_new_message
    global answer
    
    global answer_scores_last

    await bot.wait_until_ready()
    await asyncio.sleep(0)

    answer_scores_last = {
        "1": 0,
        "2": 0,
        "3": 0,
        
    }

    answer_message = []
    
    while not bot.is_closed:
	    
        if answer_scores != answer_scores_last:
            
            if wrong and answer :
                one_cross = ""
                two_cross = ""
                three_cross = ""
                
                
                one_check = ""
                two_check = ""
                three_check = ""

                 
                if wrong == 1:
                    one_cross = " :x:"
                if wrong == 2:
                    two_cross = " :x:"
                if wrong == 3:
                    three_cross = " :x:"    
                    
                if answer == 1:
                    one_check = " :one:"
                if answer == 2:
                    two_check = " :two:"
                if answer == 3:
                    three_check = " :three:"
                
                if not sent_new_message:
                    
                    embed=discord.Embed( description="**Connecting To loco Server.**", color=0xfeae70)
                    embed.add_field(name="**__Answer 1__**", value=f"{answer_scores['1']}{one_cross}{one_check}", inline=False)
                    embed.add_field(name="**__Answer 2__**", value=f"{answer_scores['2']}{two_cross}{two_check}", inline=False)
                    embed.add_field(name="**__Answer 3__**", value=f"{answer_scores['3']}{three_cross}{three_check}", inline=False)
                    
                    embed.set_author(	name="Trivia Pride")
                    embed.set_footer(text=f"Team Trivia Pride Pro || Roshan45 & KarthikTJ", icon_url="")
                   
                    answer_message = await send_embed(bot, embed)
                    sent_new_message = True
                else:
                    
                    embed=discord.Embed( description="****Connecting To loco Server.****", color=0xfeae70)
                    embed.add_field(name="**__Answer 1__**", value=f"{answer_scores['1']}{one_cross}{one_check}", inline=False)
                    embed.add_field(name="**__Answer 2 __**", value=f"{answer_scores['2']}{two_cross}{two_check}", inline=False)
                    embed.add_field(name="**__Answer 3__**", value=f"{answer_scores['3']}{three_cross}{three_check}", inline=False)	

                    embed.set_author(	name="Trivia Pride")
                    embed.set_footer(text=f"Team Trivia Pride Pro || Roshan45 & KarthikTJ", icon_url="")
                    x = await edit_embed(bot, answer_message, embed)

                    
		    
                answer_scores_last = answer_scores.copy()
                await asyncio.sleep(1.1)
                continue

        answer_scores_last = answer_scores.copy()
        await asyncio.sleep(0.05)



loop = asyncio.get_event_loop()


loop.create_task(bot.start("NjUyNDgzMzI5MTE1MDI5NTA0.Xf8z_Q.QCahGuHGd3x6MpFiq7VOD5c49co")) 


loop.create_task(selfbot.start("NTQ5Nzc0MDA1MzE0NTE5MDQ0.XeTRxg.Z18gFvRAy95sDrqt_Xwea58V9JA", bot=False))



loop.create_task(discord_send())
loop.run_forever()
