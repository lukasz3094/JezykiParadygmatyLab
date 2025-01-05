wagi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
max_waga = 10

def podziel_paczki(wagi, max_waga):
    wagi_sort = sorted(wagi, reverse=True)

    kursy = []

    for waga in wagi_sort:
        if waga > max_waga:
            return ValueError("Waga paczki jest wieksza niz maksymalna waga paczki")

        dodano = False

        for kurs in kursy:
            if sum(kurs) + waga <= max_waga:
                kurs.append(waga)
                dodano = True
                break

        if not dodano:
            kursy.append([waga])

    return kursy

print(podziel_paczki(wagi, max_waga))




