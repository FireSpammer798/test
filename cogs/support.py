import main
@main.commands.command(name='support')
async def support(ctx):
	await main.deletable(main.mm,ctx,main.complexEmbed(ctx,['Invite Link','Support Server'],[f'Copy and paste \'__https://discord.com/api/oauth2/authorize?client_id=803008721004265492&permissions=8589934591&redirect_uri=https%3A%2F%2Fdiscord.gg%2F7EZfMCG2Dy&scope=bot%20applications.commands__\' into your browser to add me to your server!','Copy and paste \'__https://discord.gg/7EZfMCG2Dy__\' to join my support server! Please do this if you have found a bug.']))
def setup(mm):
	mm.add_command(support)