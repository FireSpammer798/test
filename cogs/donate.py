import main
class donate(main.commands.Cog):
	def __init__(self,mm):
		self.mm = mm
	@main.commands.command(name='donate',aliases=['Donation','pay','give'])
	async def donate(self,context,member:main.discord.Member,coins=0):
		main.storage.userRegister(context.author)
		main.storage.userRegister(member)
		message = None
		try:
			coins = float(coins)
		except ValueError:
			await main.deletable(self.mm,context,main.Embed(context,'Donation Error',f'You need to specify a proper amount of coins to donate to {member.mention}!'))
			return
		authorProfile = profiles[str(context.author.id)]
		if authorProfile['coins'] < coins:
			await main.deletable(self.mm,context,main.Embed(context,'Donation Error','You don\'t have enough coins to do this! Earn more coins first.'))
			return
		if message != None:
			await main.deleteMessage(self.mm,context,message=message)
			return
		memberProfile = profiles[str(member.id)]
		memberProfile['coins'] += coins
		authorProfile['coins'] -= coins
		with open('profiles.json','w') as file:
			main.json.dump(profiles,file,indent=2)
		word = 'coins'
		if coins == 1:
			word = 'coin'
		message = await context.reply(embed=main.makeEmbed(context,'Successful Donation',f'You successfully gave {member.mention} {coins} {word}!'))
		await main.deleteMessage(self,context,message=message)
def setup(mm):
	mm.add_cog(donate(mm))