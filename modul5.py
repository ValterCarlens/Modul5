import os
os.system('cls')

#uppgift 1
"""
thislist = ["bla", "hej", "kmt"]
for x in thislist:
    print(thislist)
"""

#uppgift2
"""
cars = ["Ford", "Volvo", "BMW"]

cars[0] = "toyota"

print(cars)
"""

#uppgift3
"""
cars = ["Ford", "Volvo", "BMW"]

cars.append("Honda")

print(cars)
"""

#uppgift4
"""
cars = ["Ford", "Volvo", "BMW"]

print(len(cars))
"""


#uppgift5
"""
cars = ["Ford", "Volvo", "BMW"]

cars.pop(1)

print(cars)
"""

#uppgift6
"""
bilar = ["Ford", "Volvo", "BMW",]

while True:
    bil=input("Lägg till bil: ")
    bilar.append(bil)
    print(bilar)
"""

#uppgift7
"""
bilar = ["Ford", "Volvo", "BMW",]

while True:
    lägg_till_bil=input("Lägg till bil: ")
    bilar.append(lägg_till_bil)
    print(bilar)
    
    ta_bort_bil=input("Ta bort bil: ")
    bilar.remove(ta_bort_bil)
    print(bilar)
    
    break

bilar = ["Ford", "Volvo", "BMW",]

while True:
    lägg_till_bil=input("Lägg till bil: ")
    bilar.append(lägg_till_bil)
    print(bilar)
    
    ta_bort_bil=int(input("Ta bort bil: "))
    bilar.pop(ta_bort_bil-1)
    print(bilar)

    break
"""

#uppgift8
"""
Vanquish_S_Ultimate = {
    "Brand": "Aston Martin",
    "Model": "Vanquish",
    "Year": "2017"
}
print(Vanquish_S_Ultimate)
"""