texto = "Python é incrível!"

# Maiúscula e minúsculas
print(texto.upper()) # PHYTON É INCRÍVEL!
print(texto.lower()) # phython é incrível!
 
# tamanho da string
print(len(texto))  # 18 caracteres (incluindo espaços e pontuação)

# Substituição
novo_texto = texto.replace("incrível", "poderoso")
print(novo_texto)  # Phyton é poderoso!