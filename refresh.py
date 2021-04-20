import datetime,math,storage,discord
from discord.ext import commands
async def refresh(mm:commands.Bot):
	datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-7))).weekday
	print(f'@{mm.user.name} is listening to \'{mm.command_prefix[int(math.remainder(1,len(mm.command_prefix))-1)]}help\' in {len(await mm.fetch_guilds(limit=None).flatten())} guilds with a latency of {round(mm.latency,5)*1000} milliseconds!')
	for guild in await mm.fetch_guilds(limit=None).flatten():
		for channel in guild.text_channels:
			if channel.is_nsfw:
				try:
					months = ['January','February','March','April','May','June','July','August','September','October','November','December']
					if datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-7))).hour >= 12:
						timeType = 'PM'
					elif datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-7))).hour < 12:
						timeType = 'AM'
					embed = discord.Embed(title='**MegaMoney**',color=0xffbf00,description=f'''_ _
_ _
**NSFW Guild**
I left **{guild.name}** because it had NSFW channels. You may add me back once no channels are NSFW.
_ _
_ _
This embed was sent on {str(datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-7))).time())[0:len(str(datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-7))).time()))-7]} {timeType} PST of {months[datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-7))).month-1]} {numberSuffix(datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-7))).day)}, {datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-7))).year}.''')
				except discord.errors.Forbidden:
					pass
				await guild.leave()
	for user in mm.users:
		storage.userRegister(user)
	await mm.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name=f'\'{mm.command_prefix[int(math.remainder(1,len(mm.command_prefix))-1)]}help\' in {len(await mm.fetch_guilds(limit=None).flatten())} guilds with a latency of {round(mm.latency*1000,3)} milliseconds...'))