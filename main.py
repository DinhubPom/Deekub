import discord
import discord.interactions 
from discord.ui import Button, View
from discord import app_commands
from datetime import datetime
import datetime,os
import pytz
import os

try:
	from PIL import Image, ImageDraw, ImageFont
except:
	os.system("pip install Pillow")

my_secret = os.environ['Token']
admin = "din8647"

intents = discord.Intents.all()
client = discord.Client(intents=intents)

MYGUILD = discord.Object(id=1231920657244229695)

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=MYGUILD)
        await self.tree.sync(guild=MYGUILD)

intents = discord.Intents.default()
client = MyClient(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await client.change_presence(activity=discord.Streaming(name='ระบบปลอมสลิปวอเล็ท', url='https://www.twitch.tv/toey.monifire'))

class slipwallet_discord(discord.ui.Modal, title="SLIPWALLET"):
	name_user = discord.ui.TextInput(label="USERNAME", placeholder="ชื่อผู้โอนจ่าย", required=True, max_length=50, style=discord.TextStyle.short)
	name_me = discord.ui.TextInput(label="NAME", placeholder="ชื่อผู้รับเงิน", required=True, max_length=50, style=discord.TextStyle.short)
	phone_me = discord.ui.TextInput(label="PHONE", placeholder="เบอร์โทรศัพท์ผู้รับ", required=True, max_length=10, style=discord.TextStyle.short)
	money = discord.ui.TextInput(label="MONEY", placeholder="จำนวนเงิน", required=True, max_length=4, style=discord.TextStyle.short)
	# tim = discord.ui.TextInput(label="TIME", placeholder="วัน/เดือน/ปี ชั่วโมง:นาที:วินาที", required=True, max_length=20, style=discord.TextStyle.short)
	async def on_submit(self, interaction: discord.Interaction):
		name_user_id = self.name_user.value 
		name_me_id = self.name_me.value
		phone_me_id = self.phone_me.value
		money_id = self.money.value
		
		
		thailand_timezone = pytz.timezone('Asia/Bangkok')
		
		
		current_time_thailand = datetime.datetime.now(thailand_timezone)
		
		time =  current_time_thailand.strftime("%H:%M:%S")
		
		day =  current_time_thailand.strftime("%d")
		month = current_time_thailand.strftime("%m")
		year = current_time_thailand.strftime("%Y")
		
		image = Image.open("truemoney.png")
		draw = ImageDraw.Draw(image)
		
		font_size_money = 87
		font_size_user = 48
		font_size_me = 48
		font_size_phone = 40
		font_size_time = 37
		
		font_path_money = "Lato-Heavy.ttf" 
		font_path_user2 = "Kanit-Light.ttf"
		font_path_user = "Kanit-ExtraLight.ttf"
		font_path_phone = "Prompt-Light.ttf"
		
		font_money = ImageFont.truetype(font_path_money, font_size_money)
		font_user = ImageFont.truetype(font_path_user, font_size_user)
		font_me = ImageFont.truetype(font_path_user, font_size_me)
		font_phone = ImageFont.truetype(font_path_phone, font_size_phone)
		font_time = ImageFont.truetype(font_path_user2, font_size_time)
		font_order = ImageFont.truetype(font_path_user2, font_size_time)
		
		
		
		phone = phone_me_id
		text_money = money_id+".00"
		text_name_user = name_user_id
		text_name_me = name_me_id
		text_name_phone = f"{phone[:3]}-xxx-{phone[6:]}"
		text_name_time = f"  {day}/{month}/{year} {time}"
		# text_name_time = f"{self.tim.value}"
		text_name_order = "50018935012188"
		
		text_position_money = (560, 270)  
		text_position_user = (302, 485)
		text_position_me = (302, 648)
		text_position_phone = (302, 720)
		text_position_time = (781, 885)
		text_position_order = (827, 953)
		
		
		text_color_money = (44, 44, 44) 
		text_color_user = (-20, -20, -20)
		text_color_me = (-20, -20, -20) 
		text_color_phone = (80, 80, 80)
		text_color_time = (60, 60, 60) 
		text_color_order = (60, 60, 60)  
		
		draw.text(text_position_money, text_money, font=font_money, fill=text_color_money)
		draw.text(text_position_user, text_name_user, font=font_user, fill=text_color_user)
		draw.text(text_position_me, text_name_me, font=font_me, fill=text_color_me)
		draw.text(text_position_phone, text_name_phone, font=font_phone, fill=text_color_phone)
		draw.text(text_position_time, text_name_time, font=font_time, fill=text_color_time)
		draw.text(text_position_order, text_name_order, font=font_order, fill=text_color_order)
		
		
		image.save("truemoney_with_text.png")
        
		file = discord.File('truemoney_with_text.png')
		embed = discord.Embed(title="✅ สร้างสลีปปลอมสำเร็จ",description=f"นี่เป็นสลีปปลอมจากข้อมูลที่คุณกรอก",color=0xFCE5CD)
		await interaction.response.send_message(embed=embed, file=file, ephemeral=True)

@client.tree.command(description="ปลอมสลิปทรูมันนี่วอเล็ท")
async def wallet(interaction: discord.Interaction):
	username = interaction.user.name
	if str(username) == admin:
		button = Button(label="สลิปวอเล็ท", style=discord.ButtonStyle.grey, emoji="📃")
		async def button_callback(interaction: discord.Interaction):
			await interaction.response.send_modal(slipwallet_discord())
		button.callback = button_callback
		view = View(timeout=None)
		view.add_item(button)
		
		embed = discord.Embed(title="\nSLIPWALLET", description=f"**บริการปลอมสลิปวอเล็ท !**", color=0x000000)
		embed.add_field(name="- 📄 __EXAMPLE ( ตัวอย่าง )__", value="กรอกข้อมูลปลอมเเปลงที่คุณต้องการที่จะกรอกลงในช่องกรอก ผู้ใช้จ่ายเงิน,ผู้รับเงิน,เบอร์ผู้รับเงิน,จำนวนเงิน\nเวลากรอกชื่อให้เว้นวรรคชื่อเเละนามสกุลของคุณด้วย ",inline=False)
		embed.set_image(url="https://images-ext-1.discordapp.net/external/4xDKAnuLeOoeFUhHfaFgDap5SgjCx_SlpQdtjMAPhqU/https/media.giphy.com/media/fecTAVKVVA2fSzg21J/giphy.gif")
		await interaction.response.send_message(embed=embed, view=view)
	else:
		await interaction.response("ไม่น่ารักเลยนะคะ!!",ephemeral=True)
		


client.run(my_secret)