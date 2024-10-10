#Simple
a = 33
b = 200
if b < a:
    print(b, "Es mayor que", a)

#Doble
c = 200
d = 333
if c > d:
    print(d, "Es mayor que",c)
else:
    print(d, "No es mayor que",c)

#Multiple
f = 200
g = 207
if f > g:
    print(f, "Es mayor que", g)
elif f < g:
    print(f, "Es menor que",g)
else:
    print(f,"Es igual que",g)

#enlazados
x = 28

if x > 10:
    print("Por encima de diez,")
    if x > 20:
        print("Y tambien por encima de 20!")
    else:
        print("Pero no enicma de 20.")

#Parametros end y sep

print("Estudiar los sabados", end='')
print("Es genial")

#print("Estudiar los sabados")
#print("Es genial")

print("Daniela","Luis","Carlos","Camila")#Agrega un espacio por defecto
print("Daniela","Luis","Carlos","Camila",sep='')#Quita el espacio
print("Daniela","Luis""Carlos","Camila",sep=",")#Agrega una coma

print("Daniela","Luis","Carlos","Camila", sep="_", end="_Curso_Python")#Implementacion end y sep

