import main
class on_command(main.commands.Cog):
	def __init__(self,mm):
		self.mm = mm
	@main.commands.Cog.listener()
	async def on_command(self,command):
		await main.refresh.refresh(self.mm)
def setup(mm):
	mm.add_cog(on_command(mm))