print("Calculadora de IMC")

peso = float (input("Digite o seu peso em kg"))
altura = float (input("Digite a sua altura em m"))

imc = peso / (altura * altura)

if (imc < 18.5):
    print("Abaixo do peso")
elif (imc < 25):
    print("Peso normal")
elif (imc < 30):
    print("sobrepeso")  
elif (imc < 35):
    print("obesidade grau 1")
elif (imc < 40):
    print("obesidade grau 2")
else:
    print("obesidade grau 3")    

