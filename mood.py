moods = []

for i in range(3):
    mood = input(f"Stimmung {i+1} eingeben (gut/schlecht): ")
    moods.append(mood)
    
gute_tage = moods.count("gut")

print("Deine Eingaben:", moods)
print("Gute Tage:", gute_tage)