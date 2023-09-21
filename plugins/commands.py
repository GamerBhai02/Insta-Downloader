from pyrogram import filters, Client as Mbot
import bs4, requests
from bot import DUMP_GROUP

@Mbot.on_message(filters.incoming & filters.private,group=-1)
async def monitor(Mbot, message):
           if DUMP_GROUP:
              await message.forward(DUMP_GROUP)
          
@Mbot.on_message(filters.command("start") & filters.incoming)
async def start(Mbot, message):
          await message.reply(f"👋 Hello {message.from_user.mention()}\nCurrently, I Am The Easiest And Fastest Instagram Downloader Bot, Supporting Reels.")
          
@Mbot.on_message(filters.command("help") & filters.incoming)
async def help(Mbot, message):
          await message.reply("☺ You can easily submit your Instagram reel and post URLs with this user-friendly bot.\n\nExample: \nReel: `https://www.instagram.com/reel/CZqWDGODoov/?igshid=MzRlODBiNWFlZA==`")
