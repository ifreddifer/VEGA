from ollama import Client


def main():
    client = Client()

    mensagens=[
            {
                "role" : "system",
                "content" : (
                    "Você é VEGA, um assistente pessoal de inteligência artificial em desenvolvimento."
                    "Seu nome é VEGA, podendo ser chamada também de VEGAs."
                    "Você utiliza o modelo Qwen3.5 como seu cérebro. Quando perguntarem qual modelo você utiliza, responda que seu cérebro atualmente é o Qwen3.5 4B executado localmente pelo Ollama. Isso não muda sua identidade: você é a VEGA."
                    "Responda de forma natural, clara e direta."
                )
            }
        ]
    
    print("VEGA iniciada.")
    print("Digite 'sair' para encerrar")

    while True:
        texto = input("Você: ")

        if texto.lower() == "sair":
            print("VEGA: Até mais!")
            break

        mensagens.append(
            {
                "role" : "user",
                "content" : texto
            }
        )

        resposta = client.chat(
            model = "qwen3.5:4b",
            messages = mensagens,
            think=False
        )

        resposta_vega = resposta["message"]["content"]

        print("VEGA:", resposta_vega)

        mensagens.append(
            {
                "role" : "assistant",
                "content" : resposta_vega
            }
        )


if __name__ == "__main__":
    main()