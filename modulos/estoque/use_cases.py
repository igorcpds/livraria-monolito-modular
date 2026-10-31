from abc import ABC, abstractmethod
from modulos.estoque.entities import ItemEstoqueEntity

class EstoquePort(ABC):
    @abstractmethod
    def obter_item(self, livro_id: int) -> ItemEstoqueEntity | None:
        pass

    @abstractmethod
    def atualizar_quantidade(self, item: ItemEstoqueEntity) -> None:
        pass


class EstoqueCleanUseCase:
    def __init__(self, port: EstoquePort):
        self.port = port

    def consultar_disponibilidade(self, livro_id: int) -> int:
        item = self.port.obter_item(livro_id)
        return item.quantidade if item else 0

    def baixar_estoque(self, livro_id: int, quantidade: int = 1) -> bool:
        item = self.port.obter_item(livro_id)
        if not item or not item.tem_disponibilidade(quantidade):
            return False
        item.debitar(quantidade)
        self.port.atualizar_quantidade(item)
        return True
