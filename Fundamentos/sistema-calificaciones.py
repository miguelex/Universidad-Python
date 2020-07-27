nota = int(input("Proporciona un valor entre 0 y 10: "))
calificacion = None

if nota >= 9 and nota <=10:
    calificacion = "A"
elif nota >= 8 and nota < 9:
    calificacion = "B"
elif nota >= 7 and nota < 8:
    calificacion = "C"
elif nota >= 6 and nota < 7:
    calificacion = "D"
elif nota >= 0 and nota < 6:
    calificacion = "F"
else:
    calificacion = "Valor desconocido"
print (calificacion)