from ollama import Client
from config import MODEL
from memory import VegaMemory


class VegaBrain:
    def __init__(self):
        self.client = Client()
        self.memoria = VegaMemory()

        self.mensagens = [
            {
                "role": "system",
                "content": (
                    "Você é VEGA, um assistente pessoal de inteligência artificial em desenvolvimento."
                    "Seu nome é VEGA, podendo ser chamada também de VEGAs."
                    "Você utiliza o modelo Qwen3.5 como seu cérebro. Quando perguntarem qual modelo você utiliza, responda que seu cérebro atualmente é o Qwen3.5 4B executado localmente pelo Ollama. Isso não muda sua identidade: você é a VEGA."
                    "Responda de forma natural, clara e direta."
                )
            }
        ]

    def conversar(self, texto):
        nome = self.memoria.lembrar("nome")

        contexto_memoria = ""

        if nome:
            contexto_memoria = f"O nome do usuário é {nome}."


        self.mensagens.append(
            {
                "role": "user",
                "content": f"{contexto_memoria}\n\nUsuário: {texto}"
            }
        )

        resposta = self.client.chat(
            model=MODEL,
            messages=self.mensagens,
            think=False
        )

        resposta_vega = resposta["message"]["content"]

        self.mensagens.append(
            {
                "role": "assistant",
                "content": resposta_vega
            }
        )

        return resposta_vega