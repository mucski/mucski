import random

def shuffle_word(word):
    word = list(word)
    random.shuffle(word)
    return ''.join(word)
    
worklist = {
    "hot dog":"You are working outside with a cart. Un scramble the following word ``dot goh``", 
    "caut": "You're a pro Paladins player. What do you buy first at match start? ", 
    "covid19": "You can't work cause of Quarantine. Kill the virus ``c _ _ _ _ _ _``",
    "jack sparrow": "You're a famous Pirate. Who are you?", 
    "bulbbulb": "Type the following word in reverse ``blubblub``", 
    "dick": "You are working as a professional hunter. Shot the u out of a duck.",
    "redbot": "I'm a bot, but do you know my name? Hint .info",
    "android": "You found a little green man inside your phone. He says he forgot his name. Help him",
    "shuffle": f"This is a test. Unscramble the word {shuffle_word('shuffle')}",
    "mucski": f"Creator of this piece of shit game {shuffle_word('mucski')}",
    "thanos": "He snaps people out of existence, who is he?",
}

searchlist = {
    "cellar": "You went into the cellar looking for a fine wine, got scared by a rat and found ``{}`` coins instead.",
    "moon": "A giant leap to man kind, Armstrong left some ``{}`` coins here though.",
    "forest": "You went trekking into the forest, found ``{}`` coins laying around in an abandoned camp.",
    "fridge": "Nothing beats frozen coins, Right? Wrong.",
    "sewer": "You descended into the sewers hoping to find a dancing clown, found ``{}`` coins instead. ",
    "dog": "Why would you do that.. that's animal abuse.",
    "toilet": "Why would you search a toilet... That's disgusting and so are you. ", 
    "box": "You rummaged through a box of forgotten items, found ``{}`` coins. Lucky you. ", 
    "drawer": "After going through many panties, a dildo, and a hand gun, you found ``{}`` coins wrapped in socks", 
    "story book": "You were looking for Little Red Riding Hood, instead you found ``{}`` coins hidden in a tree bark. ", 
    "set": "You are the next star for Ironing Man. While equipping his armor you found ``{}`` coins in one of the hidden compartments. ",
    "hospital": "You searched the hospital and found ``{}`` coins. Don't eat them though, may be infected with covid19.",
    "school": "You went looking for coins in your school locker, got a wedgy out of it instead. Bullies.",
    "trash": "Found nothing. Must've picked the wrong trash.",
    'club': 'You barged into a club, found ``{}`` coins laying around on the dance floor',
    'bank': 'They though you gonna rob them. You got arrested',
    'beach': 'You went to the beach, found ``{}`` coins in a sand castle.',
}

bad_location = ['fridge','dog','toilet','trash','school', 'bank']

petlist = {
    "rock": {
        "description": "Your very own pet rock.",
        "price": 500,
        "emoji": ":moyai:",
    },
    "turtle": {
        "description": "Throwing it in a sewer is not advised.",
        "price": 1000,
        "emoji": ":turtle:",
    },
    "dog": {
        "description": "Loyal, friendly, and full of fleas",
        "price": 2000,
        "emoji": ":dog:",
    },
    "cat": {
        "description": "Lazy and fat, but cute nonetheless.",
        "price": 2000,
        "emoji": ":cat:",
    },
}

shoplist = {
    "bone": {
        "description": "Perfect for them doggos",
        "price": 200,
        "quantity": 1,
        "emoji": "soon",
        "type": "food",
    },
    "fish": {
        "description": "Perfect for a cat",
        "price": 200,
        "quantity": 1,
        "emoji": "soon",
        "type": "food",
    },
    "ball": {
        "description": "Have some fun with your pet",
        "price": 500,
        "quantity": 1,
        "emoji": "soon",
        "type": "toy",
    },
    "soap": {
        "description": "Classic way to keep your pet squeeky clea.",
        "price": 500,
        "quantity": 1,
        "emoji": "soon",
        "type": "cleaning",
    },
}

pet_resp = [
    'Your {} ran into the forest, found a cabin and touched a spaghett, and took {} coins that were in a cupboard.', 
    'Your {} dressed up as a pirate and venture outwards on the sea, found {} coins in a pirate chest on an abandoned island.',
    'Your {} was learning russian so he can say Suka Blyat, Putin awarded him with {} coins.',
    'Your {} sung the national anthem and got rewarded {} coins for it. Isnt that nice?',
    'Your {} learned to drive, then crashed his car. Got paid {} coins for insurance.',
    'Your {} met with Mucski and asked him, "whatsup with these weak ass jokes and lines". Mucski threw {} coins in its face and ran away crying.',
    'Your {} found the exit of this program. Total score: {} coins. Just joking, theres no escape',
]