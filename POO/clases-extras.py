class Persona:
    def __init__ (this, n, e, *v, **d):
        this.nombre = n
        this.edad = e
        this.valores = v
        this.diccionario = d
    
    def desplegar(this):
        print("Nombre:", this.nombre)
        print("Edad:", this.edad)
        print("Valores (Tupla)", this.valores)
        print("Diccioanrio", this.diccionario)
        
p1 = Persona ("Juan", 28)
p1.desplegar()

p2 = Persona ("Karla", 22, 2,3,4)
p2.desplegar()

p3 = Persona ("Paola", 20, 2,3, m="manzana", p="pera")
p3.desplegar()