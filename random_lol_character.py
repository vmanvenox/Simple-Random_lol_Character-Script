# List of support champions in League of Legends
support_champions = ["Alistar", "Amumu", "Anivia", "Ashe", "Bard", "Blitzcrank", "Brand", "Braum", "Fiddlesticks", "Galio", "Heimerdinger", "Ivern", "Leona", "Lulu", "Lux", "Malphite", "Maokai", "Morgana", "Nami", "Nautilus", "Pantheon", "Poppy", "Pyke", "Rakan", "Renata Glasc", "Senna", "Seraphine", "Sett", "Shaco", "Shen", "Sona", "Soraka", "Swain", "Syndra", "Tahm Kench", "Thresh", "Vel'Koz", "Xerath", "Yuumi", "Zac", "Zilean", "Zoe", "Zyra", "Taric"]

# Import the random module
import random

# Generate a random index between 0 and the length of the support_champions list
random_index = random.randint(0, len(support_champions) - 1)

# Get the champion at the random index
random_support = support_champions[random_index]

# Print the randomly chosen champion
print(f"Your randomly chosen support champion is: {random_support}")

# made by KingTreemox aka Treemox
