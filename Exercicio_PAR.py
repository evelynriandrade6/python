import time

numero = float(input("Digite um número para saber se é par ou ímpar: "))
resto = numero % 2

if (resto == 0):
    print('"P-A-R!"')
else:
    print("Tente outra vez!")

time.sleep(5)