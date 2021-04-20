import main
class on_message(main.commands.Cog):
	def __init__(self,mm):
		self.mm = mm
	@main.commands.Cog.listener()
	async def on_message(self,message):
		if message.content in self.mm.command_prefix or message.content in ['<@803008721004265492>','<@!803008721004265492>']:
			if message.content in ['<@803008721004265492>','<@!803008721004265492>']:
				message.content = 'mm!'
			await main.deletable(self.mm,message,main.complexEmbed(message,[f'{message.content}math',f'{message.content}profile [member]',f'''{message.content}buy <item> [amount]
{message.content}purchase <item> <amount>''',f'''{message.content}donate <member> <coins>
{message.content}give <member> <coins>''',f'{message.content}mine',f'''{message.content}reload
{message.content}refresh
{message.content}restart'''],['This will give you somewhere from 50 to 150 coins for solving a math problem in 10 seconds.','This will let you view either your own or someone else\'s profile.',f'This will let you buy an item from my shop. You need to have enough coins for this!','This will let you give someone a certain amount of coins. You must have enough coins to donate!','This will let you mine for ores.','This will let you refresh me. Please run this command if anything seems to be working improperly.']))
		await main.refresh.refresh(self.mm)
def setup(mm):
	mm.add_cog(on_message(mm))