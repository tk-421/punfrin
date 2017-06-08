import random

puns = {
    '1' : "Oscar Wilde once boasted to a crowd he could make a pun from any subject, so a man yelled back 'do the queen' and wilde responded 'ahh, but the Queen is not  subject!'",

    '2' : "On the subject on penii and watching porn - I am literally thinking a head.",

    '3' : "Whenever Tim Howard retires (hopefully not for a while) -- he'll probably be pretty comfy. He sure saves a lot.",

    '4' : "I am the cos(stoner) to everyone's sin(stoner)",

    '5' : "did you guys hear the nigerian team captain at the world cup offered to pay back all the fans who had extended stays booked in brazil? all he needed was their bank account and routing numbers to get the process started",

    '6' : "(While talking about weed) o shit my head has gone to pot",

    '7' : "we need to protect our young goats, our kids, if you will",

    '8' : "did you hear about the ghost hunter who couldn't find any ghosts? he was despirited",

    '9' : "startup idea biodegradable diapers with a tree seed inside new startup idea to increase company efficiency. no bathrooms, just diapers when used, you just dig a hole and plant the soiled soilness acts as soil and then a tree grows!",

    '10' : "I have a few jokes about unemployed people but it doesn't matter none of them work.",

    '11' : "I can't believe I got fired from the calendar factory. All I did was take a day off.",

    '12' : "Did you hear about the guy who got hit in the head with a can of soda? He was lucky it was a soft drink.",

    '13' : "A courtroom artist was arrested today for an unknown reason... details are sketchy.",

    '14' : "What do you call an academically successful slice of bread? An honor roll.",

    '15' : "Why did the scientist install a knocker on his door? He wanted to win the No-bell prize!",

    '16' : "When I get naked in the bathroom, the shower usually gets turned on.",

    '17' : "My first job was working in an orange juice factory, but I got canned: couldn't concentrate.",

    '18' : "Claustrophobic people are more productive thinking out of the box.",

    '19' : "What do prisoners use to call each other? Cell phones.",

    '20' : "What do you call Watson when Sherlock isn't around? Holmeless.",

    '21' : "Having sex in an elevator is wrong on so many levels.",

    '22' : "I used to be a banker, but then I lost interest.",

    '23' : "I saw an ad for burial plots, and thought to myself this is the last thing I need.",

    '24' : "My math teacher called me average. How mean!",

    '25' : "What do you call a cow with no legs? Ground beef.",

    '26' : "Atheism is a non-prophet organization.",

    '27' : "Why couldn't the bike stand up on it's own? It was two tired.",

    '28' : "I owe a lot to the sidewalks. They've been keeping me off the streets for years.",

    '29' : "Thank you, my arms, for always being there by my side.",

    '30' : "Where should a dog go when it's lost its tail? The retail store of course.",

    '31' : "37 consonants, 25 vowels, a question mark, and a comma went to court. They will be sentenced next Friday.",

    '32' : "If goods get damaged in transport, does it become `bads`?",

    '33' : "Having sex in an elevator is wrong on so many levels.",

    '34' : "If Apple made a car, would it have Windows?",

    '35' : "Ancient humans, venturing across the ice bridge to North America, got lost quite often. They found it very hard to keep their Bering Strait.",

    '36' : "What do you get after playing the lute for 10 hours straight? Minstrel cramps.",

    '37' : "I tried to come up with a pun about famous German philosophers, but I Kant.",

    '38' : "I saw a wino eating grapes. I told him, you gotta wait.",

    '39' : "Did you hear about the restaurant on the moon? Great food, no atmosphere.",

    '40' : "What do you call a fake noodle? An Impasta.",

    '41' : "How does a penguin build it's house? Igloos it together.",

    '42' : "What did the grape do when he got stepped on? He let out a little wine.",

    '43' : "The shovel was a ground-breaking invention.",

    '44' : "The rotation of earth really makes my day.",

    '45' : "I used to work in a shoe recycling shop. It was sole destroying.",

    '46' : "Show me a piano falling down a mineshaft and I'll show you A-flat minor.",

    '47' : "To write with a broken pencil is pointless.",

    '48' : "Those who get too big for their britches will be exposed in the end.",

    '49' : "When a clock is hungry it goes back four seconds.",

    '50' : "A chicken crossing the road is poultry in motion.",

    '51' : "What's the definition of a will? It's a dead giveaway.",

    '52' : "The man who fell into an upholstery machine is fully recovered.",

    '53' : "Bakers trade bread recipes on a knead to know basis.",

    '54' : "He wears glasses during math because it improves division.",

    '55' : " She was only a whisky maker but he loved her still.",

    '56' : "She had a boyfriend with a wooden leg, but broke it off.",

    '57' : "Those who jump off a Paris bridge are in Seine.",

    '58' : "It wasn't school John disliked it was just the principal of it.",

    '59' : "There was once a cross-eyed teacher who couldn't control his pupils.",

    '60' : "A boiled egg in the morning is hard to beat.",

    '61' : "The short fortune-teller who escaped from prison was a small medium at large",

    '62' : "Some Spanish government employees are Seville servants.",

    '63' : "When cannibals ate a missionary they got a taste of religion.",

    '64' : "Marathon runners with bad footwear suffer the agony of defeat.",

    '65' : "In democracy its your vote that counts. In feudalism its your count that votes.",

    '66' : "It was an emotional wedding. Even the cake was in tiers.",

    '67' : "Local Area Network in Australia: the LAN down under.",

    '68' : "An office with many people and few electrical outlets could be in for a power struggle.",

    '69' : "Ancient orators tended to Babylon.",

    '70' : "You feel stuck with your debt if you can't budge it.",

    '71' : "A backwards poet writes inverse.",

    '72' : "When the smog lifts in Los Angeles, U C L A.",

    '73' : "A plateau is a high form of flattery.",

    '74' : "Seven days without a pun makes one weak.",

    '75' : "A toothless termite walked into a tavern and said, 'Is the bar tender here?'",

    '77' : "Santa's helpers are subordinate clauses.",

    '78' : "Two banks with different rates have a conflict of interest.",

    '79' : "When a new hive is done bees have a house swarming party.",

    '80' : " Looting a drugstore is called Pillaging",

    '81' : "A music store had a small sign which read: Bach in a Minuet."

    }

def generate_random_pun():
    pun = random.choice(list(puns))
    rv = puns[pun]
    rv.encode('ascii')
    return rv
