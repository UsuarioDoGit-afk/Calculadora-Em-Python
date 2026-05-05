#Calculadora Funcional Em Python

print("Calculadora Por Cristian")

while True:

try:  

    dig1 = float(input("Digite o primeiro Dígito: "))  
  
    dig2 = float(input("Digite o segundo Dígito "))   
    break  
except ValueError:  
    print("Inválido!")

ope = input("Digite a Operação: ")

if ope == "+":
print(f'O Resultado da Soma é: {dig1 + dig2} !')
elif ope == "-":
print(f'O Resultado da Subtração é: {dig1 - dig2} !')
elif ope == "*":
print(f'O Resultado da Multiplicação é: {dig1 * dig2}')
elif ope == "/":
print(f'O Resultado da Divisão é: {dig1 / dig2}')
else:
print("Inválido!")
