#funcion subtotal
subtotal = lambda cant, price: cant*price

#funcion descuento
descuento = lambda subtotal, cantidad: 0.10 * subtotal if cantidad > 10 else 0

#funcion iva
iva = lambda subtotal: subtotal * 0.19

#funcion neto a pagar
neto = lambda subtotal, iva: subtotal - iva

if __name__ == "__main__":
    
        producto = {
           "nombre" :input("ingrese el producto: "),
           "precio" : int(input("ingrese precio: ")),
           "cantidad": int(input("ingrese cantidad: "))
        }
        subto = subtotal(producto["cantidad"], producto["precio"])
        iva = iva(subto)
        valorne = neto(subto, iva)
        desc = descuento(subto, producto["cantidad"])
        print("subtotal: ", subto)
        print("descuento: ", desc)
        print("iva: ", iva)
        print("neto a pagar: ", valorne)