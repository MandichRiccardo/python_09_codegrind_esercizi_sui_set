# esercizio 1
mio_set = set()
print(mio_set)
# esercizio 2
frutta = {"mela", "banana", "kiwi", "mela"}
print(frutta)
# esercizio 3
frutta.add("pesca")
print(frutta)
# esercizio 4
frutta.remove("mela")
print(frutta)
# esercizio 5
if "ananas" in frutta:
    print("l'elemento 'ananas' è presente nel set")
else:
    print("l'elemento 'ananas' non è presente nel set")
# esercizio 6
nuovo_set = {"banana", "kiwi", "arancia"}
print(nuovo_set)
# esercizio 7
numeri = set(range(1, 6))
print(numeri)
# esercizio 8
numeri_pari = set(x for x in numeri if x%2 == 0)
print(numeri_pari)