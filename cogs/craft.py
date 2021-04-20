import main
class craft(main.commands.Cog):
	def __init__(self,mm):
		self.mm = mm
	@main.commands.command(name='craft',aliases=['Crafting','build','make'])
	@main.commands.check(main.check)
	async def craft(self,ctx,*,item):
		main.storage.userRegister(ctx.author)
		if item.lower() not in main.storage.craftables:
			await main.deleteMessage(self,ctx,await ctx.reply(embed=main.Embed(ctx,'Crafting Error','This item can not be crafted! It might not even be a valid item.')))
			return
		
def setup(mm):
	mm.add_cog(craft(mm))