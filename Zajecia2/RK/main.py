# imie = input("Jak masz na imię? ")
# wynik = 'Cześć {}'.format(imie)
# print(wynik)
# print(wynik[-1])
# print(type(wynik[2:3]))
# print(wynik[2:])
# print(wynik[:3])
# print(wynik[::2])
#
#
# string = ""
# int = 0
# float = 0.0
#
# print('{} {} {}'.format(type(string), type(int), type(float)))
#
#
# list = ['a', 'b', 'c', 'd']
# print('{}'.format(list))
# list_join = '-'.join(list)
# print('{}'.format(list_join))
# list_split = list_join.split("-")
# print('{}'.format(list_split))
#
#
# XD = 'Metody Wiedzy Inżynierii są najlepsze'
# print('{} {}'.format(XD, len(XD)))
# XD = XD.replace('ą', 'a')
# XD = XD.replace('ż', 'z')
# print('{} {}'.format(XD, len(XD)))
# print('{} {}'.format(set(XD), len(set(XD))))
#
#
# string = ""
# int = 0
# wynik = (string, int)
# print('{} {}'.format(wynik, type(wynik)))
#
#
list1 = [1, 2, 3]
list2 = ['1', '2', '3']
list3 = list1 + list2
print('{}'.format(list3))
print('{}'.format(list3.index(2)))
list3.append(4)
print('{}'.format(list3))
list3.extend('4')
print('{}'.format(list3))
list3.insert(0, 0)
print('{}'.format(list3))

