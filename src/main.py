def main():
    print("VEGA iniciada")
    print("Digite 'sair para encerrar.'")

    while True:
        mensagem = input("Voce: ")

        if mensagem.lower() == "sair":
            print("VEGA: Até mais!")
            break
    
        print(f"VEGA: Você disse: {mensagem}")


if __name__ == "__main__" :
    main()