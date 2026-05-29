def numero_perfeito(n):

    soma = 0

    for i in range(1, n):

        if n % i == 0:
            soma += i

    if soma == n:
        return True
    else:
        return False

print(numero_perfeito(6))
