import datetime,math,storage,discord,time
from discord.ext import commands,tasks
@tasks.loop()
async def refresh(mm:commands.Bot):
	while True:
		requests = 1
		print(f'@{mm.user.name} is listening to \'mm!help\' in {len(await mm.fetch_guilds(limit=None).flatten())} guilds with a latency of {round(mm.latency*1000,3)} milliseconds!')
		guilds = {'guilds': []}
		requests += 1
		for guild in await mm.fetch_guilds(limit=None).flatten():
			guilds['guilds'].append(guild.id)
			for channel in guild.text_channels:
				if channel.is_nsfw:
					try:
						embed = discord.Embed(title='**MegaMoney**',color=0xffbf00,description=f'''_ _
	_ _
	**NSFW Guild**
	I left **{guild.name}** because it had NSFW channels. You may add me back once no channels are NSFW.
	_ _
	_ _
	This embed was sent on {str(datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-7))).time())[0:len(str(datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-7))).time()))-7]} {datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-7))).strftime('%p')} PST of {datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-7))).strftime('%A')}, {datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-7))).strftime('%B')} {numberSuffix(datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-7))).day)}, {datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-7))).year}.''')
						await guild.owner.send(embed=embed)
					except discord.errors.Forbidden:
						pass
					await guild.leave()
			requests += 2
		for user in mm.users:
			storage.userRegister(user)
		latency = str(round(mm.latency*1000,3))
		requests += 1
		await mm.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name=f'\'{mm.command_prefix[int(math.remainder(1,len(mm.command_prefix))-1)]}help\' in {len(await mm.fetch_guilds(limit=None).flatten())} guilds with a latency of {round(mm.latency*1000,3)} milliseconds...'))
		requests //= 50
		time.sleep(requests+1)