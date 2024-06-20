#Variable de Precios de los productos
Precio_Producto1=2499.99
Precio_Producto2=15049.49



#la variable de descuento
Descuento=0.20

#La variable del Impuesto
Tasa_Impuesto=0.18

#Calcular subtotal
Subtotal=Precio_Producto1+Precio_Producto2

#Aplicar Descuento
Subtotal_Descuento=Subtotal*Descuento

#Total despues del descuento
SubTotalDescuento=Subtotal-Subtotal_Descuento
#Calcular el impuesto

Impuesto=SubTotalDescuento*Tasa_Impuesto

#calculo despues del impuesto + el total a pagar
SubtotalImpuesto=Impuesto+SubTotalDescuento



print("subtotal",Subtotal)
print("Descuento",Subtotal_Descuento)
print("Impuesto", Impuesto)
print("Total", SubtotalImpuesto)





print("subtotal",Subtotal)
print("Descuento",Subtotal_Descuento)
print("Impuesto", Impuesto)
print("Total", SubtotalImpuesto)

