# ======================
# strings

message = "Hello"
print(message)
print(len(message))

message += " world"
print(message)
print("tamanho da string: ", len(message))

# ======================
# listas (array)
items = ["Hello", "world", 44, 3.1416, "BR"]
print(type(items)) # list
print(len(items))  # 2

for item in items:
    print(item, type(item))
    if item == "BR":
        print("best country")

# range gera um intervalo de valores, de 0 a 10
for i in range(0, 10, 2):
    print(i)
    
paises = ["SK", "AR", "BR"]
paises = sorted(paises) # ordena

for i, pais in enumerate(paises):
    print(i, pais)

indice = 0
# f-string
print(f"item na posicao {indice} é: { paises[indice] }")

