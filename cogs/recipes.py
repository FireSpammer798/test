import main
class recipes(main.commands.Cog):
	def __init__(self,mm):
		self.mm = mm
	@main.commands.command(name='recipes',aliases=['Recipe'])
	async def recipes(self,ctx,*,item=None):
		if item == None or item not in list(main.storage.buyables):
			await main.deletable(self.mm,ctx,main.Embed(ctx,'Recipe Error','You need to provide a valid item to view the recipes for!'))
			return
		names = []
		values = []
		for craftable in list(main.storage.craftables):
			craftable = main.storage.craftables[craftable]
			if item in list(craftable['recipe']):
				names.append(f'{ctx.prefix}craft {craftable["name"].lower()}')
				values.append(f'This will let you craft {craftable["name"]} for {craftable["recipe"][item]}. Type \'__{ctx.prefix}recipe {craftable["name"].lower()}__\' to view the full recipe for this item.')
		if names != []:
			await main.deletable(self.mm,ctx,main.complexEmbed(ctx,names,values))
		else:
			await main.deletable(self.mm,ctx,main.Embed(ctx,'Recipe Error',f'So far, none of my craftables require any amount of {main.storage.buyables[item]["plural"]}. Please join my support server at __https://discord.gg/yzvKeCWfg4__ for more information.'))
def setup(mm):
	mm.add_cog(recipes(mm))