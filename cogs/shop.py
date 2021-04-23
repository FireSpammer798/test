import main
class shop(main.commands.Cog):
	def __init__(self,mm):
		self.mm = mm
	@main.commands.command(name='shop')
	async def shop(self,ctx):
		names = []
		values = []
		for item in list(main.storage.buyables):
			buyable = main.storage.buyables[item]
			names.append(f'''{ctx.prefix}buy {item} [amount]
{ctx.prefix}purchase {item} [amount]''')
			values.append(f'This will let you buy an amount of {buyable["plural"]} for {"{:,}".format(buyable["buy"])} coins.')
		await main.deletable(self.mm,ctx,main.complexEmbed(ctx,names,values))
def setup(mm):
	mm.add_cog(shop(mm))