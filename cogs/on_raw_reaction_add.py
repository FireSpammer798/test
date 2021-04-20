import discord,main
class on_raw_reaction_add(main.commands.Cog):
	def __init__(self,mm):
		self.mm = mm
	@main.commands.Cog.listener()
	async def on_raw_reaction_add(self,payload):
		message = await self.mm.get_channel(id=payload.channel_id).fetch_message(id=payload.message_id)
def setup(mm):
	mm.add_cog(on_raw_reaction_add(mm))