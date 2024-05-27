import time
# Etapa 1
beatles = []
print("Etapa 1:", beatles)
# Etapa 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Etapa 2:", beatles)
# Etapa 3
for i in range(2):
    beatles.append(input("Digite o próximo da lista: "))
print("Etapa 3:", beatles)
# Etapa 4
for i in range(2):
    del beatles[-1]
print("Etapa 4:", beatles)
# Etapa 5

beatles.insert(0, "Ringo Starr")


print("Etapa 5:", beatles)

print("o fabuloso", len(beatles))
time.sleep(3)