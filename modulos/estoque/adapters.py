from bancos_de_dados import ITENS_DB
from modulos.estoque.entities import ItemEstoqueEntity
from modulos.estoque.use_cases import EstoquePort, EstoqueCleanUseCase

class ItensDBEstoqueAdapter(EstoquePort):
    def obter_item(self, livro_id: int) -> ItemEstoqueEntity | None:
        registo = next((i for i in ITENS_DB if i["id"] == int(livro_id)), None)
        if registo:
            return ItemEstoqueEntity(livro_id=registo["id"], quantidade=registo["qtd"])
        return None

    def atualizar_quantidade(self, item: ItemEstoqueEntity) -> None:
        for registo in ITENS_DB:
            if registo["id"] == item.livro_id:
                registo["qtd"] = item.quantidade
                break

# Fachada pública do módulo Estoque para comunicação interna entre módulos
estoque_facade = EstoqueCleanUseCase(port=ItensDBEstoqueAdapter())
