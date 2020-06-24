n = int(input())
k = int(input())
basket = k % n
eachSchooler = k // n
print(f'{n} students делят {k} что-то между собой, каждый получит по {eachSchooler} что-то и останется ещё {basket} в корзине.')
print(179 % 100 // 10)
a = 325
b = a // 100
c = a % 10
d = a % 100 // 10
print(b)
print(c)
print(d)
print(b + c + d)
import math
n = int(input())
m = int(input())
days = m / n
print(type(days))
a = int(input())
b = int(input())
n = int(input())
amount = (a * 100 + b) * n
print(amount // 100, amount % 100)
# ---------------------------------
n = int(input())
z = n - n % 2 + 2
print(z)
# -----------------------------------
n = int(input())
a = n // 60
b = n % 60
print(a, b)
# -----------------------------------
a = int(input())
b = int(input())
c = int(input())
print(round((a + b + c) / 2))
# -----------------------------------
a = int(input())
b = int(input())

days = min(a, b)
maxDays = (max(a, b) - days) // 2

print(days, maxDays)
# ------------------------------------
n = int(input())
print(n // 60 % 24, n % 60)
# ------------------------------------
n = int(input())
hours = n // 60 // 60 % 24

minutesOne = n // 60 % 60 // 10
minutesTwo = n // 60 % 60 % 10

secondsOne = n % 60 // 10
secondsTwo = n % 60 % 10

print(f'{hours}:{minutesOne}{minutesTwo}:{secondsOne}{secondsTwo}')