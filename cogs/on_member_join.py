import main
class on_member_join(main.commands.Cog):
	def __init__(self,mm):
		self.mm = mm
	@main.commands.Cog.listener()
	async def on_member_join(self,member):
		if member.guild.id == 761796772011311144:
			months = ['January','February','March','April','May','June','July','August','September','October','November','December']
			now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-7)))
			embed = discord.Embed(title='**MegaMoney**',color=0xffbf00,description=f'''_ _
_ _
**New Member**
Welcome, {member.mention}, to **{member.guild.name}**! <@655263219459293210> hopes you will have a good time chatting with my other fans!
_ _
_ _
This embed was sent on {str(now.time())[0:len(str(now.time()))-7]} PST of {months[now.month-1]} {main.numberSuffix(now.day)}, {now.year}.''')
			await self.mm.get_channel(id=823615621799477313).send(embed=embed)
		main.storage.userRegister(member)
def setup(mm):
	return