import requests
import pprint
# https://jsoncrack.com/editor

url="https://restcountries.com/v3.1/all?fields=name,borders"
odgovor=requests.get(url)
drzave=odgovor.json()
dr=[]

#prebermo vse države iz all linka v seznam
"""
for d in drzave:
    dr.append(d.get("name").get("official"))

"""

# vsako državo iz seznama poklčiemo na endpoint z detajli države
"""
for d in dr:
    c=requests.get(f"https://restcountries.com/v3.1/name/{d}").json()
    print(c[0].get("capital"))
"""
# 1: Poišči državo z največ sosedi (borders)
# Namig: Nekatere države so otoki in nimajo ključa "borders"!

"""
url="https://restcountries.com/v3.1/all?fields=name,borders"
call=requests.get(url).json()

print(call[0])

for c in call[:20]:
     print(c["name"]["common"])
     print(c.get("borders",[]))


max_sosedi=0
max_sosedi_ime=""

for c in call:
    ime = c["name"]["common"]
    bor = c.get("borders",[])

    if len(bor) > max_sosedi:
        max_sosedi=len(bor)
        max_sosedi_ime=ime

print(max_sosedi_ime,max_sosedi)
"""
# 2: Poišči države kjer govorijo največ jezikov (languages)
# Namig: Nekatere države nimajo ključa "languages"
"""
url = "https://restcountries.com/v3.1/all?fields=name,languages"
call=requests.get(url).json()



for c in call[:10]:
     print(c["name"]["common"])
     print(c.get("languages",[]))

max_jeziki=0
max_jeziki_ime=""

for c in call:
    ime = c["name"]["common"]
    jezik = c.get("languages",[])

    if len(jezik)>max_jeziki:
        max_jezik=len(jezik)
        max_jeziki_ime=ime

print(max_jeziki_ime,max_jeziki)
"""


url = "https://restcountries.com/v3.1/all?fields=name,languages"
call = requests.get(url).json()

max_jezikov = 0
max_jezik_ime = ""

# Ogled prvega dela podatkov
for c in call[:10]:
    print(c["name"]["common"])
    print(c.get("languages", []))

# Iskanje države z največ jeziki
for c in call:
    ime = c["name"]["common"]
    jeziki = c.get("languages", [])

    if len(jeziki) > max_jezikov:
        max_jezikov = len(jeziki)
        max_jezik_ime = ime

print(max_jezik_ime, max_jezikov)

# 3: Izračunaj povprečno število prebivalcev (population) po celinah (continents)
# Namig: Vedno preveri, če je population večji od 0

# 4: Poišči državo z največ časovnimi pasovi (timezones)
# Namig: Vsaka država ima vsaj en timezone

url = "https://restcountries.com/v3.1/all?fields=name,timezones"
call = requests.get(url).json()


print(call[0])

for c in call[:20]:
     print(c["name"]["common"])
     print(c.get("timezones",[]))


# 5: Izpiši vse države, ki imajo v imenu presledek
# Namig: Uporabi ["name"]["common"] za ime države



# 6: Izpiši število držav, ki imajo za uradni jezik angleščino

# 7: V katerem časovnem pasu (timezone) je največ držav?
# Namig: Ena država ima lahko več timezone-ov

# 8: Katera črka se največkrat pojavi kot prva črka v imenu države?
# Namig: Za ime uporabi ["name"]["common"].lower()

# 9: Katera država ima najdaljše ime?

# 10: Izračunaj še eno statistiko po želji.
