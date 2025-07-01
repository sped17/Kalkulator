# Kalkulator
Prosty kalkulator konsolowy stworzony na potrzeby projektu zaliczeniowego.

## Funkcjonalności
- Dodawanie
- Odejmowanie
- Mnożenie
- Dzielenie

Dla dwóch liczb stało lub zmiennoprzecinkowych
Brak twardego zdefiniowania liczby miejsc po przecinku oraz ilości liczb wyświetlanych

# Klonowanie repozytorium
git clone [https://github.com/sped17/Kalkulator]
# Instalacja zależności
pip install -r requirements.txt
```
## Użycie
  Po uruchomieniu programu w konsoli zobaczymy prosty kalkulator tekstowy
  Kalkulator pozwala na operację na 2 liczbach zmiennoprzecinkowych 

  W przypadku nieprawidłowych danych wejściowych użytkownik powinien otrzymać odpowidni komunikat:
    - Nie można dzielić przez 0
    - Nie można dodawać czegokolwiek innego niż liczby 
    - Brak funckji o podanym numerze 

## Dokumentacja
  Funkcje:
    is_num
      Input: INT | FLOAT x, INT | FLOAT y
      Output: None
      W przypadku gdy wprowadzone liczby x lub y nie są liczbami, a innymi znakami podnosi ValueError
      Funkcja stosowana do walidacji danych wejściowych

    dodawanie
      Input: INT | FLOAT x, INT | FLOAT y
      Output: (x+y)
      Funkcja zwraca dodane do siebie argumenty wejściowe

    odejmowanie
      Input: INT | FLOAT x, INT | FLOAT y
      Output: (x-y)
      Funkcja zwraca odjęte do siebie argumenty wejściowe

    mnozenie
      Input: INT | FLOAT x, INT | FLOAT y
      Output: (x*y)
      Funkcja zwraca pomnożone przez siebie argumenty wejściowe

    dzielenie
      Input: INT | FLOAT x, INT | FLOAT y
      Output: (x/y)
      Funkcja sprawdza czy argument y nie jest 0 - dzielenie przez 0 = operacja nie możliwa matematycznie
      następnie zwraca argument x podzielony przez argument y 

  Testy:
    100% zaimplementowanych funkcji 

  Actions:
    Automatyczne testy przy każdym push'u i pull'u pokrywające aktualnie 100% zaimplementowanych funkcji    