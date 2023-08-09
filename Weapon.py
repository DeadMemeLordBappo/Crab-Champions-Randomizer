import random

wepList = ["Auto Rifle", "Dual Pistols", "Dual Shotguns", "Auto Shotgun", "Burst Pistol", "Sniper Rifle", "Cluster Launcher", "Blade Launcher", "Minigun", "Rocket Launcher", "Orb Launcher", "Crossbow", "Melee Only", "Grenades Only", "Melee and Grenades Only"]

#The simple way of picking a random weapon and difficulty
randItem = random.choice(wepList)
print("You will be using (the): " + randItem)
