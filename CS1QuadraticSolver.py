from math import sqrt
import cmath

a = input('Input a : ')
b = input('Input b : ')
c = input('Input c : ')

print("----------------------------------------------")

discrim = b**2 - 4*a*c

if discrim > 0:
    num_roots = 2
    sol1 = ((-b) + sqrt(discrim))/(2*a)    
    sol2 = ((-b) - sqrt(discrim))/(2*a)
    print("There are 2 roots. The solutions are {0} and {1}" .format(sol1, sol2))
elif discrim == 0:
    num_roots = 1
    x = (-b) / 2*a
    print("There is one root: {0} " .format(x))
else:
    num_roots = 0
    sol1 = ((-b) + cmath.sqrt(discrim))/(2*a)    
    sol2 = ((-b) - cmath.sqrt(discrim))/(2*a)
    print("There are no roots. The imaginary solutions are {0} and {1}" .format(sol1, sol2))


print("----------------------------------------------")

print("https://docs.python.org/3/library/math.html, https://docs.python.org/3/library/cmath.html")
print("^^^^^ Sources I used ^^^^^")
