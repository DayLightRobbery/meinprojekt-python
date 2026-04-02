def frage_moods(anzahl):
    moods = []
    for i in range(anzahl):
        mood = input(f"Stimmung {i+1}: ")
        moods.append(mood)
    return moods

def auswertung(moods):
    gute = moods.count("gut")
    schlechte = moods.count("schlecht")
    print("Gute Tage:", gute)
    print("Schlechte Tage:", schlechte)
    
# Hauptprogramm
mood_liste = frage_moods(5)
auswertung(mood_liste)