import datetime

moods = []

# Stimmung hinzufügen
def add_mood():
    mood = input("Stimmung (gut/schlecht): ")
    datum = datetime.date.today()
    moods.append({"mood": mood, "datum": str(datum)})
    
    
# Verlauf anzeigen
def show_moods():
    if not moods:
        print("Keine Einträge.")
        return

    for eintrag in moods:
        print(f"{eintrag['datum']} - {eintrag['mood']}")
        
# Statistik
def statistik():
    gute = sum(1 for m in moods if m["mood"] == "gut")
    schlechte = sum(1 for m in moods if m["mood"] == "schlecht")
    
    print("Gute Tage:", gute)
    print("Schlechte Tage:", schlechte)
    
def main():
    while True:
        print("\n1: Eintragen 2: Verlauf 3: Statistik 4: Ende")
        wahl = input("Auswahl: ")
        
        if wahl == "1":
            add_mood()
        elif wahl == "2":
            show_moods()
        elif wahl == "3":
            statistik()
        elif wahl == "4":
            break
        else:
            print("Ungültig!")
            
if __name__ == "__main__":
    main()