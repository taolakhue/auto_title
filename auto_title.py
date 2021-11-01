from asyncio.windows_events import NULL
from logging import NullHandler
import discord
import asyncio
import pyautogui
import time
import re
import datetime

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
    async def on_message(self, message):
        #prevent the bot to reply to itself
        if message.author.id == self.user.id:
            return
        
        def check_input(m):
            m=re.split('[ .,_]',m.content)
            for i in m:
                if i.isdigit() == False:
                    return False
            return True 

        if message.content.startswith('$title'):
            await message.channel.send('What is the title you want? Dumb pineapple')
            try:
          
                title = await self.wait_for('message', timeout=40.0)
            except asyncio.TimeoutError:
                return await message.channel.send(f'Time out. Please request title again')
            if title.content == "duke" or title.content == "Duke" or title.content=="duke " or title.content=="Duke ":
                await message.channel.send('what is your coordinate? pls seperated by space.')
                try:
                    coordinate= await self.wait_for('message',timeout=40.0, check = check_input)
                except asyncio.TimeoutError:
                    return await message.channel.send(f'Time out.Please request title again')
                # coord bar
                pyautogui.click(x=1296, y=96)
                pyautogui.click(x=1689, y=284)
                time.sleep(1)
                for x in coordinate.content:
                    if x == " " or x=="," or x=="_" or x==".":
                        pyautogui.press('enter')
                        pyautogui.click(x=1909,y=260)
                        time.sleep(1)
                    else:
                        pyautogui.press(x,interval=1.3)

                pyautogui.press('enter')
                pyautogui.click(x=2087, y=288)
                time.sleep(2)
                #Title bar "Duke"
                pyautogui.click(x=1678,y=509,interval=0.85) #house position
                pos = pyautogui.locateOnScreen("crown.png",confidence=0.8)
                pyautogui.click(pos,duration =0.85) #title button
                pyautogui.click(x=1532,y=651,interval=0.85,clicks=2) #duke button
                pyautogui.click(x=1731,y=1014,interval=0.85) #confirm button

            if title.content == "scientist" or title.content =="Scientist" or title.content=="scientist " or title.content =="Scientist ":
                await message.channel.send('what is your coordinate? pls seperated by space.')
                try:
                    coordinate = await self.wait_for('message',timeout=20.0,check= check_input)  
                except asyncio.TimeoutError:
                    return await message.channel.send(f'Time out.Please request title again')
                
                #coord bar
                pyautogui.click(x=1296, y=96)
                pyautogui.click(x=1689, y=284)
                time.sleep(1)
                for x in coordinate.content:
                    if x == " " or x=="," or x=="." or x=="_":
                        pyautogui.press('enter')
                        pyautogui.click(x=1909,y=260)
                        time.sleep(1)
                    else:
                        pyautogui.press(x,interval=2)
                    
                pyautogui.press('enter')
                pyautogui.click(x=2087, y=288)
                time.sleep(2)
                #title bar "scientist"
                pyautogui.click(x=1678,y=509,interval=0.85) #house
                pos = pyautogui.locateOnScreen("crown.png",confidence=0.8)
                pyautogui.click(pos,duration =0.85) #title button
                pyautogui.click(x=2231,y=652,interval=0.85,clicks=2)#scientist
                pyautogui.click(x=1731,y=1014,interval=0.85) #confirm
              

                #coord bar
            if title.content == "architect" or title.content == "Architect" or title.content == "architect " or title.content =="Architect ":
                await message.channel.send('What is your coordinate?pls seperated by space.')
                try:
                    coordinate = await self.wait_for('message',timeout=20.0,check=check_input)  
                except asyncio.TimeoutError:
                    return await message.channel.send(f'Time out.Please request title again')
                
                #coord bar
                pyautogui.click(x=1296, y=96)
                pyautogui.click(x=1689, y=284)
                time.sleep(1)
                for x in coordinate.content:
                    if x == " " or x=="," or x=="." or x=="_":
                        pyautogui.press('enter')
                        pyautogui.click(x=1909,y=260)
                        time.sleep(1)
                    else:
                        pyautogui.press(x,interval=2)
                    
                pyautogui.press('enter')
                pyautogui.click(x=2087, y=288)
                time.sleep(2.0)
                #title bar
                pyautogui.click(x=1678,y=509, interval=0.85,clicks=2) #house
                pos = pyautogui.locateOnScreen("crown.png",confidence=0.8)
                pyautogui.click(pos,duration =0.85)
                #pyautogui.click(x=1041,y=396,interval=0.85) #title button
                pyautogui.click(x=1876,y=644,interval=0.85,clicks=2)
                pyautogui.click(x=1731,y=1014,interval=0.85)
                

client = MyClient()
client.run('ODQ5NDY5MTEyNTQ2ODg1Njgz.YLbnwg.U_J4Pcg4Zr-U-GE6uLXwju3jBFE')

