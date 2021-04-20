import main
class settings(main.commands.Cog):
	def __init__(self,mm):
		self.mm = mm
	@main.commands.command(name='settings',aliases=['Settings'])
	@main.commands.check(main.check)
	async def settings(self,ctx,setting=None,mode=None):
		if setting == None:
			await main.deletable(self.mm,ctx,main.Embed(ctx,'Settings Error','You need to provide a setting to change!'))
def setup(mm):
	mm.add_cog(settings(mm))