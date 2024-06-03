import time

# Função que possui muitas atribuições
# Parece mais um método
def somar():
    n1 = int(input("Digite o primeiro número da adição: "))
    n2 = int(input("Digite o segundo número da adição: "))
    print (n1 + n2)

somar()

# Função exclusiva de soma de dois números
def somar2(n1, n2):
    soma = n1 + n2
    return soma
# print("Soma 2:", somar2(22,20))

# Terceiro exemplo de função
def somar3(n1, n2):
    return n1 + n2
# numero1 = float(input("Digite um número: "))
# numero2 = float(input("Digite outro número: "))

# Chamada da função
# print(somar2(numero1, numero2))

# Chamada da função por argumentos
print(somar3(n2 = 12, n1 = 5))

# Função com parâmetros default (padrão)
def somar4(n1 = 0, n2 = 0):
    return n1 + n2

# print(somar4(50, 25))
# print(somar4())

# Função com apenas a.guns valores default
def somar5(n1, n2=0):
    return n1 + n2

print(somar5(50, 25)) # 75
# print(somar5()) # Erro
print(somar5(10)) # 10
print(somar5(n2 = 51, n1 = 12))

def somar6(n1, n2):
    if n1 == 1:
        return 1

print(somar6(1,3)) # True
print(somar6(13,3)) # None


print(somar6(1, 2) + 10) # Mostrar 11
print(somar6(2, 2) + 10) # Mostrar type não suportado

time.sleep(3)