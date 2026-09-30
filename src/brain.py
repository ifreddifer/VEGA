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

                    "Quando o usuário informar uma informação pessoal estável sobre si mesmo que possa ser útil no futuro, identifique essa informação como uma possível memória. "
                    "Use o formato exatamente assim:\n"
                    "MEMORIA: chave = valor\n"
                    "Exemplo: MEMORIA: nome = Fernando\n"
                    "Se não houver uma informação apropriada para memorizar, não escreva nenhuma linha MEMORIA."
                )
            }
        ]

    def conversar(self, texto):
        memorias = self.memoria.todas()

        contexto_memoria = ""

        if memorias:
            contexto_memoria = (
                "Informações conhecidas sobre o usuário:\n"
                f"{memorias}"
            )


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

        for linha in resposta_vega.splitlines():
            if linha.startswith("MEMORIA:"):
                memoria = linha.replace("MEMORIA:", "").strip()

                if "=" in memoria:
                    chave, valor = memoria.split("=", 1)

                    chave = chave.strip()
                    valor = valor.strip()

                    self.memoria.guardar(chave, valor)

        self.mensagens.append(
            {
                "role": "assistant",
                "content": resposta_vega
            }
        )

        return resposta_vega