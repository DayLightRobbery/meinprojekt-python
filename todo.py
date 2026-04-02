# Datei, in der Aufgaben gespeichert werden
DATEI = "todos.txt"

# Aufgaben laden (falls Datei existiert)
def lade_todos():
    try:
        with open(DATEI, "r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []
        
# Aufgaben speichern
def speichere_todos(todos):
    with open(DATEI, "w") as f:
        for todo in todos:
            f.write(todo + "\n")

# Aufgabe hinzufügen
def todos_hinzufuegen(todos):
    aufgabe = input("Neue Aufgabe: ")
    todos.append(aufgabe)
        
# Aufgaben anzeigen
def todos_anzeigen(todos):
    if not todos:
        print("Keine Aufgaben vorhanden.")
        return
    
    for i, todo in enumerate(todos):
        print(f"{i}: {todo}")
        
# Aufgabe löschen
def todo_loeschen(todos):
    todos_anzeigen(todos)
    try:
        index = int(input("Index zum Löschen: "))
        todos.pop(index)
    except:
        print("Ungültige Eingabe!")
        
# Hauptprogramm (Menü)
def main():
    todos = lade_todos()
    
    while True:
        print("\n1: Anzeigen 2: Hinzufügen 3: Löschen 4: Beenden")
        wahl = input("Auswahl: ")
        
        if wahl == "1":
            todos_anzeigen(todos)
        elif wahl == "2":
            todos_hinzufuegen(todos)
        elif wahl == "3":
            todo_loeschen(todos)
        elif wahl == "4":
            speichere_todos(todos)
            print("Gespeichert. Tschüss!")
            break
        else:
            print("Ungültige Auswahl")
            
# Startpunkt
if __name__ == "__main__":
    main()
            