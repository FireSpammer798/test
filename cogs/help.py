import discord,main
from discord.ext import commands
class help(commands.Cog):
	def __init__(self,mm):
		self.mm = mm
	@commands.command(name='help',aliases=['Help'])
	async def help(self,context):
		await main.deletable(self.mm,context,main.complexEmbed(context,[f'{context.prefix}math',f'{context.prefix}profile [member]',f'''{context.prefix}buy <item> [amount]
{context.prefix}purchase <item> <amount>''',f'''{context.prefix}donate <member> <coins>
{context.prefix}give <member> <coins>''',f'{context.prefix}mine',f'''{context.prefix}reload
{context.prefix}refresh
{context.prefix}restart'''],['This will give you somewhere from 50 to 150 coins for solving a math problem in 10 seconds.','This will let you view either your own or someone else\'s profile.',f'This will let you buy an item from my shop. You need to have enough coins for this!','This will let you give someone a certain amount of coins. You must have enough coins to donate!','This will let you mine for ores.','This will let you refresh me. Please run this command if anything seems to be working improperly.']))
def setup(mm):
	mm.add_cog(help(mm))