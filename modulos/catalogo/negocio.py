from modulos.catalogo.dados import CatalogoDados
from modulos.estoque.adapters import estoque_facade

class CatalogoNegocio:
    @staticmethod
    def listar_catalogo_com_estoque(termo: str = ""):
        livros = CatalogoDados.listar_todos()
        if termo:
            t = termo.lower()
            livros = [l for l in livros if t in l["titulo"].lower() or t in l["autor"].lower()]
        # Comunicação lateral Catálogo <-> Estoque
        resultado = []
        for l in livros:
            copia = dict(l)
            copia["estoque_disponivel"] = estoque_facade.consultar_disponibilidade(l["id"])
            resultado.append(copia)
        return resultado

    @staticmethod
    def validar_livro_para_carrinho(livro_id: int = None, isbn: str = None):
        livro = CatalogoDados.buscar_por_isbn(isbn) if isbn else CatalogoDados.buscar_por_id(livro_id)
        if livro and estoque_facade.consultar_disponibilidade(livro["id"]) > 0:
            return livro
        return None
