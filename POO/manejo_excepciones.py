from numeros_identicos_exception import NumerosIdenticosException
resultado = None

try:
    a = int(input("Primer numero: "))
    b = int(input("Segundo nuemo: "))
    if a == b:
        raise NumerosIdenticosException("Ocurrio un error, numeros identicos")
    resultado = a / b
except ZeroDivisionError as e:
    print("Ocurrio un error con AeroDivisionError", e)
    print(type(e))
except TypeError as e:
    print("Ocurrio un error con TyperError", e)
    print(type(e))
except ValueError as e:
    print("Ocurrio un error con ValuesError", e)
    print(type(e))
except Exception as e:
    print("Ocurrio un error con Exception", e)
    print(type(e))
else:
    print("No hubo ninguna excepcion")
finally:
    print("Fin del manejo de excepciones")
    
print("resultado: ", resultado)
print("continuamos...")