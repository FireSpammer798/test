import main
class profile(main.commands.Cog):
	def __init__(self,mm):
		self.mm = mm
	@main.commands.command(name='profile',aliases=['Profile'])
	@main.commands.check(main.check)
	async def profile(self,context,member:main.discord.Member=None):
		if member == None:
			member = context.author
		with open('profiles.json','r') as file:
			profiles = main.json.load(file)
		profile = profiles[str(context.author.id)]
		await main.deleteMessage(self.mm,context,message=await context.reply(embed=main.complexEmbed(context,['Coins','Prestiges'],[f'{member.mention} has {profile["coins"]} coins.',f'{member.mention} has {profile["prestiges"]} prestiges.'])))
def setup(mm):
	mm.add_cog(profile(mm))