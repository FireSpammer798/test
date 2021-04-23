import random,json,discord,math,time
from discord.ext import commands,tasks
buyables = {
	'bone': {
		'buy': 1000,
		'single': 'Bone',
		'plural': 'Bones'
	},
	'mist': {
		'buy': 5000,
		'single': 'Mist',
		'plural': 'Mist'
	},
	'fang': {
		'buy': 10000,
		'single': 'Fang',
		'plural': 'Fang'
	},
	'flamer': {
		'buy': 25000,
		'single': 'Flamer',
		'plural': 'Flamers'
	}
}
swords = {
	'dragon sword': {
		'damage': 250,
		'recipe': {
		  'dragon blood': 15
		},
		'chances': {
		  'zombie': 45,
		  
		},
		'mobs': 35
	},
	'starter sword': {
		'damage': 5,
		'recipe': None,
		'chances': {
			'zombie': 100,
			'dragon': 0,
			'ghost': 0
		},
		'mobs': 30
	},
	'diamond sword': {
		'name': 'Diamond Sword',
		'damage': 20,
		'recipe': {
			'diamond': 30
		},
		'chances': {
			'zombie': 95,
			'ghost': 4,
			'dragon': 1
		},
		'mobs': 5
	},
	'ruby sword': {
		'name': 'Ruby Sword',
		'damage': 25,
		'recipe': {
			'ruby': 30
		},
		'chances': {
			'zombie': 92.5,
			'dragon': 2,
			'ghost': 5.5
		},
		'mobs': 6
	}
}
def userRegister(user:discord.User):
	with open('profiles.json','r') as file:
		profiles = json.load(file)
	if str(user.id) in list(profiles) or user.bot == True:
		return
	profiles[str(user.id)] = {'coins': 0, 'prestiges': 0, 'armor': {'helmet': {'name': 'Starter Helmet', 'health': 8, 'defense:': 0.987258545, 'sell': 0}, 'chestplate': {'name': 'Starter Chestplate', 'health': 8, 'defense:': 0.987258545, 'sell': 0}, 'leggings': {'name': 'Starter Leggings', 'health': 8, 'defense:': 0.987258545, 'sell': 0}, 'boots': {'name': 'Starter Boots', 'health': 8, 'defense:': 0.987258545, 'sell': 0}}, 'tools': {'weapon': {'name': 'Starter Sword', 'sell': 0, 'mobs': 1, 'chances': {'zombie': 100, 'ghost': 0, 'vampire': 0, 'blazer': 0}}, 'hoe': {'name': 'Starter Hoe', 'sell': 0, 'crops': 1, 'chances': {'wheat': 100, 'corn': 0, 'watermelon': 0, 'pumpkin': 0}}, 'pickaxe': {'name': 'Starter Pickaxe', 'ores': 1, 'chances': {'copper': 100, 'gold': 0, 'diamond': 0, 'titanium': 0}}, 'axe': {'name': 'Starter Axe', 'woods': 1, 'chances': {'acacia wood': 100, 'birch wood': 0, 'jungle wood': 0, 'oak wood': 0, 'spruce wood': 0}}}, 'inventory': {'bone': 0, 'mist': 0, 'fang': 0, 'flamer': 0, 'copper': 0, 'gold': 0, 'diamond': 0, 'titanium': 0, 'acacia wood': 100, 'birch wood': 0, 'oak wood': 0, 'spruce wood': 0}}
	with open('profiles.json','w') as file:
		json.dump(profiles,file,indent=2)
craftables = {
	'dragon helmet': {
		'destination': [
			'armor',
			'helmet'
		],
		'health': 500,
		'defense': 0.316227766,
		'name': 'Dragon Helmet',
		'recipe': {
			'dragon blood': 5
		}
	},
	'dragon chestplate': {
		'destination': [
			'armor',
			'chestplate'
		],
		'health': 800,
		'defense': 0.316227766,
		'name': 'Dragon Helmet',
		'recipe': {
			'dragon blood': 8
		}
	},
	'dragon leggings': {
		'destination': [
			'armor',
			'leggings'
		],
		'health': 700,
		'defense': 0.316227766,
		'name': 'Dragon Helmet',
		'recipe': {
			'dragon blood': 7
		}
	},
	'dragon boots': {
		'destination': [
			'armor',
			'boots'
		],
		'health': 400,
		'defense': 0.334370152,
		'name': 'Dragon Helmet',
		'recipe': {
			'dragon blood': 4
		}
	},
	'ghost helmet': {
		'destination': [
			'armor',
			'boots'
		],
		'health': 300,
		'defense': 0.334370152,
		'name': 'Ghost Helmet',
		'recipe': {
			'mist': 5
		}
	},
	'ghost chestplate': {
		'destination': [
			'armor',
			'chestplate'
		],
		'health': 480,
		'defense': 0.334370152,
		'name': 'Ghost Chestplate',
		'recipe': {
			'mist': 5
		}
	},
	'ghost leggings': {
		'destination': [
			'armor',
			'leggings'
		],
		'health': 600,
		'defense': 0.334370152,
		'name': 'Ghost Leggings',
		'recipe': {
			'mist': 5
		}
	},
	'ghost boots': {
		'destination': [
			'armor',
			'boots'
		],
		'health': 240,
		'defense': 0.334370152,
		'name': 'Ghost Boots',
		'recipe': {
			'mist': 5
		}
	}
}
pickaxes = {
	'diamond pickaxe': {
		'chances': {
			'diamond': None
		},
		'ores': 5,
		'name': 'Diamond Pickaxe'
	},
	'starter pickaxe': {
		'chances': {
			'diamond': None
		}
	}
}