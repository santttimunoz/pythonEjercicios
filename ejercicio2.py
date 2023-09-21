mayor = lambda n1, n2: f"mayor es {n1}" if n1 > n2 else f"el mayor es {n2}"

if __name__ == "__main__":
   numero1 = int(input("ingresar numero uno: \n"))
   numero2 = int(input("ingresar numero dos: \n"))

   print(mayor(numero1, numero2))
