from dataclasses import dataclass

@dataclass
class ItemEstoqueEntity:
    livro_id: int
    quantidade: int

    def tem_disponibilidade(self, qtd_pedida: int = 1) -> bool:
        return self.quantidade >= qtd_pedida

    def debitar(self, qtd_pedida: int = 1):
        if not self.tem_disponibilidade(qtd_pedida):
            raise ValueError("Estoque insuficiente para o livro selecionado.")
        self.quantidade -= qtd_pedida
