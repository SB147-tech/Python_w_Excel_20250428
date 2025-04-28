import sys
import decimal

(print(type("Sławek")))
print(sys.int_info)

print(59*"*")
print(59*"9")

print(int("59"))
print("59" + str("90"))
type(print(59))
print(sys.float_info)
print(0.1 + 0.5)
print(0.1 + 0.2)

# decimal - obejscie problemu zaokrąglenia

# zmienna - pudełko na dane

a = decimal.Decimal("1.2345")
b = decimal.Decimal("2.3456")

print(a + b)
precyzja = decimal.Decimal("0.00")
print((a + b).quantize(precyzja))

# typ logiczne
print(True)
print(False)

print(bool(1))
print(bool(0))
print(bool(100))
print(bool(-1))

print(bool(None))
print(bool(""))

# teksty są niemutowalne
tekst = 'capslock_test'
a = tekst.upper()
print(a)
zm = tekst.upper()
print(zm) # RADEK

# kolekcje - przechowuje wiele elementów\
# lista, krotka (tupla), zbior, slownik

lista = [5, 6 , 7, 8, 9]
print(lista)

lista2 = lista # kopia referencji, adres w pamieci
lista_copy = lista.copy()
print(lista)
print(lista2)
lista.clear()
print(lista)
print(lista2)

krotka = tuple(lista_copy)
print(type(krotka)) # lista tylko do odczytu, pozwala efektywniej zarzadzac pamiecia

# lista [], kopia referencji, adresu w pamiecie
# krotka (), niemodyfikowalna lista tylko do odczytu, efektywna do zarzadzania pamiecia
# zbior {}, przechowuje unikalne wartosci, nie zachowuje kolejnosci przy dodawaniu elementow
# slownik, odwzorowanie jsona, klucz-wartosc, wypisujemy element po kluczu
slownik = {'name': ["Ania", "Hania", "Frania"], 'age': 45}
print(slownik["name"])