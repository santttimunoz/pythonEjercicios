#funciones tradicionales
def suma(n1, n2):
    return n1+n2 

def resta():
 pass

#funcion lamba
sumar = lambda n1, n2: n1+n2
    

if __name__ == "__main__":


 numero = int(input("ingresa numero 1: \n"))
 numero2 = int(input("ingrese numero 2: \n"))

 print(f'resultado 1: {suma(numero, numero2)}')

 print(f'resultado 2: {sumar(numero, numero2)}')