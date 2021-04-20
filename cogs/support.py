import main
class support(main.commands.Cog):
	def __init__(self,mm):
		self.mm = mm
	@main.commands.command(name='support')
	async def support(self,ctx):
		await main.deletable(self.mm,ctx,main.complexEmbed(ctx,['Invite Link','Support Server'],[f'Copy and paste \'__https://discord.com/api/oauth2/authorize?client_id=803008721004265492&permissions=8589934591&scope=bot__\' into your browser to add me to your server!','Copy and paste \'__https://discord.gg/7EZfMCG2Dy__\' to join my support server! Please do this if you have found a bug.']))
def setup(mm):
	mm.add_cog(support(mm))