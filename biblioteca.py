import random
import os

def escolher_palavra():
    palavras = ["casa", "flores", "computador", "jogo", "desenvolvedor", "vontade", "primavera", "pastel", "feijoada", "felicidade"]
    return random.choice(palavras)

def jogoDaForca():
    jogarNovamente = "s"
    while jogarNovamente == "s":
        print("BEM-VINDO AO JOGO DA FORCA!\n")

        tamPalavra = 0
        alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                    "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        quantAcertos = 0
        erros = []
        acertos = []
        chances = 5
        cont = 0
        forca = [
            "   ________     ",
            "   |            ",
            "   |            ",
            "   |            ",
            "   |            ",
            "   |            ",
            " __|__          "
        ]
        palavra = escolher_palavra()
        formacao = ["_"] * len(palavra)

        print(" \nSabendo que a palavra tem esse formato: ")
        for a in palavra:
            print("_", end="")
            tamPalavra += 1

        while True:
            letra = str(input("\nCom apenas 6 tentativas, digite uma letra que acredita que exite na palavra: ")).lower()
            if letra not in alfabeto:
                print("Digite apenas uma letra por vez. Números também não são válidos!")
            else:
                break
        while True:
            for b in range (len(palavra)):
                if palavra[b] == letra:
                    formacao[b] = letra
                    quantAcertos += 1
                    acertos += letra

            if quantAcertos == tamPalavra:
                print(f"Você acertou a palavra!\nA palavra é {palavra}.")
                break
            else:
                print(f"Palavra: {' '.join(formacao)}")

            if letra not in palavra:
                erros += letra
                print("Você errou!")
                print(f"As letras erradas até agora são: {erros}")
                cont = 1
                chances = chances - 1

            if cont > 0:

                if chances < 5:
                    forca[1] = "   |     |"
                if chances < 4:
                    forca[2] = "   |     O"
                if chances < 3:
                    forca[3] = "   |    /|\\"
                if chances < 2:
                    forca[4] = "   |     |"
                if chances < 1:
                    forca[4] = "   |     |"
                if chances < 0:
                    forca[5] = "   |    / \\"

            for linha in forca:
                print(linha)
            if chances < 0:
                print(f"Você perdeu!\n A palavra é {palavra}")
                break
            letra = input("Digite a próxima letra: ").lower()
            while letra in acertos or letra in erros:
                print("Essa letra já foi usada!")
                letra = input("Digite a próxima letra: ").lower()

            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

        jogarNovamente = input("Deseja jogar novamente? (s/n)").lower()

        if jogarNovamente == "n":
            break
        if jogarNovamente not in 'SsNn':
            jogarNovamente = input("Opeção Invalida!\nAperte s para continuar jogando e n para sair do jogo.")

    print("FIM DE JOGO!")
