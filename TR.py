def berechne (a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    
def main():
    try:
        a = float(input("Zahl 1: "))
        b = float(input("Zahl 2: "))
        op = input("Operator (+, -, *, /): ")
        
        if op == "/" and b == 0:
            print("Division durch 0 nicht erlaubt !")
            return
        
        ergebnis = berechne(a, b, op)
        print("Ergebnis:", ergebnis)
        
    except ValueError:
        print("Bitte gültige Zahlen eingeben!")
        
if __name__ == "__main__":
    main()