import main
class purge(main.commands.Cog):
	def __init__(self,mm):
		self.mm = mm
	@main.commands.command(name='purge',aliases=['Purging','clear','delete'])
	@main.commands.check(main.check)
	async def purge(self,context,amount=0):
		messages = 0
		try:
			amount = int(amount)
		except ValueError:
			await main.deletable(self,context,main.Embed(context,'Purging Error',f'{context.author.mention}, I need a proper __integer__ to know how many messages to purge! Try again with no non-number characters.'))
			return
		if context.channel.permissions_for(context.author).manage_messages == True:
			try:
				for message in await context.channel.history(limit=amount+1).flatten():
					if message.pinned == False:
						try:
							await message.delete()
							messages += 1
						except Exception:
							pass
			except main.discord.errors.Forbidden:
				await main.deletable(self,context,main.Embed(context,'Purging Error',f'Sorry, {context.author.mention}, but I don\'t have the required permissions to do this!'))
				return
			await main.deleteMessage(self.mm,context,await context.send(embed=main.Embed(context,'Successful Purge',f'I successfully purged {messages} messages!')))
		elif context.channel.permissions_for(context.author).manage_messages == False:
			await main.deletable(self,context,main.Embed(context,'Purging Error',f'Sorry, {context.author.mention}, but you don\'t have the required permissions to do this!'))
def setup(mm):
	mm.add_cog(purge(mm))