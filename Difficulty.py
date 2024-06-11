#Importing the randomness here
import random

#Just defining the difficulties and the modifiers, and an additional thing for picking modifiers
DifficultyList = ["easy", "Normal", "NIGHTMARE", "  U L T R A   C H A O S"]
ModifierList = ["Strategic Enemies", "Regenerating Enemies", "Locked Slots", "Buffed Enemies", "Resurrecting Enemies", "Expensive Shops", "Double Challenge", "Evolved Enemies", "Unfair Bosses", "Eternal Punishment", "Limited Heals", "No Safety Net"]
RandModNum = random.randint(1,12)

#Picking and printing the difficulty
randDiff = random.choice(DifficultyList)

print("You will be playing on " + randDiff + ",")

#Picking a random amount of difficulty modifiers, then putting them in a list
num_mods = max(0, min(RandModNum, len(ModifierList)))
picked_mods = random.sample(ModifierList, num_mods)

#Finally printing the picked stuff out
if (RandModNum == 12):
    print("with ALL modifiers on!")
else:
   print("with the following " + str(RandModNum) + " challenge modifier(s) enabled: ")
for mod in picked_mods:
    print(mod) 

