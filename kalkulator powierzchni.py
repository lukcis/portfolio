# kwadrat, koło, trapez, trójkąt
figura = str(input("Podaj nazwę figury, której chcesz obliczyć pole powierzchni: kwardat, kolo, trapez, trojkat: "))
dozwolone_figury = ['kwardat', 'kolo', 'trapez', 'trojkat']

while figura not in dozwolone_figury:
    print('Wprowadz poprawną nazwę figury')
    figura = str(input("Wprowadź jedną z podanych figur: kwardat, kolo, trapez, trojkat: "))
else:
    if  figura == 'kwadrat':
        bok_kwadratu = int(input("podaj długość boku kwadratu: "))
        pole_figury = bok_kwadratu * bok_kwadratu
        print("pole figury wynosi: ", pole_figury, "cm")
    elif figura == 'kolo':
        promien = int(input("podaj długość promienia: "))
        pole_figury = 3.14 * promien
        print("pole figury wynosi: ", pole_figury, "cm")
    elif figura == 'trojkat':
        dlugosc_podstawy = int(input("podaj długość podstawy trójkąta: "))
        wysokosc = int(input("podaj długość wysokości trójkąta: "))
        pole_figury = 1/2 * dlugosc_podstawy * wysokosc
        print("pole figury wynosi: ", pole_figury, "cm")
    elif figura == 'trapez':
        dlugosc_podstawy_1 = int(input("podaj długość krótszej podstawy trapeza: "))
        dlugosc_podstawy_2 = int(input("podaj długość dłuższej podstawy trapeza: "))
        wysokosc = int(input("podaj długość wysokości trapeza: "))
        pole_figury = 1/2 * (dlugosc_podstawy_2 + dlugosc_podstawy_1) * wysokosc
        print("pole figury wynosi: ", pole_figury, "cm")