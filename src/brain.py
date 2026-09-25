from ollama import Client
from config import MODEL


class VegaBrain:
    def __init__(self):
        self.client = Client()

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
        self.mensagens.append(
            {
                "role": "user",
                "content": texto
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