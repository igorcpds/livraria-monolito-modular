from modulos.catalogo.negocio import CatalogoNegocio
from modulos.catalogo.rotas import catalogo_rotas_bp

class CatalogoAplicacao:
    blueprint = catalogo_rotas_bp

    @staticmethod
    def obter_livros(termo: str = ""):
        return CatalogoNegocio.listar_catalogo_com_estoque(termo)

    @staticmethod
    def buscar_item_disponivel(livro_id: int = None, isbn: str = None):
        return CatalogoNegocio.validar_livro_para_carrinho(livro_id=livro_id, isbn=isbn)
