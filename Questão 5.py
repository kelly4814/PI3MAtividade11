def verificar_palindromo(texto):

    if texto == texto[::-1]:
        return True
    else:
        return False

print(verificar_palindromo("ana"))
