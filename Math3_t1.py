import math
from tabulate import tabulate

# T1.1
print("T1.1")
# A)
r = 2.493
a = (r * (180/math.pi))
print(f"A) " + str(a) + "°")

# B)
r = 0.911
b = r * (180/math.pi)
print(f"B) " + str(b) + "°")

# T1.2
print("T1.2")
# A)
degree = 137.7
d = degree * math.pi / 180
print(f"A) " + str(d) + " rad")
# B)
degree = 62.3
d = degree * math.pi / 180
print(f"B) " + str(d) + " rad")

# T1.3
print("T1.3")


d = [30, 45, 60, 90, 120, 135, 150, 180, 270, 360]
t = ()
li = []
for i in range(len(d)):
    num = (d[i] * math.pi/180)
    li.append([d[i], str(num)])

data = li
col_names = ["Aste", "Radiaani"]

print(tabulate(data, headers=col_names))

# T2
print("T2")
cat1 = 2.3
cat2 = 4.7


def hypo():
    hy = math.sqrt(((cat1**2)+(cat2**2)))
    return hy


def angle():
    hy = hypo()
    angle1 = math.degrees(math.asin(cat1/hy))
    angle2 = math.degrees(math.asin(cat2/hy))
    print(f"Kulma 1:", angle1, ", Kulma 2:", angle2)


h = hypo()
print(f"Hypotenuusan pituus:", h)
angle()

# T3
print("T3")
print("Luvun 0 kertoma:", math.factorial(0))
print("Luvun 4 kertoma:", math.factorial(4))
print("Luvun 7 kertoma:", math.factorial(7))
print("Luvun 15 kertoma:", math.factorial(15))
