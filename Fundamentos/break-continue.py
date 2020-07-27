#Imprimir solo letras a
for letra in "Holanda":
    if letra == "a":
        print(letra)
        break
    
#Imprimir solo numeos pares sin continuer

for i in range(6):
    if i  % 2 == 0:
        print(i)

#Imprimir solo numeos pares con continuer

for i in range(6):
    if i  % 2 != 0:
        continue
    print(i)
