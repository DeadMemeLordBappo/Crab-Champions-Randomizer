import random

wepList = ["Auto Rifle", "Dual Pistols", "Dual Shotguns", "Auto Shotgun", "Burst Pistol", "Sniper Rifle", "Cluster Launcher", "Blade Launcher", "Minigun", "Rocket Launcher", "Orb Launcher", "Crossbow", "Arcane Wand", "Marksman Rifle", "Laser Cannons", "Flamethrower", "Seagle"]
grenadeList = ["Ice Blast", "Laser Beam", "Black Hole", "Grappling Hook", "Grenade"]
meleeList = ["Claw", "Dagger", "Hammer"]
def generate_control_values():
    while True:
        wepAllowed = random.randint(0, 1)
        grenAllowed = random.randint(0, 1)
        meleeAllowed = random.randint(0, 1)
        keyAllowed = random.randint(0, 1)
        
        if wepAllowed == 1 or grenAllowed == 1 or meleeAllowed == 1 or keyAllowed == 1:
            break
    
    return wepAllowed, grenAllowed, meleeAllowed, keyAllowed

# Generate control values
wepAllowed, grenAllowed, meleeAllowed, keyAllowed = generate_control_values()


#The simple way of picking a random weapon if allowed
if (wepAllowed == 1):
    randItem = random.choice(wepList)
    print("For the main weapon, you will be using the: " + randItem)
else:
    print("You cannot use any main weapon.")
    
#Picking an ability if allowed
if (grenAllowed == 1):
    randGrenade = random.choice(grenadeList)
    print("For the ability, you will be using the: " + randGrenade)
else:
    print("You cannot use any abilities")

#picking a melee if allowed
if (meleeAllowed == 1):
    randMelee = random.choice(meleeList)
    print("For the melee weapon, you will be using the: " + randMelee)
else:
    print("You cannot use any melee weapons")

if (keyAllowed == 1):
    print("You can use the key totem!")
else:
    print("You cannot use the key totem.")
