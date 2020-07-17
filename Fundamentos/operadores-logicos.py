#a = int(input("Introduce un valor: "))
a =3
valorMinimo = 0
valorMaximo = 5
dentroRango = a >= valorMinimo and a <= valorMaximo
#print(dentroRango)
if(dentroRango):
    print("Dentro del rango")
else:
    print("Fuera del Rango")
    
vacaciones = False
diaDescanso = True
if(vacaciones or diaDescanso):
    print("Puedes ir al parque")
else:
    print("Tienes deberes que hacer")

print(not(vacaciones))