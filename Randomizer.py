#Just an import
import random

#Defining Weapon, Difficulty, and Modifier lists
wepList = ["Auto Rifle", "Dual Pistols", "Dual Shotguns", "Auto Shotgun", "Burst Pistol", "Sniper Rifle", "Cluster Launcher", "Blade Launcher", "Minigun", "Rocket Launcher", "Orb Launcher", "Crossbow"]
difList = ["Easy", "Normal", "Nightmare"]
modList = ["Random Islands", "Regen Enemies", "Locked Slots", "Buffed Enemies", "Manual Collection", "Double Challenge", "Resurrecting Enemies", "Evolved Enemies", "Unfair Bosses", "Eternal Punishment", "Volatile Explosions", "No Safety Net"]

#The simple way of picking a random difficulty
randDiff = random.choice(difList)

#Printing the results of the above code
print("You will be playing on: " + randDiff + " difficulty.")

#Generating a random number between 1 and 12
rand_num = random.randint(1,12)

#Making sure the given number isn't out of range - redundant but still keeping it bc idk
num_mods = max(0, min(rand_num, len(modList)))

#putting the picked mods into a list
picked_mods = random.sample(modList, num_mods)

#printing out each picked mod to the screen
print("You will be playing with the following " + str(rand_num) + " challenge modifier(s): ")
for mod in picked_mods:
    print(mod)




