import main
class stats(main.commands.Cog):
	def __init__(self,mm):
		self.mm = mm
	@main.commands.command(name='stats',aliases=['Stats Viewer','mm','megamoney'])
	@main.commands.check(main.check)
	async def stats(self,context):
		await main.deletable(self.mm,context,main.complexEmbed(context,['Guilds','Users','Birthday'],[f'||Including **{context.guild.name}**, ||I am currently participating in {len(await self.mm.fetch_guilds(limit=None).flatten())} guilds.',f'||Including bots, ||I am currently used by {len(self.mm.users)-1} total Discord users.','I was created on 14:08:58 PM PST of Sunday, January 24th, 2021.']))
def setup(mm):
	mm.add_cog(stats(mm))