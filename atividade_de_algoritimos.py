# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 13:51:18 2023

@author: Mathe
"""
import math
#soma
a=3
b= 6
c= -10
d= 25

print(a + c)

#encontrar o maior valor

print(max(a,b,c,d))

#menor valor
print(min(a,b,c,d))

#função de segundo grau

delta = b * b - (4 * a * c)
if delta < 0:
    print("função inexistente")
elif delta == 0:
    raiz = -b / (2*a)
    print('delta = 0 , raiz =' ,raiz)
else:
    raiz1 = (-b + math.sqrt(delta) ) / (2*a)
    raiz2 = (-b - math.sqrt(delta) ) / (2*a)
    print('Raizes: ',raiz1,' e ',raiz2)

#fatorial
numero = 7
resultado=1
for i in range(1,numero+1,1):
    resultado *= i

print(resultado)

#verificando numero primo
flag = 1
i = 2
n = 11

for i in range(2,n):
    if(n%i == 0):
        flag = 0
        i += 1
if(flag == 0):
    print("não é primo")
else:
    print("é primo")    
    
    
#fibonacci
n = 1000
penultimo = 1
ultimo = 1

if (n==1) or (n==2):
    print("1")
else:
    for a in range(2,n):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        a += 1
    print(termo)
   