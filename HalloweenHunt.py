class Area:
	def __init__(self, name, desc, items, enemies, npcs, exts, itemUsed, itemUsedBoo, talk, triggered, bullythere, itemInspect, lookShort, noTakeItems):
		self.name = name
		self.desc = desc
		self.items = items
		self.enemies = enemies
		self.npcs = npcs
		self.exts = exts
		self.itemUsed = itemUsed
		self.itemUsedBoo = itemUsedBoo
		self.talk = talk
		self.triggered = triggered
		self.bullythere = bullythere
		self.itemInspect = itemInspect
		self.lookShort = lookShort
		self.noTakeItems = noTakeItems
		
world = {}

world['BCH'] = Area("BCH", "\n\nTo win this game you must collect 5 candies, defeat 4 bullies, and help a lost teenager.\n\n“Honey, hurry up or I will be late!” your mom shouted from the floor below you. You take one last look in the mirror and grimace at the halloween costume that your mom made for you. She had described it as a scary ghost, but when you saw your reflection all you could see was the loose stitching done in leftover thread and the old, and slightly discoloured, bedsheet your grandmother had given you for your seventh birthday the month prior. You trot down the stairs and out the door to see your mom waiting impatiently in the car. You take one last look at your house bare of halloween decorations, all closed curtains, no lights on, and a sign on the porch saying that no one was home and to take a candy from the bowl next to it. With a sigh, you hop in the car and your mom begins to drive off. \n\nYou look at the neighbour's house where your father is spending the evening to watch the football game with his friends, and consider why you didn't just ask to go with him instead of trick-or-treating alone.\n\nAfter a short drive, your mom parks in a driveway of a house in a neighbourhood you don’t recognize. The house has two levels and you can see the shadows of some other people in the window. This house also has a sign stating to take a chocolate from the bowl that rests in the lap of a cheap plastic skeleton on the front steps. \n\n“Don’t cause too much trouble. Mom is going to be busy with her friends here so only come back once your entire bag is filled with candy, got it?” \n\nYour mom walked into the house before you could answer and left you alone on the sidewalk with nothing but street lights illuminating the way. There is a skeleton, a screw, and a candy bowl next to you. \n\nYou turn around and standing in front of you are four kids, that seem to be only a few years older than you. The one with the bike demands for your candy, with their three henchmen behind them. When you refuse, the ringleader states that you will regret this and they all split up. Looks like your night is not going to be as easy as you thought.\n\nYou can move by typing 'N', 'E', 'S', or 'W', look around by typing 'look', inspect objects, talk to people, give and take available items, check your inventory with 'I'.", ['screw', 'skeleton', 'candy', 'bowl'], [], [], {'s': 'N#1', 'w': 'N#4', 'e': 'N#3'}, [], False, None, None, False, {'screw': 'The screw must have come loose from the skeleton, it could definitely poke a hole through something.', 'skeleton': 'It is just a cheap skeleton from the local dollar store.', 'candy': 'The candy looks a little old, but it is free so you might as well take it.', 'bowl': 'The bowl is orange and has fake spiders inside of it.'}, "Your mom is doing her book club in the house in front of you.", ['skeleton', 'bowl'])

world['BCH2'] = Area("BCH2", "Your mom is doing her book club in the house in front of you.", ['screw', 'skeleton', 'candy', 'bowl'], [], [], {'s': 'N#1', 'e': 'N#3', 'w': 'N#4'}, [], False, None, None, False, {'screw': 'The screw must have come loose from the skeleton, it could definitely poke a hole through something.', 'skeleton': 'It is just a cheap skeleton from the local dollar store.', 'candy': 'The candy looks a little old, but it is free so you might as well take it.', 'bowl': 'The bowl is orange and has fake spiders inside of it.'}, "Your mom is doing her book club in the house in front of you.", ['skeleton', 'bowl'])

