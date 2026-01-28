import sys

# Pobierz kwote od uzytkownika
kwota = input("Podaj kwote:")       # wprowadzony jest string
miesiace = input("podaj miesiace")        # 3 lata
oprocentowanie = input("oproncetowanie")    # w procentach

# Sprawdzamy czy kwota czy jest liczbą (ale typ jest nadal str!)
czy_liczba = kwota.isdigit() 
czy_liczba1 = miesiace.isdigit()
licz_procent = oprocentowanie.isdigit()
if czy_liczba and czy_liczba1 and licz_procent:
    print("Podana kwota jest liczbą")
    print("Konwersja do typu float")
    kwota = float(kwota) 
    oprocentowanie = float(oprocentowanie)
    miesiace = float(miesiace)
    print(f"Nasza kwota to: {kwota}, oprocentowanie to: {oprocentowanie}, miesiace to: {miesiace}")
else:
    if czy_liczba == False :
        print("Błędna kwota, podałeś litery, znaki lub nic nie podales")
    if czy_liczba1 == False :
        print("Błędna ilość miesięcy, podałeś litery, znaki lub nic nie podales")
    if licz_procent == False :
        print("Błędne oprocentowanie, podałeś litery, znaki lub nic nie podales")   
    sys.exit(1)

print(f"Wyliczamy zysk z lokaty dla warunków: kwota {kwota}, czas, {miesiace} miesięcy, oprocentowanie {oprocentowanie} procent")

lata = miesiace / 12
kwota_koncowa = kwota * (1 + oprocentowanie / 100) ** lata
zysk = kwota_koncowa - kwota

print(f"Zysk wynosi {round(zysk, 2)}")
print(f"Zysk wynosi {zysk:.2f}")
