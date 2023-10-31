"""

tipuri de date python

primitive - imutabile

int - fara limita
float
string
bool

colectii de date

lista - [] - Mutabil - neordonata
tuplu (tuple) - () - Imutabil - ordonata
multime (set) - {} - perechi cheie - valoare / mutabil / ordonata - cheia - mutabila / valoare - imutabila
dictionar (dict) - {}

"""

pare = [0, 2, 4, 6, 8]
impare = [1, 3, 5, 7, 9]
pare.append(10)
pare.remove(0)
pare.pop()
pare.insert(0, 0)
print(pare)
print(impare)
print(pare + impare)

tuplu_numere_pare = (0, 2, 4, 6, 8)
tuplu_numere_impare = (1, 3, 5, 7, 9)

dict_numere = {
1 : "one", 
"2" : "two", 
3 : "three"
}

print(dict_numere[1])
print(dict_numere["2"])
print(dict_numere)


"""

compunerea functiilor



"""

def suma(x):
	return x + 10

def produs(x):
	return x * 10

print("************************************")
print(produs(suma(5)))

def comp(f, g):
	return lambda x: f(g(x))

print(comp(suma, produs)(2))










