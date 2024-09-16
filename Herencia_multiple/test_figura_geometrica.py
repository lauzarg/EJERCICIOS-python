from Cuadrado import Cuadrado

cuadrado1 = Cuadrado(5, 'Rojo')

#print (cuadrado1.ancho)
#print (cuadrado1.alto)
#print (cuadrado1.color)
print (cuadrado1.calcular_area())


print (cuadrado1)


#MRO - Method Resolution Order - ver en que orden se están accediendo a las clases padre
# print (Cuadrado.mro())