import sympy as sp
from scipy.integrate import quad

print("Notum ákveðið heildi til þess að reikna flatarmálið sem afmarkast af grafi f(x) og g(x): ")
print("Dæmi: -x**2+5*x-3")

print()
tmp_fall_fx = input("Sláðu inn fall f(x) = ")
tmp_fall_gx = input("Sláðu inn fall g(x) = ")

print()
efriMork = int(input("Sláðu inn x fyrir efri mörk svæðis: "))
nedriMork = int(input("Sláðu inn x fyrir neðri mörk svæðis: "))

fx = sp.Symbol('x')
gx = sp.Symbol('x')

newFX = sp.integrate(tmp_fall_fx, fx)
newGX = sp.integrate(tmp_fall_gx, gx)

x = efriMork
firstFX = eval(str(newFX))
x = nedriMork
laterFX = eval(str(newFX))

x = efriMork
firstGX = eval(str(newGX))
x = nedriMork
laterGX = eval(str(newGX))

area = firstFX-laterFX-(firstGX-laterGX)

print()
print("Flatarmálið milli f(x) og g(x) er: " + str(round(area, 2)))

