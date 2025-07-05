import kalkulator as kalk
import os

def menu():
    
    x = float(input("Wprowadź pierwszą liczbę: "))
    y = float(input("Wprowadź drugą liczbę: "))
    print("\n")
    print("--------------------------------------------------------------------")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Potegowanie")
    print("9. Wyczyść ekran")
    print("0. Wyjdź z programu")
    print("--------------------------------------------------------------------")
    wybor = input("Wybierz operacje matematyczną jaką chcesz wykonać: ")
    while True:
        match wybor:
            case "1":
                print("Wynik: ", kalk.dodawanie(x,y))
                break
            case "2":
                print("Wynik: ", kalk.odejmowanie(x,y))
                break
            case "3":
                print("Wynik: ", kalk.mnozenie(x,y))
                break
            case "4":
                print("Wynik: ", kalk.dzielenie(x,y))
                break
            case "5":
                print("Wynik: ", kalk.potegowanie(y,x))
            case "9":
                os.system("cls")
            case "0":
                return 0
            case _:
                print("Nie poprawny wybor!")
                wybor = input("Wybierz operacje jeszcze raz: ")
                continue
        

def main():
    menu()
if __name__ == "__main__":
    main()    