def funkcja_slonie(dane):
    liczba_sloni = int(dane.readline())

    line2 = str(dane.readline())
    wagi = [int(i) for i in list(line2.split(" "))]

    min_waga = min(wagi)  # waga najlżejszego słonia w ogóle

    line3 = str(dane.readline())
    kolejnosc = [int(i) - 1 for i in list(line3.split(" "))]

    line4 = str(dane.readline())
    kolejnosc_docelowa = [int(i) - 1 for i in list(line4.split(" "))]
    miejsca = [None for i in range(liczba_sloni)]
    for a in range(liczba_sloni):
        miejsca[kolejnosc_docelowa[a]] = kolejnosc[a]  # na miejsce którego słonia trzeba przestawić słonia i

    bool_list = [False for i in range(liczba_sloni)]  # czy słoń należy do już zbadanego cyklu

    wynik = 0

    for i in range(liczba_sloni):
        if not bool_list[i]:
            min_c = float('inf')  # masa najlżejszego słonia w cyklu
            suma = 0  # suma mas słoni w cyklu
            slon = i
            dlugosc = 0  # długość cyklu
            x = True

            while x:
                min_c = min(min_c, wagi[slon])
                suma += wagi[slon]
                slon = miejsca[slon]
                bool_list[slon] = True
                dlugosc += 1
                if slon == i:
                    x = False

            wynik += min(suma + (dlugosc - 2) * min_c, suma + min_c + (dlugosc + 1) * min_waga)
    return wynik


plik = open('dane/slo1.in', 'r')

print(funkcja_slonie(plik))
