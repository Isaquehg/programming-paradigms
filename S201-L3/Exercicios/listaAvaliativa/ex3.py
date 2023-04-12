continuar = True

while(continuar):
    print("1 - Triângulo")
    print("2 - Retângulo")
    print("3 - Círculo")
    print("4 - Sair")
    forma = int(input("Selecione o tipo de forma geométrica: "))

    if(forma == 1):
        print("Entre com a base e altura")
        h = float(input("Altura: "))
        b = float(input("Base: "))

        area = (b * h) / 2

        print(f"Área do Triângulo: {area}")

    elif(forma == 2):  
        print("Entre com os lados do retangulo")
        l1 = float(input("Lado 1: "))
        l2 = float(input("Lado 2: "))

        area = l1 * l2

        print(f"Área do Retângulo: {area}") 

    elif(forma == 3): 
        print("Entre com o raio do círculo")
        r = float(input("Raio: "))

        area = 3.14 * r * r

        print(f"Área do Círculo: {area}") 
    
    elif(forma == 4):
        continuar = False