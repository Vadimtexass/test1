#1
n = int(input())
print(n + n * n)

#2
a = 46
b = "string "
c = b * 5
print(a, c)

#3
#num = '5934'
#numbers = num.split()
#print(numbers)

num = '5934'
numbers = ', '.join([ch for ch in num])
print(numbers)

#4
name = input("Hi my name is ")
lastName = input("My last name is ")
age = int(input("I'm "))
print(age)

#5
q = 136
print(q // 7)

#6
w = int(input())
e = int(input())
r = int(input())
print(w+e+r, w-e-r, w/e/r, w*e*r, w%e%r)

#7
s = 10
d = 10.5
f = "20"
g = int(f)
print(s * d * g)

#8
z = float(input())
if z > 0:
    print("Положительное")
elif z < 0:
    print("Отрицательное")
else:
    print("Zero")

#9
k = input("Enter number: ")
if k.isdigit():
    print("Correct")
else:
    print("Please, enter number")



#10
c = 24
if c > 18:
    print("Вам уже все можно")
elif c == 18:
    print("Ура, Вам 18 лет!")
else:
    print("Вы еще слишком молоды")

#11
v = float(input())
b = input()
n = float(input())
if b == "+":
    print(v + n)
elif b == "-":
    print(v - n)
elif b == "*":
    print(v * n)
elif b == "/":
    if n != 0:
        print(v / n)
    else:
        print("Divided by Zero")

#12
r = float(input())
t = float(input())
if r > t:
    print("Profit")
else:
    print("Decrease")

#13
u = 3
i = 8
if u % 2 == 0:
    print(u)
else:
    print(i)

#14
h = 14
if 10 < h <= 15 and h != 12:
    print(True)
elif h == 18:
    print(True)




























