def verificar_senha(senha):

    tem_numero = False
    tem_maiuscula = False
    tem_simbolo = False

    for caractere in senha:

        if caractere.isdigit():
            tem_numero = True

        if caractere.isupper():
            tem_maiuscula = True

        if not caractere.isalnum():
            tem_simbolo = True

    score = 0

    if tem_numero:
        score += 1

    if tem_maiuscula:
        score += 1

    if tem_simbolo:
        score += 1

    if score == 3:
        return "Senha forte"
    elif score == 2:
        return "Senha média"
    else:
        return "Senha fraca"


def main():
    senha = input("Digite sua senha: ")

    resultado = verificar_senha(senha)

    print("\nResultado:", resultado)


if __name__ == "__main__":
    main() 