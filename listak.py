# listák készítése

# ez egy üres lista
a = []

# stringeket tartalmazó lista
b = ['valami', 'szoveg']

# vegyes típusokat tartalmazó lista
c = ['valami', 42, True]

# listába listát is tehetünk
d = ['kutya', [4, 3, 5], ['a']]

e = [[], [], [['a', 'b', 'c', ['x', 'y']]]]

# ez a sor a b listából kiválasztja a második elemet
# a listákat nullától indexeljük
print(b[1])

print(c[2])

print(d[2][0])

print(e[2][0][3][1])

print(a)

# listához elemet az append függvénnyel tudunk hozzáadni - mindig a lista legvégére
a.append('szoveg1')
# az append függvényt a listán lehet meghívni
a.append('szoveg2')

print(a)

a = [2, 4, 6, 8, 10, 12, 14, 16, 18]
# ha tartományt választunk ki, akkor kettősponttal
# választjuk el a tól:ig részt
# ahol az alsó korlát incluzive: benne lesz,
# a felső korlát az exclusive: nem lesz benne
print(a[2:5])

print(a[12:8])
print(a[1:7])
print(a[3:8])

# ha nem adunk felső korlátot, akkor:
print(a[2:])

# ha nem adunk alsó korlátot:
print(a[:5])

# ha nem adunk se alsó, se felső korlátot:
print(a[:])  # = print(a)

# ha még egy :-ot beírunk, akkor azt adjuk meg,
# hogy hanyassával kérjük az elemeket
# pl. 4. elemig felfelé kérem, de csak minden 2. elemet
print(a[:4:2])

# megfordítja a listát:
print(a[::-1])

# megfordítja a listát és kettesével adja vissza:
print(a[::-2])

# hátulról is lehet elemet kiválasztani:
# pl. a legutolsó elem:
print(a[-1])

# ha egy pontos helyre akarjuk az elemet beilleszteni:
# akkor azt is meg kell adni, hogy hova kérem, és mi elé kérem
# pl. a 3. elem elé berakunk egy 'a' stringet
a.insert(3, 'a')
print(a)

# elemet kivenni a lista legvégéről
# ha kell, akkor a pop függvény vissza is adja
# azt az elemet, amit kitöröl
last = a.pop()
print(a)
print(last)

# ha adunk paramétert a pop-nak, akkor az az
# index legyen
a.pop(1)
print(a)

# egy konkrét elemet kivenni érték alapján
a.remove('a')
print(a)

# ez errort dobna, mert az elem már nincs benne a listában
# a.remove('a')

# hanyadik elem a 10-es:
print(a.index(10))

# megszámoljuk a 2-eseket a listában:
b = [2, 2, 4, 3, 2, 2, 2]
print("{} darab kettes szám van a 'b' listában".format(b.count(2)))

# listák növekvő sorba rendezése
c = [3, 7, 5, 12, 9]
c.sort()
print(c)

# string elemek esetén abc sorrendbe rendez
d = ['laci', 'béla', 'tibi', 'kati']
# ha a reverse flag-et True-ra állítjuk, akkor fordított sorrendbe helyezi
d.sort(reverse=True)
print(d)

# megfordítani a sorrendet:
# nem megrendezem, csak meg akarom fordítani
a = [2, 4, 6, 8, 10, 12, 14, 16, 18]
a.reverse()
print(a)

x = ['h', 'e', 'l', 'l', 'o']
x.reverse()
print(x)

# minden elemet kitöröl a listából
# üres listát csinál belőle
x.clear()  # vagy: x = []
print(x)

# listákat mergelni / összefűzni:
a = [2, 4, 6, 8, 10, 12, 14, 16, 18]
x = ['h', 'e', 'l', 'l', 'o']
print(a+x)
print(x+a)  # metódussal - x.extend(a)
x.extend(a)
print('A lista összefűzve metódussal: {}'.format(x))

# zip: cipzár...
print(list(zip(x, a)))

s = 'this is my string'
# listává konvertálni:
my_string_list = list(s)
print(my_string_list)

# listát létrehozni stringből:
# meg kell adni egy separátort, amivel megmondom,
# hogy mi alapján akarom
# pl. itt a szóközök alapján
my_string_list = s.split(' ')
print(my_string_list)

s = '123-345-454'
my_string_list = s.split('-')
print(my_string_list)

a = [2, 4, 6, 8, 10, 12, 14, 16, 18]
x = ['h', 'e', 'l', 'l', 'o']

# összeolvasztani listát stringgé:
# úgy, hogy megmondjuk, mi legyen közötte
# pl. az x lista elemeit összeolvasztja úgy,
# hogy csillagokat tesz közéjük
my_string = '*'.join(x)
print(my_string)
my_string = 'SZIA'.join(x)
print(my_string)
my_string = ''.join(x)
print(my_string)

# a join metódus csak olyan tömbökkel tud dolgozni, ami stringeket tartalmaz
# számokat nem tud olyan könnyen összefűzni
# erre pl. errort adna:
# my_string = '*'.join(a) << ERROR!

# csak ha minden számot átkonvertálunk stringbe
#                           list comprehension!
my_string = '*'.join([str(item) for item in a])
print(my_string)

# list comprehension kifejtve for ciklussal:
result = []
for item in a:
    # a result listába beletesszük az 'a' lista
    # minden elemét, stringgé alakítva:
    result.append(str(item))
# a result lista ugyanazt tartalmazza, mint az 'a' lista
# csak int típusok helyett stringek vannak benne
print(result)
