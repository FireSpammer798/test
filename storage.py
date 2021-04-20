import random,json,discord,math
buyables = {
  'dragon blood': {
    'chance': 0.01,
    'buy': 30000,
    'sell': 27000,
    'single': 'drop of Dragon Blood',
    'plural': 'drops of Dragon Blood'
  },
  'mist': {
    'chance': 0.02,
    'buy': 1000,
    'sell': 900,
    'single': 'Mist',
    'plural': 'Mist'
  },
  'gold': {
    'chance': 30,
    'buy': 10,
    'sell': 9,
    'single': 'bar of Gold',
    'plural': 'bars of Gold'
  },
	'ruby': {
		'buy': 1000,
		'sell': 900,
		'single': 'Ruby',
		'plural': 'Rubies'
	},
}
swords = {
	'dragon sword': {
		'damage': 250,
		'recipe': {
		  'dragon blood': 15
		},
		'chances': {
		  'zombie': 45,
		  'dragon': 20,
		  'ghost': 25
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
	profiles[str(user.id)] = {}
	profile = profiles[str(user.id)]
	profile['coins'] = 0
	profile['prestiges'] = 0
	profile['armor'] = {}
	armor = profile['armor']
	armor['helmet'] = {}
	helmet = armor['helmet']
	armor['chestplate'] = {}
	armor['leggings'] = {}
	armor['boots'] = {}
	profile['tools'] = {}
	tools = profile['tools']
	tools['weapon'] = None
	tools['hoe'] = None
	tools['pickaxe'] = None
	tools['axe'] = None
	profile['inventory'] = {}
	inventory = profile['inventory']
	inventory['wood'] = 0
	inventory['wheat'] = 0
	inventory['pumpkins'] = 0
	inventory['rubies'] = 0
	inventory['diamonds'] = 0
	inventory['emeralds'] = 0
	inventory['gold'] = 0
	inventory['polished wood'] = 0
	inventory['dragon blood'] = 0
	inventory['bone'] = 0
	inventory['mist'] = 0
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