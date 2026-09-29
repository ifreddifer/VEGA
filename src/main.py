from brain import VegaBrain
from memory import VegaMemory


def main():
    vega = VegaBrain()
    memoria = VegaMemory()

    print("VEGA iniciada.")
    print("Digite 'sair' para encerrar.")
    print("Digite '/memoria' para consultar as memórias.")
    print("Digite '/lembrar *chave*' para consultar as memórias especificas.")
    print("Digite '/guardar *chave* *valor*' para guardar na memória.")

    while True:
        texto = input("Você: ")

        if texto.lower() == "sair":
            print("VEGA: Até mais!")
            break

        if texto.lower() == "/memoria":
            memorias = memoria.todas()

            if memorias:
                print("VEGA - Memórias armazenadas:")
                for chave, valor in memorias.items():
                    print(f"- {chave}: {valor}")
            else:
                print("VEGA: Ainda não tenho memórias armazenadas.")

            continue

        if texto.lower().startswith("/lembrar "):
            chave = texto[9:].strip()

            valor = memoria.lembrar(chave)

            if valor is not None:
                print(f"VEGA: {valor}")
            else:
                print(f"VEGA: não encontrei a memória '{chave}'.")

            continue

        if texto.lower().startswith("/guardar "):
            partes = texto[9:].strip().split(" ", 1)

            if len(partes) < 2:
                print("VEGA: Use o formato '/guardar chave valor.")
                continue

            chave = partes[0]
            valor = partes[1]

            memoria.guardar(chave, valor)

            print(f"VEGA: Memória '{chave}' salva.")

            continue

        if texto.lower().startswith("/esquecer "):
            chave = texto[10:].strip()

            if memoria.lembrar(chave) is not None:
                memoria.esquecer(chave)
                print(f"VEGA: Memória '{chave}' esquecida.")
            else:
                print(f"VEGA: Não encontrei a memória '{chave}'.")

            continue

        resposta = vega.conversar(texto)

        print("VEGA:", resposta)


if __name__ == "__main__":
    main()