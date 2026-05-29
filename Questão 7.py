def contar_digitos(n):

    contador = 0

    while n > 0:
        n = n // 10
        contador += 1

    return contador

print(contar_digitos(12345))
