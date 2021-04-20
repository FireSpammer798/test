import discord,storage,json,main,datetime
from discord.ext import commands
class on_guild_add(commands.Cog):
	def __init__(self,mm):
		self.mm = mm
	@commands.Cog.listener()
	async def on_guild_add(self,guild):
		now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-7)))
		for entry in await guild.audit_log_actions(limit=None,action=discord.AuditLogAction.bot_add):
			print(entry.reason)
		await self.mm.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name=f'mm!help in {str(len(await mm.fetch_guilds(limit=None).flatten()))} guilds...'))
		for member in guild.members:
			with open('profiles.json','r') as file:
				profiles = json.load(file)
			storage.userRegister(member)
		for channel in guild.text_channels:
			if channel.is_nsfw:
				try:
					now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-7)))
					months = ['January','February','March','April','May','June','July','August','September','October','November','December']
					if now.hour >= 12:
						timeType = 'PM'
					elif now.hour < 12:
						timeType = 'AM'
					embed = discord.Embed(title='**MegaMoney**',color=0xffbf00,description=f'''_ _
_ _
**NSFW Guild**
I left **{guild.name}** because it had NSFW channels.
_ _
_ _
This embed was sent on {str(now.time())[0:len(str(now.time()))-7]} {timeType} PST of {months[now.month-1]} {numberSuffix(now.day)}, {now.year}.''')
				except discord.errors.Forbidden:
					pass
				await guild.leave()
				return
def setup(mm):
	mm.add_cog(on_guild_add(mm))