import main
class math(main.commands.Cog):
	def __init__(self,mm):
		self.mm = mm
	@main.commands.command(name='math',aliases=['Math'])
	@main.commands.cooldown(1,15)
	@main.commands.check(main.check)
	async def math(self,ctx):
		main.storage.userRegister(ctx.author)
		with open('profiles.json','r') as file:
			profiles = main.json.load(file)
		def randomProblem():
			mathOperations = ['*','+','-','!']
			strOperations = ['times','plus','minus','factorial']
			titleOperations = ['Multiplication','Addition','Subtraction','Factorial']
			operationIndex = main.random.randint(0,len(mathOperations)-1)
			operation = mathOperations[operationIndex]
			if operation in '+-':
				number1 = main.random.randint(0,5000)
				number2 = main.random.randint(0,5000)
			elif operation == '*':
				number1 = main.random.randint(0,100)
				number2 = main.random.randint(0,100)
			elif operation == '!':
				number1 = main.random.randint(0,10)
				number2 = 1
			if operation == '*':
				answer = number1*number2
			elif operation == '+':
				answer = number1+number2
			elif operation == '-':
				answer = number1-number2
			elif operation == '!':
				answer = main.math.factorial(number1)*number2
			return number1,operation,number2,answer,strOperations[operationIndex],titleOperations[operationIndex]
		number1,operation,number2,answer,strOperation,title = randomProblem()
		if operation != '!':
			messages = [await ctx.reply(embed=main.Embed(ctx,title,f'What is {str(number1)} {strOperation} {str(number2)}? You have 15 seconds to answer.')),ctx.message]
		else:
			messages = [await ctx.reply(embed=main.Embed(ctx,title,f'What is {number1} factorial? You have 15 seconds to answer.'))]
		response = ''
		#await ctx.message.add_reaction('♂')
		#await ctx.message.add_reaction('♀')
		while True:
			try:
				msg = await self.mm.wait_for('message',timeout=15)
				if msg.author == ctx.author and msg.channel == ctx.channel:
					try:
						response = float(msg.content)
					except ValueError:
						response = ''
					if type(response) in [float,int] and float(response) == answer:
						messages.append(msg)
						coins = main.random.randint(5000,15000)
						coins /= 100
						messages.append(await msg.reply(embed=main.makeEmbed(ctx,'Correct Answer',f'Congratulations! You answered the question correctly! You received {coins} coins.')))
						with open('profiles.json','r') as file:
							profiles = main.json.load(file)
						profile = profiles[str(ctx.author.id)]
						profile['coins'] += coins
						with open('profiles.json','w') as file:
							main.json.dump(profiles,file,indent=2)
						break
					elif type(response) in [float,int] and response != answer:
						messages.append(msg)
						messages.append(await msg.reply(embed=main.makeEmbed(ctx,'Incorrect Answer',f'Sorry, {ctx.author.mention}, but that is not the answer. Better luck next time!')))
						break
			except main.asyncio.TimeoutError:
				messages.append(await ctx.reply(embed=main.makeEmbed(ctx,'Math Timeout',f'Sorry, {ctx.author.mention}, but you didn\'t answer the question in time. Try again later.')))
				break
		await messages[len(messages)-1].add_reaction('🚫')
		while True:
			reaction,user=await self.mm.wait_for('reaction_add')
			if reaction.message == messages[len(messages)-1] and str(reaction.emoji) == '🚫' and user == ctx.author:
				for message in messages:
					try:
						await message.delete()
					except Exception:
						pass
def setup(mm):
	mm.add_cog(math(mm))