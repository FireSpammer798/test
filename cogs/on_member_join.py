import main
class on_member_join(main.commands.Cog):
	def __init__(self,mm):
		self.mm = mm
	@main.commands.Cog.listener()
	async def on_member_join(self,member):
		if member.guild.id == 834113328459677747:
			embed = main.discord.Embed(title='**MegaMoney**',color=0xffbf00,description=f'''_ _
_ _
**New Member**
Welcome, {member.mention}, to **{member.guild.name}**! <@655263219459293210> hopes you will have a good time chatting with my other fans!
_ _
_ _
This embed was sent on {str(main.datetime.datetime.now(main.datetime.timezone(main.datetime.timedelta(hours=-7))).time())[0:len(str(main.datetime.datetime.now(main.datetime.timezone(main.datetime.timedelta(hours=-7))).time()))-7]} {main.datetime.datetime.now(main.datetime.timezone(main.datetime.timedelta(hours=-7))).strftime('%p')} PST of {main.datetime.datetime.now(main.datetime.timezone(main.datetime.timedelta(hours=-7))).strftime('%A')}, {main.datetime.datetime.now(main.datetime.timezone(main.datetime.timedelta(hours=-7))).strftime('%B')} {numberSuffix(main.datetime.datetime.now(main.datetime.timezone(main.datetime.timedelta(hours=-7))).day)}, {main.datetime.datetime.now(main.datetime.timezone(main.datetime.timedelta(hours=-7))).year}.''')
			await self.mm.get_channel(id=834113329147805711).send(embed=embed)
		await main.refresh.refresh(self.mm)
def setup(mm):
	return