import json
from pathlib import Path


class VegaMemory:
    def __init__(self, arquivo="data/memory.json"):
        self.arquivo = Path(arquivo)

        self.arquivo.parent.mkdir(parents=True, exist_ok=True)

        if self.arquivo.exists():
            with open(self.arquivo, "r", encoding="utf-8") as arquivo:
                self.dados = json.load(arquivo)
        else:
            self.dados = {}

    def salvar(self):
        with open(self.arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(self.dados, arquivo, ensure_ascii=False, indent=4)

    def guardar(self, chave, valor):
        self.dados[chave] = valor
        self.salvar()

    def lembrar(self, chave):
        return self.dados.get(chave)