world['N#1'] = Area("N#1", "The house in front of you is brightly decorated with lights and jack-o-lanterns with various decorations on the lawn of witches and ghosts. The owner of the house left the candy in the bowl next to them. Items present are, a slip of paper, a wallet, and a candy.", ['wallet', 'paper', 'candy'], [], [], {'n': 'BCH2', 's': 'CC', 'e': 'Street'}, [], False, None, None, False, {'wallet': "The wallet's ID has a woman's photo that looks similar to one of the bullies.", 'paper': 'The slip of paper has an address on it', 'candy': 'This is the expensive candy that your parents refuse to buy.'}, "It looks like the owner of the house is falling asleep and has no clue about the things lying next to him. There is a slip of paper, a wallet, and a candy.", [])

world['N#4'] = Area("N#4", "This house’s owner is trying to wrangle his two toddler daughters that are stumbling around the yard. The bowl of candy is still quite full on the porch. There is also a purple flier, candy, and a small rectangular green paper that you realize is a twenty dollar bill near the garage.", ['flier', 'money', 'candy'], [], [], {'n': 'SP', 'w': 'N#5', 'e': 'BCH2'}, [], False, None, None, False, {'flier': "The flier says that if you redeem it at the local haunted house, the workers will scare anyone you want for $20.", 'money': 'You found a crisp twenty dollar bill. Finders keepers, losers weepers.', 'candy': 'What a coincidence, this is the same candy your mom left on your own porch.'}, "The father of those two rambunctious kids seems like his hands are tied. Better not bother him. The items that are on this property are a purple flier, candy, and a twenty dollar bill.", [])

world['N#3'] = Area("N#3", "The house is decorated in orange lights and fake cobwebs everywhere. You approach the front door and see a sign saying that the owner has gone out to get more candy. The bowl has only a few candies left.", ['candy'], [], [], {'n': 'Park', 'w': 'BCH2', 'e': 'B#1'}, [], False, None, None, False, {'candy': "This one is your dad's favourite, maybe you could give it to him tonight."}, "The bowl is nearly empty, better not take too many candies and leave some for the other kids. The sign appears as though it was hastily written and taped to the door.", [])

world['CC'] = Area("CC", "The community centre seems to be closed for the occasion of Halloween due to the lack of lights illuminating the usually bright building. There is a teenager that looks lost and is pacing from here to the house south of the centre. You can also see one of the bullies circling the surrounding places. You can also hear frightened screams and laughter from the west.", [], ['bullyno1'], ['teen'], {'n': 'N#1', 's': 'N#2', 'w': 'HH'}, ['paper'], False, "The teen looks embarrassed and admits that they are searching for a party. They had a slip of paper with the address, but dropped it earlier.", "The teen’s face lit up with excitement as you handed over the slip that you found.", True, {}, "The community centre is closed and a lost teen is walking back and forth from here to the house just south. The bully roaming doesn’t seem to see you, unless you have someway to fight them off, it is best to avoid them.", [])

world['Street'] = Area("Street", "The street is dimly lit with the few streetlights that are lined up along the sidewalk. You can see one of the bullies moving between here and the alley that is southwards. They don’t seem to see you, you are better off to avoid confrontation until you can find some way to get them to leave you alone. There is a flashlight on ground near one of the streetlights.", ['flashlight'], ['bullyno2'], [], {'s': 'Alley', 'w': 'N#1', 'e': 'Gas'}, [], False, None, None, True, {'flashlight': "You wonder who dropped their flashlight. It still works."}, "The street is fairly empty with the exception of one of the bullies from earlier pacing between here and what lies south of here. There is a flashlight on the ground that appears to be in perfect condition.", [])

world['N#5'] = Area("N#5", "This house that you visit is dressed up with lights all orange. The owner looks like they are dressed in a costume of a scarecrow and waiting to scare the next kid that comes to take candy from the bowl.", ['candy'], [], [], {'n': 'FF', 'e': 'N#4'}, [], False, None, None, False, {'candy': "The candy wrapper has a lot of fun colours and the name is in a language you don't recognize. This could be your only chance of having this."}, "The scarecrow next to the bowl of candy is ready to scare whoever comes to take one.", [])

