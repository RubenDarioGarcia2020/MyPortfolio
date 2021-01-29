# programa que saluda
print("Ingrese nombre de la persona a quien saludar: \n")
nom_persona=input()
apel_persona=input("Ingrese apellido de la persona a quien saludar: \n")
print("Hola, cómo estás", nom_persona, apel_persona, "?")

print("\nDesea saludar a otra persona? : \n")
otro_saludo=int(input("ingrese 1 en caso afirmativo - 0 para salir: --> "))

while otro_saludo == 1:
    print("Ingrese nombre de la persona a quien saludar: \n")
    nom_persona=input()
    apel_persona=input("Ingrese apellido de la persona a quien saludar: \n")
    print("Hola, cómo estás ", nom_persona, apel_persona, "?")
    print("\nDesea saludar a otra persona? : \n")
    otro_saludo=int(input("ingrese 1 en caso afirmativo - 0 para salir: --> \n"))
