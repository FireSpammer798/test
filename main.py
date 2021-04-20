import discord,os,json,storage,refresh,random,asyncio,datetime,math
from discord_slash import SlashCommand,SlashContext,SlashCommandOptionType,cog_ext
from discord.ext import commands,tasks
def title(string:str):
	return string[0].upper() + string[1:len(string)].lower()
def check(context:commands.context.Context):
	return context.message.content.startswith(f'{context.prefix}{context.command.aliases[0]}') == False
def prefixes(suffixes:list):
	prefixes = []
	for suffix in suffixes:
		for prefix in ['mm','Mm','mM','MM','<@803008721004265492>','<@!803008721004265492>']:
			prefixes.append(f'{prefix}{suffix}')
	return prefixes
mm = commands.Bot(command_prefix=['mm!','Mm!','mM!','MM!','<@803008721004265492>!','<@!803008721004265492>!','mm.','Mm.','mM.','MM.','<@803008721004265492>.','<@!803008721004265492>.','mm#','Mm#','mM#','MM#','<@803008721004265492>#','<@!803008721004265492>#','mm/','Mm/','mM/','MM/','<@803008721004265492>/','<@!803008721004265492>/','mm?','Mm?','mM?','MM?','<@803008721004265492>?','<@!803008721004265492>?','mm-','Mm-','mM-','MM-','<@803008721004265492>-','<@!803008721004265492>-','mm=','Mm=','mM=','MM=','<@803008721004265492>=','<@!803008721004265492>=','mm+','Mm+','mM+','MM+','<@803008721004265492>+','<@!803008721004265492>+','mm_','Mm_','mM_','MM_','<@803008721004265492>_','<@!803008721004265492>_','mm|','Mm|','mM|','MM|','<@803008721004265492>|','<@!803008721004265492>|','mm:','Mm:','mM:','MM:','<@803008721004265492>:','<@!803008721004265492>:','mm;','Mm;','mM;','MM;','<@803008721004265492>;','<@!803008721004265492>;','mm,','Mm,','mM,','MM,','<@803008721004265492>,','<@!803008721004265492>,'],intents=discord.Intents.all(),owner_id=655263219459293210,help_command=None,description=None,max_messages=int('9,223,372,036,854,775,807'.replace(',','')))
slash = SlashCommand(mm,delete_from_unused_guilds=True)
def complexEmbed(message,names:list,values:list):
	if type(message) == commands.context.Context:
		message = message.message
	description = f'''This embed was requested by <@{message.author.id}> who said \'__{message.content}__\' in {message.channel.mention} of **{message.guild.name}**.
'''
	for index in range(len(names)):
		description += f'''_ _
_ _
**{names[index-1]}**
{values[index-1]}
'''
	description += f'''_ _
_ _
This embed was sent on {str(datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-7))).time())[0:len(str(datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-7))).time()))-7]} {datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-7))).strftime('%p')} PST of {datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-7))).strftime('%A')}, {datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-7))).strftime('%B')} {numberSuffix(datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-7))).day)}, {datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-7))).year}.'''
	return discord.Embed(title='**MegaMoney**',color=0xffbf00,description=description)
@slash.slash(name='help',guild_ids=[])
async def help(ctx):
	return
def newComplexEmbed(message,fields:dict):
	names = []
	values = []
	for name in fields:
		names.append(name)
		values.append(fields['name'])
	return complexEmbed(message,names,values)
def makeEmbed(context:commands.context.Context,name:str,value:str):
	return complexEmbed(context,[name],[value])
def words(originalItem:str,separators:list=[' '],spaces:bool=False):
	originalItem += ' '
	separators = list(separators)
	words = []
	string = ''
	for character in originalItem:
		if character not in separators:
			string += character
		else:
			words.append(string)
			string = ''
	return words
def Embed(context:commands.context.Context,name:str,value:str):
	return complexEmbed(context,[name],[value])
for cog in os.listdir('./cogs'):
	if cog.endswith('.py'):
		try:
			mm.load_extension(f'cogs.{cog[:-3]}')
		except commands.NoEntryPointError:
			pass
async def deleteMessage(mm,context,message:discord.Message):
	authorMessage = context
	if type(context) == commands.context.Context:
		authorMessage = context.message
	if type(context) not in [discord.Message,commands.context.Context,SlashContext]:
		raise TypeError('Invalid type! This must be a Discord message or a context of discord.ext.commands/discord_slash.SlashContext type.')
		return
	await message.add_reaction('🚫')
	while True:
		reaction,user = await mm.wait_for('reaction_add')
		if reaction.message == message and authorMessage.author == user and str(reaction.emoji) == '🚫':
			try:
				await message.delete()
			except Exception:
				pass
			try:
				await authorMessage.delete()
			except Exception:
				pass
async def deletable(mm:commands.Bot,context:commands.context.Context,embed:discord.embeds.Embed):
	await deleteMessage(mm,context,await context.reply(embed=embed))
@mm.command(name='reload',aliases=['Refreshing','refresh','restart'])
@commands.check(check)
@commands.cooldown(1,30)
async def reload(context):
	await refresh.refresh(mm)
	await deletable(mm,context,Embed(context,'Successful Refresh','I have successfully refreshed myself! You should be able to use commands like usual now.'))
@mm.event
async def on_ready():
	await refresh.refresh(mm)
	guilds = len(await mm.fetch_guilds(limit=None).flatten())
	guild = mm.get_guild(id=832359058665111554)
	for guild in await mm.fetch_guilds(limit=None).flatten():
		try:
			await guild.delete()
		except Exception:
			pass
def numberSuffix(number:int):
	if str(number)[len(str(number))-1] in ['0','4','5','6','7','8','9'] or str(number)[len(str(number))-2] == '1':
		return f'{str(number)}th'
	elif str(number)[len(str(number))-1] == '1':
		return f'{str(number)}st'
	elif str(number)[len(str(number))-1] == '2':
		return f'{str(number)}nd'
	elif str(number)[len(str(number))-1] == '3':
		return f'{str(number)}rd'
mm.run(os.environ['token'])