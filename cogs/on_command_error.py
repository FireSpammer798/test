import discord,main
from discord.ext import commands
class on_command_error(commands.Cog):
	def __init__(self,mm):
		self.mm = mm
	@commands.Cog.listener()
	async def on_command_error(self,context,error):
		message = None
		if isinstance(error,commands.CommandNotFound):
			return
		if isinstance(error,commands.MissingRequiredArgument):
			message = await context.send(embed=main.Embed(context,f'{context.command.aliases[0]} Error','You are missing a required argument!'))
		elif isinstance(error,commands.CommandOnCooldown):
			await context.reply(embed=main.Embed(context,f'{context.command.aliases[0]} Error',f'{context.author.mention}, you did this too recently. Try again in {str(error)[34:len(str(error))-1]} seconds.'))
		elif isinstance(error,commands.CheckFailure):
			return
		else:
			raise error
			await main.deleteMessage(self,context,await context.reply(embed=main.ComplexEmbed(context,['Unknown Error','Error Value'],[f'An unknown error has occured and it has been reported to my owner. If it doesn\'t get resolved soon, please contact him via my support server at https://discord.gg/7EZfMCG2Dy. Thanks for using {self.mm.user.mention}!',f'```{error}```'])))
def setup(mm):
	mm.add_cog(on_command_error(mm))