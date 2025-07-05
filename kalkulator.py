def is_num(x,y):
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        raise ValueError("Wprowadzona wartosc nie jest liczba")
    
def dodawanie(x,y):
    is_num(x,y)
    return (x+y)

def odejmowanie(x,y):
    is_num(x,y)
    return (x-y)

def mnozenie(x,y):
    is_num(x,y)
    return (x*y)

def dzielenie(x,y):
    is_num(x,y)
    if y == 0:
        return "Blad! Nie mozna dzielic przez 0!"
    return (x/y)

def potegowanie(x,y):
    is_num(x,y)
    if y == 0:
        return 1
    else:
        return x**y