world['SP'] = Area("SP", "The skate park is empty with only the graffiti on the ramps and a lone skateboard that looks like its been left here for a good while. There is a cool looking rock that was painted over and could probably fit in your pocket and be added to your collection at home. It seems that one of the bullies has reached the skate park and is waiting for you as she walks between here and the surrounding area, with her bike resting against one of the ramps.", ['skateboard', 'rock'], ['bullyno4'], [], {'s': 'N#4', 'w': 'FF'}, ['screw'], False, None, "You grabbed the screw from your basket and poked a small hole in the tires of the bike. That should stop her from bothering you.", True, {'skateboard': "The skateboard has some fine cracks in it and it a little beat up around the edges. You probably don't need to take this.", 'rock': "This is a pretty rock, small enough to carry while still being heavy enough to cause some damage if you weren't careful."}, 'The graffiti on the ramps is slowly fading, and the bully’s bike is resting against a ramp. There is a rock that could fit nicely in your collection as well.', ['skateboard'])

world['B#1'] = Area("B#1", "You are in front of yet another house. This time there is a woman walking back and forth between this house and the one to the west. She seems pretty frantic.", [], [], ['woman'], {'w': 'N#3', 'e': 'B#2'}, ['wallet'], False, "The woman appears a little frantic and asks if you have seen her wallet that here little sister had taken. It seems like the little sister is part of the bully group. She said that if you help her find it, she will be happy to help you with something in return.", "You handed the sister back her wallet that you found and told her that her sister has been tormenting you with her friends. She says that her returned favour will be bringing the sister back home. You eventually see her dragging her younger sister inside by the arm and scolding her harshly. That makes your night a bit easier.", False, {}, "The woman seems to be in her early twenties and has quite the worry creases on her forehead. There doesn’t appear to be anything that you can be helpful to you here.", [])

world['Park'] = Area("Park", "The park is packed with the people, including a teen marching back and forth between here and the school up north. The teen is dressed as a ghost and seems to be trying to get the attention of those who pass by.", [], [], ['teen'], {'n': 'School', 's': 'N#3', 'e': 'BBCourt'}, [], False, "The teen dressed as a ghost informs you about haunted house where all proceeds go to charity that he works at. The teen said that the best way to get someone to leave you alone is to give them a good scare. The teen also said that if you find one of the fliers that the teen hid around town, the workers will scare someone for you.", None, False, {}, "The teen does not seem to be getting many potential customers.", [])

world['N#2'] = Area("N#2", "The house you stand in front of seems to be empty for the night with a bowl of candy on the porch. You can hear loud music and laughter from the west. 	Items available are candy from the bowl. There is a teenager that looks lost and is pacing from here to the house south of the centre. You can also see one of the bullies circling the surrounding places.", ['candy'], [], ['teen'], {'n': 'CC', 'w': 'HP'}, ['paper'], False, "The teen looks embarrassed and admits that they are searching for a party. They had a slip of paper with the address, but dropped it earlier.", "The teen’s face lit up with excitement as you handed over the slip that you found.", False, {'candy': "This is the candy that your best friend at school loves and you are yet to try. If you eat this tonight, maybe you will find out what's so great about them."}, "The house has all their lights turned off and a bowl of candy for any trick-or-treaters. There is a lost teen is walking back and forth from here to the house just south. The bully roaming doesn’t seem to see you, unless you have someway to fight them off, it is best to avoid them.", [])

