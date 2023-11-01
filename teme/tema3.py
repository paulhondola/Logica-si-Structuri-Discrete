# ex 1

a_0 = 2
n = 4
def prog_aritm(a_0, n):
	if n == 0:
		return a_0
	else:
		return 2 * prog_aritm(a_0, n - 1) - 3

print("ex1:", prog_aritm(a_0, n))

# ex 2

def fibo_rec(n):
	if n == 0 or n == 1:
		return n
	else:
		return fibo_rec(n - 1) + fibo_rec(n - 2)

print("ex2:", fibo_rec(5))

# ex 3

def sum_n(n):
	if n == 0:
		return 0
	else:
		return n + sum_n(n - 1)

print("ex3:", sum_n(10))


# ex 4

def prod_cifre(n):
	if n == 0:
		return 1
	else:
		return (n % 10) * prod_cifre(n // 10)
	
print("ex4 a:", prod_cifre(1234))

def nr_cifre(n):
	if n == 0:
		return 0
	else:
		return 1 + nr_cifre(n // 10)

print("ex4 b:", nr_cifre(1234567))

def cif_max(n):
	if n == 0:
		return 0
	else:
		cifra_curenta = n % 10
		max_temp = cif_max(n // 10)
		if cifra_curenta > max_temp:
			return cifra_curenta
		else:
			return max_temp

print("ex4 c:", cif_max(1274536))

def nr_cif_pare(n):
	if n == 0:
		return 0
	else:
		return (n % 2 == 0) + nr_cif_pare(n // 10)

print("ex4 d:", nr_cif_pare(134112))

# ex 5

def exp(baza, exponent):
	if exponent == 0:
		return 1
	else:
		return baza * exp(baza, exponent - 1)

print("ex5:", exp(2, 5))

# ex 6
import math

def prime(n):
	def aux(div):
		if div > math.sqrt(n):
			return True
		elif n % div == 0:
			return False
		else:
			return aux(div + 1)

	return aux(2)

print("ex6 17:", prime(17))
print("ex6 18:", prime(18))

# ex 7

def cmmdc(a, b):
	if a % b == 0:
		return b
	else:
		return cmmdc(b, a % b)

print("ex7:", cmmdc(30, 20))

# ex 8

print("ex8:")

# ex 9

min_val = 1.242
max_val = 8.424

def interval(min_value, max_value):
	if math.ceil(min_value) < max_value:
		print(math.ceil(min_value), end=' ')
		interval(min_value + 1, max_value)

print("ex9:", end = ' ')
interval(min_val, max_val)
print()

# ex 10

cifra = 5

def is_present(n, cif):
	if n == 0:
		return False
	elif n % 10 == cif:
		return True
	else:
		return is_present(n // 10, cif)

print("ex10 a:", is_present(12345, 5))

def nr_ap(n, cif):
	if n == 0:
		return 0
	else:
		return int(n % 10 == cif) + nr_ap(n // 10, cif)

print("ex10 b:", nr_ap(12355545, 5))

# ex 11

def palindrom(n):

	n = str(n)

	def aux(start, end):
		if start > end:
			return True
		elif n[start] != n[end]:
			return False
		else:
			return aux(start + 1, end - 1)

	return aux(0, len(n) - 1)

print("ex11 121:", palindrom(121))
print("ex11 1231:", palindrom(1231))

# ex 12

def f(x):
	return 2 * x

def comp(f, x, n):
	if n == 0:
		return x
	else:
		return f(comp(f, x, n - 1))

print("ex12:", comp(f, 4, 3))

# ex 13

def suma_13a(n):
	if n == 0:
		return 1
	else:
		return 1 / (n + 1) + suma_13a(n - 1)

print("ex13 a:", suma_13a(995))

def factorial(aux):
		if aux == 1:
			return 1
		else:
			return aux * factorial(aux - 1)
		
def taylor(x, n):
	if n == 0:
		return 1
	else:
		return (x ** n) / (factorial(n)) + taylor(x, n - 1)

print("ex13: e^x =", taylor(2, 3)) 

def suma_13c(n):
	if n == 1:
		return 1
	else:
		return math.sqrt(1 + math.sqrt(suma_13c(n - 1)))

print("ex13 c:", suma_13c(995))

# ex 14

def binary_rec(x):
	if x == 0:
		return ''
	else:
		return binary_rec(x // 2) + str(x % 2) 

print("ex14:", binary_rec(29))

# ex 15

print("ex15:", end=' ')

def triunghi(n):
	if n == 0:
		pass
	else:	
		triunghi(n - 1)
		print()
		def aux(line):
			if line == 0:
				pass
			else:
				print(n, end=' ')
				aux(line - 1)

		
		aux(n)

triunghi(5)
print()

# ex 16

def rest(a, p):

	def aux(k):
		if a ** k % p == 1:
			return k
		else:
			return aux(k + 1)

	return aux(1)

print("ex16:", rest(4, 7))



