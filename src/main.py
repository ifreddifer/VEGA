from brain import VegaBrain


def main():
    vega = VegaBrain()

    print("VEGA iniciada.")
    print("Digite 'sair' para encerrar.")

    while True:
        texto = input("Você: ")

        if texto.lower() == "sair":
            print("VEGA: Até mais!")
            break

        resposta = vega.conversar(texto)

        print("VEGA:", resposta)


if __name__ == "__main__":
    main()