world['HH'] = Area("HH", "The haunted house is illuminated in the parking lot of the community centre in dark purple lights. The are various decorations lining against the walls with witches, vampires, ghouls, and zombies entering and leaving the haunted house for their shifts. There is a line of kids and teens waiting to be scared and a table where a worker is waiting for customers to pay or redeem on of the fliers left around town with the offer to scare someone for a discounted price.", [], [], ['worker'], {'s': 'HP', 'e': 'CC'}, ['flier', 'money'], False, "The worker at the table asks if you have a flier you wish to redeem to get the workers to scare someone for twenty dollars.", "With a bored expression, the worker accepts the flier and money and gathers his coworkers after you tell them who you wish to scare. They return after a few minutes stating that the young kid you wished to scare has ran off for good.", False, {}, "The haunted house is covered in decorations and various workers walking in and out. There is a line-up of customers and a worker acting as a receptionist at a table. Behind a table is a worker.", [])

world['Gas'] = Area("Gas", "The gas station seems relatively empty with a few cars. It looks like most people are out trick-or-treating or watching over their kids. There is an abandoned house south of here and a bus station east.", [], [], [], {'s': 'AH', 'w': 'Street', 'e': 'Bus'}, [], False, None, None, False, {}, "The gas station is dimly lit and some of the lights are flickering. There is nothing here but there is an abandoned house to the south and a bus station to the east.", [])

world['Alley'] = Area("Alley", "The alley has nearly no lighting, but with many places to hide and several metal trash cans lying about. One of the bullies is walking back and forth from here to the street up north. The bully looks a little spooked from being in such an eerie place. If you make some sort of noise or break something, maybe they will run away…", [], ['bullyno2'], [], {'n': 'Street', 'e': 'AH'}, ['rock'], False, None, "You grabbed the rock and threw it against the trash cans, causing a big crashing noise. The bully lets out a little shriek and runs off. At least they are gone now.", True, {}, "The alley has metal trash cans that will cause a loud noise if you throw something solid against them. A bully is wearily walking between here and the street up north.", [])

world['BBCourt'] = Area("BBCourt", "The court looks empty and has a basketball resting underneath one of the nets. One of the bullies is walking back and forth between here and the baseball diamond north of here. She seems a little concerned and looking for something, maybe she is looking for you or something she could have dropped.", ['basketball'], ['bullyno3'], [], {'n': 'BBDia', 'w': 'Park'}, [], False, None, None, True, {'basketball': "The grips on the ball are a starting to wear off. This ball has definitely been well loved. Hopefully someone comes back for it."}, "The basketball court is empty and one of the bullies is walking to the baseball diamond to the north and back. She seems to be looking for something she might have dropped earlier.", ['basketball'])

world['School'] = Area("School", "The school has some kids playing on the structures and there is a teen dressed as a ghost trying to get their attention. He is walking from the school to the park just south attempting to get customers for something.", [], [], ['teen'], {'n': 'RS', 's': 'Park', 'e': 'BBDia'}, [], False, None, None, False, {}, "The school seems a lot creepier when only the moon illuminates the playground. There is a teen trying to grab the attention of those around him.", [])

world['FF'] = Area("FF", "You can see the bored workers through the windows of the fast food place. There are only a handful of customers eating greasy food inside. There is nothing for you to do here, you aren’t even hungry.", [], [], [], {'s': 'N#5', 'e': 'SP'}, [], False, None, None, False, {}, "The smell of greasy food is intoxicating, but your mom would be mad if you got food before dinner.", [])

world['HP'] = Area("HP", "There are teens dancing and some are sleeping on the front lawn. The music is playing loudly from inside the house and there is a strange scent in the air. There is an empty beer bottle on the ground.", ['bottle'], [], [], {'n': 'HH', 'e': 'N#2'}, [], False, None, None, False, {'bottle': "The bottle is empty and the glass is green. Maybe it is safer for everybody to just throw it out."}, "The party seems to be in full swing and there is an empty glass bottle by your feet.", [])

world['AH'] = Area("AH", "This house has been vacant and it appears as though it’s been that way for years. You can see a community worker attempting to clean up the garbage that has been left behind by whoever has visited this property before.", [], [], ['worker'], {'n': 'Gas', 'w': 'Alley'}, [], False, "The worker tells you that this house has been empty for nearly a decade and that the structure of the house is no longer completely secure. It is better to not enter the house.", None, False, {}, "The house seems to be crumbling in certain places and a city worker is cleaning the garbage that has been left behind.", [])

