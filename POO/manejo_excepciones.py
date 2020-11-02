resultado = None
a = "10"
b = 0

try:
    resultado = a / b
except ZeroDivisionError as e:
    print("Ocurrio un error", e)
    print(type(e))
except TypeError as e:
    print("Ocurrio un error", e)
    print(type(e))
    
print("resultado: ", resultado)
print("continuamos...")