world['BUS'] = Area("BUS", "The bus station is vacant and there is nothing surrounding it, except for where you came from.", [], [], [], {'w': 'Gas'}, [], False, None, None, False, {}, "There is no one waiting at the bus station.", [])

world['RS'] = Area("RS", "The school you arrive at is the rival school of your own. There is graffiti on the school building and the parking lot is empty. There is no one here, but you can smell cigarette smoke lingering in the air. There is a reason why your mom always makes you stay away from here.", [], [], [], {'s': 'School'}, [], False, None, None, False, {}, "There is nothing here, but a horrible scent.", [])

world['BBDia'] = Area("BBDia", "The baseball diamond in this neighbourhood has seen better days. You can see one of the bullies walking back and forth between here and the basketball court just south of here. She appears to be looking for something she might have dropped earlier.", [], ['bullyno3'], [], {'s': 'BBCourt', 'w': 'School'}, [], False, None, None, True, {}, "The bully is walking around here and the lines of the baseball diamond could definitely be repainted.", [])

world['B#2'] = Area("B#2", "The house in front of you has its lights off and there is not even a bowl of candy on the porch. There is a woman pacing frantically between here and the house to the west. She seems to be looking for something, or maybe someone.", [], [], ['woman'], {'w': 'B#1'}, ['wallet'], False, "The woman appears a little frantic and asks if you have seen her wallet that here little sister had taken. It seems like the little sister is part of the bully group. She said that if you help her find it, she will be happy to help you with something in return.", "You handed the sister back her wallet that you found and told her that her sister has been tormenting you with her friends. She says that her returned favour will be bringing the sister back home. You eventually see her dragging her younger sister inside by the arm and scolding her harshly. That makes your night a bit easier.", False, {}, "The woman seems to be in her early twenties and has quite the worry creases on her forehead. There doesn’t appear to be anything that you can be helpful to you here.", [])
bullyCount = 0
class Player:
	def __init__(self, inventory, room, used, teenHelped, bullyCount, candyCount):
		self.inventory = inventory
		self.room = world[room]
		self.used = used
		self.teenHelped = teenHelped
		self.bullyCount = bullyCount
		self.candyCount = candyCount
	
	def move(self, direction):
		if direction not in self.room.exts:
			print("There is nowhere to go that way.")
			return
		nextRoom = self.room.exts[direction]
		##print(nextRoom)
		self.room = world[nextRoom]
		print(self.room.desc)
		return
		
	def take(self, item): ##It doesnt convert the items back to the new room, fix that ##NVM I THINK I JUST HAD THE WRONG LIST OOPS MY BAD ##CHECK ALL OF THEM AGAIN ##Make a list of useless items if you have the chance.
		#self.room = world[room]
		if item not in self.room.items:
			print("I am unfamiliar with that.")
			##print(self.room.desc)
			##print(self.room.items)
			return
		elif item in self.inventory and item != 'candy':
			print("You have already grabbed that.")
			return
		if item in self.room.items and item in self.room.noTakeItems:
			print("You probably shouldn't take that.")
			return
		if item in self.room.items and item not in self.room.noTakeItems:
			if item == 'candy':
				self.candyCount += 1
				print(int(5-self.candyCount) , str(" candies left to collect."))
			else:
				pass
			self.inventory.append(item)
			print(item, "was added to your inventory.")
			##self.room.items = self.room.items.remove(item)
			##print(self.inventory)
			return
			
	def use(self, item): ##Make a useable items list to differentiate and know which item can be used where. ##Make a list of text that will occur when the item is used, and a boolean to store if the encounter has happened yet.
		##print(item)
		if item in self.used:
			print("You have already used that item.")
		if item not in self.room.itemUsed:
			print("That can't be used here.")
			return
		if item not in self.room.itemUsed and item not in self.inventory:
			print("I don't understand.")
			return
		if item in self.room.itemUsed and item not in self.inventory and item not in self.used:
			print("You don't have that item.")
			return
		if item in self.room.itemUsed and item in self.inventory:
			self.room.itemUsed.remove(item)
			if self.room.itemUsed == []:
				if item == 'paper':
					self.teenHelped = True
					print("That's your good deed for the day.")
				else:
					print("You have defeated a bully.")
					self.bullyCount += 1
					print(int(4-self.bullyCount) , str(" bullies left to take care of."))
				print(self.room.triggered)
				self.room.itemUsedBoo = True
				self.used.append(item)
				self.inventory.remove(item)
				return
			else:
				self.inventory.remove(item)
				print("You gave the item.")
				
				return
			
	def talk(self, person):
		#print(self.room.npcs)
		if person not in self.room.npcs:
			print("There is no such person here.")
			return
		if person in self.room.npcs and self.room.itemUsedBoo == True:
			print("You have already done everything you can for them.")
			return
		print(self.room.talk)
		return
		
	def inspect(self, item):
		if item not in self.room.itemInspect:
			print("There is nothing to inspect.")
			return
		print(self.room.itemInspect[item])
		return
	
player = Player([], 'BCH', [], False, 0, 0)
print(player.room.desc)
while True:
	if player.bullyCount == 4 and player.candyCount == 5 and player.teenHelped == True:
		print("You win!")
		break
	userInput = input('\n\n>>')
	userInput = userInput.lower()
	sepInput = userInput.strip().lower().split()
	if userInput in {'n', 'e', 's', 'w'}:
		player.move(sepInput[0])
	elif sepInput[0] == 'look':
		print(player.room.lookShort)
	elif sepInput[0] == "i":
		print(player.inventory)
	elif sepInput[0] == "help":
		print("To win this game you must collect 5 candies, defeat 4 bullies, and help a lost teenager.\n\nYou can move by typing 'N', 'E', 'S', or 'W', look around by typing 'look', inspect objects, talk to people, give and take available items, check your inventory with 'I'.")
	if sepInput[0] == "go" and sepInput[0] != sepInput[-1]:
		if sepInput[1] in {'n', 'north'}:
			player.move('n')
		elif sepInput[1] in {'s', 'south'}:
			player.move('s')
		elif sepInput[1] in {'w', 'west'}:
			player.move('w')
		elif sepInput[1] in {'e', 'east'}:
			player.move('e')
		else:
			print("I don't understand that command.")
	if (sepInput[0] == "use" or sepInput[0] == "give") and sepInput[0] != sepInput[-1]:
		if sepInput[1] in player.room.itemUsed:
			player.use(sepInput[1])
		elif sepInput[1] is None:
			print("I don't understand that command.")
		else:
			print("I don't understand that command.")
	elif (sepInput[0] == "take" or sepInput[0] == "grab" or sepInput[0] == "get") and sepInput[0] != sepInput[-1]:
		if sepInput[1] in player.room.items:
			player.take(sepInput[1])
		elif sepInput[1] is None:
			print("I don't understand that command.")
		else:
			print("I don't understand that command.")
			
	elif (sepInput[0] == "talk" or sepInput[0] == "ask") and sepInput[0] != sepInput[-1]:
		#print(sepInput[1])
		if sepInput[-1] == sepInput[0]:
			print("I don't understand that command.")
		if sepInput[1] in player.room.npcs:
			player.talk(sepInput[1])
		else:
			print("I don't understand that command.")
	elif sepInput[0] == "inspect":
		if sepInput[-1] == sepInput[0]:
			print("I don't understand that command.")
		if sepInput[1] in player.room.items:
			player.inspect(sepInput[1])
		else:
			print("I don't understand that command.")
		#player.talk(sepInput[1])
	else:
		pass